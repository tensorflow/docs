page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.experimental.function_executor_type


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/experimental/function_executor_type">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/context.py#L1779-L1799">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Context manager for setting the executor of eager defined functions.

### Aliases:

* <a href="/api_docs/python/tf/experimental/function_executor_type"><code>tf.compat.v1.experimental.function_executor_type</code></a>
* <a href="/api_docs/python/tf/experimental/function_executor_type"><code>tf.compat.v2.experimental.function_executor_type</code></a>


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
