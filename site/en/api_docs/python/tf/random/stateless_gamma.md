description: Outputs deterministic pseudorandom values from a gamma distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.stateless_gamma" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.stateless_gamma

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/stateless_random_ops.py#L200-L294">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs deterministic pseudorandom values from a gamma distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.stateless_gamma`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.stateless_gamma(
    shape, seed, alpha, beta=None, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated values follow a gamma distribution with specified concentration
(`alpha`) and inverse scale (`beta`) parameters.

This is a stateless version of <a href="../../tf/random/gamma.md"><code>tf.random.gamma</code></a>: if run twice with the same
seeds, it will produce the same pseudorandom numbers. The output is consistent
across multiple runs on the same hardware (and between CPU and GPU), but may
change between versions of TensorFlow or on non-CPU/GPU hardware.

A slight difference exists in the interpretation of the `shape` parameter
between `stateless_gamma` and `gamma`: in `gamma`, the `shape` is always
prepended to the shape of the broadcast of `alpha` with `beta`; whereas in
`stateless_gamma` the `shape` parameter must always encompass the shapes of
each of `alpha` and `beta` (which must broadcast together to match the
trailing dimensions of `shape`).

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
samples = tf.random.stateless_gamma([10, 2], seed=[12, 34], alpha=[0.5, 1.5])
# samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
# the samples drawn from each distribution

samples = tf.random.stateless_gamma([7, 5, 2], seed=[12, 34], alpha=[.5, 1.5])
# samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
# represents the 7x5 samples drawn from each of the two distributions

alpha = tf.constant([[1.], [3.], [5.]])
beta = tf.constant([[3., 4.]])
samples = tf.random.stateless_gamma(
    [30, 3, 2], seed=[12, 34], alpha=alpha, beta=beta)
# samples has shape [30, 3, 2], with 30 samples each of 3x2 distributions.

with tf.GradientTape() as tape:
  tape.watch([alpha, beta])
  loss = tf.reduce_mean(tf.square(tf.random.stateless_gamma(
      [30, 3, 2], seed=[12, 34], alpha=alpha, beta=beta)))
dloss_dalpha, dloss_dbeta = tape.gradient(loss, [alpha, beta])
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
A 1-D integer Tensor or Python array. The shape of the output tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A shape [2] integer Tensor of seeds to the random number generator.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
Tensor. The concentration parameter of the gamma distribution. Must
be broadcastable with `beta`, and broadcastable with the rightmost
dimensions of `shape`.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
Tensor. The inverse scale parameter of the gamma distribution. Must be
broadcastable with `alpha` and broadcastable with the rightmost dimensions
of `shape`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Floating point dtype of `alpha`, `beta`, and the output.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
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
A Tensor of the specified shape filled with random gamma values.
For each i, each `samples[..., i] is an independent draw from the gamma
distribution with concentration alpha[i] and scale beta[i].
</td>
</tr>
</table>

