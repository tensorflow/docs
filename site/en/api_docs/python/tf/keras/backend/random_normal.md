description: Returns a tensor with normal distribution of values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.random_normal" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.random_normal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/backend.py#L5637-L5662">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a tensor with normal distribution of values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.random_normal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.random_normal(
    shape, mean=0.0, stddev=1.0, dtype=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It is an alias to <a href="../../../tf/random/normal.md"><code>tf.random.normal</code></a>.

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
A float, the mean value of the normal distribution to draw samples.
Default to 0.0.
</td>
</tr><tr>
<td>
`stddev`
</td>
<td>
A float, the standard deviation of the normal distribution
to draw samples. Default to 1.0.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
<a href="../../../tf/dtypes/DType.md"><code>tf.dtypes.DType</code></a>, dtype of returned tensor. Default to use Keras
backend dtype which is float32.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Integer, random seed. Will use a random numpy integer when not
specified.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor with normal distribution of values.
</td>
</tr>

</table>

