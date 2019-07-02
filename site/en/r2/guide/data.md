# tf.data -- Input Pipeline API

The `tf.data` API enables you to build complex input pipelines from simple,
reusable pieces. For example, the pipeline for an image model might aggregate
data from files in a distributed file system, apply random perturbations to each
image, and merge randomly selected images into a batch for training. The
pipeline for a text model might involve extracting symbols from raw text data,
converting them to embedding identifiers with a lookup table, and batching
together sequences of different lengths. The `tf.data` API makes it possible to
handle large amounts of data, different data formats, and perform complex
transformations.

The `tf.data` API introduces a `tf.data.Dataset` abstraction that represents a
sequence of elements, in which each element consists of one or more `Tensor`
objects. For example, in an image pipeline, an element might be a single
training example, with a pair of tensors representing the image and its label.

There are two distinct ways to create a dataset:

*   A data **source** constructs a `Dataset` from data stored in memory in one
    ore more files.

*   A data **transformation** constructs a dataset from one or more
    `tf.data.Dataset` objects.

## Basic mechanics

To create an input pipeline, you must start with a data *source*. For example,
to construct a `Dataset` from data in memory, you can use
`tf.data.Dataset.from_tensors()` or `tf.data.Dataset.from_tensor_slices()`.
Alternatively, if your input data is stored in a file in the recommended
TFRecord format, you can use `tf.data.TFRecordDataset()`.

Once you have a `Dataset` object, you can *transform* it into a new `Dataset` by
chaining method calls on the `tf.data.Dataset` object. For example, you can
apply per-element transformations such as `Dataset.map()`, and multi-element
transformations such as `Dataset.batch()`. See the documentation for
`tf.data.Dataset` for a complete list of transformations.

The `Dataset` object is a Python iterable. This makes it possible to consume its
elements using a for loop:

```python
dataset = tf.data.Dataset.range(10)
for elem in dataset:
  print(elem.numpy())  # prints 0, 1, ..., 9
```

or by explicitly creating a Python iterator using `iter` and consuming its
elements using `next`:

```python
dataset = tf.data.Dataset.range(10)
it = iter(dataset)
print(next(it))  # prints 0
print(next(it))  # prints 1
```

Alternatively, dataset elements can be consumed using the `reduce`
transformation, which reduces all elements to produce a single result. The
following example illustrates how to use the `reduce` transformation to compute
the sum of a dataset of integers.

```python
dataset = tf.data.Dataset.from_tensor_slices([8, 3, 0, 8, 2, 1])
print(dataset.reduce(0, lambda state, value: state + value))  # prints 22
```

<!-- TODO(jsimsa): Talk about `tf.function` support. -->

### Dataset structure

A dataset comprises elements that each have the same structure. An element
contains one or more `tf.Tensor` objects, called *components*. Each component
has a `tf.DType` representing the type of elements in the tensor, and a
`tf.TensorShape` representing the (possibly partially specified) static shape of
each element.

<!-- TODO(jsimsa): Talk about the API once it stabilizes. -->

The `Dataset` transformations support datasets of any structure. When using the
`Dataset.map()`, `Dataset.flat_map()`, and `Dataset.filter()` transformations,
which apply a function to each element, the element structure determines the
arguments of the function:

```python
dataset1 = tf.data.Dataset.from_tensor_slices(tf.random_uniform([4, 10]))
dataset1 = dataset1.map(lambda x: ...)

dataset2 = tf.data.Dataset.from_tensor_slices(
   (tf.random_uniform([4]),
    tf.random_uniform([4, 100], maxval=100, dtype=tf.int32)))
dataset2 = dataset2.flat_map(lambda x, y: ...)

# Note: Argument destructuring is not available in Python 3.
dataset3 = tf.data.Dataset.zip((dataset1, dataset2))
dataset3 = dataset3.filter(lambda x, (y, z): ...)
```

## Reading input data

### Consuming NumPy arrays

If all of your input data fit in memory, the simplest way to create a `Dataset`
from them is to convert them to `tf.Tensor` objects and use
`Dataset.from_tensor_slices()`.

```python
# Load the training data into two NumPy arrays, for example using `np.load()`.
with np.load("/var/data/training_data.npy") as data:
  features = data["features"]
  labels = data["labels"]

# Assume that each row of `features` corresponds to the same row as `labels`.
assert features.shape[0] == labels.shape[0]

dataset = tf.data.Dataset.from_tensor_slices((features, labels))
```

Note that the above code snippet will embed the `features` and `labels` arrays
in your TensorFlow graph as `tf.constant()` operations. This works well for a
small dataset, but wastes memory---because the contents of the array will be
copied multiple times---and can run into the 2GB limit for the `tf.GraphDef`
protocol buffer.

### Consuming TFRecord data

The `tf.data` API supports a variety of file formats so that you can process
large datasets that do not fit in memory. For example, the TFRecord file format
is a simple record-oriented binary format that many TensorFlow applications use
for training data. The `tf.data.TFRecordDataset` class enables you to
stream over the contents of one or more TFRecord files as part of an input
pipeline.

```python
# Creates a dataset that reads all of the examples from two files.
filenames = ["/var/data/file1.tfrecord", "/var/data/file2.tfrecord"]
dataset = tf.data.TFRecordDataset(filenames)
```

The `filenames` argument to the `TFRecordDataset` initializer can either be a
string, a list of strings, or a `tf.Tensor` of strings. Therefore if you have
two sets of files for training and validation purposes, you can create a factory
method that produces the dataset, taking filenames as an input argument:

```python
def make_dataset(filenames)
  dataset = tf.data.TFRecordDataset(filenames)
  dataset = dataset.map(...)  # Parse the record into tensors.
  dataset = dataset.repeat()  # Repeat the input indefinitely.
  dataset = dataset.batch(32)

training_dataset = make_dataset(["/var/data/training1.tfrecord", ...])
validation_dataset = make_dataset(["/var/data/validation1.tfrecord", ...])
```

### Consuming text data

Many datasets are distributed as one or more text files. The
`tf.data.TextLineDataset` provides an easy way to extract lines from one or more
text files. Given one or more filenames, a `TextLineDataset` will produce one
string-valued element per line of those files.

```python
filenames = ["/var/data/file1.txt", "/var/data/file2.txt"]
dataset = tf.data.TextLineDataset(filenames)
```

By default, a `TextLineDataset` yields *every* line of each file, which may
not be desirable, for example if the file starts with a header line, or contains
comments. These lines can be removed using the `Dataset.skip()` and
`Dataset.filter()` transformations. To apply these transformations to each
file separately, we use `Dataset.flat_map()` to create a nested `Dataset` for
each file.

```python
filenames = ["/var/data/file1.txt", "/var/data/file2.txt"]

dataset = tf.data.Dataset.from_tensor_slices(filenames)

# Use `Dataset.flat_map()` to transform each file as a separate nested dataset,
# and then concatenate their contents sequentially into a single "flat" dataset.
#
# * Skip the first line (header row).
# * Filter out lines beginning with "#" (comments).
dataset = dataset.flat_map(
    lambda filename: (
        tf.data.TextLineDataset(filename)
        .skip(1)
        .filter(lambda line: tf.not_equal(tf.strings.substr(line, 0, 1), "#"))))
```

### Consuming CSV data

The CSV file format is a popular format for storing tabular data in plain text.
The `tf.data.experimental.CsvDataset` class provides a way to extract records
from one or more CSV files that comply with
[RFC 4180](https://tools.ietf.org/html/rfc4180). Given one or more filenames and
a list of defaults, a `CsvDataset` will produce a tuple of elements whose types
correspond to the types of the defaults provided, per CSV record.

```python
# Creates a dataset that reads all of the records from two CSV files, each with
# eight float columns.
filenames = ["/var/data/file1.csv", "/var/data/file2.csv"]
record_defaults = [tf.float32] * 8   # Eight required float columns
dataset = tf.data.experimental.CsvDataset(filenames, record_defaults)
```

If some columns are empty, you can provide defaults instead of types.

```python
# Creates a dataset that reads all of the records from two CSV files, each with
# four float columns which may have missing values.
record_defaults = [[0.0]] * 8
dataset = tf.data.experimental.CsvDataset(filenames, record_defaults)
```

By default, a `CsvDataset` yields *every* column of *every* line of the file,
which may not be desirable, for example if the file starts with a header line
that should be ignored, or if some columns are not required in the input.
These lines and fields can be removed with the `header` and `select_cols`
arguments respectively.

```python
# Creates a dataset that reads all of the records from two CSV files with
# headers, extracting float data from columns 2 and 4.
record_defaults = [[0.0]] * 2  # Only provide defaults for the selected columns
dataset = tf.data.experimental.CsvDataset(filenames, record_defaults, header=True, select_cols=[2,4])
```

<!--
TODO(mrry): Add these sections.

### Consuming from a Python generator
-->

## Preprocessing data

The `Dataset.map(f)` transformation produces a new dataset by applying a given
function `f` to each element of the input dataset. It is based on the
[`map()`](https://en.wikipedia.org/wiki/Map_\(higher-order_function\)) function
that is commonly applied to lists (and other structures) in functional
programming languages. The function `f` takes the `tf.Tensor` objects that
represent a single element in the input, and returns the `tf.Tensor` objects
that will represent a single element in the new dataset. Its implementation uses
standard TensorFlow operations to transform one element into another.

This section covers common examples of how to use `Dataset.map()`.

### Parsing `tf.Example` protocol buffer messages

Many input pipelines extract `tf.train.Example` protocol buffer messages from a
TFRecord format. Each `tf.train.Example` record contains one or more "features",
and the input pipeline typically converts these features into tensors.

```python
# Transforms a scalar string `example_proto` into a pair of a scalar string and
# a scalar integer, representing an image and its label, respectively.
def _parse_function(example_proto):
  features = {"image": tf.FixedLenFeature((), tf.string, default_value=""),
              "label": tf.FixedLenFeature((), tf.int64, default_value=0)}
  parsed_features = tf.parse_single_example(example_proto, features)
  return parsed_features["image"], parsed_features["label"]

# Creates a dataset that reads all of the examples from two files, and extracts
# the image and label features.
filenames = ["/var/data/file1.tfrecord", "/var/data/file2.tfrecord"]
dataset = tf.data.TFRecordDataset(filenames)
dataset = dataset.map(_parse_function)
```

### Decoding image data and resizing it

When training a neural network on real-world image data, it is often necessary
to convert images of different sizes to a common size, so that they may be
batched into a fixed size.

```python
# Reads an image from a file, decodes it into a dense tensor, and resizes it
# to a fixed shape.
def _parse_function(filename, label):
  image_string = tf.io.read_file(filename)
  image_decoded = tf.image.decode_jpeg(image_string)
  image_resized = tf.image.resize(image_decoded, [28, 28])
  return image_resized, label

# A vector of filenames.
filenames = tf.constant(["/var/data/image1.jpg", "/var/data/image2.jpg", ...])

# `labels[i]` is the label for the image in `filenames[i].
labels = tf.constant([0, 37, ...])

dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
dataset = dataset.map(_parse_function)
```

### Applying arbitrary Python logic

For performance reasons, we encourage you to use TensorFlow operations for
preprocessing your data whenever possible. However, it is sometimes useful to
call upon external Python libraries when parsing your input data. To do so,
invoke, the `tf.py_function()` operation in a `Dataset.map()` transformation.

```python
import cv2

# Use a custom OpenCV function to read the image, instead of the standard
# TensorFlow `tf.io.read_file()` operation.
def _read_py_function(filename, label):
  image_decoded = cv2.imread(filename.decode(), cv2.IMREAD_GRAYSCALE)
  return image_decoded, label

# Use standard TensorFlow operations to resize the image to a fixed shape.
def _resize_function(image_decoded, label):
  image_decoded.set_shape([None, None, None])
  image_resized = tf.image.resize(image_decoded, [28, 28])
  return image_resized, label

filenames = ["/var/data/image1.jpg", "/var/data/image2.jpg", ...]
labels = [0, 37, 29, 1, ...]

dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
dataset = dataset.map(
    lambda filename, label: tuple(tf.py_function(
        _read_py_function, [filename, label], [tf.uint8, label.dtype])))
dataset = dataset.map(_resize_function)
```

<!--
TODO(mrry): Add this section.

### Handling text data with unusual sizes
-->

## Batching dataset elements

### Simple batching

The simplest form of batching stacks `n` consecutive elements of a dataset into
a single element. The `Dataset.batch()` transformation does exactly this, with
the same constraints as the `tf.stack()` operator, applied to each component
of the elements: i.e. for each component *i*, all elements must have a tensor
of the exact same shape.

```python
inc_dataset = tf.data.Dataset.range(100)
dec_dataset = tf.data.Dataset.range(0, -100, -1)
dataset = tf.data.Dataset.zip((inc_dataset, dec_dataset))
batched_dataset = dataset.batch(4)

it = iter(batched_dataset)
print(next(it))  # ==> ([0, 1, 2,   3],   [ 0, -1,  -2,  -3])
print(next(it))  # ==> ([4, 5, 6,   7],   [-4, -5,  -6,  -7])
print(next(it))  # ==> ([8, 9, 10, 11],   [-8, -9, -10, -11])
```

### Batching tensors with padding

The above recipe works for tensors that all have the same size. However, many
models (e.g. sequence models) work with input data that can have varying size
(e.g. sequences of different lengths). To handle this case, the
`Dataset.padded_batch()` transformation enables you to batch tensors of
different shape by specifying one or more dimensions in which they may be
padded.

```python
dataset = tf.data.Dataset.range(100)
dataset = dataset.map(lambda x: tf.fill([tf.cast(x, tf.int32)], x))
dataset = dataset.padded_batch(4, padded_shapes=(None,))

it = iter(batched_dataset)
print(next(it))  # ==> [[0, 0, 0], [1, 0, 0], [2, 2, 0], [3, 3, 3]]
print(next(it))  # ==> [[4, 4, 4, 4, 0, 0, 0],
                 #      [5, 5, 5, 5, 5, 0, 0],
                 #      [6, 6, 6, 6, 6, 6, 0],
                 #      [7, 7, 7, 7, 7, 7, 7]]
```

The `Dataset.padded_batch()` transformation allows you to set different padding
for each dimension of each component, and it may be variable-length (signified
by `None` in the example above) or constant-length. It is also possible to
override the padding value, which defaults to 0.

<!--
TODO(mrry): Add this section.

### Dense ragged -> tf.SparseTensor
-->

## Training workflows

### Processing multiple epochs

The `tf.data` API offers two main ways to process multiple epochs of the same
data.

The simplest way to iterate over a dataset in multiple epochs is to use the
`Dataset.repeat()` transformation. For example, to create a dataset that repeats
its input for 10 epochs:

```python
filenames = ["/var/data/file1.tfrecord", "/var/data/file2.tfrecord"]
dataset = tf.data.TFRecordDataset(filenames)
dataset = dataset.map(...)
dataset = dataset.repeat(10)
dataset = dataset.batch(32)
```

Applying the `Dataset.repeat()` transformation with no arguments will repeat
the input indefinitely. The `Dataset.repeat()` transformation concatenates its
arguments without signaling the end of one epoch and the beginning of the next
epoch.

If you would like to perform custom computation (e.g. to collect statistics) at
the end of each epoch, you can do so as follows:

```python
filenames = ["/var/data/file1.tfrecord", "/var/data/file2.tfrecord"]
dataset = tf.data.TFRecordDataset(filenames)
dataset = dataset.map(...)
dataset = dataset.batch(32)

# Compute for 100 epochs.
for _ in range(100):
  for elem in dataset:
    # Perform per-element computation here

  # Perform per-epoch computation here
```

### Randomly shuffling input data

The `Dataset.shuffle()` transformation randomly shuffles the input dataset
using a similar algorithm to `tf.RandomShuffleQueue`: it maintains a fixed-size
buffer and chooses the next element uniformly at random from that buffer.

```python
filenames = ["/var/data/file1.tfrecord", "/var/data/file2.tfrecord"]
dataset = tf.data.TFRecordDataset(filenames)
dataset = dataset.map(...)
dataset = dataset.shuffle(buffer_size=10000)
dataset = dataset.batch(32)
dataset = dataset.repeat()
```

## Using high-level APIs

### tf.keras

The `tf.keras` API simplifies many aspects of creating and executing machine
learning models. Its `.fit()` and `.validate()` APIs support datasets as inputs:

```python
def make_dataset(filenames)
dataset = tf.data.TFRecordDataset(filenames)
dataset = dataset.map(...)
dataset = dataset.shuffle(buffer_size=10000)
dataset = dataset.batch(32)

model = ...

training_dataset = make_dataset(["/var/data/train1.tfrecord", ...])
validation_dataset = make_dataset(["/var/data/validate1.tfrecord", ...])

model.fit(training_dataset, ...)
model.validate(validation_dataset, ...)
```

### tf.estimator

To use a `Dataset` in the `input_fn` of a `tf.estimator.Estimator`, simply
return the `Dataset` and the framework will take care of consuming its elements
for you. For example:

```python
def dataset_input_fn():
  filenames = ["/var/data/file1.tfrecord", "/var/data/file2.tfrecord"]
  dataset = tf.data.TFRecordDataset(filenames)

  # Use `tf.parse_single_example()` to extract data from a `tf.Example`
  # protocol buffer, and perform any additional per-record preprocessing.
  def parser(record):
    keys_to_features = {
        "image_data": tf.FixedLenFeature((), tf.string, default_value=""),
        "date_time": tf.FixedLenFeature((), tf.int64, default_value=""),
        "label": tf.FixedLenFeature((), tf.int64,
                                    default_value=tf.zeros([], dtype=tf.int64)),
    }
    parsed = tf.parse_single_example(record, keys_to_features)

    # Perform additional preprocessing on the parsed data.
    image = tf.image.decode_jpeg(parsed["image_data"])
    image = tf.reshape(image, [299, 299, 1])
    label = tf.cast(parsed["label"], tf.int32)

    return {"image_data": image, "date_time": parsed["date_time"]}, label

  # Use `Dataset.map()` to build a pair of a feature dictionary and a label
  # tensor for each example.
  dataset = dataset.map(parser)
  dataset = dataset.shuffle(buffer_size=10000)
  dataset = dataset.batch(32)
  dataset = dataset.repeat(num_epochs)

  # Each element of `dataset` is tuple containing a dictionary of features
  # (in which each value is a batch of values for that feature), and a batch of
  # labels.
  return dataset
```
