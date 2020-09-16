description: Computes the cosine similarity between labels and predictions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.cosine_similarity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.cosine_similarity

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/losses.py#L1686-L1728">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the cosine similarity between labels and predictions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.losses.cosine_similarity`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.losses.cosine`, `tf.compat.v1.keras.losses.cosine_proximity`, `tf.compat.v1.keras.losses.cosine_similarity`, `tf.compat.v1.keras.metrics.cosine`, `tf.compat.v1.keras.metrics.cosine_proximity`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.losses.cosine_similarity(
    y_true, y_pred, axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that it is a number between -1 and 1. When it is a negative number
between -1 and 0, 0 indicates orthogonality and values closer to -1
indicate greater similarity. The values closer to 1 indicate greater
dissimilarity. This makes it usable as a loss function in a setting
where you try to maximize the proximity between predictions and
targets. If either `y_true` or `y_pred` is a zero vector, cosine
similarity will be 0 regardless of the proximity between predictions
and targets.

`loss = -sum(l2_norm(y_true) * l2_norm(y_pred))`

#### Standalone usage:



```
>>> y_true = [[0., 1.], [1., 1.], [1., 1.]]
>>> y_pred = [[1., 0.], [1., 1.], [-1., -1.]]
>>> loss = tf.keras.losses.cosine_similarity(y_true, y_pred, axis=1)
>>> loss.numpy()
array([-0., -0.999, 0.999], dtype=float32)
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
</tr><tr>
<td>
`axis`
</td>
<td>
Axis along which to determine similarity.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Cosine similarity tensor.
</td>
</tr>

</table>

