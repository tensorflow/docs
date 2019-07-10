page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.deserialize

Inverse of the `serialize` function.

### Aliases:

* `tf.compat.v1.keras.optimizers.deserialize`
* `tf.compat.v2.keras.optimizers.deserialize`
* `tf.compat.v2.optimizers.deserialize`
* `tf.keras.optimizers.deserialize`

``` python
tf.keras.optimizers.deserialize(
    config,
    custom_objects=None
)
```



Defined in [`python/keras/optimizers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizers.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`config`</b>: Optimizer configuration dictionary.
* <b>`custom_objects`</b>: Optional dictionary mapping names (strings) to custom
  objects (classes and functions) to be considered during deserialization.


#### Returns:

A Keras Optimizer instance.
