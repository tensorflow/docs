description: Computes the (weighted) mean of the given values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.metrics.mean" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.metrics.mean

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/metrics_impl.py#L315-L393">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the (weighted) mean of the given values.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.metrics.mean(
    values, weights=None, metrics_collections=None, updates_collections=None,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `mean` function creates two local variables, `total` and `count`
that are used to compute the average of `values`. This average is ultimately
returned as `mean` which is an idempotent operation that simply divides
`total` by `count`.

For estimation of the metric over a stream of data, the function creates an
`update_op` operation that updates these variables and returns the `mean`.
`update_op` increments `total` with the reduced sum of the product of `values`
and `weights`, and it increments `count` with the reduced sum of `weights`.

If `weights` is `None`, weights default to 1. Use weights of 0 to mask values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A `Tensor` of arbitrary dimensions.
</td>
</tr><tr>
<td>
`weights`
</td>
<td>
Optional `Tensor` whose rank is either 0, or the same rank as
`values`, and must be broadcastable to `values` (i.e., all dimensions must
be either `1`, or the same as the corresponding `values` dimension).
</td>
</tr><tr>
<td>
`metrics_collections`
</td>
<td>
An optional list of collections that `mean`
should be added to.
</td>
</tr><tr>
<td>
`updates_collections`
</td>
<td>
An optional list of collections that `update_op`
should be added to.
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
`mean`
</td>
<td>
A `Tensor` representing the current mean, the value of `total` divided
by `count`.
</td>
</tr><tr>
<td>
`update_op`
</td>
<td>
An operation that increments the `total` and `count` variables
appropriately and whose value matches `mean_value`.
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
If `weights` is not `None` and its shape doesn't match `values`,
or if either `metrics_collections` or `updates_collections` are not a list
or tuple.
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

