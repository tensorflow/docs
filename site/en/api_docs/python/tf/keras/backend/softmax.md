page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.softmax


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/softmax">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4280-L4292">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Softmax of a tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/softmax"><code>tf.compat.v1.keras.backend.softmax</code></a>
* <a href="/api_docs/python/tf/keras/backend/softmax"><code>tf.compat.v2.keras.backend.softmax</code></a>


``` python
tf.keras.backend.softmax(
    x,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: The dimension softmax would be performed on.
    The default is -1 which indicates the last dimension.


#### Returns:

A tensor.
