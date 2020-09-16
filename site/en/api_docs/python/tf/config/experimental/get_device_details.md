description: Returns details about a physical devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.get_device_details" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental.get_device_details

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L534-L576">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns details about a physical devices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.get_device_details`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.get_device_details(
    device
)
</code></pre>



<!-- Placeholder for "Used in" -->

This API takes in a <a href="../../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> returned by
<a href="../../../tf/config/list_physical_devices.md"><code>tf.config.list_physical_devices</code></a>. It returns a dict with string keys
containing various details about the device. Each key is only supported by a
subset of devices, so you should not assume the returned dict will have any
particular key.

```
>>> gpu_devices = tf.config.list_physical_devices('GPU')
>>> if gpu_devices:
...   details = tf.config.experimental.get_device_details(gpu_devices[0])
...   details.get('device_name', 'Unknown GPU')
```

Currently, details are only returned for GPUs. This function returns an
empty dict if passed a non-GPU device.

The returned dict may have the following keys:
* `'device_name'`: A human-readable name of the device as a string, e.g.
  "Titan V". Unlike <a href="../../../tf/config/PhysicalDevice.md#name"><code>tf.config.PhysicalDevice.name</code></a>, this will be the same for
  multiple devices if each device is the same model. Currently only available
  for GPUs.
* `'compute_capability'`: The
  [compute capability](https://developer.nvidia.com/cuda-gpus) of the device
  as a tuple of two ints, in the form `(major_version, minor_version)`. Only
  available for NVIDIA GPUs

Note: This is similar to <a href="../../../tf/sysconfig/get_build_info.md"><code>tf.sysconfig.get_build_info</code></a> in that both functions
can return information relating to GPUs. However, this function returns
run-time information about a specific device (such as a GPU's compute
capability), while <a href="../../../tf/sysconfig/get_build_info.md"><code>tf.sysconfig.get_build_info</code></a> returns compile-time
information about how TensorFlow was built (such as what version of CUDA
TensorFlow was built for).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device`
</td>
<td>
A <a href="../../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> returned by
<a href="../../../tf/config/list_physical_devices.md"><code>tf.config.list_physical_devices</code></a> or <a href="../../../tf/config/get_visible_devices.md"><code>tf.config.get_visible_devices</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dict with string keys.
</td>
</tr>

</table>

