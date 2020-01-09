page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.experimental.function_executor_type


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/context.py#L1786-L1806">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Context manager for setting the executor of eager defined functions.

### Aliases:

* `tf.compat.v1.experimental.function_executor_type`
* `tf.compat.v2.experimental.function_executor_type`


``` python
tf.experimental.function_executor_type(executor_type)
```



<!-- Placeholder for "Used in" -->

Eager defined functions are functions decorated by tf.contrib.eager.defun.

#### Args:


* <b>`executor_type`</b>: a string for the name of the executor to be used to execute
  functions defined by tf.contrib.eager.defun.


#### Yields:

Context manager for setting the executor of eager defined functions.
