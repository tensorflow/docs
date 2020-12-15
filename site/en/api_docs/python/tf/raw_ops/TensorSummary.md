description: Outputs a Summary protocol buffer with a tensor.

robots: noindex

# tf.raw_ops.TensorSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Outputs a `Summary` protocol buffer with a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorSummary(
    tensor, description='', labels=[], display_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op is being phased out in favor of TensorSummaryV2, which lets callers pass
a tag as well as a serialized SummaryMetadata proto string that contains
plugin-specific data. We will keep this op to maintain backwards compatibility.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor`. A tensor to serialize.
</td>
</tr><tr>
<td>
`description`
</td>
<td>
An optional `string`. Defaults to `""`.
A json-encoded SummaryDescription proto.
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
An unused list of strings.
</td>
</tr><tr>
<td>
`display_name`
</td>
<td>
An optional `string`. Defaults to `""`. An unused string.
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

