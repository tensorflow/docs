description: Set the list of visible devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.set_visible_devices" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.set_visible_devices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L440-L474">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Set the list of visible devices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.config.experimental.set_visible_devices`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.set_visible_devices`, `tf.compat.v1.config.set_visible_devices`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.set_visible_devices(
    devices, device_type=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Specifies which `PhysicalDevice` objects are visible to the runtime.
TensorFlow will only allocate memory and place operations on visible
physical devices, as otherwise no `LogicalDevice` will be created on them.
By default all discovered devices are marked as visible.

The following example demonstrates disabling the first GPU on the machine.

```
>>> physical_devices = tf.config.list_physical_devices('GPU')
>>> try:
...   # Disable first GPU
...   tf.config.set_visible_devices(physical_devices[1:], 'GPU')
...   logical_devices = tf.config.list_logical_devices('GPU')
...   # Logical device was not created for first GPU
...   assert len(logical_devices) == len(physical_devices) - 1
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
`devices`
</td>
<td>
List of `PhysicalDevice`s to make visible
</td>
</tr><tr>
<td>
`device_type`
</td>
<td>
(optional) Only configure devices matching this device type.
For example "CPU" or "GPU". Other devices will be left unaltered.
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

