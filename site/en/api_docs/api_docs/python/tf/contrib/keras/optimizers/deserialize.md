

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.optimizers.deserialize

``` python
deserialize(
    config,
    custom_objects=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/optimizers.py).

Inverse of the `serialize` function.

#### Arguments:

    config: Optimizer configuration dictionary.
    custom_objects: Optional dictionary mapping
        names (strings) to custom objects
        (classes and functions)
        to be considered during deserialization.


#### Returns:

    A Keras Optimizer instance.