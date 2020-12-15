description: Computes the crossentropy metric between the labels and predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.CategoricalCrossentropy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.CategoricalCrossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L3018-L3078">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the crossentropy metric between the labels and predictions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.CategoricalCrossentropy`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.CategoricalCrossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.CategoricalCrossentropy(
    name='categorical_crossentropy', dtype=None, from_logits=(False),
    label_smoothing=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is the crossentropy metric class to be used when there are multiple
label classes (2 or more). Here we assume that labels are given as a `one_hot`
representation. eg., When labels values are [2, 0, 1],
 `y_true` = [[0, 0, 1], [1, 0, 0], [0, 1, 0]].

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
</tr><tr>
<td>
`from_logits`
</td>
<td>
(Optional) Whether output is expected to be a logits tensor.
By default, we consider that output encodes a probability distribution.
</td>
</tr><tr>
<td>
`label_smoothing`
</td>
<td>
(Optional) Float in [0, 1]. When > 0, label values are
smoothed, meaning the confidence on label values are relaxed. e.g.
`label_smoothing=0.2` means that we will use a value of `0.1` for label
`0` and `0.9` for label `1`"
</td>
</tr>
</table>



#### Standalone usage:



```
>>> # EPSILON = 1e-7, y = y_true, y` = y_pred
>>> # y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON)
>>> # y` = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]
>>> # xent = -sum(y * log(y'), axis = -1)
>>> #      = -((log 0.95), (log 0.1))
>>> #      = [0.051, 2.302]
>>> # Reduced xent = (0.051 + 2.302) / 2
>>> m = tf.keras.metrics.CategoricalCrossentropy()
>>> m.update_state([[0, 1, 0], [0, 0, 1]],
...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
>>> m.result().numpy()
1.1769392
```

```
>>> m.reset_states()
>>> m.update_state([[0, 1, 0], [0, 0, 1]],
...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]],
...                sample_weight=tf.constant([0.3, 0.7]))
>>> m.result().numpy()
1.6271976
```

Usage with `compile()` API:

```python
model.compile(
  optimizer='sgd',
  loss='mse',
  metrics=[tf.keras.metrics.CategoricalCrossentropy()])
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/metrics.py#L588-L620">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_state(
    y_true, y_pred, sample_weight=None
)
</code></pre>

Accumulates metric statistics.

`y_true` and `y_pred` should have the same shape.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`y_true`
</td>
<td>
Ground truth values. shape = `[batch_size, d0, .. dN]`.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The predicted values. shape = `[batch_size, d0, .. dN]`.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional `sample_weight` acts as a
coefficient for the metric. If a scalar is provided, then the metric is
simply scaled by the given value. If `sample_weight` is a tensor of size
`[batch_size]`, then the metric for each sample of the batch is rescaled
by the corresponding element in the `sample_weight` vector. If the shape
of `sample_weight` is `[batch_size, d0, .. dN-1]` (or can be broadcasted
to this shape), then each metric element of `y_pred` is scaled by the
corresponding value of `sample_weight`. (Note on `dN-1`: all metric
functions reduce by 1 dimension, usually the last axis (-1)).
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





