description: Computes recall@k of the predictions with respect to sparse labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.recall_at_k" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.recall_at_k

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/metrics_impl.py#L2483-L2573">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes recall@k of the predictions with respect to sparse labels.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.recall_at_k(
    labels, predictions, k, class_id=None, weights=None, metrics_collections=None,
    updates_collections=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `class_id` is specified, we calculate recall by considering only the
    entries in the batch for which `class_id` is in the label, and computing
    the fraction of them for which `class_id` is in the top-k `predictions`.
If `class_id` is not specified, we'll calculate recall as how often on
    average a class among the labels of a batch entry is in the top-k
    `predictions`.

`sparse_recall_at_k` creates two local variables,
`true_positive_at_<k>` and `false_negative_at_<k>`, that are used to compute
the recall_at_k frequency. This frequency is ultimately returned as
`recall_at_<k>`: an idempotent operation that simply divides
`true_positive_at_<k>` by total (`true_positive_at_<k>` +
`false_negative_at_<k>`).

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`recall_at_<k>`. Internally, a `top_k` operation computes a `Tensor`
indicating the top `k` `predictions`. Set operations applied to `top_k` and
`labels` calculate the true positives and false negatives weighted by
`weights`. Then `update_op` increments `true_positive_at_<k>` and
`false_negative_at_<k>` using these values.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

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
dimension of `predictions`. Values outside this range always count
towards `false_negative_at_<k>`.
</td>
</tr><tr>
<td>
`predictions`
</td>
<td>
Float `Tensor` with shape [D1, ... DN, num_classes] where
N >= 1. Commonly, N=1 and predictions has shape [batch size, num_classes].
The final dimension contains the logit values for each class. [D1, ... DN]
must match `labels`.
</td>
</tr><tr>
<td>
`k`
</td>
<td>
Integer, k for @k metric.
</td>
</tr><tr>
<td>
`class_id`
</td>
<td>
Integer class ID for which we want binary metrics. This should be
in range [0, num_classes), where num_classes is the last dimension of
`predictions`. If class_id is outside this range, the method returns NAN.
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
`recall`
</td>
<td>
Scalar `float64` `Tensor` with the value of `true_positives` divided
by the sum of `true_positives` and `false_negatives`.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
`Operation` that increments `true_positives` and
`false_negatives` variables appropriately, and whose value matches
`recall`.
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

