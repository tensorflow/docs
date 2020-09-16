description: Serializes the tree ensemble to a proto.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesSerializeEnsemble" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesSerializeEnsemble

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Serializes the tree ensemble to a proto.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesSerializeEnsemble`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesSerializeEnsemble(
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
A tuple of `Tensor` objects (stamp_token, tree_ensemble_serialized).
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
`tree_ensemble_serialized`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr>
</table>

