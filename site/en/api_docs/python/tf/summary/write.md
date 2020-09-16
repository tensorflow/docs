description: Writes a generic summary to the default SummaryWriter if one exists.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.write" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.write

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L620-L684">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Writes a generic summary to the default SummaryWriter if one exists.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.write(
    tag, tensor, step=None, metadata=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This exists primarily to support the definition of type-specific summary ops
like scalar() and image(), and is not intended for direct use unless defining
a new type-specific summary op.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tag`
</td>
<td>
string tag used to identify the summary (e.g. in TensorBoard), usually
generated with `tf.summary.summary_scope`
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
the Tensor holding the summary data to write or a callable that
returns this Tensor. If a callable is passed, it will only be called when
a default SummaryWriter exists and the recording condition specified by
`record_if()` is met.
</td>
</tr><tr>
<td>
`step`
</td>
<td>
Explicit `int64`-castable monotonic step value for this summary. If
omitted, this defaults to <a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a>, which must
not be None.
</td>
</tr><tr>
<td>
`metadata`
</td>
<td>
Optional SummaryMetadata, as a proto or serialized bytes
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
<a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a> is None.
</td>
</tr>
</table>

