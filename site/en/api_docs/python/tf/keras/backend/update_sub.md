page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.update_sub


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/update_sub">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1590-L1601">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Update the value of `x` by subtracting `decrement`.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/update_sub"><code>tf.compat.v1.keras.backend.update_sub</code></a>
* <a href="/api_docs/python/tf/keras/backend/update_sub"><code>tf.compat.v2.keras.backend.update_sub</code></a>


``` python
tf.keras.backend.update_sub(
    x,
    decrement
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A Variable.
* <b>`decrement`</b>: A tensor of same shape as `x`.


#### Returns:

The variable `x` updated.
