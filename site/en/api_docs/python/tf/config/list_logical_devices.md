description: Return a list of logical devices created by runtime.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.list_logical_devices" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.list_logical_devices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/framework/config.py#L338-L372">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return a list of logical devices created by runtime.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.list_logical_devices`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.list_logical_devices`, `tf.compat.v1.config.list_logical_devices`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.list_logical_devices(
    device_type=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Logical devices may correspond to physical devices or remote devices in the
cluster. Operations and tensors may be placed on these devices by using the
`name` of the <a href="../../tf/config/LogicalDevice.md"><code>tf.config.LogicalDevice</code></a>.

Calling <a href="../../tf/config/list_logical_devices.md"><code>tf.config.list_logical_devices</code></a> triggers the runtime to configure any
<a href="../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a> visible to the runtime, thereby preventing
further configuration. To avoid runtime initialization, call
<a href="../../tf/config/list_physical_devices.md"><code>tf.config.list_physical_devices</code></a> instead.

#### For example:



```
>>> logical_devices = tf.config.list_logical_devices('GPU')
>>> if len(logical_devices) > 0:
...   # Allocate on GPU:0
...   with tf.device(logical_devices[0].name):
...     one = tf.constant(1)
...   # Allocate on GPU:1
...   with tf.device(logical_devices[1].name):
...     two = tf.constant(2)
```

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
List of initialized `LogicalDevice`s
</td>
</tr>

</table>

