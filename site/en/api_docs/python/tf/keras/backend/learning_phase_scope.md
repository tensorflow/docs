page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.learning_phase_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/learning_phase_scope">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L355-L397">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Provides a scope within which the learning phase is equal to `value`.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/learning_phase_scope"><code>tf.compat.v1.keras.backend.learning_phase_scope</code></a>
* <a href="/api_docs/python/tf/keras/backend/learning_phase_scope"><code>tf.compat.v2.keras.backend.learning_phase_scope</code></a>


``` python
tf.keras.backend.learning_phase_scope(value)
```



<!-- Placeholder for "Used in" -->

The learning phase gets restored to its original value upon exiting the scope.

#### Arguments:


* <b>`value`</b>: Learning phase value, either 0 or 1 (integers).


#### Yields:

None.



#### Raises:


* <b>`ValueError`</b>: if `value` is neither `0` nor `1`.
