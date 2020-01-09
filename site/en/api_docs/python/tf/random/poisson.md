page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.poisson


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/random/poisson">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/random_ops.py#L499-L536">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Draws `shape` samples from each of the given Poisson distribution(s).

### Aliases:

* <a href="/api_docs/python/tf/random/poisson"><code>tf.compat.v1.random.poisson</code></a>
* <a href="/api_docs/python/tf/random/poisson"><code>tf.compat.v1.random_poisson</code></a>
* <a href="/api_docs/python/tf/random/poisson"><code>tf.random_poisson</code></a>


``` python
tf.random.poisson(
    lam,
    shape,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)
```



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

#### Args:


* <b>`lam`</b>: A Tensor or Python value or N-D array of type `dtype`.
  `lam` provides the rate parameter(s) describing the poisson
  distribution(s) to sample.
* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output samples
  to be drawn per "rate"-parameterized distribution.
* <b>`dtype`</b>: The type of the output: `float16`, `float32`, `float64`, `int32` or
  `int64`.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distributions.
  See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: Optional name for the operation.


#### Returns:


* <b>`samples`</b>: a `Tensor` of shape `tf.concat([shape, tf.shape(lam)], axis=0)`
  with values of type `dtype`.
