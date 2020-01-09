page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.executing_eagerly


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/executing_eagerly">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/eager/context.py#L1591-L1602">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns True if the current thread has eager execution enabled.

### Aliases:

* <a href="/api_docs/python/tf/executing_eagerly"><code>tf.compat.v1.executing_eagerly</code></a>
* <a href="/api_docs/python/tf/executing_eagerly"><code>tf.compat.v2.executing_eagerly</code></a>
* <a href="/api_docs/python/tf/executing_eagerly"><code>tf.contrib.eager.executing_eagerly</code></a>
* <a href="/api_docs/python/tf/executing_eagerly"><code>tf.contrib.eager.in_eager_mode</code></a>


``` python
tf.executing_eagerly()
```



<!-- Placeholder for "Used in" -->

Eager execution is typically enabled via
<a href="../tf/enable_eager_execution"><code>tf.compat.v1.enable_eager_execution</code></a>, but may also be enabled within the
context of a Python function via tf.contrib.eager.py_func.
