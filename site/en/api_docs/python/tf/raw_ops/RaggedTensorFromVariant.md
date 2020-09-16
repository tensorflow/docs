description: Decodes a variant Tensor into a RaggedTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RaggedTensorFromVariant" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RaggedTensorFromVariant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Decodes a `variant` Tensor into a `RaggedTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedTensorFromVariant`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedTensorFromVariant(
    encoded_ragged, input_ragged_rank, output_ragged_rank, Tvalues,
    Tsplits=tf.dtypes.int64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Decodes the given `variant` Tensor and returns a `RaggedTensor`. The input
could be a scalar, meaning it encodes a single `RaggedTensor` with ragged_rank
`output_ragged_rank`. It could also have an arbitrary rank, in which case each
element is decoded into a `RaggedTensor` with ragged_rank `input_ragged_rank`
and these are then stacked according to the input shape to output a single
`RaggedTensor` with ragged_rank `output_ragged_rank`. Each `variant` element in
the input Tensor is decoded by retrieving from the element a 1-D `variant`
Tensor with `input_ragged_rank + 1` Tensors, corresponding to the splits and
values of the decoded `RaggedTensor`. If `input_ragged_rank` is -1, then it is
inferred as `output_ragged_rank` - `rank(encoded_ragged)`. See
`RaggedTensorToVariant` for the corresponding encoding logic.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`encoded_ragged`
</td>
<td>
A `Tensor` of type `variant`.
A `variant` Tensor containing encoded `RaggedTensor`s.
</td>
</tr><tr>
<td>
`input_ragged_rank`
</td>
<td>
An `int` that is `>= -1`.
The ragged rank of each encoded `RaggedTensor` component in the input. If set to
-1, this is inferred as `output_ragged_rank` - `rank(encoded_ragged)`
</td>
</tr><tr>
<td>
`output_ragged_rank`
</td>
<td>
An `int` that is `>= 0`.
The expected ragged rank of the output `RaggedTensor`. The following must hold:
`output_ragged_rank = rank(encoded_ragged) + input_ragged_rank`.
</td>
</tr><tr>
<td>
`Tvalues`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
</td>
</tr><tr>
<td>
`Tsplits`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int64"><code>tf.int64</code></a>.
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
A tuple of `Tensor` objects (output_nested_splits, output_dense_values).
</td>
</tr>
<tr>
<td>
`output_nested_splits`
</td>
<td>
A list of `output_ragged_rank` `Tensor` objects with type `Tsplits`.
</td>
</tr><tr>
<td>
`output_dense_values`
</td>
<td>
A `Tensor` of type `Tvalues`.
</td>
</tr>
</table>

