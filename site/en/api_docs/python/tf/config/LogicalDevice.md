description: Abstraction for a logical device initialized by the runtime.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.LogicalDevice" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="device_type"/>
<meta itemprop="property" content="name"/>
</div>

# tf.config.LogicalDevice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/eager/context.py#L245-L259">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Abstraction for a logical device initialized by the runtime.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.LogicalDevice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.LogicalDevice(
    name, device_type
)
</code></pre>



<!-- Placeholder for "Used in" -->

A <a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a> corresponds to an initialized logical device on a
<a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> or a remote device visible to the cluster. Tensors
and operations can be placed on a specific logical device by calling
<a href="../../tf/device.md"><code>tf.device</code></a> with a specified <a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a>.

#### Fields:


* <b>`name`</b>: The fully qualified name of the device. Can be used for Op or function
  placement.
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
