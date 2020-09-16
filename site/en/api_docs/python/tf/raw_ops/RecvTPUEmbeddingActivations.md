description: An op that receives embedding activations on the TPU.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RecvTPUEmbeddingActivations" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RecvTPUEmbeddingActivations

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An op that receives embedding activations on the TPU.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RecvTPUEmbeddingActivations`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RecvTPUEmbeddingActivations(
    num_outputs, config, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The TPU system performs the embedding lookups and aggregations specified by
the arguments to TPUEmbeddingEnqueue(Integer/Sparse/SparseTensor)Batch. The
results of these aggregations are visible to the Tensorflow Graph as the
outputs of a RecvTPUEmbeddingActivations op. This op returns a list containing
one Tensor of activations per table specified in the model. There can be at
most one RecvTPUEmbeddingActivations op in the TPU graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_outputs`
</td>
<td>
An `int` that is `>= 1`.
The number of output activation tensors, equal to the number of
embedding tables in the model.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
A `string`. Serialized TPUEmbeddingConfiguration proto.
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
A list of `num_outputs` `Tensor` objects with type `float32`.
</td>
</tr>

</table>

