description: Set the logical device configuration for a <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.set_logical_device_configuration" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.set_logical_device_configuration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L620-L685">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Set the logical device configuration for a <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.set_virtual_device_configuration`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.set_virtual_device_configuration`, `tf.compat.v1.config.set_logical_device_configuration`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.set_logical_device_configuration(
    device, logical_devices
)
</code></pre>



<!-- Placeholder for "Used in" -->

A visible <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> will by default have a single
<a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a> associated with it once the runtime is initialized.
Specifying a list of <a href="../../tf/config/LogicalDeviceConfiguration.md"><code>tf.config.LogicalDeviceConfiguration</code></a> objects allows
multiple devices to be created on the same <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

The following example splits the CPU into 2 logical devices:

```
>>> physical_devices = tf.config.list_physical_devices('CPU')
>>> assert len(physical_devices) == 1, "No CPUs found"
>>> # Specify 2 virtual CPUs. Note currently memory limit is not supported.
>>> try:
...   tf.config.set_logical_device_configuration(
...     physical_devices[0],
...     [tf.config.LogicalDeviceConfiguration(),
...      tf.config.LogicalDeviceConfiguration()])
...   logical_devices = tf.config.list_logical_devices('CPU')
...   assert len(logical_devices) == 2
...
...   tf.config.set_logical_device_configuration(
...     physical_devices[0],
...     [tf.config.LogicalDeviceConfiguration(),
...      tf.config.LogicalDeviceConfiguration(),
...      tf.config.LogicalDeviceConfiguration(),
...      tf.config.LogicalDeviceConfiguration()])
... except:
...   # Cannot modify logical devices once initialized.
...   pass
```

The following example splits the GPU into 2 logical devices with 100 MB each:

```
>>> physical_devices = tf.config.list_physical_devices('GPU')
>>> try:
...   tf.config.set_logical_device_configuration(
...     physical_devices[0],
...     [tf.config.LogicalDeviceConfiguration(memory_limit=100),
...      tf.config.LogicalDeviceConfiguration(memory_limit=100)])
...
...   logical_devices = tf.config.list_logical_devices('GPU')
...   assert len(logical_devices) == len(physical_devices) + 1
...
...   tf.config.set_logical_device_configuration(
...     physical_devices[0],
...     [tf.config.LogicalDeviceConfiguration(memory_limit=10),
...      tf.config.LogicalDeviceConfiguration(memory_limit=10)])
... except:
...   # Invalid device or cannot modify logical devices once initialized.
...   pass
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device`
</td>
<td>
The `PhysicalDevice` to configure.
</td>
</tr><tr>
<td>
`logical_devices`
</td>
<td>
(optional) List of <a href="../../tf/config/LogicalDeviceConfiguration.md"><code>tf.config.LogicalDeviceConfiguration</code></a>
objects to allocate for the specified `PhysicalDevice`. If None, the
default configuration will be used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If argument validation fails.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
Runtime is already initialized.
</td>
</tr>
</table>

