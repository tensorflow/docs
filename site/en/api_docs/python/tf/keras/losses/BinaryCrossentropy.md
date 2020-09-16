description: Computes the cross-entropy loss between true labels and predicted labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.BinaryCrossentropy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.losses.BinaryCrossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L499-L576">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the cross-entropy loss between true labels and predicted labels.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.losses.BinaryCrossentropy`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.BinaryCrossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.BinaryCrossentropy(
    from_logits=(False), label_smoothing=0, reduction=losses_utils.ReductionV2.AUTO,
    name='binary_crossentropy'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use this cross-entropy loss when there are only two label classes (assumed to
be 0 and 1). For each example, there should be a single floating-point value
per prediction.

In the snippet below, each of the four examples has only a single
floating-pointing value, and both `y_pred` and `y_true` have the shape
`[batch_size]`.

#### Usage:



```
>>> y_true = [[0., 1.], [0., 0.]]
>>> y_pred = [[0.6, 0.4], [0.4, 0.6]]
>>> # Using 'auto'/'sum_over_batch_size' reduction type.
>>> bce = tf.keras.losses.BinaryCrossentropy()
>>> bce(y_true, y_pred).numpy()
0.815
```

```
>>> # Calling with 'sample_weight'.
>>> bce(y_true, y_pred, sample_weight=[1, 0]).numpy()
0.458
```

 ```
 >>> # Using 'sum' reduction type.
>>> bce = tf.keras.losses.BinaryCrossentropy(
...     reduction=tf.keras.losses.Reduction.SUM)
>>> bce(y_true, y_pred).numpy()
1.630
 ```

```
>>> # Using 'none' reduction type.
>>> bce = tf.keras.losses.BinaryCrossentropy(
...     reduction=tf.keras.losses.Reduction.NONE)
>>> bce(y_true, y_pred).numpy()
array([0.916 , 0.714], dtype=float32)
```

Usage with the <a href="../../../tf/keras.md"><code>tf.keras</code></a> API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', loss=tf.keras.losses.BinaryCrossentropy())
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
Whether to interpret `y_pred` as a tensor of
[logit](https://en.wikipedia.org/wiki/Logit) values. By default, we
assume that `y_pred` contains probabilities (i.e., values in [0, 1]).
**Note - Using from_logits=True may be more numerically stable.
</td>
</tr><tr>
<td>
`label_smoothing`
</td>
<td>
Float in [0, 1]. When 0, no smoothing occurs. When > 0,
we compute the loss between the predicted labels and a smoothed version
of the true labels, where the smoothing squeezes the labels towards 0.5.
Larger values of `label_smoothing` correspond to heavier smoothing.
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
will raise an error. Please see this custom training [tutorial]
(https://www.tensorflow.org/tutorials/distribute/custom_training)
for more details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional) Name for the op. Defaults to 'binary_crossentropy'.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L147-L157">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L248-L253">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the config dictionary for a `Loss` instance.


<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L112-L145">View source</a>

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





