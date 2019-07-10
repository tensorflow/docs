page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.filter_for_shard

``` python
tf.data.experimental.filter_for_shard(
    num_shards,
    shard_index
)
```



Defined in [`tensorflow/python/data/experimental/ops/filter_for_shard_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/experimental/ops/filter_for_shard_ops.py).

Creates a `Dataset` that includes only 1/`num_shards` of this dataset.

This dataset operator is very useful when running distributed training, as
it allows each worker to read a unique subset.

When reading a single input file, you can skip elements as follows:

```python
d = tf.data.TFRecordDataset(FLAGS.input_file)
d = d.apply(tf.data.experimental.naive_shard(FLAGS.num_workers,
                                             FLAGS.worker_index))
d = d.repeat(FLAGS.num_epochs)
d = d.shuffle(FLAGS.shuffle_buffer_size)
d = d.map(parser_fn, num_parallel_calls=FLAGS.num_map_threads)
```

Important caveats:

- Be sure to shard before you use any randomizing operator (such as
  shuffle).
- Generally it is best if the shard operator is used early in the dataset
  pipeline. For example, when reading from a set of TFRecord files, shard
  before converting the dataset to input samples. This avoids reading every
  file on every worker. The following is an example of an efficient
  sharding strategy within a complete pipeline:

```python
d = Dataset.list_files(FLAGS.pattern)
d = d.apply(tf.data.experimental.naive_shard(FLAGS.num_workers,
                                             FLAGS.worker_index))
d = d.repeat(FLAGS.num_epochs)
d = d.shuffle(FLAGS.shuffle_buffer_size)
d = d.interleave(tf.data.TFRecordDataset,
                 cycle_length=FLAGS.num_readers, block_length=1)
d = d.map(parser_fn, num_parallel_calls=FLAGS.num_map_threads)
```

#### Args:

* <b>`num_shards`</b>: A <a href="../../../tf/dtypes#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    shards operating in parallel.
* <b>`shard_index`</b>: A <a href="../../../tf/dtypes#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the worker index.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.


#### Raises:

* <b>`ValueError`</b>: if `num_shards` or `shard_index` are illegal values. Note: error
    checking is done on a best-effort basis, and errors aren't guaranteed to
    be caught upon dataset creation. (e.g. providing in a placeholder tensor
    bypasses the early checking, and will instead result in an error during
    a session.run call.)