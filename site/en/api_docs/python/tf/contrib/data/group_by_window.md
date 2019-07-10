page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.group_by_window

``` python
tf.contrib.data.group_by_window(
    key_func,
    reduce_func,
    window_size=None,
    window_size_func=None
)
```



Defined in [`tensorflow/contrib/data/python/ops/grouping.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/data/python/ops/grouping.py).

See the guide: [Dataset Input Pipeline > Transformations on existing datasets](../../../../../api_guides/python/input_dataset#Transformations_on_existing_datasets)

A transformation that groups windows of elements by key and reduces them.

This transformation maps each consecutive element in a dataset to a key
using `key_func` and groups the elements by key. It then applies
`reduce_func` to at most `window_size_func(key)` elements matching the same
key. All except the final window for each key will contain
`window_size_func(key)` elements; the final window may be smaller.

You may provide either a constant `window_size` or a window size determined by
the key through `window_size_func`.

#### Args:

* <b>`key_func`</b>: A function mapping a nested structure of tensors
    (having shapes and types defined by `self.output_shapes` and
    `self.output_types`) to a scalar <a href="../../../tf/int64"><code>tf.int64</code></a> tensor.
* <b>`reduce_func`</b>: A function mapping a key and a dataset of up to `window_size`
    consecutive elements matching that key to another dataset.
* <b>`window_size`</b>: A <a href="../../../tf/int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of
    consecutive elements matching the same key to combine in a single
    batch, which will be passed to `reduce_func`. Mutually exclusive with
    `window_size_func`.
* <b>`window_size_func`</b>: A function mapping a key to a <a href="../../../tf/int64"><code>tf.int64</code></a> scalar
    <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the number of consecutive elements matching
    the same key to combine in a single batch, which will be passed to
    `reduce_func`. Mutually exclusive with `window_size`.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.


#### Raises:

* <b>`ValueError`</b>: if neither or both of {`window_size`, `window_size_func`} are
    passed.