description: Performs gradient updates of embedding tables.

robots: noindex

# tf.raw_ops.SendTPUEmbeddingGradients

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Performs gradient updates of embedding tables.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SendTPUEmbeddingGradients`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SendTPUEmbeddingGradients(
    inputs, learning_rates, config, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of at least 1 `Tensor` objects with type `float32`.
A TensorList of gradients with which to update embedding tables.
This argument has the same length and shapes as the return value of
RecvTPUEmbeddingActivations, but contains gradients of the model's loss
with respect to the embedding activations. The embedding tables are updated
from these gradients via the optimizer specified in the TPU embedding
configuration given to tpu.initialize_system.
</td>
</tr><tr>
<td>
`learning_rates`
</td>
<td>
A list of `Tensor` objects with type `float32`.
A TensorList of float32 scalars, one for each dynamic learning
rate tag: see the comments in
//third_party/tensorflow/core/protobuf/tpu/optimization_parameters.proto.
Multiple tables can share the same dynamic learning rate tag as specified
in the configuration. If the learning rates for all tables are constant,
this list should be empty.
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
The created Operation.
</td>
</tr>

</table>

