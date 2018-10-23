

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.in_test_phase

### `tf.contrib.keras.backend.in_test_phase`

``` python
in_test_phase(
    x,
    alt,
    training=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Selects `x` in test phase, and `alt` otherwise.

Note that `alt` should have the *same shape* as `x`.

#### Arguments:

    x: What to return in test phase
        (tensor or callable that returns a tensor).
    alt: What to return otherwise
        (tensor or callable that returns a tensor).
    training: Optional scalar tensor
        (or Python boolean, or Python integer)
        specifing the learning phase.


#### Returns:

    Either `x` or `alt` based on `K.learning_phase`.