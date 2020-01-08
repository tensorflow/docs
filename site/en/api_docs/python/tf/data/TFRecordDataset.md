page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.TFRecordDataset

## Class `TFRecordDataset`

Inherits From: [`Dataset`](../../tf/data/Dataset)



Defined in [`tensorflow/python/data/ops/readers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/data/ops/readers.py).

See the guides: [Dataset Input Pipeline > Reader classes](../../../../api_guides/python/input_dataset#Reader_classes), [Reading data > `QueueRunner`](../../../../api_guides/python/reading_data#_QueueRunner_)

A `Dataset` comprising records from one or more TFRecord files.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    filenames,
    compression_type=None,
    buffer_size=None,
    num_parallel_reads=None
)
```

Creates a `TFRecordDataset` to read for one or more TFRecord files.

NOTE: The `num_parallel_reads` argument can be used to improve performance
when reading from a remote filesystem.

#### Args:

* <b>`filenames`</b>: A <a href="../../tf/string"><code>tf.string</code></a> tensor or <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a> containing one or
    more filenames.
* <b>`compression_type`</b>: (Optional.) A <a href="../../tf/string"><code>tf.string</code></a> scalar evaluating to one of
    `""` (no compression), `"ZLIB"`, or `"GZIP"`.
* <b>`buffer_size`</b>: (Optional.) A <a href="../../tf/int64"><code>tf.int64</code></a> scalar representing the number of
    bytes in the read buffer. 0 means no buffering.
* <b>`num_parallel_reads`</b>: (Optional.) A <a href="../../tf/int64"><code>tf.int64</code></a> scalar representing the
    number of files to read in parallel. Defaults to reading files
    sequentially.


#### Raises:

* <b>`TypeError`</b>: If any argument does not have the expected type.
* <b>`ValueError`</b>: If any argument does not have the expected shape.



## Properties

<h3 id="output_classes"><code>output_classes</code></h3>



<h3 id="output_shapes"><code>output_shapes</code></h3>



<h3 id="output_types"><code>output_types</code></h3>





## Methods

<h3 id="__iter__"><code>__iter__</code></h3>

``` python
__iter__()
```

Creates an `Iterator` for enumerating the elements of this dataset.

The returned iterator implements the Python iterator protocol and therefore
can only be used in eager mode.

#### Returns:

An `Iterator` over the elements of this dataset.


#### Raises:

* <b>`RuntimeError`</b>: If eager execution is not enabled.

<h3 id="apply"><code>apply</code></h3>

``` python
apply(transformation_func)
```

Apply a transformation function to this dataset.

`apply` enables chaining of custom `Dataset` transformations, which are
represented as functions that take one `Dataset` argument and return a
transformed `Dataset`.

For example:

```
dataset = (dataset.map(lambda x: x ** 2)
           .apply(group_by_window(key_func, reduce_func, window_size))
           .map(lambda x: x ** 3))
```

#### Args:

* <b>`transformation_func`</b>: A function that takes one `Dataset` argument and
      returns a `Dataset`.


#### Returns:

* <b>`Dataset`</b>: The `Dataset` returned by applying `transformation_func` to this
      dataset.

<h3 id="batch"><code>batch</code></h3>

``` python
batch(
    batch_size,
    drop_remainder=False
)
```

Combines consecutive elements of this dataset into batches.

The tensors in the resulting element will have an additional outer
dimension, which will be `batch_size` (or `N % batch_size` for the last
element if `batch_size` does not divide the number of input elements `N`
evenly and `drop_remainder` is `False`). If your program depends on the
batches having the same outer dimension, you should set the `drop_remainder`
argument to `True` to prevent the smaller batch from being produced.

#### Args:

* <b>`batch_size`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    consecutive elements of this dataset to combine in a single batch.
* <b>`drop_remainder`</b>: (Optional.) A <a href="../../tf/bool"><code>tf.bool</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing
    whether the last batch should be dropped in the case its has fewer than
    `batch_size` elements; the default behavior is not to drop the smaller
    batch.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="cache"><code>cache</code></h3>

``` python
cache(filename='')
```

Caches the elements in this dataset.

#### Args:

* <b>`filename`</b>: A <a href="../../tf/string"><code>tf.string</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the name of a
    directory on the filesystem to use for caching tensors in this Dataset.
    If a filename is not provided, the dataset will be cached in memory.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="concatenate"><code>concatenate</code></h3>

``` python
concatenate(dataset)
```

Creates a `Dataset` by concatenating given dataset with this dataset.

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3 }
b = { 4, 5, 6, 7 }

# Input dataset and dataset to be concatenated should have same
# nested structures and output types.
# c = { (8, 9), (10, 11), (12, 13) }
# d = { 14.0, 15.0, 16.0 }
# a.concatenate(c) and a.concatenate(d) would result in error.

a.concatenate(b) == { 1, 2, 3, 4, 5, 6, 7 }
```

#### Args:

* <b>`dataset`</b>: `Dataset` to be concatenated.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="filter"><code>filter</code></h3>

``` python
filter(predicate)
```

Filters this dataset according to `predicate`.

#### Args:

* <b>`predicate`</b>: A function mapping a nested structure of tensors (having shapes
    and types defined by `self.output_shapes` and `self.output_types`) to a
    scalar <a href="../../tf/bool"><code>tf.bool</code></a> tensor.


#### Returns:

* <b>`Dataset`</b>: The `Dataset` containing the elements of this dataset for which
      `predicate` is `True`.

<h3 id="flat_map"><code>flat_map</code></h3>

``` python
flat_map(map_func)
```

Maps `map_func` across this dataset and flattens the result.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors (having shapes
    and types defined by `self.output_shapes` and `self.output_types`) to a
    `Dataset`.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="from_generator"><code>from_generator</code></h3>

``` python
from_generator(
    generator,
    output_types,
    output_shapes=None,
    args=None
)
```

Creates a `Dataset` whose elements are generated by `generator`.

The `generator` argument must be a callable object that returns
an object that support the `iter()` protocol (e.g. a generator function).
The elements generated by `generator` must be compatible with the given
`output_types` and (optional) `output_shapes` arguments.

For example:

```python
import itertools

def gen():
  for i in itertools.count(1):
    yield (i, [1] * i)

ds = Dataset.from_generator(
    gen, (tf.int64, tf.int64), (tf.TensorShape([]), tf.TensorShape([None])))
value = ds.make_one_shot_iterator().get_next()

sess.run(value)  # (1, array([1]))
sess.run(value)  # (2, array([1, 1]))
```

NOTE: The current implementation of `Dataset.from_generator()` uses
<a href="../../tf/py_func"><code>tf.py_func</code></a> and inherits the same constraints. In particular, it
requires the `Dataset`- and `Iterator`-related operations to be placed
on a device in the same process as the Python program that called
`Dataset.from_generator()`. The body of `generator` will not be
serialized in a `GraphDef`, and you should not use this method if you
need to serialize your model and restore it in a different environment.

NOTE: If `generator` depends on mutable global variables or other external
state, be aware that the runtime may invoke `generator` multiple times
(in order to support repeating the `Dataset`) and at any time
between the call to `Dataset.from_generator()` and the production of the
first element from the generator. Mutating global variables or external
state can cause undefined behavior, and we recommend that you explicitly
cache any external state in `generator` before calling
`Dataset.from_generator()`.

#### Args:

* <b>`generator`</b>: A callable object that returns an object that supports the
    `iter()` protocol. If `args` is not specified, `generator` must take
    no arguments; otherwise it must take as many arguments as there are
    values in `args`.
* <b>`output_types`</b>: A nested structure of <a href="../../tf/DType"><code>tf.DType</code></a> objects corresponding to
    each component of an element yielded by `generator`.
* <b>`output_shapes`</b>: (Optional.) A nested structure of <a href="../../tf/TensorShape"><code>tf.TensorShape</code></a>
    objects corresponding to each component of an element yielded by
    `generator`.
* <b>`args`</b>: (Optional.) A tuple of <a href="../../tf/Tensor"><code>tf.Tensor</code></a> objects that will be evaluated
    and passed to `generator` as NumPy-array arguments.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="from_sparse_tensor_slices"><code>from_sparse_tensor_slices</code></h3>

``` python
from_sparse_tensor_slices(sparse_tensor)
```

Splits each rank-N <a href="../../tf/SparseTensor"><code>tf.SparseTensor</code></a> in this dataset row-wise. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.from_tensor_slices()`.

#### Args:

* <b>`sparse_tensor`</b>: A <a href="../../tf/SparseTensor"><code>tf.SparseTensor</code></a>.


#### Returns:

* <b>`Dataset`</b>: A `Dataset` of rank-(N-1) sparse tensors.

<h3 id="from_tensor_slices"><code>from_tensor_slices</code></h3>

``` python
from_tensor_slices(tensors)
```

Creates a `Dataset` whose elements are slices of the given tensors.

Note that if `tensors` contains a NumPy array, and eager execution is not
enabled, the values will be embedded in the graph as one or more
<a href="../../tf/constant"><code>tf.constant</code></a> operations. For large datasets (> 1 GB), this can waste
memory and run into byte limits of graph serialization.  If tensors contains
one or more large NumPy arrays, consider the alternative described in
[this guide](https://tensorflow.org/guide/datasets#consuming_numpy_arrays).

#### Args:

* <b>`tensors`</b>: A nested structure of tensors, each having the same size in the
    0th dimension.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="from_tensors"><code>from_tensors</code></h3>

``` python
from_tensors(tensors)
```

Creates a `Dataset` with a single element, comprising the given tensors.

Note that if `tensors` contains a NumPy array, and eager execution is not
enabled, the values will be embedded in the graph as one or more
<a href="../../tf/constant"><code>tf.constant</code></a> operations. For large datasets (> 1 GB), this can waste
memory and run into byte limits of graph serialization.  If tensors contains
one or more large NumPy arrays, consider the alternative described in
[this guide](https://tensorflow.org/guide/datasets#consuming_numpy_arrays).

#### Args:

* <b>`tensors`</b>: A nested structure of tensors.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="interleave"><code>interleave</code></h3>

``` python
interleave(
    map_func,
    cycle_length,
    block_length=1
)
```

Maps `map_func` across this dataset, and interleaves the results.

For example, you can use `Dataset.interleave()` to process many input files
concurrently:

```python
# Preprocess 4 files concurrently, and interleave blocks of 16 records from
# each file.
filenames = ["/var/data/file1.txt", "/var/data/file2.txt", ...]
dataset = (Dataset.from_tensor_slices(filenames)
           .interleave(lambda x:
               TextLineDataset(x).map(parse_fn, num_parallel_calls=1),
               cycle_length=4, block_length=16))
```

The `cycle_length` and `block_length` arguments control the order in which
elements are produced. `cycle_length` controls the number of input elements
that are processed concurrently. If you set `cycle_length` to 1, this
transformation will handle one input element at a time, and will produce
identical results = to <a href="../../tf/data/Dataset#flat_map"><code>tf.data.Dataset.flat_map</code></a>. In general,
this transformation will apply `map_func` to `cycle_length` input elements,
open iterators on the returned `Dataset` objects, and cycle through them
producing `block_length` consecutive elements from each iterator, and
consuming the next input element each time it reaches the end of an
iterator.

For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3, 4, 5 }

# NOTE: New lines indicate "block" boundaries.
a.interleave(lambda x: Dataset.from_tensors(x).repeat(6),
             cycle_length=2, block_length=4) == {
    1, 1, 1, 1,
    2, 2, 2, 2,
    1, 1,
    2, 2,
    3, 3, 3, 3,
    4, 4, 4, 4,
    3, 3,
    4, 4,
    5, 5, 5, 5,
    5, 5,
}
```

NOTE: The order of elements yielded by this transformation is
deterministic, as long as `map_func` is a pure function. If
`map_func` contains any stateful operations, the order in which
that state is accessed is undefined.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors (having shapes
    and types defined by `self.output_shapes` and `self.output_types`) to a
    `Dataset`.
* <b>`cycle_length`</b>: The number of elements from this dataset that will be
    processed concurrently.
* <b>`block_length`</b>: The number of consecutive elements to produce from each
    input element before cycling to another input element.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="list_files"><code>list_files</code></h3>

``` python
list_files(
    file_pattern,
    shuffle=None,
    seed=None
)
```

A dataset of all files matching a pattern.

NOTE: The default behavior of this method is to return filenames in
a non-deterministic random shuffled order. Pass a `seed` or `shuffle=False`
to get results in a deterministic order.

Example:
  If we had the following files on our filesystem:
    - /path/to/dir/a.txt
    - /path/to/dir/b.py
    - /path/to/dir/c.py
  If we pass "/path/to/dir/*.py" as the directory, the dataset would
  produce:
    - /path/to/dir/b.py
    - /path/to/dir/c.py

#### Args:

* <b>`file_pattern`</b>: A string or scalar string <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing
    the filename pattern that will be matched.
* <b>`shuffle`</b>: (Optional.) If `True`, the file names will be shuffled randomly.
    Defaults to `True`.
* <b>`seed`</b>: (Optional.) A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
    random seed that will be used to create the distribution. See
    <a href="../../tf/set_random_seed"><code>tf.set_random_seed</code></a> for behavior.


#### Returns:

Dataset: A `Dataset` of strings corresponding to file names.

<h3 id="make_initializable_iterator"><code>make_initializable_iterator</code></h3>

``` python
make_initializable_iterator(shared_name=None)
```

Creates an `Iterator` for enumerating the elements of this dataset.

Note: The returned iterator will be in an uninitialized state,
and you must run the `iterator.initializer` operation before using it:

```python
dataset = ...
iterator = dataset.make_initializable_iterator()
# ...
sess.run(iterator.initializer)
```

#### Args:

* <b>`shared_name`</b>: (Optional.) If non-empty, the returned iterator will be
    shared under the given name across multiple sessions that share the
    same devices (e.g. when using a remote server).


#### Returns:

An `Iterator` over the elements of this dataset.


#### Raises:

* <b>`RuntimeError`</b>: If eager execution is enabled.

<h3 id="make_one_shot_iterator"><code>make_one_shot_iterator</code></h3>

``` python
make_one_shot_iterator()
```

Creates an `Iterator` for enumerating the elements of this dataset.

Note: The returned iterator will be initialized automatically.
A "one-shot" iterator does not currently support re-initialization.

#### Returns:

An `Iterator` over the elements of this dataset.

<h3 id="map"><code>map</code></h3>

``` python
map(
    map_func,
    num_parallel_calls=None
)
```

Maps `map_func` across the elements of this dataset.

This transformation applies `map_func` to each element of this dataset, and
returns a new dataset containing the transformed elements, in the same
order as they appeared in the input.

For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3, 4, 5 }

a.map(lambda x: x + 1) = { 2, 3, 4, 5, 6 }
```

The input signature of `map_func` is determined by the structure of each
element in this dataset. For example:

```python
# Each element is a <a href="../../tf/Tensor"><code>tf.Tensor</code></a> object.
a = { 1, 2, 3, 4, 5 }
# `map_func` takes a single argument of type <a href="../../tf/Tensor"><code>tf.Tensor</code></a> with the same
# shape and dtype.
result = a.map(lambda x: ...)

# Each element is a tuple containing two <a href="../../tf/Tensor"><code>tf.Tensor</code></a> objects.
b = { (1, "foo"), (2, "bar"), (3, "baz") }
# `map_func` takes two arguments of type <a href="../../tf/Tensor"><code>tf.Tensor</code></a>.
result = b.map(lambda x_int, y_str: ...)

# Each element is a dictionary mapping strings to <a href="../../tf/Tensor"><code>tf.Tensor</code></a> objects.
c = { {"a": 1, "b": "foo"}, {"a": 2, "b": "bar"}, {"a": 3, "b": "baz"} }
# `map_func` takes a single argument of type `dict` with the same keys as
# the elements.
result = c.map(lambda d: ...)
```

The value or values returned by `map_func` determine the structure of each
element in the returned dataset.

```python
# `map_func` returns a scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a> of type <a href="../../tf/float32"><code>tf.float32</code></a>.
def f(...):
  return tf.constant(37.0)
result = dataset.map(f)
result.output_classes == tf.Tensor
result.output_types == tf.float32
result.output_shapes == []  # scalar

# `map_func` returns two <a href="../../tf/Tensor"><code>tf.Tensor</code></a> objects.
def g(...):
  return tf.constant(37.0), tf.constant(["Foo", "Bar", "Baz"])
result = dataset.map(g)
result.output_classes == (tf.Tensor, tf.Tensor)
result.output_types == (tf.float32, tf.string)
result.output_shapes == ([], [3])

# Python primitives, lists, and NumPy arrays are implicitly converted to
# <a href="../../tf/Tensor"><code>tf.Tensor</code></a>.
def h(...):
  return 37.0, ["Foo", "Bar", "Baz"], np.array([1.0, 2.0] dtype=np.float64)
result = dataset.map(h)
result.output_classes == (tf.Tensor, tf.Tensor, tf.Tensor)
result.output_types == (tf.float32, tf.string, tf.float64)
result.output_shapes == ([], [3], [2])

# `map_func` can return nested structures.
def i(...):
  return {"a": 37.0, "b": [42, 16]}, "foo"
result.output_classes == ({"a": tf.Tensor, "b": tf.Tensor}, tf.Tensor)
result.output_types == ({"a": tf.float32, "b": tf.int32}, tf.string)
result.output_shapes == ({"a": [], "b": [2]}, [])
```

In addition to <a href="../../tf/Tensor"><code>tf.Tensor</code></a> objects, `map_func` can accept as arguments and
return <a href="../../tf/SparseTensor"><code>tf.SparseTensor</code></a> objects.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors (having
    shapes and types defined by `self.output_shapes` and
   `self.output_types`) to another nested structure of tensors.
* <b>`num_parallel_calls`</b>: (Optional.) A <a href="../../tf/int32"><code>tf.int32</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>,
    representing the number elements to process in parallel. If not
    specified, elements will be processed sequentially.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="padded_batch"><code>padded_batch</code></h3>

``` python
padded_batch(
    batch_size,
    padded_shapes,
    padding_values=None,
    drop_remainder=False
)
```

Combines consecutive elements of this dataset into padded batches.

This transformation combines multiple consecutive elements of the input
dataset into a single element.

Like <a href="../../tf/data/Dataset#batch"><code>tf.data.Dataset.batch</code></a>, the tensors in the resulting element will
have an additional outer dimension, which will be `batch_size` (or
`N % batch_size` for the last element if `batch_size` does not divide the
number of input elements `N` evenly and `drop_remainder` is `False`). If
your program depends on the batches having the same outer dimension, you
should set the `drop_remainder` argument to `True` to prevent the smaller
batch from being produced.

Unlike <a href="../../tf/data/Dataset#batch"><code>tf.data.Dataset.batch</code></a>, the input elements to be batched may have
different shapes, and this transformation will pad each component to the
respective shape in `padding_shapes`. The `padding_shapes` argument
determines the resulting shape for each dimension of each component in an
output element:

* If the dimension is a constant (e.g. `tf.Dimension(37)`), the component
  will be padded out to that length in that dimension.
* If the dimension is unknown (e.g. `tf.Dimension(None)`), the component
  will be padded out to the maximum length of all elements in that
  dimension.

See also <a href="../../tf/contrib/data/dense_to_sparse_batch"><code>tf.contrib.data.dense_to_sparse_batch</code></a>, which combines elements
that may have different shapes into a <a href="../../tf/SparseTensor"><code>tf.SparseTensor</code></a>.

#### Args:

* <b>`batch_size`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    consecutive elements of this dataset to combine in a single batch.
* <b>`padded_shapes`</b>: A nested structure of <a href="../../tf/TensorShape"><code>tf.TensorShape</code></a> or
    <a href="../../tf/int64"><code>tf.int64</code></a> vector tensor-like objects representing the shape
    to which the respective component of each input element should
    be padded prior to batching. Any unknown dimensions
    (e.g. `tf.Dimension(None)` in a <a href="../../tf/TensorShape"><code>tf.TensorShape</code></a> or `-1` in a
    tensor-like object) will be padded to the maximum size of that
    dimension in each batch.
* <b>`padding_values`</b>: (Optional.) A nested structure of scalar-shaped
    <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the padding values to use for the
    respective components.  Defaults are `0` for numeric types and
    the empty string for string types.
* <b>`drop_remainder`</b>: (Optional.) A <a href="../../tf/bool"><code>tf.bool</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing
    whether the last batch should be dropped in the case its has fewer than
    `batch_size` elements; the default behavior is not to drop the smaller
    batch.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="prefetch"><code>prefetch</code></h3>

``` python
prefetch(buffer_size)
```

Creates a `Dataset` that prefetches elements from this dataset.

#### Args:

* <b>`buffer_size`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
    maximum number of elements that will be buffered when prefetching.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="range"><code>range</code></h3>

``` python
range(*args)
```

Creates a `Dataset` of a step-separated range of values.

For example:

```python
Dataset.range(5) == [0, 1, 2, 3, 4]
Dataset.range(2, 5) == [2, 3, 4]
Dataset.range(1, 5, 2) == [1, 3]
Dataset.range(1, 5, -2) == []
Dataset.range(5, 1) == []
Dataset.range(5, 1, -2) == [5, 3]
```

#### Args:

* <b>`*args`</b>: follow same semantics as python's xrange.
    len(args) == 1 -> start = 0, stop = args[0], step = 1
    len(args) == 2 -> start = args[0], stop = args[1], step = 1
    len(args) == 3 -> start = args[0], stop = args[1, stop = args[2]


#### Returns:

* <b>`Dataset`</b>: A `RangeDataset`.


#### Raises:

* <b>`ValueError`</b>: if len(args) == 0.

<h3 id="repeat"><code>repeat</code></h3>

``` python
repeat(count=None)
```

Repeats this dataset `count` times.

NOTE: If this dataset is a function of global state (e.g. a random number
generator), then different repetitions may produce different elements.

#### Args:

* <b>`count`</b>: (Optional.) A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
    number of times the dataset should be repeated. The default behavior
    (if `count` is `None` or `-1`) is for the dataset be repeated
    indefinitely.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="shard"><code>shard</code></h3>

``` python
shard(
    num_shards,
    index
)
```

Creates a `Dataset` that includes only 1/`num_shards` of this dataset.

This dataset operator is very useful when running distributed training, as
it allows each worker to read a unique subset.

When reading a single input file, you can skip elements as follows:

```python
d = tf.data.TFRecordDataset(FLAGS.input_file)
d = d.shard(FLAGS.num_workers, FLAGS.worker_index)
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
d = d.shard(FLAGS.num_workers, FLAGS.worker_index)
d = d.repeat(FLAGS.num_epochs)
d = d.shuffle(FLAGS.shuffle_buffer_size)
d = d.interleave(tf.data.TFRecordDataset,
                 cycle_length=FLAGS.num_readers, block_length=1)
d = d.map(parser_fn, num_parallel_calls=FLAGS.num_map_threads)
```

#### Args:

* <b>`num_shards`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    shards operating in parallel.
* <b>`index`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the worker index.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.


#### Raises:

* <b>`ValueError`</b>: if `num_shards` or `index` are illegal values. Note: error
    checking is done on a best-effort basis, and aren't guaranteed to be
    caught upon dataset creation. (e.g. providing in a placeholder tensor
    bypasses the early checking, and will instead result in an error during
    a session.run call.)

<h3 id="shuffle"><code>shuffle</code></h3>

``` python
shuffle(
    buffer_size,
    seed=None,
    reshuffle_each_iteration=None
)
```

Randomly shuffles the elements of this dataset.

#### Args:

* <b>`buffer_size`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
    number of elements from this dataset from which the new
    dataset will sample.
* <b>`seed`</b>: (Optional.) A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the
    random seed that will be used to create the distribution. See
    <a href="../../tf/set_random_seed"><code>tf.set_random_seed</code></a> for behavior.
* <b>`reshuffle_each_iteration`</b>: (Optional.) A boolean, which if true indicates
    that the dataset should be pseudorandomly reshuffled each time it is
    iterated over. (Defaults to `True`.)


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="skip"><code>skip</code></h3>

``` python
skip(count)
```

Creates a `Dataset` that skips `count` elements from this dataset.

#### Args:

* <b>`count`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number
    of elements of this dataset that should be skipped to form the
    new dataset.  If `count` is greater than the size of this
    dataset, the new dataset will contain no elements.  If `count`
    is -1, skips the entire dataset.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="take"><code>take</code></h3>

``` python
take(count)
```

Creates a `Dataset` with at most `count` elements from this dataset.

#### Args:

* <b>`count`</b>: A <a href="../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    elements of this dataset that should be taken to form the new dataset.
    If `count` is -1, or if `count` is greater than the size of this
    dataset, the new dataset will contain all elements of this dataset.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.

<h3 id="zip"><code>zip</code></h3>

``` python
zip(datasets)
```

Creates a `Dataset` by zipping together the given datasets.

This method has similar semantics to the built-in `zip()` function
in Python, with the main difference being that the `datasets`
argument can be an arbitrary nested structure of `Dataset` objects.
For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3 }
b = { 4, 5, 6 }
c = { (7, 8), (9, 10), (11, 12) }
d = { 13, 14 }

# The nested structure of the `datasets` argument determines the
# structure of elements in the resulting dataset.
Dataset.zip((a, b)) == { (1, 4), (2, 5), (3, 6) }
Dataset.zip((b, a)) == { (4, 1), (5, 2), (6, 3) }

# The `datasets` argument may contain an arbitrary number of
# datasets.
Dataset.zip((a, b, c)) == { (1, 4, (7, 8)),
                            (2, 5, (9, 10)),
                            (3, 6, (11, 12)) }

# The number of elements in the resulting dataset is the same as
# the size of the smallest dataset in `datasets`.
Dataset.zip((a, d)) == { (1, 13), (2, 14) }
```

#### Args:

* <b>`datasets`</b>: A nested structure of datasets.


#### Returns:

* <b>`Dataset`</b>: A `Dataset`.



