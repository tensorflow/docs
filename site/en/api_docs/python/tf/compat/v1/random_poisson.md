description: Draws shape samples from each of the given Poisson distribution(s).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.random_poisson" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.random_poisson

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/random_ops.py#L623-L661">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Draws `shape` samples from each of the given Poisson distribution(s).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.poisson`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.random_poisson(
    lam, shape, dtype=tf.dtypes.float32, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`lam` is the rate parameter describing the distribution(s).

#### Example:



```python
samples = tf.random.poisson([0.5, 1.5], [10])
# samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
# the samples drawn from each distribution

samples = tf.random.poisson([12.2, 3.3], [7, 5])
# samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
# represents the 7x5 samples drawn from each of the two distributions
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`lam`
</td>
<td>
A Tensor or Python value or N-D array of type `dtype`.
`lam` provides the rate parameter(s) describing the poisson
distribution(s) to sample.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output samples
to be drawn per "rate"-parameterized distribution.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output: `float16`, `float32`, `float64`, `int32` or
`int64`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer. Used to create a random seed for the distributions.
See
<a href="../../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>
for behavior.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`samples`
</td>
<td>
a `Tensor` of shape `tf.concat([shape, tf.shape(lam)], axis=0)`
with values of type `dtype`.
</td>
</tr>
</table>

