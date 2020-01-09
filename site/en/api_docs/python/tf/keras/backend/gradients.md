page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.gradients


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/gradients">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L3681-L3693">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the gradients of `loss` w.r.t. `variables`.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/gradients"><code>tf.compat.v1.keras.backend.gradients</code></a>
* <a href="/api_docs/python/tf/keras/backend/gradients"><code>tf.compat.v2.keras.backend.gradients</code></a>


``` python
tf.keras.backend.gradients(
    loss,
    variables
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`loss`</b>: Scalar tensor to minimize.
* <b>`variables`</b>: List of variables.


#### Returns:

A gradients tensor.
