description: Logarithm of the hyperbolic cosine of the prediction error.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.log_cosh" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.log_cosh

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/losses.py#L1459-L1495">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Logarithm of the hyperbolic cosine of the prediction error.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.losses.logcosh`, `tf.keras.metrics.log_cosh`, `tf.keras.metrics.logcosh`, `tf.losses.log_cosh`, `tf.losses.logcosh`, `tf.metrics.log_cosh`, `tf.metrics.logcosh`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.log_cosh`, `tf.compat.v1.keras.losses.logcosh`, `tf.compat.v1.keras.metrics.log_cosh`, `tf.compat.v1.keras.metrics.logcosh`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.log_cosh(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

`log(cosh(x))` is approximately equal to `(x ** 2) / 2` for small `x` and
to `abs(x) - log(2)` for large `x`. This means that 'logcosh' works mostly
like the mean squared error, but will not be so strongly affected by the
occasional wildly incorrect prediction.

#### Standalone usage:



```
>>> y_true = np.random.random(size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.logcosh(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> x = y_pred - y_true
>>> assert np.allclose(
...     loss.numpy(),
...     np.mean(x + np.log(np.exp(-2. * x) + 1.) - math_ops.log(2.), axis=-1),
...     atol=1e-5)
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
Logcosh error values. shape = `[batch_size, d0, .. dN-1]`.
</td>
</tr>

</table>

