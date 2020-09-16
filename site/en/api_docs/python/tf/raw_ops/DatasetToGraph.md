description: Returns a serialized GraphDef representing input_dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.DatasetToGraph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.DatasetToGraph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns a serialized GraphDef representing `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DatasetToGraph`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DatasetToGraph(
    input_dataset, stateful_whitelist=[], allow_stateful=(False),
    strip_device_assignment=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a graph representation for `input_dataset`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
A variant tensor representing the dataset to return the graph representation for.
</td>
</tr><tr>
<td>
`stateful_whitelist`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
</td>
</tr><tr>
<td>
`allow_stateful`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`strip_device_assignment`
</td>
<td>
An optional `bool`. Defaults to `False`.
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

