description: Computes the mean absolute error between labels and predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.MAE" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.MAE

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/losses.py#L1201-L1231">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the mean absolute error between labels and predictions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.losses.mae`, `tf.keras.losses.mean_absolute_error`, `tf.keras.metrics.MAE`, `tf.keras.metrics.mae`, `tf.keras.metrics.mean_absolute_error`, `tf.losses.MAE`, `tf.losses.mae`, `tf.losses.mean_absolute_error`, `tf.metrics.MAE`, `tf.metrics.mae`, `tf.metrics.mean_absolute_error`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.MAE`, `tf.compat.v1.keras.losses.mae`, `tf.compat.v1.keras.losses.mean_absolute_error`, `tf.compat.v1.keras.metrics.MAE`, `tf.compat.v1.keras.metrics.mae`, `tf.compat.v1.keras.metrics.mean_absolute_error`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.MAE(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

`loss = mean(abs(y_true - y_pred), axis=-1)`

#### Standalone usage:



```
>>> y_true = np.random.randint(0, 2, size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.mean_absolute_error(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> assert np.array_equal(
...     loss.numpy(), np.mean(np.abs(y_true - y_pred), axis=-1))
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
Mean absolute error values. shape = `[batch_size, d0, .. dN-1]`.
</td>
</tr>

</table>

