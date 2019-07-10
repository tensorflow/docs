page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.layers.deserialize

Instantiates a layer from a config dictionary.

### Aliases:

* `tf.compat.v1.keras.layers.deserialize`
* `tf.compat.v2.keras.layers.deserialize`
* `tf.keras.layers.deserialize`

``` python
tf.keras.layers.deserialize(
    config,
    custom_objects=None
)
```



Defined in [`python/keras/layers/serialization.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/layers/serialization.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`config`</b>: dict of the form {'class_name': str, 'config': dict}
* <b>`custom_objects`</b>: dict mapping class names (or function names)
    of custom (non-Keras) objects to class/functions


#### Returns:

Layer instance (may be Model, Sequential, Network, Layer...)
