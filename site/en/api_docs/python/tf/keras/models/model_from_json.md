page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.model_from_json

``` python
tf.keras.models.model_from_json(
    json_string,
    custom_objects=None
)
```



Defined in [`tensorflow/python/keras/engine/saving.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/engine/saving.py).

Parses a JSON model configuration file and returns a model instance.

#### Arguments:

* <b>`json_string`</b>: JSON string encoding a model configuration.
* <b>`custom_objects`</b>: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.


#### Returns:

A Keras model instance (uncompiled).