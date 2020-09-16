description: Computes the weighted loss.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.compute_weighted_loss" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.compute_weighted_loss

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/losses/losses_impl.py#L138-L203">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the weighted loss.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.compute_weighted_loss(
    losses, weights=1.0, scope=None, loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`losses`
</td>
<td>
`Tensor` of shape `[batch_size, d1, ... dN]`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`losses`, and must be broadcastable to `losses` (i.e., all dimensions must
be either `1`, or the same as the corresponding `losses` dimension).
</td>
</tr><tr>
<td>
`scope`
</td>
<td>
the scope for the operations performed in computing the loss.
</td>
</tr><tr>
<td>
`loss_collection`
</td>
<td>
the loss will be added to these collections.
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
Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
`NONE`, this has the same shape as `losses`; otherwise, it is scalar.
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
If `weights` is `None` or the shape is not compatible with
`losses`, or if the number of dimensions (rank) of either `losses` or
`weights` is missing.
</td>
</tr>
</table>



#### Note:

When calculating the gradient of a weighted loss contributions from
both `losses` and `weights` are considered. If your `weights` depend
on some model parameters but you do not want this to affect the loss
gradient, you need to apply <a href="../../../../tf/stop_gradient.md"><code>tf.stop_gradient</code></a> to `weights` before
passing them to `compute_weighted_loss`.




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

