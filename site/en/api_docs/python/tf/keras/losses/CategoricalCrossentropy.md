description: Computes the crossentropy loss between the labels and predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.CategoricalCrossentropy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.losses.CategoricalCrossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/losses.py#L587-L662">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the crossentropy loss between the labels and predictions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.losses.CategoricalCrossentropy`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.CategoricalCrossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.CategoricalCrossentropy(
    from_logits=(False), label_smoothing=0, reduction=losses_utils.ReductionV2.AUTO,
    name='categorical_crossentropy'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use this crossentropy loss function when there are two or more label classes.
We expect labels to be provided in a `one_hot` representation. If you want to
provide labels as integers, please use `SparseCategoricalCrossentropy` loss.
There should be `# classes` floating point values per feature.

In the snippet below, there is `# classes` floating pointing values per
example. The shape of both `y_pred` and `y_true` are
`[batch_size, num_classes]`.

#### Standalone usage:



```
>>> y_true = [[0, 1, 0], [0, 0, 1]]
>>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
>>> # Using 'auto'/'sum_over_batch_size' reduction type.
>>> cce = tf.keras.losses.CategoricalCrossentropy()
>>> cce(y_true, y_pred).numpy()
1.177
```

```
>>> # Calling with 'sample_weight'.
>>> cce(y_true, y_pred, sample_weight=tf.constant([0.3, 0.7])).numpy()
0.814
```

```
>>> # Using 'sum' reduction type.
>>> cce = tf.keras.losses.CategoricalCrossentropy(
...     reduction=tf.keras.losses.Reduction.SUM)
>>> cce(y_true, y_pred).numpy()
2.354
```

```
>>> # Using 'none' reduction type.
>>> cce = tf.keras.losses.CategoricalCrossentropy(
...     reduction=tf.keras.losses.Reduction.NONE)
>>> cce(y_true, y_pred).numpy()
array([0.0513, 2.303], dtype=float32)
```

Usage with the `compile()` API:

```python
model.compile(optimizer='sgd', loss=tf.keras.losses.CategoricalCrossentropy())
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`from_logits`
</td>
<td>
Whether `y_pred` is expected to be a logits tensor. By
default, we assume that `y_pred` encodes a probability distribution.
**Note - Using from_logits=True is more numerically stable.**
</td>
</tr><tr>
<td>
`label_smoothing`
</td>
<td>
Float in [0, 1]. When > 0, label values are smoothed,
meaning the confidence on label values are relaxed. e.g.
`label_smoothing=0.2` means that we will use a value of `0.1` for label
`0` and `0.9` for label `1`"
</td>
</tr><tr>
<td>
`reduction`
</td>
<td>
(Optional) Type of <a href="../../../tf/keras/losses/Reduction.md"><code>tf.keras.losses.Reduction</code></a> to apply to
loss. Default value is `AUTO`. `AUTO` indicates that the reduction
option will be determined by the usage context. For almost all cases
this defaults to `SUM_OVER_BATCH_SIZE`. When used with
<a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>, outside of built-in training loops such as
<a href="../../../tf/keras.md"><code>tf.keras</code></a> `compile` and `fit`, using `AUTO` or `SUM_OVER_BATCH_SIZE`
will raise an error. Please see this custom training [tutorial](
https://www.tensorflow.org/tutorials/distribute/custom_training)
for more details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the op. Defaults to 'categorical_crossentropy'.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/losses.py#L156-L166">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

Instantiates a `Loss` from its config (output of `get_config()`).


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config`
</td>
<td>
Output of `get_config()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Loss` instance.
</td>
</tr>

</table>



<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/losses.py#L258-L263">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the config dictionary for a `Loss` instance.


<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/losses.py#L117-L154">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    y_true, y_pred, sample_weight=None
)
</code></pre>

Invokes the `Loss` instance.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`y_true`
</td>
<td>
Ground truth values. shape = `[batch_size, d0, .. dN]`, except
sparse loss functions such as sparse categorical crossentropy where
shape = `[batch_size, d0, .. dN-1]`
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The predicted values. shape = `[batch_size, d0, .. dN]`
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Optional `sample_weight` acts as a
coefficient for the loss. If a scalar is provided, then the loss is
simply scaled by the given value. If `sample_weight` is a tensor of size
`[batch_size]`, then the total loss for each sample of the batch is
rescaled by the corresponding element in the `sample_weight` vector. If
the shape of `sample_weight` is `[batch_size, d0, .. dN-1]` (or can be
broadcasted to this shape), then each loss element of `y_pred` is scaled
by the corresponding value of `sample_weight`. (Note on`dN-1`: all loss
functions reduce by 1 dimension, usually axis=-1.)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Weighted loss float `Tensor`. If `reduction` is `NONE`, this has
shape `[batch_size, d0, .. dN-1]`; otherwise, it is scalar. (Note `dN-1`
because all loss functions reduce by 1 dimension, usually axis=-1.)
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the shape of `sample_weight` is invalid.
</td>
</tr>
</table>





