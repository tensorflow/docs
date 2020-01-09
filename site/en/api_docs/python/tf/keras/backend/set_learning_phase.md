page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.set_learning_phase


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/set_learning_phase">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L334-L352">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the learning phase to a fixed value.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/set_learning_phase"><code>tf.compat.v1.keras.backend.set_learning_phase</code></a>
* <a href="/api_docs/python/tf/keras/backend/set_learning_phase"><code>tf.compat.v2.keras.backend.set_learning_phase</code></a>


``` python
tf.keras.backend.set_learning_phase(value)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`value`</b>: Learning phase value, either 0 or 1 (integers).


#### Raises:


* <b>`ValueError`</b>: if `value` is neither `0` nor `1`.
