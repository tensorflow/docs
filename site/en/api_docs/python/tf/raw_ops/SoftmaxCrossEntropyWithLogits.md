description: Computes softmax cross entropy cost and gradients to backpropagate.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SoftmaxCrossEntropyWithLogits" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SoftmaxCrossEntropyWithLogits

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes softmax cross entropy cost and gradients to backpropagate.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SoftmaxCrossEntropyWithLogits`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SoftmaxCrossEntropyWithLogits(
    features, labels, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Inputs are the logits, not probabilities.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
batch_size x num_classes matrix
</td>
</tr><tr>
<td>
`labels`
</td>
<td>
A `Tensor`. Must have the same type as `features`.
batch_size x num_classes matrix
The caller must ensure that each batch of labels represents a valid
probability distribution.
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
A tuple of `Tensor` objects (loss, backprop).
</td>
</tr>
<tr>
<td>
`loss`
</td>
<td>
A `Tensor`. Has the same type as `features`.
</td>
</tr><tr>
<td>
`backprop`
</td>
<td>
A `Tensor`. Has the same type as `features`.
</td>
</tr>
</table>

