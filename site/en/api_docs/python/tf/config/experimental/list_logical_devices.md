page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.experimental.list_logical_devices


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/config/experimental/list_logical_devices">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/config.py#L321-L347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return a list of logical devices created by runtime.

### Aliases:

* <a href="/api_docs/python/tf/config/experimental/list_logical_devices"><code>tf.compat.v1.config.experimental.list_logical_devices</code></a>
* <a href="/api_docs/python/tf/config/experimental/list_logical_devices"><code>tf.compat.v2.config.experimental.list_logical_devices</code></a>


``` python
tf.config.experimental.list_logical_devices(device_type=None)
```



<!-- Placeholder for "Used in" -->

Logical devices may correspond to physical devices or remote devices in the
cluster. Operations and tensors may be placed on these devices by using the
`name` of the LogicalDevice.

#### For example:



```python
logical_devices = tf.config.experimental.list_logical_devices('GPU')
# Allocate on GPU:0
with tf.device(logical_devices[0].name):
  one = tf.constant(1)
# Allocate on GPU:1
with tf.device(logical_devices[1].name):
  two = tf.constant(2)
```

#### Args:


* <b>`device_type`</b>: (optional) Device type to filter by such as "CPU" or "GPU"


#### Returns:

List of LogicalDevice objects
