page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.tile


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/tile">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2886-L2900">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a tensor by tiling `x` by `n`.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/tile"><code>tf.compat.v1.keras.backend.tile</code></a>
* <a href="/api_docs/python/tf/keras/backend/tile"><code>tf.compat.v2.keras.backend.tile</code></a>


``` python
tf.keras.backend.tile(
    x,
    n
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable
* <b>`n`</b>: A list of integer. The length must be the same as the number of
    dimensions in `x`.


#### Returns:

A tiled tensor.
