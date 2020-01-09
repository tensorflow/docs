page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.get_device_policy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental/get_device_policy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L189-L212">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Gets the current device policy.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental/get_device_policy"><code>tf.compat.v1.config.experimental.get_device_policy</code></a>
* <a href="/api_docs/python/tf/config/experimental/get_device_policy"><code>tf.compat.v2.config.experimental.get_device_policy</code></a>


``` python
tf.config.experimental.get_device_policy()
```



<!-- Placeholder for "Used in" -->

The device policy controls how operations requiring inputs on a specific
device (e.g., on GPU:0) handle inputs on a different device (e.g. GPU:1).

This function only gets the device policy for the current thread. Any
subsequently started thread will again use the default policy.

#### Returns:

Current thread device policy
