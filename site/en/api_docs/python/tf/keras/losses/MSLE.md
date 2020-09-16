description: Computes the mean squared logarithmic error between y_true and y_pred.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.MSLE" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.MSLE

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/losses.py#L1268-L1304">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the mean squared logarithmic error between `y_true` and `y_pred`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.losses.mean_squared_logarithmic_error`, `tf.keras.losses.msle`, `tf.keras.metrics.MSLE`, `tf.keras.metrics.mean_squared_logarithmic_error`, `tf.keras.metrics.msle`, `tf.losses.MSLE`, `tf.losses.mean_squared_logarithmic_error`, `tf.losses.msle`, `tf.metrics.MSLE`, `tf.metrics.mean_squared_logarithmic_error`, `tf.metrics.msle`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.MSLE`, `tf.compat.v1.keras.losses.mean_squared_logarithmic_error`, `tf.compat.v1.keras.losses.msle`, `tf.compat.v1.keras.metrics.MSLE`, `tf.compat.v1.keras.metrics.mean_squared_logarithmic_error`, `tf.compat.v1.keras.metrics.msle`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.MSLE(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

`loss = mean(square(log(y_true + 1) - log(y_pred + 1)), axis=-1)`

#### Standalone usage:



```
>>> y_true = np.random.randint(0, 2, size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.mean_squared_logarithmic_error(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> y_true = np.maximum(y_true, 1e-7)
>>> y_pred = np.maximum(y_pred, 1e-7)
>>> assert np.array_equal(
...     loss.numpy(),
...     np.mean(
...         np.square(np.log(y_true + 1.) - np.log(y_pred + 1.)), axis=-1))
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
Ground truth values. shape = `[batch_size, d0, .. dN]`.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The predicted values. shape = `[batch_size, d0, .. dN]`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Mean squared logarithmic error values. shape = `[batch_size, d0, .. dN-1]`.
</td>
</tr>

</table>

