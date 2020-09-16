description: Retrieves the tree ensemble resource stamp token, number of trees and growing statistics.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesGetEnsembleStates" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesGetEnsembleStates

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Retrieves the tree ensemble resource stamp token, number of trees and growing statistics.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesGetEnsembleStates`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesGetEnsembleStates(
    tree_ensemble_handle, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tree_ensemble_handle`
</td>
<td>
A `Tensor` of type `resource`.
Handle to the tree ensemble.
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
A tuple of `Tensor` objects (stamp_token, num_trees, num_finalized_trees, num_attempted_layers, last_layer_nodes_range).
</td>
</tr>
<tr>
<td>
`stamp_token`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`num_trees`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`num_finalized_trees`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`num_attempted_layers`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`last_layer_nodes_range`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

