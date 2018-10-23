

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.optimizers.get

### `tf.contrib.keras.optimizers.get`

``` python
get(identifier)
```



Defined in [`tensorflow/contrib/keras/python/keras/optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/optimizers.py).

Retrieves a Keras Optimizer instance.

#### Arguments:

    identifier: Optimizer identifier, one of
        - String: name of an optimizer
        - Dictionary: configuration dictionary.
        - Keras Optimizer instance (it will be returned unchanged).
        - TensorFlow Optimizer instance
            (it will be wrapped as a Keras Optimizer).


#### Returns:

    A Keras Optimizer instance.


#### Raises:

    ValueError: If `identifier` cannot be interpreted.