page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.is_variable_initialized


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/variables.py#L3273-L3285">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Tests if a variable has been initialized.

### Aliases:

* <a href="/api_docs/python/tf/is_variable_initialized"><code>tf.compat.v1.is_variable_initialized</code></a>


``` python
tf.is_variable_initialized(variable)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`variable`</b>: A `Variable`.


#### Returns:

Returns a scalar boolean Tensor, `True` if the variable has been
initialized, `False` otherwise.



**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.
