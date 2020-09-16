description: Returns a tensor with random binomial distribution of values. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.random_binomial" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.random_binomial

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L5855-L5890">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a tensor with random binomial distribution of values. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.random_binomial`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.random_binomial(
    shape, p=0.0, dtype=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/keras/backend/random_bernoulli.md"><code>tf.keras.backend.random_bernoulli</code></a> instead.

DEPRECATED, use <a href="../../../tf/keras/backend/random_bernoulli.md"><code>tf.keras.backend.random_bernoulli</code></a> instead.

The binomial distribution with parameters `n` and `p` is the probability
distribution of the number of successful Bernoulli process. Only supports
`n` = 1 for now.

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
`p`
</td>
<td>
A float, `0. <= p <= 1`, probability of binomial distribution.
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



#### Example:



```
>>> random_binomial_tensor = tf.keras.backend.random_binomial(shape=(2,3),
... p=0.5)
>>> random_binomial_tensor
<tf.Tensor: shape=(2, 3), dtype=float32, numpy=...,
dtype=float32)>
```