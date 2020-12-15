description: Computes false negatives at provided threshold values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.false_negatives_at_thresholds" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.false_negatives_at_thresholds

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/metrics_impl.py#L1573-L1626">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes false negatives at provided threshold values.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.false_negatives_at_thresholds(
    labels, predictions, thresholds, weights=None, metrics_collections=None,
    updates_collections=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

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
A `Tensor` whose shape matches `predictions`. Will be cast to
`bool`.
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
An optional list of collections that `false_negatives`
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
`false_negatives`
</td>
<td>
A float `Tensor` of shape `[len(thresholds)]`.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
An operation that updates the `false_negatives` variable and
returns its current value.
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

