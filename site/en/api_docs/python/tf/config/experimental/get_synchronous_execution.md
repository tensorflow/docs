page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_synchronous_execution


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental/get_synchronous_execution">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L258-L268">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets whether operations are executed synchronously or asynchronously.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental/get_synchronous_execution"><code>tf.compat.v1.config.experimental.get_synchronous_execution</code></a>
* <a href="/api_docs/python/tf/config/experimental/get_synchronous_execution"><code>tf.compat.v2.config.experimental.get_synchronous_execution</code></a>


``` python
tf.config.experimental.get_synchronous_execution()
```



<!-- Placeholder for "Used in" -->

TensorFlow can execute operations synchronously or asynchronously. If
asynchronous execution is enabled, operations may return "non-ready" handles.

#### Returns:

Current thread execution mode
