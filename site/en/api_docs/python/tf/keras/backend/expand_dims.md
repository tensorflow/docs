page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.expand_dims


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/expand_dims">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2955-L2966">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds a 1-sized dimension at index "axis".

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/expand_dims"><code>tf.compat.v1.keras.backend.expand_dims</code></a>
* <a href="/api_docs/python/tf/keras/backend/expand_dims"><code>tf.compat.v2.keras.backend.expand_dims</code></a>


``` python
tf.keras.backend.expand_dims(
    x,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: Position where to add a new axis.


#### Returns:

A tensor with expanded dimensions.
