description: Get the memory usage, in bytes, for the chosen device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.config.experimental.get_memory_usage" />
<meta itemprop="path" content="Stable" />
</div>

# tf.config.experimental.get_memory_usage

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/config.py#L513-L537">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get the memory usage, in bytes, for the chosen device.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.config.experimental.get_memory_usage`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.config.experimental.get_memory_usage(
    device
)
</code></pre>



<!-- Placeholder for "Used in" -->

See https://www.tensorflow.org/api_docs/python/tf/device for specifying device
strings.

#### For example:



```
>>> gpu_devices = tf.config.list_physical_devices('GPU')
>>> if gpu_devices:
...   tf.config.experimental.get_memory_usage('GPU:0')
```

Does not work for CPU.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device`
</td>
<td>
Device string to get the bytes in use for.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Total memory usage in bytes.
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
Non-existent or CPU device specified.
</td>
</tr>
</table>

