description: Draws shape samples from each of the given Gamma distribution(s).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.gamma" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.gamma

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/random_ops.py#L477-L568">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Draws `shape` samples from each of the given Gamma distribution(s).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.gamma`, `tf.compat.v1.random_gamma`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.gamma(
    shape, alpha, beta=None, dtype=tf.dtypes.float32, seed=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`alpha` is the shape parameter describing the distribution(s), and `beta` is
the inverse scale parameter(s).

Note: Because internal calculations are done using `float64` and casting has
`floor` semantics, we must manually map zero outcomes to the smallest
possible positive floating-point value, i.e., `np.finfo(dtype).tiny`.  This
means that `np.finfo(dtype).tiny` occurs more frequently than it otherwise
should.  This bias can only happen for small values of `alpha`, i.e.,
`alpha << 1` or large values of `beta`, i.e., `beta >> 1`.

The samples are differentiable w.r.t. alpha and beta.
The derivatives are computed using the approach described in
(Figurnov et al., 2018).

#### Example:



```python
samples = tf.random.gamma([10], [0.5, 1.5])
# samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
# the samples drawn from each distribution

samples = tf.random.gamma([7, 5], [0.5, 1.5])
# samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
# represents the 7x5 samples drawn from each of the two distributions

alpha = tf.constant([[1.],[3.],[5.]])
beta = tf.constant([[3., 4.]])
samples = tf.random.gamma([30], alpha=alpha, beta=beta)
# samples has shape [30, 3, 2], with 30 samples each of 3x2 distributions.

loss = tf.reduce_mean(tf.square(samples))
dloss_dalpha, dloss_dbeta = tf.gradients(loss, [alpha, beta])
# unbiased stochastic derivatives of the loss function
alpha.shape == dloss_dalpha.shape  # True
beta.shape == dloss_dbeta.shape  # True
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output samples
to be drawn per alpha/beta-parameterized distribution.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
A Tensor or Python value or N-D array of type `dtype`. `alpha`
provides the shape parameter(s) describing the gamma distribution(s) to
sample. Must be broadcastable with `beta`.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
A Tensor or Python value or N-D array of type `dtype`. Defaults to 1.
`beta` provides the inverse scale parameter(s) of the gamma
distribution(s) to sample. Must be broadcastable with `alpha`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of alpha, beta, and the output: `float16`, `float32`, or
`float64`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A Python integer. Used to create a random seed for the distributions.
See
<a href="../../tf/random/set_seed.md"><code>tf.random.set_seed</code></a>
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
a `Tensor` of shape
`tf.concat([shape, tf.shape(alpha + beta)], axis=0)` with values of type
`dtype`.
</td>
</tr>
</table>



#### References:

Implicit Reparameterization Gradients:
  [Figurnov et al., 2018]
  (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)
  ([pdf]
  (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf))
