page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.model_from_yaml

``` python
tf.keras.models.model_from_yaml(
    yaml_string,
    custom_objects=None
)
```



Defined in [`tensorflow/python/keras/engine/saving.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/engine/saving.py).

Parses a yaml model configuration file and returns a model instance.

#### Arguments:

* <b>`yaml_string`</b>: YAML string encoding a model configuration.
* <b>`custom_objects`</b>: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.


#### Returns:

A Keras model instance (uncompiled).


#### Raises:

* <b>`ImportError`</b>: if yaml module is not found.