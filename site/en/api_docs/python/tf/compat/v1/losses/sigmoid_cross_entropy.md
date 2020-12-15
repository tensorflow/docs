description: Creates a cross-entropy loss using tf.nn.sigmoid_cross_entropy_with_logits.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.losses.sigmoid_cross_entropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.losses.sigmoid_cross_entropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/losses/losses_impl.py#L656-L719">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a cross-entropy loss using tf.nn.sigmoid_cross_entropy_with_logits.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.losses.sigmoid_cross_entropy(
    multi_class_labels, logits, weights=1.0, label_smoothing=0, scope=None,
    loss_collection=tf.GraphKeys.LOSSES, reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
</code></pre>



<!-- Placeholder for "Used in" -->

`weights` acts as a coefficient for the loss. If a scalar is provided,
then the loss is simply scaled by the given value. If `weights` is a
tensor of shape `[batch_size]`, then the loss weights apply to each
corresponding sample.

If `label_smoothing` is nonzero, smooth the labels towards 1/2:

    new_multiclass_labels = multiclass_labels * (1 - label_smoothing)
                            + 0.5 * label_smoothing

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`multi_class_labels`
</td>
<td>
`[batch_size, num_classes]` target integer labels in
`{0, 1}`.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Float `[batch_size, num_classes]` logits outputs of the network.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`multi_class_labels`, and must be broadcastable to `multi_class_labels` 
(i.e., all dimensions must be either `1`, or the same as the 
corresponding `losses` dimension).
</td>
</tr><tr>
<td>
`label_smoothing`
</td>
<td>
If greater than `0` then smooth the labels.
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
Weighted loss `Tensor` of the same type as `logits`. If `reduction` is
`NONE`, this has the same shape as `logits`; otherwise, it is scalar.
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
If the shape of `logits` doesn't match that of
`multi_class_labels` or if the shape of `weights` is invalid, or if
`weights` is None.  Also if `multi_class_labels` or `logits` is None.
</td>
</tr>
</table>




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a>.

