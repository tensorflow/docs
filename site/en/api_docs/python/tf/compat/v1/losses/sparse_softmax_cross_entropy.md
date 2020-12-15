description: Cross-entropy loss using <a href="../../../../tf/nn/sparse_softmax_cross_entropy_with_logits.md"><code>tf.nn.sparse_softmax_cross_entropy_with_logits</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.sparse_softmax_cross_entropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.sparse_softmax_cross_entropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/losses/losses_impl.py#L845-L901">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Cross-entropy loss using <a href="../../../../tf/nn/sparse_softmax_cross_entropy_with_logits.md"><code>tf.nn.sparse_softmax_cross_entropy_with_logits</code></a>.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.sparse_softmax_cross_entropy(
    labels, logits, weights=1.0, scope=None, loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
</code></pre>



<!-- Placeholder for "Used in" -->

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of shape `[batch_size]`, then the loss weights apply to each
corresponding sample.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
`Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of
`labels` and result) and dtype `int32` or `int64`. Each entry in `labels`
must be an index in `[0, num_classes)`. Other values will raise an
exception when this op is run on CPU, and return `NaN` for corresponding
loss and gradient rows on GPU.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Unscaled log probabilities of shape
`[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float16`, `float32` or
`float64`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Coefficients for the loss. This must be scalar or broadcastable to
`labels` (i.e. same rank and each dimension is either 1 or the same).
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
Weighted loss `Tensor` of the same type as `logits`. If `reduction` is
`NONE`, this has the same shape as `labels`; otherwise, it is scalar.
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
If the shapes of `logits`, `labels`, and `weights` are
incompatible, or if any of them are None.
</td>
</tr>
</table>




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

