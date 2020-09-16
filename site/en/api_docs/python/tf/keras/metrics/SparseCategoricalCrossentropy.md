description: Computes the crossentropy metric between the labels and predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.SparseCategoricalCrossentropy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.SparseCategoricalCrossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/metrics.py#L3048-L3117">
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
<p>`tf.metrics.SparseCategoricalCrossentropy`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.SparseCategoricalCrossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.SparseCategoricalCrossentropy(
    name='sparse_categorical_crossentropy', dtype=None, from_logits=(False), axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use this crossentropy metric when there are two or more label classes.
We expect labels to be provided as integers. If you want to provide labels
using `one-hot` representation, please use `CategoricalCrossentropy` metric.
There should be `# classes` floating point values per feature for `y_pred`
and a single floating point value per feature for `y_true`.

In the snippet below, there is a single floating point value per example for
`y_true` and `# classes` floating pointing values per example for `y_pred`.
The shape of `y_true` is `[batch_size]` and the shape of `y_pred` is
`[batch_size, num_classes]`.

#### Usage:



```
>>> # y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]]
>>> # logits = log(y_pred)
>>> # softmax = exp(logits) / sum(exp(logits), axis=-1)
>>> # softmax = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]
>>> # xent = -sum(y * log(softmax), 1)
>>> # log(softmax) = [[-2.9957, -0.0513, -16.1181],
>>> #                [-2.3026, -0.2231, -2.3026]]
>>> # y_true * log(softmax) = [[0, -0.0513, 0], [0, 0, -2.3026]]
>>> # xent = [0.0513, 2.3026]
>>> # Reduced xent = (0.0513 + 2.3026) / 2
>>> m = tf.keras.metrics.SparseCategoricalCrossentropy()
>>> _ = m.update_state([1, 2],
...                    [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
>>> m.result().numpy()
1.1769392
```

```
>>> m.reset_states()
>>> _ = m.update_state([1, 2],
...                    [[0.05, 0.95, 0], [0.1, 0.8, 0.1]],
...                    sample_weight=tf.constant([0.3, 0.7]))
>>> m.result().numpy()
1.6271976
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile(
  'sgd',
  loss='mse',
  metrics=[tf.keras.metrics.SparseCategoricalCrossentropy()])
```

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
(Optional ) Whether `y_pred` is expected to be a logits tensor.
By default, we assume that `y_pred` encodes a probability distribution.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
(Optional) Defaults to -1. The dimension along which the metric is
computed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`fn`
</td>
<td>
The metric function to wrap, with signature
`fn(y_true, y_pred, **kwargs)`.
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
</tr><tr>
<td>
`**kwargs`
</td>
<td>
The keyword arguments that are passed on to `fn`.
</td>
</tr>
</table>



## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/metrics.py#L218-L224">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset_states()
</code></pre>

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/metrics.py#L376-L386">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>result()
</code></pre>

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/metrics.py#L574-L605">View source</a>

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





