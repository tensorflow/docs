description: Get the virtual device configuration for a <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.get_logical_device_configuration" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.get_logical_device_configuration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/framework/config.py#L503-L541">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get the virtual device configuration for a <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.get_virtual_device_configuration`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.get_virtual_device_configuration`, `tf.compat.v1.config.get_logical_device_configuration`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.get_logical_device_configuration(
    device
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns the list of <a href="../../tf/config/LogicalDeviceConfiguration.md"><code>tf.config.LogicalDeviceConfiguration</code></a>
objects previously configured by a call to
<a href="../../tf/config/set_logical_device_configuration.md"><code>tf.config.set_logical_device_configuration</code></a>.

#### For example:



```
>>> physical_devices = tf.config.list_physical_devices('CPU')
>>> assert len(physical_devices) == 1, "No CPUs found"
>>> configs = tf.config.get_logical_device_configuration(
...   physical_devices[0])
>>> try:
...   assert configs is None
...   tf.config.set_logical_device_configuration(
...     physical_devices[0],
...     [tf.config.LogicalDeviceConfiguration(),
...      tf.config.LogicalDeviceConfiguration()])
...   configs = tf.config.get_logical_device_configuration(
...     physical_devices[0])
...   assert len(configs) == 2
... except:
...   # Cannot modify virtual devices once initialized.
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
`PhysicalDevice` to query
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
List of <a href="../../tf/config/LogicalDeviceConfiguration.md"><code>tf.config.LogicalDeviceConfiguration</code></a> objects or
`None` if no virtual device configuration has been set for this physical
device.
</td>
</tr>

</table>

