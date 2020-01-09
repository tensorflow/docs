page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.dropout


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/dropout">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4535-L4552">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets entries in `x` to zero at random, while scaling the entire tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/dropout"><code>tf.compat.v1.keras.backend.dropout</code></a>
* <a href="/api_docs/python/tf/keras/backend/dropout"><code>tf.compat.v2.keras.backend.dropout</code></a>


``` python
tf.keras.backend.dropout(
    x,
    level,
    noise_shape=None,
    seed=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: tensor
* <b>`level`</b>: fraction of the entries in the tensor
    that will be set to 0.
* <b>`noise_shape`</b>: shape for randomly generated keep/drop flags,
    must be broadcastable to the shape of `x`
* <b>`seed`</b>: random seed to ensure determinism.


#### Returns:

A tensor.
