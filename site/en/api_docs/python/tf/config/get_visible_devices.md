description: Get the list of visible physical devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.get_visible_devices" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.get_visible_devices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/config.py#L442-L473">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get the list of visible physical devices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.get_visible_devices`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.get_visible_devices`, `tf.compat.v1.config.get_visible_devices`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.get_visible_devices(
    device_type=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns the list of `PhysicalDevice`s currently marked as visible to the
runtime. A visible device will have at least one `LogicalDevice` associated
with it once the runtime is initialized.

The following example verifies all visible GPUs have been disabled:

```
>>> physical_devices = tf.config.list_physical_devices('GPU')
>>> try:
...   # Disable all GPUS
...   tf.config.set_visible_devices([], 'GPU')
...   visible_devices = tf.config.get_visible_devices()
...   for device in visible_devices:
...     assert device.device_type != 'GPU'
... except:
...   # Invalid device or cannot modify virtual devices once initialized.
...   pass
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
List of visible `PhysicalDevice`s
</td>
</tr>

</table>

