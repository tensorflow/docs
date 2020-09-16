description: Computes the mean absolute percentage error between y_true and y_pred.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.MAPE" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.MAPE

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/losses.py#L1231-L1265">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the mean absolute percentage error between `y_true` and `y_pred`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.losses.mape`, `tf.keras.losses.mean_absolute_percentage_error`, `tf.keras.metrics.MAPE`, `tf.keras.metrics.mape`, `tf.keras.metrics.mean_absolute_percentage_error`, `tf.losses.MAPE`, `tf.losses.mape`, `tf.losses.mean_absolute_percentage_error`, `tf.metrics.MAPE`, `tf.metrics.mape`, `tf.metrics.mean_absolute_percentage_error`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.MAPE`, `tf.compat.v1.keras.losses.mape`, `tf.compat.v1.keras.losses.mean_absolute_percentage_error`, `tf.compat.v1.keras.metrics.MAPE`, `tf.compat.v1.keras.metrics.mape`, `tf.compat.v1.keras.metrics.mean_absolute_percentage_error`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.MAPE(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

`loss = 100 * mean(abs((y_true - y_pred) / y_true), axis=-1)`

#### Standalone usage:



```
>>> y_true = np.random.random(size=(2, 3))
>>> y_true = np.maximum(y_true, 1e-7)  # Prevent division by zero
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.mean_absolute_percentage_error(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> assert np.array_equal(
...     loss.numpy(),
...     100. * np.mean(np.abs((y_true - y_pred) / y_true), axis=-1))
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
Mean absolute percentage error values. shape = `[batch_size, d0, .. dN-1]`.
</td>
</tr>

</table>

