description: Get if memory growth is enabled for a PhysicalDevice.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.get_memory_growth" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental.get_memory_growth

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L477-L503">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get if memory growth is enabled for a `PhysicalDevice`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.get_memory_growth`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.get_memory_growth(
    device
)
</code></pre>



<!-- Placeholder for "Used in" -->

If memory growth is enabled for a `PhysicalDevice`, the runtime initialization
will not allocate all memory on the device.

#### For example:



```
>>> physical_devices = tf.config.list_physical_devices('GPU')
>>> try:
...   tf.config.experimental.set_memory_growth(physical_devices[0], True)
...   assert tf.config.experimental.get_memory_growth(physical_devices[0])
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
A boolean indicating the memory growth setting for the `PhysicalDevice`.
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
Invalid `PhysicalDevice` specified.
</td>
</tr>
</table>

