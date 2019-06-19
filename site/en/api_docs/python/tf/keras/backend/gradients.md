page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.gradients

``` python
tf.keras.backend.gradients(
    loss,
    variables
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Returns the gradients of `loss` w.r.t. `variables`.

#### Arguments:

* <b>`loss`</b>: Scalar tensor to minimize.
* <b>`variables`</b>: List of variables.


#### Returns:

A gradients tensor.