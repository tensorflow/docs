description: Computes Kullback-Leibler divergence loss between y_true and y_pred.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.KLD" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.KLD

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/losses.py#L1608-L1649">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes Kullback-Leibler divergence loss between `y_true` and `y_pred`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.losses.kl_divergence`, `tf.keras.losses.kld`, `tf.keras.losses.kullback_leibler_divergence`, `tf.keras.metrics.KLD`, `tf.keras.metrics.kl_divergence`, `tf.keras.metrics.kld`, `tf.keras.metrics.kullback_leibler_divergence`, `tf.losses.KLD`, `tf.losses.kl_divergence`, `tf.losses.kld`, `tf.losses.kullback_leibler_divergence`, `tf.metrics.KLD`, `tf.metrics.kl_divergence`, `tf.metrics.kld`, `tf.metrics.kullback_leibler_divergence`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.KLD`, `tf.compat.v1.keras.losses.kl_divergence`, `tf.compat.v1.keras.losses.kld`, `tf.compat.v1.keras.losses.kullback_leibler_divergence`, `tf.compat.v1.keras.metrics.KLD`, `tf.compat.v1.keras.metrics.kl_divergence`, `tf.compat.v1.keras.metrics.kld`, `tf.compat.v1.keras.metrics.kullback_leibler_divergence`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.KLD(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

`loss = y_true * log(y_true / y_pred)`

See: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

#### Standalone usage:



```
>>> y_true = np.random.randint(0, 2, size=(2, 3)).astype(np.float64)
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.kullback_leibler_divergence(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> y_true = tf.keras.backend.clip(y_true, 1e-7, 1)
>>> y_pred = tf.keras.backend.clip(y_pred, 1e-7, 1)
>>> assert np.array_equal(
...     loss.numpy(), np.sum(y_true * np.log(y_true / y_pred), axis=-1))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`y_true`
</td>
<td>
Tensor of true targets.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
Tensor of predicted targets.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with loss.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `y_true` cannot be cast to the `y_pred.dtype`.
</td>
</tr>
</table>

