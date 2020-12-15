description: Calculates how often predictions matches one-hot labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.categorical_accuracy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.metrics.categorical_accuracy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/metrics.py#L3242-L3268">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calculates how often predictions matches one-hot labels.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.metrics.categorical_accuracy`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.metrics.categorical_accuracy`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.metrics.categorical_accuracy(
    y_true, y_pred
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Standalone usage:


>>> y_true = [[0, 0, 1], [0, 1, 0]]
>>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
>>> m = tf.keras.metrics.categorical_accuracy(y_true, y_pred)
>>> assert m.shape == (2,)
>>> m.numpy()
array([0., 1.], dtype=float32)

You can provide logits of classes as `y_pred`, since argmax of
logits and probabilities are same.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`y_true`
</td>
<td>
One-hot ground truth values.
</td>
</tr><tr>
<td>
`y_pred`
</td>
<td>
The prediction values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Categorical accuracy values.
</td>
</tr>

</table>

