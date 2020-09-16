description: Configuration class for a logical devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.LogicalDeviceConfiguration" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="memory_limit"/>
</div>

# tf.config.LogicalDeviceConfiguration

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/eager/context.py#L264-L281">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration class for a logical devices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.VirtualDeviceConfiguration`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.LogicalDeviceConfiguration`, `tf.compat.v1.config.experimental.VirtualDeviceConfiguration`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.LogicalDeviceConfiguration(
    memory_limit=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The class specifies the parameters to configure a <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>
as it is initialized to a <a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a> during runtime
initialization. Not all fields are valid for all device types.

See <a href="../../tf/config/get_logical_device_configuration.md"><code>tf.config.get_logical_device_configuration</code></a> and
<a href="../../tf/config/set_logical_device_configuration.md"><code>tf.config.set_logical_device_configuration</code></a> for usage examples.

#### Fields:


* <b>`memory_limit`</b>: (optional) Maximum memory (in MB) to allocate on the virtual
  device. Currently only supported for GPUs.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`memory_limit`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `memory_limit` <a id="memory_limit"></a>
