description: Adds a Sum-of-Squares loss to the training procedure.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.mean_squared_error" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.mean_squared_error

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/losses/losses_impl.py#L602-L653">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adds a Sum-of-Squares loss to the training procedure.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.mean_squared_error(
    labels, predictions, weights=1.0, scope=None,
    loss_collection=tf.GraphKeys.LOSSES, reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
</code></pre>



<!-- Placeholder for "Used in" -->

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a tensor of size
`[batch_size]`, then the total loss for each sample of the batch is rescaled
by the corresponding element in the `weights` vector. If the shape of
`weights` matches the shape of `predictions`, then the loss of each
measurable element of `predictions` is scaled by the corresponding value of
`weights`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
The ground truth output tensor, same dimensions as 'predictions'.
</td>
</tr><tr>
<td>
`predictions`
</td>
<td>
The predicted outputs.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`labels`, and must be broadcastable to `labels` (i.e., all dimensions must
be either `1`, or the same as the corresponding `losses` dimension).
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
The scope for the operations performed in computing the loss.
</td>
</tr><tr>
<td>
`loss_collection`
</td>
<td>
collection to which the loss will be added.
</td>
</tr><tr>
<td>
`reduction`
</td>
<td>
Type of reduction to apply to loss.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
shape as `labels`; otherwise, it is scalar.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the shape of `predictions` doesn't match that of `labels` or
if the shape of `weights` is invalid.  Also if `labels` or `predictions`
is None.
</td>
</tr>
</table>




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

