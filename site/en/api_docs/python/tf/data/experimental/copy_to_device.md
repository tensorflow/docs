page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.copy_to_device

A transformation that copies dataset elements to the given `target_device`.

### Aliases:

* `tf.compat.v1.data.experimental.copy_to_device`
* `tf.compat.v2.data.experimental.copy_to_device`
* `tf.data.experimental.copy_to_device`

``` python
tf.data.experimental.copy_to_device(
    target_device,
    source_device='/cpu:0'
)
```



Defined in [`python/data/experimental/ops/prefetching_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/prefetching_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`target_device`</b>: The name of a device to which elements will be copied.
* <b>`source_device`</b>: The original device on which `input_dataset` will be placed.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
