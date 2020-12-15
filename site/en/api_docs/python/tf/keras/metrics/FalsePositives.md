description: Calculates the number of false positives.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.FalsePositives" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.FalsePositives

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L980-L1025">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculates the number of false positives.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.FalsePositives`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.FalsePositives`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.FalsePositives(
    thresholds=None, name=None, dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `sample_weight` is given, calculates the sum of the weights of
false positives. This metric creates one local variable, `accumulator`
that is used to keep track of the number of false positives.

If `sample_weight` is `None`, weights default to 1.
Use `sample_weight` of 0 to mask values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`thresholds`
</td>
<td>
(Optional) Defaults to 0.5. A float value or a python
list/tuple of float threshold values in [0, 1]. A threshold is compared
with prediction values to determine the truth value of predictions
(i.e., above the threshold is `true`, below is `false`). One metric
value is generated for each threshold value.
</td>
</tr><tr>
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
>>> m = tf.keras.metrics.FalsePositives()
>>> m.update_state([0, 1, 0, 0], [0, 0, 1, 1])
>>> m.result().numpy()
2.0
```

```
>>> m.reset_states()
>>> m.update_state([0, 1, 0, 0], [0, 0, 1, 1], sample_weight=[0, 0, 1, 0])
>>> m.result().numpy()
1.0
```

Usage with `compile()` API:

```python
model.compile(optimizer='sgd',
              loss='mse',
              metrics=[tf.keras.metrics.FalsePositives()])
```

## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L968-L971">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L961-L966">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>result()
</code></pre>

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L941-L959">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    y_true, y_pred, sample_weight=None
)
</code></pre>

Accumulates the metric statistics.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`y_true`
</td>
<td>
The ground truth values.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The predicted values.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional weighting of each example. Defaults to 1. Can be a
`Tensor` whose rank is either 0, or the same rank as `y_true`, and must
be broadcastable to `y_true`.
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





