page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.prefetch_to_device

A transformation that prefetches dataset values to the given `device`. (deprecated)

``` python
tf.contrib.data.prefetch_to_device(
    device,
    buffer_size=None
)
```



Defined in [`contrib/data/python/ops/prefetching_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/prefetching_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/prefetch_to_device"><code>tf.data.experimental.prefetch_to_device(...)</code></a>.

NOTE: Although the transformation creates a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>, the
transformation must be the final `Dataset` in the input pipeline.

#### Args:


* <b>`device`</b>: A string. The name of a device to which elements will be prefetched.
* <b>`buffer_size`</b>: (Optional.) The number of elements to buffer on `device`.
  Defaults to an automatically chosen value.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
