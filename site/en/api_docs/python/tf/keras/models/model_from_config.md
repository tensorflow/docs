

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.model_from_config

``` python
tf.keras.models.model_from_config(
    config,
    custom_objects=None
)
```



Defined in [`tensorflow/python/keras/engine/saving.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/engine/saving.py).

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