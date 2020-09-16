description: Computes precision values for different thresholds on predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.precision_at_thresholds" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.precision_at_thresholds

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/metrics_impl.py#L2051-L2129">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes precision values for different `thresholds` on `predictions`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.precision_at_thresholds(
    labels, predictions, thresholds, weights=None, metrics_collections=None,
    updates_collections=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `precision_at_thresholds` function creates four local variables,
`true_positives`, `true_negatives`, `false_positives` and `false_negatives`
for various values of thresholds. `precision[i]` is defined as the total
weight of values in `predictions` above `thresholds[i]` whose corresponding
entry in `labels` is `True`, divided by the total weight of values in
`predictions` above `thresholds[i]` (`true_positives[i] / (true_positives[i] +
false_positives[i])`).

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`precision`.

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
The ground truth values, a `Tensor` whose dimensions must match
`predictions`. Will be cast to `bool`.
</td>
</tr><tr>
<td>
`predictions`
</td>
<td>
A floating point `Tensor` of arbitrary shape and whose values
are in the range `[0, 1]`.
</td>
</tr><tr>
<td>
`thresholds`
</td>
<td>
A python list or tuple of float thresholds in `[0, 1]`.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`labels`, and must be broadcastable to `labels` (i.e., all dimensions must
be either `1`, or the same as the corresponding `labels` dimension).
</td>
</tr><tr>
<td>
`metrics_collections`
</td>
<td>
An optional list of collections that `auc` should be
added to.
</td>
</tr><tr>
<td>
`updates_collections`
</td>
<td>
An optional list of collections that `update_op` should
be added to.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional variable_scope name.
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
A float `Tensor` of shape `[len(thresholds)]`.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
An operation that increments the `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` variables that
are used in the computation of `precision`.
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
If `predictions` and `labels` have mismatched shapes, or if
`weights` is not `None` and its shape doesn't match `predictions`, or if
either `metrics_collections` or `updates_collections` are not a list or
tuple.
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

