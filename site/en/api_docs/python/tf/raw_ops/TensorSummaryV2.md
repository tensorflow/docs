description: Outputs a Summary protocol buffer with a tensor and per-plugin data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TensorSummaryV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TensorSummaryV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs a `Summary` protocol buffer with a tensor and per-plugin data.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorSummaryV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorSummaryV2(
    tag, tensor, serialized_summary_metadata, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tag`
</td>
<td>
A `Tensor` of type `string`.
A string attached to this summary. Used for organization in TensorBoard.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A `Tensor`. A tensor to serialize.
</td>
</tr><tr>
<td>
`serialized_summary_metadata`
</td>
<td>
A `Tensor` of type `string`.
A serialized SummaryMetadata proto. Contains plugin
data.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `string`.
</td>
</tr>

</table>

