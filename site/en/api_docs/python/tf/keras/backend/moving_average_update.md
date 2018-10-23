

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.moving_average_update

``` python
moving_average_update(
    x,
    value,
    momentum
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Compute the moving average of a variable.

#### Arguments:

* <b>`x`</b>: A Variable.
* <b>`value`</b>: A tensor with the same shape as `variable`.
* <b>`momentum`</b>: The moving average momentum.


#### Returns:

An Operation to update the variable.