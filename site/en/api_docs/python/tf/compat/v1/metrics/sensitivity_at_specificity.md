description: Computes the specificity at a given sensitivity.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.sensitivity_at_specificity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.sensitivity_at_specificity

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/metrics_impl.py#L2809-L2908">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the specificity at a given sensitivity.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.sensitivity_at_specificity(
    labels, predictions, specificity, weights=None, num_thresholds=200,
    metrics_collections=None, updates_collections=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `sensitivity_at_specificity` function creates four local
variables, `true_positives`, `true_negatives`, `false_positives` and
`false_negatives` that are used to compute the sensitivity at the given
specificity value. The threshold for the given specificity value is computed
and used to evaluate the corresponding sensitivity.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`sensitivity`. `update_op` increments the `true_positives`, `true_negatives`,
`false_positives` and `false_negatives` counts with the weight of each case
found in the `predictions` and `labels`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

For additional information about specificity and sensitivity, see the
following: https://en.wikipedia.org/wiki/Sensitivity_and_specificity

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
`specificity`
</td>
<td>
A scalar value in range `[0, 1]`.
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
`num_thresholds`
</td>
<td>
The number of thresholds to use for matching the given
specificity.
</td>
</tr><tr>
<td>
`metrics_collections`
</td>
<td>
An optional list of collections that `sensitivity`
should be added to.
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
`sensitivity`
</td>
<td>
A scalar `Tensor` representing the sensitivity at the given
`specificity` value.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
An operation that increments the `true_positives`,
`true_negatives`, `false_positives` and `false_negatives` variables
appropriately and whose value matches `sensitivity`.
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
If `predictions` and `labels` have mismatched shapes, if
`weights` is not `None` and its shape doesn't match `predictions`, or if
`specificity` is not between 0 and 1, or if either `metrics_collections`
or `updates_collections` are not a list or tuple.
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

