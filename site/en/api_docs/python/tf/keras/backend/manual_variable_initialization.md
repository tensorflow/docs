page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.manual_variable_initialization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/manual_variable_initialization">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L247-L261">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the manual variable initialization flag.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/manual_variable_initialization"><code>tf.compat.v1.keras.backend.manual_variable_initialization</code></a>
* <a href="/api_docs/python/tf/keras/backend/manual_variable_initialization"><code>tf.compat.v2.keras.backend.manual_variable_initialization</code></a>


``` python
tf.keras.backend.manual_variable_initialization(value)
```



<!-- Placeholder for "Used in" -->

This boolean flag determines whether
variables should be initialized
as they are instantiated (default), or if
the user should handle the initialization
(e.g. via <a href="../../../tf/initialize_all_variables"><code>tf.compat.v1.initialize_all_variables()</code></a>).

#### Arguments:


* <b>`value`</b>: Python boolean.
