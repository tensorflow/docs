description: A transformation that prefetches dataset values to the given device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.prefetch_to_device" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.prefetch_to_device

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/prefetching_ops.py#L36-L56">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that prefetches dataset values to the given `device`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.prefetch_to_device`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.prefetch_to_device(
    device, buffer_size=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

NOTE: Although the transformation creates a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>, the
transformation must be the final `Dataset` in the input pipeline.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device`
</td>
<td>
A string. The name of a device to which elements will be prefetched.
</td>
</tr><tr>
<td>
`buffer_size`
</td>
<td>
(Optional.) The number of elements to buffer on `device`.
Defaults to an automatically chosen value.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
</td>
</tr>

</table>

