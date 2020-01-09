page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.moving_average_update


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/moving_average_update">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1604-L1623">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compute the moving average of a variable.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/moving_average_update"><code>tf.compat.v1.keras.backend.moving_average_update</code></a>
* <a href="/api_docs/python/tf/keras/backend/moving_average_update"><code>tf.compat.v2.keras.backend.moving_average_update</code></a>


``` python
tf.keras.backend.moving_average_update(
    x,
    value,
    momentum
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A Variable.
* <b>`value`</b>: A tensor with the same shape as `variable`.
* <b>`momentum`</b>: The moving average momentum.


#### Returns:

An Operation to update the variable.
