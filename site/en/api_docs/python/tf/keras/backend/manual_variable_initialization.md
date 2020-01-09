page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.manual_variable_initialization


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L252-L266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Sets the manual variable initialization flag.

### Aliases:

* `tf.compat.v1.keras.backend.manual_variable_initialization`
* `tf.compat.v2.keras.backend.manual_variable_initialization`


``` python
tf.keras.backend.manual_variable_initialization(value)
```



<!-- Placeholder for "Used in" -->

This boolean flag determines whether
variables should be initialized
as they are instantiated (default), or if
the user should handle the initialization
(e.g. via <a href="../../../tf/compat/v1/initialize_all_variables"><code>tf.compat.v1.initialize_all_variables()</code></a>).

#### Arguments:


* <b>`value`</b>: Python boolean.
