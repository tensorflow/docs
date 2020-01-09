page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.gamma


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/random/gamma">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/random_ops.py#L413-L496">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Draws `shape` samples from each of the given Gamma distribution(s).

### Aliases:

* <a href="/api_docs/python/tf/random/gamma"><code>tf.compat.v1.random.gamma</code></a>
* <a href="/api_docs/python/tf/random/gamma"><code>tf.compat.v1.random_gamma</code></a>
* <a href="/api_docs/python/tf/random/gamma"><code>tf.compat.v2.random.gamma</code></a>
* <a href="/api_docs/python/tf/random/gamma"><code>tf.random_gamma</code></a>


``` python
tf.random.gamma(
    shape,
    alpha,
    beta=None,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)
```



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
The derivatives are computed using the approach described in the paper

[Michael Figurnov, Shakir Mohamed, Andriy Mnih.
Implicit Reparameterization Gradients, 2018](https://arxiv.org/abs/1805.08498)

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

#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output samples
  to be drawn per alpha/beta-parameterized distribution.
* <b>`alpha`</b>: A Tensor or Python value or N-D array of type `dtype`. `alpha`
  provides the shape parameter(s) describing the gamma distribution(s) to
  sample. Must be broadcastable with `beta`.
* <b>`beta`</b>: A Tensor or Python value or N-D array of type `dtype`. Defaults to 1.
  `beta` provides the inverse scale parameter(s) of the gamma
  distribution(s) to sample. Must be broadcastable with `alpha`.
* <b>`dtype`</b>: The type of alpha, beta, and the output: `float16`, `float32`, or
  `float64`.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distributions.
  See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: Optional name for the operation.


#### Returns:


* <b>`samples`</b>: a `Tensor` of shape
  `tf.concat([shape, tf.shape(alpha + beta)], axis=0)` with values of type
  `dtype`.
