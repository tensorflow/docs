page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.parallel_interleave

``` python
tf.contrib.data.parallel_interleave(
    map_func,
    cycle_length,
    block_length=1,
    sloppy=False,
    buffer_output_elements=None,
    prefetch_input_elements=None
)
```



Defined in [`tensorflow/contrib/data/python/ops/interleave_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/data/python/ops/interleave_ops.py).

A parallel version of the `Dataset.interleave()` transformation. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.experimental.parallel_interleave(...)`.

`parallel_interleave()` maps `map_func` across its input to produce nested
datasets, and outputs their elements interleaved. Unlike
<a href="../../../tf/data/Dataset#interleave"><code>tf.data.Dataset.interleave</code></a>, it gets elements from `cycle_length` nested
datasets in parallel, which increases the throughput, especially in the
presence of stragglers. Furthermore, the `sloppy` argument can be used to
improve performance, by relaxing the requirement that the outputs are produced
in a deterministic order, and allowing the implementation to skip over nested
datasets whose elements are not readily available when requested.

Example usage:

```python
# Preprocess 4 files concurrently.
filenames = tf.data.Dataset.list_files("/path/to/data/train*.tfrecords")
dataset = filenames.apply(
    tf.contrib.data.parallel_interleave(
        lambda filename: tf.data.TFRecordDataset(filename),
        cycle_length=4))
```

WARNING: If `sloppy` is `True`, the order of produced elements is not
deterministic.

#### Args:

* <b>`map_func`</b>: A function mapping a nested structure of tensors to a `Dataset`.
* <b>`cycle_length`</b>: The number of input `Dataset`s to interleave from in parallel.
* <b>`block_length`</b>: The number of consecutive elements to pull from an input
    `Dataset` before advancing to the next input `Dataset`.
* <b>`sloppy`</b>: If false, elements are produced in deterministic order. Otherwise,
    the implementation is allowed, for the sake of expediency, to produce
    elements in a non-deterministic order.
* <b>`buffer_output_elements`</b>: The number of elements each iterator being
    interleaved should buffer (similar to the `.prefetch()` transformation for
    each interleaved iterator).
* <b>`prefetch_input_elements`</b>: The number of input elements to transform to
    iterators before they are needed for interleaving.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.