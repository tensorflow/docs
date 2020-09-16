description: Computes precision@k of the predictions with respect to sparse labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.precision_at_top_k" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.precision_at_top_k

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/metrics_impl.py#L3426-L3512">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes precision@k of the predictions with respect to sparse labels.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.precision_at_top_k(
    labels, predictions_idx, k=None, class_id=None, weights=None,
    metrics_collections=None, updates_collections=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Differs from `sparse_precision_at_k` in that predictions must be in the form
of top `k` class indices, whereas `sparse_precision_at_k` expects logits.
Refer to `sparse_precision_at_k` for more details.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
`int64` `Tensor` or `SparseTensor` with shape
[D1, ... DN, num_labels] or [D1, ... DN], where the latter implies
num_labels=1. N >= 1 and num_labels is the number of target classes for
the associated prediction. Commonly, N=1 and `labels` has shape
[batch_size, num_labels]. [D1, ... DN] must match `predictions`. Values
should be in range [0, num_classes), where num_classes is the last
dimension of `predictions`. Values outside this range are ignored.
</td>
</tr><tr>
<td>
`predictions_idx`
</td>
<td>
Integer `Tensor` with shape [D1, ... DN, k] where
N >= 1. Commonly, N=1 and predictions has shape [batch size, k].
The final dimension contains the top `k` predicted class indices.
[D1, ... DN] must match `labels`.
</td>
</tr><tr>
<td>
`k`
</td>
<td>
Integer, k for @k metric. Only used for the default op name.
</td>
</tr><tr>
<td>
`class_id`
</td>
<td>
Integer class ID for which we want binary metrics. This should be
in range [0, num_classes], where num_classes is the last dimension of
`predictions`. If `class_id` is outside this range, the method returns
NAN.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
`Tensor` whose rank is either 0, or n-1, where n is the rank of
`labels`. If the latter, it must be broadcastable to `labels` (i.e., all
dimensions must be either `1`, or the same as the corresponding `labels`
dimension).
</td>
</tr><tr>
<td>
`metrics_collections`
</td>
<td>
An optional list of collections that values should
be added to.
</td>
</tr><tr>
<td>
`updates_collections`
</td>
<td>
An optional list of collections that updates should
be added to.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name of new update operation, and namespace for other dependent ops.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`precision`
</td>
<td>
Scalar `float64` `Tensor` with the value of `true_positives`
divided by the sum of `true_positives` and `false_positives`.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
`Operation` that increments `true_positives` and
`false_positives` variables appropriately, and whose value matches
`precision`.
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
If `weights` is not `None` and its shape doesn't match
`predictions`, or if either `metrics_collections` or `updates_collections`
are not a list or tuple.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If eager execution is enabled.
</td>
</tr>
</table>

