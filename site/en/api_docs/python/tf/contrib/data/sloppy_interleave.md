

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.sloppy_interleave

``` python
tf.contrib.data.sloppy_interleave(
    map_func,
    cycle_length,
    block_length=1
)
```



Defined in [`tensorflow/contrib/data/python/ops/interleave_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/data/python/ops/interleave_ops.py).

A non-deterministic version of the `Dataset.interleave()` transformation. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.contrib.data.parallel_interleave(..., sloppy=True)`.

`sloppy_interleave()` maps `map_func` across `dataset`, and
non-deterministically interleaves the results.

The resulting dataset is almost identical to `interleave`. The key
difference is that if retrieving a value from a given output iterator would
cause `get_next` to block, that iterator will be skipped, and consumed
when next available. If consuming from all iterators would cause the
`get_next` call to block, the `get_next` call blocks until the first value is
available.

If the underlying datasets produce elements as fast as they are consumed, the
`sloppy_interleave` transformation behaves identically to `interleave`.
However, if an underlying dataset would block the consumer,
`sloppy_interleave` can violate the round-robin order (that `interleave`
strictly obeys), producing an element from a different underlying
dataset instead.

Example usage:

```python
# Preprocess 4 files concurrently.
filenames = tf.data.Dataset.list_files("/path/to/data/train*.tfrecords")
dataset = filenames.apply(
    tf.contrib.data.sloppy_interleave(
        lambda filename: tf.data.TFRecordDataset(filename),
        cycle_length=4))
```

WARNING: The order of elements in the resulting dataset is not
deterministic. Use `Dataset.interleave()` if you want the elements to have a
deterministic order.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors (having shapes
    and types defined by `self.output_shapes` and `self.output_types`) to a
    `Dataset`.
* <b>`cycle_length`</b>: The number of input `Dataset`s to interleave from in parallel.
* <b>`block_length`</b>: The number of consecutive elements to pull from an input
    `Dataset` before advancing to the next input `Dataset`. Note:
    `sloppy_interleave` will skip the remainder of elements in the
    `block_length` in order to avoid blocking.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.