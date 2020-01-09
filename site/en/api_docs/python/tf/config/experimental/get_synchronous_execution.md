page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_synchronous_execution


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/config.py#L258-L268">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets whether operations are executed synchronously or asynchronously.

### Aliases:

* `tf.compat.v1.config.experimental.get_synchronous_execution`
* `tf.compat.v2.config.experimental.get_synchronous_execution`


``` python
tf.config.experimental.get_synchronous_execution()
```



<!-- Placeholder for "Used in" -->

TensorFlow can execute operations synchronously or asynchronously. If
asynchronous execution is enabled, operations may return "non-ready" handles.

#### Returns:

Current thread execution mode
