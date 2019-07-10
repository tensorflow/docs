page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.logcosh

Logarithm of the hyperbolic cosine of the prediction error.

### Aliases:

* `tf.compat.v1.keras.losses.logcosh`
* `tf.compat.v2.keras.losses.logcosh`
* `tf.compat.v2.losses.logcosh`
* `tf.keras.losses.logcosh`

``` python
tf.keras.losses.logcosh(
    y_true,
    y_pred
)
```



Defined in [`python/keras/losses.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/losses.py).

<!-- Placeholder for "Used in" -->

`log(cosh(x))` is approximately equal to `(x ** 2) / 2` for small `x` and
to `abs(x) - log(2)` for large `x`. This means that 'logcosh' works mostly
like the mean squared error, but will not be so strongly affected by the
occasional wildly incorrect prediction.

#### Arguments:


* <b>`y_true`</b>: tensor of true targets.
* <b>`y_pred`</b>: tensor of predicted targets.


#### Returns:

Tensor with one scalar loss entry per sample.
