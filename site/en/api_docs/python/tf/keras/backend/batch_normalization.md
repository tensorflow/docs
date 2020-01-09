page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.batch_normalization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/batch_normalization">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2500-L2556">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Applies batch normalization on x given mean, var, beta and gamma.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/batch_normalization"><code>tf.compat.v1.keras.backend.batch_normalization</code></a>
* <a href="/api_docs/python/tf/keras/backend/batch_normalization"><code>tf.compat.v2.keras.backend.batch_normalization</code></a>


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
