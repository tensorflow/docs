description: Return a list of physical devices visible to the host runtime.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.list_physical_devices" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.list_physical_devices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/config.py#L370-L402">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return a list of physical devices visible to the host runtime.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.list_physical_devices`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.list_physical_devices`, `tf.compat.v1.config.list_physical_devices`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.list_physical_devices(
    device_type=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Physical devices are hardware devices present on the host machine. By default
all discovered CPU and GPU devices are considered visible.

This API allows querying the physical hardware resources prior to runtime
initialization. Thus, giving an opportunity to call any additional
configuration APIs. This is in contrast to <a href="../../tf/config/list_logical_devices.md"><code>tf.config.list_logical_devices</code></a>,
which triggers runtime initialization in order to list the configured devices.

The following example lists the number of visible GPUs on the host.

```
>>> physical_devices = tf.config.list_physical_devices('GPU')
>>> print("Num GPUs:", len(physical_devices))
Num GPUs: ...
```

However, the number of GPUs available to the runtime may change during runtime
initialization due to marking certain devices as not visible or configuring
multiple logical devices.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device_type`
</td>
<td>
(optional string) Only include devices matching this device
type. For example "CPU" or "GPU".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
List of discovered <a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> objects
</td>
</tr>

</table>

