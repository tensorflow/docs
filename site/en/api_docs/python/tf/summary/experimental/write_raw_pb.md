description: Writes a summary using raw <a href="../../../tf/compat/v1/Summary.md"><code>tf.compat.v1.Summary</code></a> protocol buffers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.experimental.write_raw_pb" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.experimental.write_raw_pb

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/summary_ops_v2.py#L681-L730">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Writes a summary using raw <a href="../../../tf/compat/v1/Summary.md"><code>tf.compat.v1.Summary</code></a> protocol buffers.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.experimental.write_raw_pb(
    tensor, step=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Experimental: this exists to support the usage of V1-style manual summary
writing (via the construction of a <a href="../../../tf/compat/v1/Summary.md"><code>tf.compat.v1.Summary</code></a> protocol buffer)
with the V2 summary writing API.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
the string Tensor holding one or more serialized `Summary` protobufs
</td>
</tr><tr>
<td>
`step`
</td>
<td>
Explicit `int64`-castable monotonic step value for this summary. If
omitted, this defaults to <a href="../../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a>, which must
not be None.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional string name for this op.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
True on success, or false if no summary was written because no default
summary writer was available.
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
if a default writer exists, but no step was provided and
<a href="../../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a> is None.
</td>
</tr>
</table>

