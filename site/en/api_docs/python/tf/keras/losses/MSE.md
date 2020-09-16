description: Computes the mean squared error between labels and predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.MSE" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.MSE

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L1166-L1198">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the mean squared error between labels and predictions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.losses.mean_squared_error`, `tf.keras.losses.mse`, `tf.keras.metrics.MSE`, `tf.keras.metrics.mean_squared_error`, `tf.keras.metrics.mse`, `tf.losses.MSE`, `tf.losses.mean_squared_error`, `tf.losses.mse`, `tf.metrics.MSE`, `tf.metrics.mean_squared_error`, `tf.metrics.mse`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.MSE`, `tf.compat.v1.keras.losses.mean_squared_error`, `tf.compat.v1.keras.losses.mse`, `tf.compat.v1.keras.metrics.MSE`, `tf.compat.v1.keras.metrics.mean_squared_error`, `tf.compat.v1.keras.metrics.mse`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.MSE(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

After computing the squared distance between the inputs, the mean value over
the last dimension is returned.

`loss = mean(square(y_true - y_pred), axis=-1)`

#### Usage:



```
>>> y_true = np.random.randint(0, 2, size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.mean_squared_error(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> assert np.array_equal(
...     loss.numpy(), np.mean(np.square(y_true - y_pred), axis=-1))
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
Mean squared error values. shape = `[batch_size, d0, .. dN-1]`.
</td>
</tr>

</table>

