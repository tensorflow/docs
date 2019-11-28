# Optimizing input pipelines with tf.data

## Overview

GPUs and TPUs can radically reduce the time required to execute a single
training step. Achieving peak performance requires an efficient input pipeline
that delivers data for the next step before the current step has finished. The
`tf.data` API helps to build flexible and efficient input pipelines. This
document explains the `tf.data` API's features and best practices for building
highly performant TensorFlow input pipelines across a variety of models and
accelerators.

This guide does the following:

*   Illustrates that TensorFlow input pipelines are essentially an
    [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) process.
*   Describes recommended practices for designing performant TensorFlow input
    pipelines.
*   Discusses the performance implications of the order in which you apply
    transformations.

## Structure of an input pipeline

A typical TensorFlow training input pipeline can be framed as an ETL process:

1.  **Extract**: Read data from memory (NumPy) or persistent storage -- either
    local (HDD or SSD) or remote (e.g. [GCS](https://cloud.google.com/storage/)
    or
    [HDFS](https://en.wikipedia.org/wiki/Apache_Hadoop#Hadoop_distributed_file_system)).
2.  **Transform**: Use CPU to parse and perform preprocessing operations on the
    data such as shuffling, batching, and domain specific transformations such
    as image decompression and augmentation, text vectorization, or video
    temporal sampling.
3.  **Load**: Load the transformed data onto the accelerator device(s) (e.g.
    GPU(s) or TPU(s)) that execute the machine learning model.

This pattern effectively utilizes the CPU, while reserving the accelerator for
the heavy lifting of training your model. In addition, viewing input pipelines
as an ETL process provides a framework that facilitates the application of
performance optimizations.

The example below represents a naive implementation of an input pipeline that
reads TFRecord files containing labeled images and converts them to batches of
image-label pairs suitable for training. The input pipeline is represented as a
`tf.data.Dataset` which can passed to high-level TensorFlow API such as
`tf.keras`.

```python
def parse_fn(example):
  "Parse TFExample records and perform simple data augmentation."
  example_fmt = {
    "image": tf.io.FixedLenFeature([], tf.string, ""),
    "label": tf.io.FixedLenFeature([], tf.int64, -1)
  }
  parsed = tf.io.parse_single_example(example, example_fmt)
  image = tf.io.decode_image(parsed["image"])
  image = _augment_helper(image)  # augments image using slice, reshape, resize_bilinear
  return image, parsed["label"]

def make_dataset():
  files = tf.data.Dataset.list_files("/path/to/dataset/train-*.tfrecord")
  dataset = tf.data.TFRecordDataset(files)
  dataset = dataset.shuffle(buffer_size=FLAGS.shuffle_buffer_size)
  dataset = dataset.map(map_func=parse_fn)
  dataset = dataset.batch(batch_size=FLAGS.batch_size)
  return dataset
```

The next section builds on this input pipeline, illustrating best practices for
designing performant TensorFlow input pipelines.

## Optimize performance

As new computing devices (such as GPUs and TPUs) make it possible to train
neural networks at an increasingly fast rate, the CPU processing is prone to
becoming the bottleneck. The `tf.data` API provides users with building blocks
to design input pipelines that effectively utilize the CPU, optimizing each step
of the ETL process.

### Pipelining

To perform a training step, you must first extract and transform the training
data and then feed it to a model running on an accelerator. However, in a naive
synchronous implementation, while the CPU is preparing the data, the accelerator
is sitting idle. Conversely, while the accelerator is training the model, the
CPU is sitting idle. The training step time is thus the sum of both CPU
pre-processing time and the accelerator training time.

**Pipelining** overlaps the preprocessing and model execution of a training
step. While the accelerator is performing training step `N`, the CPU is
preparing the data for step `N+1`. Doing so reduces the step time to the maximum
(as opposed to the sum) of the training and the time it takes to extract and
transform the data.

Without pipelining, the CPU and the GPU/TPU sit idle much of the time:

![without pipelining](https://www.tensorflow.org/images/datasets_without_pipelining.png)

With pipelining, idle time diminishes significantly:

![with pipelining](https://www.tensorflow.org/images/datasets_with_pipelining.png)

The `tf.data` API provides a software pipelining mechanism through the
`tf.data.Dataset.prefetch` transformation, which can be used to decouple the
time when data is produced from the time when data is consumed. In particular,
the transformation uses a background thread and an internal buffer to prefetch
elements from the input dataset ahead of the time they are requested. The number
of elements to prefetch should be equal to (or possibly greater than) the number
of batches consumed by a single training step. You could either manually tune
this value, or set it to `tf.data.experimental.AUTOTUNE` which will prompt the
tf.data runtime to tune the value dynamically at runtime.

To apply this change to our running example, insert:

```python
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
```

as the last transformation of your input pipeline.

Note that the prefetch transformation provides benefits any time there is an
opportunity to overlap the work of a "producer" with the work of a "consumer."

### Parallelize data transformation

When preparing a batch, input elements may need to be pre-processed. To this
end, the `tf.data` API offers the `tf.data.Dataset.map` transformation, which
applies a user-defined function (for example, `parse_fn` from the running
example) to each element of the input dataset. Because input elements are
independent of one another, the pre-processing can be parallelized across
multiple CPU cores. To make this possible, the `map` transformation provides the
`num_parallel_calls` argument to specify the level of parallelism. For example,
the following diagram illustrates the effect of setting `num_parallel_calls=2`
to the `map` transformation:

![parallel map](https://www.tensorflow.org/images/datasets_parallel_map.png)

Choosing the best value for the `num_parallel_calls` argument depends on your
hardware, characteristics of your training data (such as its size and shape),
the cost of your map function, and what other processing is happening on the CPU
at the same time; a simple heuristic is to use the number of available CPU
cores. For instance, if the machine executing the example above had 4 cores, it
would have been more efficient to set `num_parallel_calls=4`. On the other hand,
setting `num_parallel_calls` to a value much greater than the number of
available CPUs can lead to inefficient scheduling, resulting in a slowdown.
Similar to the `prefetch` transformation, the `map` transformation supports
`tf.data.experimental.AUTOTUNE` which will delegate the decision about what
level of parallelism to use to the tf.data runtime.

To apply this change to our running example, replace:

```python
dataset = dataset.map(map_func=parse_fn)
```

with:

```python
dataset = dataset.map(map_func=parse_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

### Parallelize data extraction

In a real-world setting, the input data may be stored remotely (for example, GCS
or HDFS), either because the input data would not fit locally or because the
training is distributed and it would not make sense to replicate the input data
on every machine. A dataset pipeline that works well when reading data locally
might become bottlenecked on I/O when reading data remotely because of the
following differences between local and remote storage:

*   **Time-to-first-byte:** Reading the first byte of a file from remote storage
    can take orders of magnitude longer than from local storage.
*   **Read throughput:** While remote storage typically offers large aggregate
    bandwidth, reading a single file might only be able to utilize a small
    fraction of this bandwidth.

In addition, once the raw bytes are read into memory, it may also be necessary
to deserialize and/or decrypt the data (e.g.
[protobuf](https://developers.google.com/protocol-buffers/)), which requires
additional computation. This overhead is present irrespective of whether the
data is stored locally or remotely, but can be worse in the remote case if data
is not prefetched effectively.

To mitigate the impact of the various data extraction overheads, the
`tf.data.Dataset.interleave` transformation can be used to parallelize the data
extraction step, interleaving the contents of other datasets (such as data file
readers). The number of datasets to overlap can be specified by the
`cycle_length` argument, while the level of parallelism can be specified by the
`num_parallel_calls` argument. Similar to the `prefetch` and `map`
transformations, the `interleave` transformation supports
`tf.data.experimental.AUTOTUNE` which will delegate the decision about what
level of parallelism to use to the tf.data runtime.

The following diagram illustrates the effect of supplying `cycle_length=2` and
`num_parallel_calls=2` to the `interleave` transformation:

![parallel io](https://www.tensorflow.org/images/datasets_parallel_io.png)

To apply this change to our running example, replace:

```python
dataset = tf.data.TFRecordDataset(files)
```

with:

```python
dataset = files.interleave(
    tf.data.TFRecordDataset, cycle_length=FLAGS.num_parallel_reads,
    num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

## Performance considerations

The `tf.data` API is designed around composable transformations to provide its
users with flexibility. Although many of these transformations are commutative,
the ordering of certain transformations has performance implications.

### Map and batch

Invoking the user-defined function passed into the `map` transformation has
overhead related to scheduling and executing the user-defined function.
Normally, this overhead is small compared to the amount of computation performed
by the function. However, if `map` does little work, this overhead can dominate
the total cost. In such cases, we recommend vectorizing the user-defined
function (that is, have it operate over a batch of inputs at once) and apply the
`batch` transformation _before_ the `map` transformation.

### Map and cache

The `tf.data.Dataset.cache` transformation can cache a dataset, either in memory
or on local storage. If the user-defined function passed into the `map`
transformation is expensive, apply the cache transformation after the `map`
transformation as long as the resulting dataset can still fit into memory or
local storage. If the user-defined function increases the space required to
store the dataset beyond the cache capacity, consider pre-processing your data
before your training job to reduce resource usage.

### Map and interleave / prefetch / shuffle

A number of transformations, including `interleave`, `prefetch`, and `shuffle`,
maintain an internal buffer of elements. If the user-defined function passed
into the `map` transformation changes the size of the elements, then the
ordering of the map transformation and the transformations that buffer elements
affects the memory usage. In general, we recommend choosing the order that
results in lower memory footprint, unless different ordering is desirable for
performance (for example, to enable fusing of the map and batch
transformations).

### Repeat and shuffle

The `tf.data.Dataset.repeat` transformation repeats the input data a finite (or
infinite) number of times; each repetition of the data is typically referred to
as an _epoch_. The `tf.data.Dataset.shuffle` transformation randomizes the order
of the dataset's examples.

If the `repeat` transformation is applied before the `shuffle` transformation,
then the epoch boundaries are blurred. That is, certain elements can be repeated
before other elements appear even once. On the other hand, if the `shuffle`
transformation is applied before the repeat transformation, then performance
might slow down at the beginning of each epoch related to initialization of the
internal state of the `shuffle` transformation. In other words, the former
(`repeat` before `shuffle`) provides better performance, while the latter
(`shuffle` before `repeat`) provides stronger ordering guarantees.

## Best practice summary

Here is a summary of the best practices for designing performant TensorFlow
input pipelines:

*   Use the `prefetch` transformation to overlap the work of a producer and
    consumer. In particular, we recommend adding `prefetch` to the end of your
    input pipeline to overlap the transformations performed on the CPU with the
    training done on the accelerator. Either manually tuning the buffer size, or
    using `tf.data.experimental.AUTOTUNE` to delegate the decision to the
    tf.data runtime.
*   Parallelize the `map` transformation by setting the `num_parallel_calls`
    argument. Either manually tuning the level of parallelism, or using
    `tf.data.experimental.AUTOTUNE` to delegate the decision to the tf.data
    runtime.
*   If you are working with data stored remotely and / or requiring
    deserialization, we recommend using the `interleave` transformation to
    parallelize the reading (and deserialization) of data from different files.
*   Vectorize cheap user-defined functions passed in to the `map` transformation
    to amortize the overhead associated with scheduling and executing the
    function.
*   If your data can fit into memory, use the `cache` transformation to cache it
    in memory during the first epoch, so that subsequent epochs can avoid the
    overhead associated with reading, parsing, and transforming it.
*   If your pre-processing increases the size of your data, we recommend
    applying the `interleave`, `prefetch`, and `shuffle` first (if possible) to
    reduce memory usage.
*   We recommend applying the `shuffle` transformation _before_ the `repeat`
    transformation.
