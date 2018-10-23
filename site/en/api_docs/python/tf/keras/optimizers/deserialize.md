

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.optimizers.deserialize

``` python
tf.keras.optimizers.deserialize(
    config,
    custom_objects=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/optimizers.py).

Inverse of the `serialize` function.

#### Arguments:

* <b>`config`</b>: Optimizer configuration dictionary.
* <b>`custom_objects`</b>: Optional dictionary mapping
        names (strings) to custom objects
        (classes and functions)
        to be considered during deserialization.


#### Returns:

A Keras Optimizer instance.