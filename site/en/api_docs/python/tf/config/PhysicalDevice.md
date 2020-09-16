description: Abstraction for a locally visible physical device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.PhysicalDevice" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="device_type"/>
<meta itemprop="property" content="name"/>
</div>

# tf.config.PhysicalDevice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/eager/context.py#L285-L306">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Abstraction for a locally visible physical device.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.PhysicalDevice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.PhysicalDevice(
    name, device_type
)
</code></pre>



<!-- Placeholder for "Used in" -->

TensorFlow can utilize various devices such as the CPU or multiple GPUs
for computation. Before initializing a local device for use, the user can
customize certain properties of the device such as it's visibility or memory
configuration.

Once a visible <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> is initialized one or more
<a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a> objects are created. Use
<a href="../../tf/config/set_visible_devices.md"><code>tf.config.set_visible_devices</code></a> to configure the visibility of a physical
device and <a href="../../tf/config/set_logical_device_configuration.md"><code>tf.config.set_logical_device_configuration</code></a> to configure multiple
<a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a> objects for a <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>. This is
useful when separation between models is needed or to simulate a multi-device
environment.

#### Fields:


* <b>`name`</b>: Unique identifier for device.
* <b>`device_type`</b>: String declaring the type of device such as "CPU" or "GPU".




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>

</td>
</tr><tr>
<td>
`device_type`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `device_type` <a id="device_type"></a>
* `name` <a id="name"></a>
