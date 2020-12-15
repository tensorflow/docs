description: Computes the precision of the predictions with respect to the labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.precision" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.precision

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/metrics_impl.py#L1956-L2048">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the precision of the predictions with respect to the labels.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.precision(
    labels, predictions, weights=None, metrics_collections=None,
    updates_collections=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `precision` function creates two local variables,
`true_positives` and `false_positives`, that are used to compute the
precision. This value is ultimately returned as `precision`, an idempotent
operation that simply divides `true_positives` by the sum of `true_positives`
and `false_positives`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the
`precision`. `update_op` weights each prediction by the corresponding value in
`weights`.

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
The predicted values, a `Tensor` of arbitrary dimensions. Will
be cast to `bool`.
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
An optional list of collections that `precision` should
be added to.
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
Scalar float `Tensor` with the value of `true_positives`
divided by the sum of `true_positives` and `false_positives`.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
`Operation` that increments `true_positives` and
`false_positives` variables appropriately and whose value matches
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

