page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.batch_normalization

Applies batch normalization on x given mean, var, beta and gamma.

### Aliases:

* `tf.compat.v1.keras.backend.batch_normalization`
* `tf.compat.v2.keras.backend.batch_normalization`
* `tf.keras.backend.batch_normalization`

``` python
tf.keras.backend.batch_normalization(
    x,
    mean,
    var,
    beta,
    gamma,
    axis=-1,
    epsilon=0.001
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

I.e. returns:
`output = (x - mean) / (sqrt(var) + epsilon) * gamma + beta`

#### Arguments:


* <b>`x`</b>: Input tensor or variable.
* <b>`mean`</b>: Mean of batch.
* <b>`var`</b>: Variance of batch.
* <b>`beta`</b>: Tensor with which to center the input.
* <b>`gamma`</b>: Tensor by which to scale the input.
* <b>`axis`</b>: Integer, the axis that should be normalized.
    (typically the features axis).
* <b>`epsilon`</b>: Fuzz factor.


#### Returns:

A tensor.
