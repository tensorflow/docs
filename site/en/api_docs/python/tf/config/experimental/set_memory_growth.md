description: Set if memory growth should be enabled for a PhysicalDevice.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.set_memory_growth" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental.set_memory_growth

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/config.py#L506-L531">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Set if memory growth should be enabled for a `PhysicalDevice`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.set_memory_growth`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.set_memory_growth(
    device, enable
)
</code></pre>



<!-- Placeholder for "Used in" -->

If memory growth is enabled for a `PhysicalDevice`, the runtime initialization
will not allocate all memory on the device. Memory growth cannot be configured
on a `PhysicalDevice` with virtual devices configured.

#### For example:



```
>>> physical_devices = tf.config.list_physical_devices('GPU')
>>> try:
...   tf.config.experimental.set_memory_growth(physical_devices[0], True)
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
`PhysicalDevice` to configure
</td>
</tr><tr>
<td>
`enable`
</td>
<td>
(Boolean) Whether to enable or disable memory growth
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
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
Runtime is already initialized.
</td>
</tr>
</table>

