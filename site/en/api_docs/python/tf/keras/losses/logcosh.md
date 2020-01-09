page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.logcosh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/losses/logcosh">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/losses.py#L913-L935">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Logarithm of the hyperbolic cosine of the prediction error.

### Aliases:

* <a href="/api_docs/python/tf/keras/losses/logcosh"><code>tf.compat.v1.keras.losses.logcosh</code></a>
* <a href="/api_docs/python/tf/keras/losses/logcosh"><code>tf.compat.v2.keras.losses.logcosh</code></a>
* <a href="/api_docs/python/tf/keras/losses/logcosh"><code>tf.compat.v2.losses.logcosh</code></a>


``` python
tf.keras.losses.logcosh(
    y_true,
    y_pred
)
```



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
