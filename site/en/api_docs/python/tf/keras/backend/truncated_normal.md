description: Returns a tensor with truncated random normal distribution of values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.truncated_normal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.truncated_normal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L5715-L5739">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a tensor with truncated random normal distribution of values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.truncated_normal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.truncated_normal(
    shape, mean=0.0, stddev=1.0, dtype=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a normal distribution
with specified mean and standard deviation,
except that values whose magnitude is more than
two standard deviations from the mean are dropped and re-picked.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A tuple of integers, the shape of tensor to create.
</td>
</tr><tr>
<td>
`mean`
</td>
<td>
Mean of the values.
</td>
</tr><tr>
<td>
`stddev`
</td>
<td>
Standard deviation of the values.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
String, dtype of returned tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Integer, random seed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor.
</td>
</tr>

</table>

