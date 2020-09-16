description: Gradient of Unbatch.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.UnbatchGrad" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.UnbatchGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Gradient of Unbatch.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UnbatchGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UnbatchGrad(
    original_input, batch_index, grad, id, container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Acts like Batch but using the given batch_index index of batching things as they
become available. This ensures that the gradients are propagated back in the
same session which did the forward pass.

original_input: The input to the Unbatch operation this is the gradient of.
batch_index: The batch_index given to the Unbatch operation this is the gradient
of.
grad: The downstream gradient.
id: The id scalar emitted by Batch.
batched_grad: The return value, either an empty tensor or the batched gradient.
container: Container to control resource sharing.
shared_name: Instances of UnbatchGrad with the same container and shared_name
 are assumed to possibly belong to the same batch. If left empty, the op name
 will be used as the shared name.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`original_input`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`batch_index`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must have the same type as `original_input`.
</td>
</tr><tr>
<td>
`id`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
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
A `Tensor`. Has the same type as `original_input`.
</td>
</tr>

</table>

