page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.hard_sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/hard_sigmoid">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4500-L4519">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Segment-wise linear approximation of sigmoid.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/hard_sigmoid"><code>tf.compat.v1.keras.backend.hard_sigmoid</code></a>
* <a href="/api_docs/python/tf/keras/backend/hard_sigmoid"><code>tf.compat.v2.keras.backend.hard_sigmoid</code></a>


``` python
tf.keras.backend.hard_sigmoid(x)
```



<!-- Placeholder for "Used in" -->

Faster than sigmoid.
Returns `0.` if `x < -2.5`, `1.` if `x > 2.5`.
In `-2.5 <= x <= 2.5`, returns `0.2 * x + 0.5`.

#### Arguments:


* <b>`x`</b>: A tensor or variable.


#### Returns:

A tensor.
