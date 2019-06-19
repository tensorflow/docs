page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.batch_normalization

``` python
tf.keras.backend.batch_normalization(
    x,
    mean,
    var,
    beta,
    gamma,
    epsilon=0.001
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Applies batch normalization on x given mean, var, beta and gamma.

I.e. returns:
`output = (x - mean) / (sqrt(var) + epsilon) * gamma + beta`

#### Arguments:

* <b>`x`</b>: Input tensor or variable.
* <b>`mean`</b>: Mean of batch.
* <b>`var`</b>: Variance of batch.
* <b>`beta`</b>: Tensor with which to center the input.
* <b>`gamma`</b>: Tensor by which to scale the input.
* <b>`epsilon`</b>: Fuzz factor.


#### Returns:

A tensor.