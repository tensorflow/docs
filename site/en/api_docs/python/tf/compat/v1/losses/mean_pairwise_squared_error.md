description: Adds a pairwise-errors-squared loss to the training procedure.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.mean_pairwise_squared_error" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.mean_pairwise_squared_error

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/losses/losses_impl.py#L505-L599">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adds a pairwise-errors-squared loss to the training procedure.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.mean_pairwise_squared_error(
    labels, predictions, weights=1.0, scope=None,
    loss_collection=tf.GraphKeys.LOSSES
)
</code></pre>



<!-- Placeholder for "Used in" -->

Unlike `mean_squared_error`, which is a measure of the differences between
corresponding elements of `predictions` and `labels`,
`mean_pairwise_squared_error` is a measure of the differences between pairs of
corresponding elements of `predictions` and `labels`.

For example, if `labels`=[a, b, c] and `predictions`=[x, y, z], there are
three pairs of differences are summed to compute the loss:
  loss = [ ((a-b) - (x-y)).^2 + ((a-c) - (x-z)).^2 + ((b-c) - (y-z)).^2 ] / 3

Note that since the inputs are of shape `[batch_size, d0, ... dN]`, the
corresponding pairs are computed within each batch sample but not across
samples within a batch. For example, if `predictions` represents a batch of
16 grayscale images of dimension [batch_size, 100, 200], then the set of pairs
is drawn from each image, but not across images.

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a tensor of size
`[batch_size]`, then the total loss for each sample of the batch is rescaled
by the corresponding element in the `weights` vector.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
The ground truth output tensor, whose shape must match the shape of
`predictions`.
</td>
</tr><tr>
<td>
`predictions`
</td>
<td>
The predicted outputs, a tensor of size
`[batch_size, d0, .. dN]` where N+1 is the total number of dimensions in
`predictions`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Coefficients for the loss a scalar, a tensor of shape
`[batch_size]` or a tensor whose shape matches `predictions`.
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
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` that returns the weighted loss.
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

