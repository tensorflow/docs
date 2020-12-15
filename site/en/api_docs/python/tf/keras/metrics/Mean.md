description: Computes the (weighted) mean of the given values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.Mean" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.Mean

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L451-L489">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the (weighted) mean of the given values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.Mean`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.Mean`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.Mean(
    name='mean', dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, if values is [1, 3, 5, 7] then the mean is 4.
If the weights were specified as [1, 1, 0, 0] then the mean would be 2.

This metric creates two variables, `total` and `count` that are used to
compute the average of `values`. This average is ultimately returned as `mean`
which is an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
(Optional) string name of the metric instance.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional) data type of the metric result.
</td>
</tr>
</table>



#### Standalone usage:



```
>>> m = tf.keras.metrics.Mean()
>>> m.update_state([1, 3, 5, 7])
>>> m.result().numpy()
4.0
>>> m.reset_states()
>>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0])
>>> m.result().numpy()
2.0
```

Usage with `compile()` API:

```python
model.add_metric(tf.keras.metrics.Mean(name='mean_1')(outputs))
model.compile(optimizer='sgd', loss='mse')
```

## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L247-L253">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L400-L410">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>result()
</code></pre>

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L342-L398">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    values, sample_weight=None
)
</code></pre>

Accumulates statistics for computing the metric.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`values`
</td>
<td>
Per-example value.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional weighting of each example. Defaults to 1.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Update op.
</td>
</tr>

</table>





