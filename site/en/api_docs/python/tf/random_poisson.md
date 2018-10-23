

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.random_poisson

``` python
tf.random_poisson(
    lam,
    shape,
    dtype=tf.float32,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/random_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/ops/random_ops.py).

Draws `shape` samples from each of the given Poisson distribution(s).

`lam` is the rate parameter describing the distribution(s).

Example:

  samples = tf.random_poisson([0.5, 1.5], [10])
  # samples has shape [10, 2], where each slice [:, 0] and [:, 1] represents
  # the samples drawn from each distribution

  samples = tf.random_poisson([12.2, 3.3], [7, 5])
  # samples has shape [7, 5, 2], where each slice [:, :, 0] and [:, :, 1]
  # represents the 7x5 samples drawn from each of the two distributions

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
    <a href="../tf/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

* <b>`samples`</b>: a `Tensor` of shape `tf.concat(shape, tf.shape(lam))` with
    values of type `dtype`.