

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.models.model_from_config

``` python
model_from_config(
    config,
    custom_objects=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/models.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/models.py).

Instantiates a Keras model from its config.

#### Arguments:

* <b>`config`</b>: Configuration dictionary.
* <b>`custom_objects`</b>: Optional dictionary mapping names
        (strings) to custom classes or functions to be
        considered during deserialization.


#### Returns:

A Keras model instance (uncompiled).


#### Raises:

* <b>`TypeError`</b>: if `config` is not a dictionary.