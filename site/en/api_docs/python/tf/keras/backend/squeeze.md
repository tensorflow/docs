page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.squeeze


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/squeeze">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L2969-L2980">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Removes a 1-dimension from the tensor at index "axis".

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/squeeze"><code>tf.compat.v1.keras.backend.squeeze</code></a>
* <a href="/api_docs/python/tf/keras/backend/squeeze"><code>tf.compat.v2.keras.backend.squeeze</code></a>


``` python
tf.keras.backend.squeeze(
    x,
    axis
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: Axis to drop.


#### Returns:

A tensor with the same data as `x` but reduced dimensions.
