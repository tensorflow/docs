

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.gradients

``` python
tf.keras.backend.gradients(
    loss,
    variables
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/backend.py).

Returns the gradients of `variables` w.r.t. `loss`.

#### Arguments:

* <b>`loss`</b>: Scalar tensor to minimize.
* <b>`variables`</b>: List of variables.


#### Returns:

A gradients tensor.