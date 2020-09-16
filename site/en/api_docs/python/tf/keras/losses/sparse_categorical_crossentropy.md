description: Computes the sparse categorical crossentropy loss.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.sparse_categorical_crossentropy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.sparse_categorical_crossentropy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/losses.py#L1530-L1558">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the sparse categorical crossentropy loss.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.keras.metrics.sparse_categorical_crossentropy`, `tf.losses.sparse_categorical_crossentropy`, `tf.metrics.sparse_categorical_crossentropy`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.sparse_categorical_crossentropy`, `tf.compat.v1.keras.metrics.sparse_categorical_crossentropy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.sparse_categorical_crossentropy(
    y_true, y_pred, from_logits=(False), axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage:



```
>>> y_true = [1, 2]
>>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
>>> loss = tf.keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> loss.numpy()
array([0.0513, 2.303], dtype=float32)
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
Ground truth values.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The predicted values.
</td>
</tr><tr>
<td>
`from_logits`
</td>
<td>
Whether `y_pred` is expected to be a logits tensor. By default,
we assume that `y_pred` encodes a probability distribution.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
(Optional) Defaults to -1. The dimension along which the entropy is
computed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Sparse categorical crossentropy loss value.
</td>
</tr>

</table>

