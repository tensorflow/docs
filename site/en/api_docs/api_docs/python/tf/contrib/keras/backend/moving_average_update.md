

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.moving_average_update

``` python
moving_average_update(
    x,
    value,
    momentum
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Compute the moving average of a variable.

#### Arguments:

    x: A Variable.
    value: A tensor with the same shape as `variable`.
    momentum: The moving average momentum.


#### Returns:

    An Operation to update the variable.