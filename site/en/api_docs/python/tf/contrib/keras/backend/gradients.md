

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.gradients

### `tf.contrib.keras.backend.gradients`

``` python
gradients(
    loss,
    variables
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Returns the gradients of `variables` w.r.t. `loss`.

#### Arguments:

    loss: Scalar tensor to minimize.
    variables: List of variables.


#### Returns:

    A gradients tensor.