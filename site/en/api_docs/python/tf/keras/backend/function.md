page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.function


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/function">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L3648-L3678">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Instantiates a Keras function.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/function"><code>tf.compat.v1.keras.backend.function</code></a>
* <a href="/api_docs/python/tf/keras/backend/function"><code>tf.compat.v2.keras.backend.function</code></a>


``` python
tf.keras.backend.function(
    inputs,
    outputs,
    updates=None,
    name=None,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`inputs`</b>: List of placeholder tensors.
* <b>`outputs`</b>: List of output tensors.
* <b>`updates`</b>: List of update ops.
* <b>`name`</b>: String, name of function.
* <b>`**kwargs`</b>: Passed to <a href="../../../tf/Session#run"><code>tf.Session.run</code></a>.


#### Returns:

Output values as Numpy arrays.



#### Raises:


* <b>`ValueError`</b>: if invalid kwargs are passed in or if in eager execution.
