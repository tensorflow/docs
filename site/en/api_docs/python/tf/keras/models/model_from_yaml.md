

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.models.model_from_yaml

``` python
model_from_yaml(
    yaml_string,
    custom_objects=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/models.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/models.py).

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