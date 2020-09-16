description: Computes the hinge loss between y_true and y_pred.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.hinge" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.hinge

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L1354-L1382">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the hinge loss between `y_true` and `y_pred`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.metrics.hinge`, `tf.losses.hinge`, `tf.metrics.hinge`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.hinge`, `tf.compat.v1.keras.metrics.hinge`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.hinge(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->

`loss = mean(maximum(1 - y_true * y_pred, 0), axis=-1)`

#### Usage:



```
>>> y_true = np.random.choice([-1, 1], size=(2, 3))
>>> y_pred = np.random.random(size=(2, 3))
>>> loss = tf.keras.losses.hinge(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> assert np.array_equal(
...     loss.numpy(),
...     np.mean(np.maximum(1. - y_true * y_pred, 0.), axis=-1))
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
The ground truth values. `y_true` values are expected to be -1 or 1.
If binary (0 or 1) labels are provided they will be converted to -1 or 1.
shape = `[batch_size, d0, .. dN]`.
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
Hinge loss values. shape = `[batch_size, d0, .. dN-1]`.
</td>
</tr>

</table>

