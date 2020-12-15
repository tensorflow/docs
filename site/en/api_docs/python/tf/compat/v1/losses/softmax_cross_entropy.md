description: Creates a cross-entropy loss using tf.nn.softmax_cross_entropy_with_logits_v2.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.softmax_cross_entropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.softmax_cross_entropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/losses/losses_impl.py#L721-L790">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a cross-entropy loss using tf.nn.softmax_cross_entropy_with_logits_v2.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.softmax_cross_entropy(
    onehot_labels, logits, weights=1.0, label_smoothing=0, scope=None,
    loss_collection=tf.GraphKeys.LOSSES, reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
</code></pre>



<!-- Placeholder for "Used in" -->

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of shape `[batch_size]`, then the loss weights apply to each
corresponding sample.

If `label_smoothing` is nonzero, smooth the labels towards 1/num_classes:
    new_onehot_labels = onehot_labels * (1 - label_smoothing)
                        + label_smoothing / num_classes

Note that `onehot_labels` and `logits` must have the same shape,
e.g. `[batch_size, num_classes]`. The shape of `weights` must be
broadcastable to loss, whose shape is decided by the shape of `logits`.
In case the shape of `logits` is `[batch_size, num_classes]`, loss is
a `Tensor` of shape `[batch_size]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`onehot_labels`
</td>
<td>
One-hot-encoded labels.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Logits outputs of the network.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Optional `Tensor` that is broadcastable to loss.
</td>
</tr><tr>
<td>
`label_smoothing`
</td>
<td>
If greater than 0 then smooth the labels.
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
`NONE`, this has shape `[batch_size]`; otherwise, it is scalar.
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
If the shape of `logits` doesn't match that of `onehot_labels`
or if the shape of `weights` is invalid or if `weights` is None.  Also if
`onehot_labels` or `logits` is None.
</td>
</tr>
</table>




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

