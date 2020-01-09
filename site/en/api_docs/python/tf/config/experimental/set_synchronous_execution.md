page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.set_synchronous_execution


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental/set_synchronous_execution">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L271-L293">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Specifies whether operations are executed synchronously or asynchronously.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental/set_synchronous_execution"><code>tf.compat.v1.config.experimental.set_synchronous_execution</code></a>
* <a href="/api_docs/python/tf/config/experimental/set_synchronous_execution"><code>tf.compat.v2.config.experimental.set_synchronous_execution</code></a>


``` python
tf.config.experimental.set_synchronous_execution(enable)
```



<!-- Placeholder for "Used in" -->

TensorFlow can execute operations synchronously or asynchronously. If
asynchronous execution is enabled, operations may return "non-ready" handles.

When `enable` is set to None, an appropriate value will be picked
automatically. The value picked may change between TensorFlow releases.

#### Args:


* <b>`enable`</b>: Whether operations should be dispatched synchronously.
  Valid values:
  - None: sets the system default.
  - True: executes each operation synchronously.
  - False: executes each operation asynchronously.
