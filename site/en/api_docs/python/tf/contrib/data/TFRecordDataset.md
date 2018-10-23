

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.TFRecordDataset

### `class tf.contrib.data.TFRecordDataset`



Defined in [`tensorflow/contrib/data/python/ops/dataset_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/data/python/ops/dataset_ops.py).

A `Dataset` comprising records from one or more TFRecord files.

## Properties

<h3 id="output_shapes"><code>output_shapes</code></h3>



<h3 id="output_types"><code>output_types</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    filenames,
    compression_type=None
)
```

Creates a `TFRecordDataset`.

#### Args:

* <b>`filenames`</b>: A `tf.string` tensor containing one or more filenames.
* <b>`compression_type`</b>: A `tf.string` scalar evaluating to one of `""` (no
    compression), `"ZLIB"`, or `"GZIP"`.

<h3 id="batch"><code>batch</code></h3>

``` python
batch(batch_size)
```

Combines consecutive elements of this dataset into batches.

#### Args:

* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    consecutive elements of this dataset to combine in a single batch.


#### Returns:

  A `Dataset`.

<h3 id="dense_to_sparse_batch"><code>dense_to_sparse_batch</code></h3>

``` python
dense_to_sparse_batch(
    batch_size,
    row_shape
)
```

Batches ragged elements of this dataset into `tf.SparseTensor`s.

Like `Dataset.padded_batch()`, this method combines multiple
consecutive elements of this dataset, which might have different
shapes, into a single element. The resulting element has three
components (`indices`, `values`, and `dense_shape`), which
comprise a `tf.SparseTensor` that represents the same data. The
`row_shape` represents the dense shape of each row in the
resulting `tf.SparseTensor`, to which the effective batch size is
prepended. For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }

a.dense_to_sparse_batch(batch_size=2, row_shape=[6]) == {
    ([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]],  # indices
     ['a', 'b', 'c', 'a', 'b'],                 # values
     [2, 6]),                                   # dense_shape
    ([[2, 0], [2, 1], [2, 2], [2, 3]],
     ['a', 'b', 'c', 'd'],
     [1, 6])
}
```

#### Args:

* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the
    number of consecutive elements of this dataset to combine in a
    single batch.
* <b>`row_shape`</b>: A `tf.TensorShape` or `tf.int64` vector tensor-like
    object representing the equivalent dense shape of a row in the
    resulting `tf.SparseTensor`. Each element of this dataset must
    have the same rank as `row_shape`, and must have size less
    than or equal to `row_shape` in each dimension.


#### Returns:

  A `Dataset`.

<h3 id="enumerate"><code>enumerate</code></h3>

``` python
enumerate(start=0)
```

Enumerate the elements of this dataset.  Similar to python's `enumerate`.

For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3 }
b = { (7, 8), (9, 10), (11, 12) }

# The nested structure of the `datasets` argument determines the
# structure of elements in the resulting dataset.
a.enumerate(start=5) == { (5, 1), (6, 2), (7, 3) }
b.enumerate() == { (0, (7, 8)), (1, (9, 10)), (2, (11, 12)) }

#### Args:

* <b>`start`</b>: A `tf.int64` scalar `tf.Tensor`, representing the start
    value for enumeration.


#### Returns:

  A `Dataset`.

<h3 id="filter"><code>filter</code></h3>

``` python
filter(predicate)
```

Filters this dataset according to `predicate`.

#### Args:

* <b>`predicate`</b>: A function mapping a nested structure of tensors (having shapes
    and types defined by `self.output_shapes` and `self.output_types`) to a
    scalar `tf.bool` tensor.


#### Returns:

  A `Dataset`.

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

  A `Dataset`.

<h3 id="from_sparse_tensor_slices"><code>from_sparse_tensor_slices</code></h3>

``` python
from_sparse_tensor_slices(sparse_tensor)
```

Splits each rank-N `tf.SparseTensor` in this dataset row-wise.

#### Args:

* <b>`sparse_tensor`</b>: A `tf.SparseTensor`.


#### Returns:

  A `Dataset` of rank-(N-1) sparse tensors.

<h3 id="from_tensor_slices"><code>from_tensor_slices</code></h3>

``` python
from_tensor_slices(tensors)
```

Creates a `Dataset` whose elements are slices of the given tensors.

#### Args:

* <b>`tensors`</b>: A nested structure of tensors, each having the same size in the
    0th dimension.


#### Returns:

  A `Dataset`.

<h3 id="from_tensors"><code>from_tensors</code></h3>

``` python
from_tensors(tensors)
```

Creates a `Dataset` with a single element, comprising the given tensors.

#### Args:

* <b>`tensors`</b>: A nested structure of tensors.


#### Returns:

  A `Dataset`.

<h3 id="group_by_window"><code>group_by_window</code></h3>

``` python
group_by_window(
    key_func,
    reduce_func,
    window_size
)
```

Performs a windowed "group-by" operation on this dataset.

This method maps each consecutive element in this dataset to a key
using `key_func` and groups the elements by key. It then applies
`reduce_func` to at most `window_size` elements matching the same
key. All execpt the final window for each key will contain
`window_size` elements; the final window may be smaller.

#### Args:

* <b>`key_func`</b>: A function mapping a nested structure of tensors
    (having shapes and types defined by `self.output_shapes` and
    `self.output_types`) to a scalar `tf.int64` tensor.
* <b>`reduce_func`</b>: A function mapping a key and a dataset of up to `batch_size`
    consecutive elements matching that key to another dataset.
* <b>`window_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    consecutive elements matching the same key to combine in a single
    batch, which will be passed to `reduce_func`.


#### Returns:

  A `Dataset`.

<h3 id="make_dataset_resource"><code>make_dataset_resource</code></h3>

``` python
make_dataset_resource()
```



<h3 id="make_initializable_iterator"><code>make_initializable_iterator</code></h3>

``` python
make_initializable_iterator(shared_name=None)
```

Creates an `Iterator` for enumerating the elements of this dataset.

**N.B.** The returned iterator will be in an uninitialized state,
and you must run the `iterator.initializer` operation before using it.

#### Args:

* <b>`shared_name`</b>: (Optional.) If non-empty, this iterator will be shared under
    the given name across multiple sessions that share the same devices
    (e.g. when using a remote server).



#### Returns:

  An `Iterator` over the elements of this dataset.

<h3 id="make_one_shot_iterator"><code>make_one_shot_iterator</code></h3>

``` python
make_one_shot_iterator()
```

Creates an `Iterator` for enumerating the elements of this dataset.

**N.B.** The returned iterator will be initialized automatically.
A "one-shot" iterator does not currently support re-initialization.

#### Returns:

  An `Iterator` over the elements of this dataset.

<h3 id="map"><code>map</code></h3>

``` python
map(
    map_func,
    num_threads=None,
    output_buffer_size=None
)
```

Maps `map_func` across this datset.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors (having
    shapes and types defined by `self.output_shapes` and
   `self.output_types`) to another nested structure of tensors.
* <b>`num_threads`</b>: (Optional.) A `tf.int32` scalar `tf.Tensor`, representing
    the number of threads to use for processing elements in parallel. If
    not specified, elements will be processed sequentially without
    buffering.
* <b>`output_buffer_size`</b>: (Optional.) A `tf.int64` scalar `tf.Tensor`,
    representing the maximum number of processed elements that will be
    buffered when processing in parallel.


#### Returns:

  A `Dataset`.

<h3 id="padded_batch"><code>padded_batch</code></h3>

``` python
padded_batch(
    batch_size,
    padded_shapes,
    padding_values=None
)
```

Combines consecutive elements of this dataset into padded batches.

Like `Dataset.dense_to_sparse_batch()`, this method combines
multiple consecutive elements of this dataset, which might have
different shapes, into a single element. The tensors in the
resulting element have an additional outer dimension, and are
padded to the respective shape in `padded_shapes`.

#### Args:

* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    consecutive elements of this dataset to combine in a single batch.
* <b>`padded_shapes`</b>: A nested structure of `tf.TensorShape` or
    `tf.int64` vector tensor-like objects representing the shape
    to which the respective component of each input element should
    be padded prior to batching. Any unknown dimensions
    (e.g. `tf.Dimension(None)` in a `tf.TensorShape` or `-1` in a
    tensor-like object) will be padded to the maximum size of that
    dimension in each batch.
* <b>`padding_values`</b>: (Optional.) A nested structure of scalar-shaped
    `tf.Tensor`, representing the padding values to use for the
    respective components.  Defaults are `0` for numeric types and
    the empty string for string types.


#### Returns:

  A `Dataset`.

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

  *args: follow same semantics as python's xrange.
    len(args) == 1 -> start = 0, stop = args[0], step = 1
    len(args) == 2 -> start = args[0], stop = args[1], step = 1
    len(args) == 3 -> start = args[0], stop = args[1, stop = args[2]


#### Returns:

  A `RangeDataset`.


#### Raises:

* <b>`ValueError`</b>: if len(args) == 0.

<h3 id="read_batch_features"><code>read_batch_features</code></h3>

``` python
read_batch_features(
    file_pattern,
    batch_size,
    features,
    reader,
    reader_args=None,
    randomize_input=True,
    num_epochs=None,
    capacity=10000
)
```

Reads batches of Examples.

#### Args:

* <b>`file_pattern`</b>: A string pattern or a placeholder with list of filenames.
* <b>`batch_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    consecutive elements of this dataset to combine in a single batch.
* <b>`features`</b>: A `dict` mapping feature keys to `FixedLenFeature` or
    `VarLenFeature` values. See `tf.parse_example`.
* <b>`reader`</b>: A function or class that can be called with a `filenames` tensor
    and (optional) `reader_args` and returns a `Dataset` of serialized
    Examples.
* <b>`reader_args`</b>: Additional arguments to pass to the reader class.
* <b>`randomize_input`</b>: Whether the input should be randomized.
* <b>`num_epochs`</b>: Integer specifying the number of times to read through the
    dataset. If None, cycles through the dataset forever.
* <b>`capacity`</b>: Capacity of the ShuffleDataset.


#### Returns:

  A `Dataset`.

<h3 id="repeat"><code>repeat</code></h3>

``` python
repeat(count=None)
```

Repeats this dataset `count` times.

#### Args:

* <b>`count`</b>: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the
    number of times the elements of this dataset should be repeated. The
    default behavior (if `count` is `None` or `-1`) is for the elements to
    be repeated indefinitely.


#### Returns:

  A `Dataset`.

<h3 id="shuffle"><code>shuffle</code></h3>

``` python
shuffle(
    buffer_size,
    seed=None
)
```

Randomly shuffles the elements of this dataset.

#### Args:

* <b>`buffer_size`</b>: A `tf.int64` scalar `tf.Tensor`, representing the
    number of elements from this dataset from which the new
    dataset will sample.
* <b>`seed`</b>: (Optional.) A `tf.int64` scalar `tf.Tensor`, representing the
    random seed that will be used to create the distribution. See
    [`tf.set_random_seed`](../../../tf/set_random_seed) for behavior.


#### Returns:

  A `Dataset`.

<h3 id="skip"><code>skip</code></h3>

``` python
skip(count)
```

Creates a `Dataset` that skips `count` elements from this dataset.

#### Args:

* <b>`count`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number
    of elements of this dataset that should be skipped to form the
    new dataset.  If `count` is greater than the size of this
    dataset, the new dataset will contain no elements.  If `count`
    is -1, skips the entire dataset.


#### Returns:

  A `Dataset`.

<h3 id="take"><code>take</code></h3>

``` python
take(count)
```

Creates a `Dataset` with at most `count` elements from this dataset.

#### Args:

* <b>`count`</b>: A `tf.int64` scalar `tf.Tensor`, representing the number of
    elements of this dataset that should be taken to form the new dataset.
    If `count` is -1, or if `count` is greater than the size of this
    dataset, the new dataset will contain all elements of this dataset.


#### Returns:

  A `Dataset`.

<h3 id="unbatch"><code>unbatch</code></h3>

``` python
unbatch()
```

Splits elements of this dataset into sequences of consecutive elements.

For example, if elements of this dataset are shaped `[B, a0, a1, ...]`,
where `B` may vary from element to element, then for each element in
this dataset, the unbatched dataset will contain `B` consecutive elements
of shape `[a0, a1, ...]`.

#### Returns:

  A `Dataset`.

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
Dataset.zip((a, b, c) == { (1, 4, (7, 8)),
                           (2, 5, (9, 10)),
                           (3, 6, (11, 12)) }

# The number of elements in the resulting dataset is the same as
# the size of the smallest dataset in `datasets`.
Dataset.zip((a, d)) == { (1, 13), (2, 14) }
```

#### Args:

* <b>`datasets`</b>: A nested structure of datasets.


#### Returns:

  A `Dataset`.



