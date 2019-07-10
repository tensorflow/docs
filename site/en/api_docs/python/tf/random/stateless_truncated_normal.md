page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.stateless_truncated_normal

Outputs deterministic pseudorandom values, truncated normally distributed.

### Aliases:

* `tf.compat.v1.random.stateless_truncated_normal`
* `tf.compat.v2.random.stateless_truncated_normal`
* `tf.contrib.stateless.stateless_truncated_normal`
* `tf.random.stateless_truncated_normal`

``` python
tf.random.stateless_truncated_normal(
    shape,
    seed,
    mean=0.0,
    stddev=1.0,
    dtype=tf.dtypes.float32,
    name=None
)
```



Defined in [`python/ops/stateless_random_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/stateless_random_ops.py).

<!-- Placeholder for "Used in" -->

This is a stateless version of <a href="../../tf/random/truncated_normal"><code>tf.random.truncated_normal</code></a>: if run twice with
the
same seeds, it will produce the same pseudorandom numbers.  The output is
consistent across multiple runs on the same hardware (and between CPU
and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
hardware.

The generated values follow a normal distribution with specified mean and
standard deviation, except that values whose magnitude is more than 2 standard
deviations from the mean are dropped and re-picked.

#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output tensor.
* <b>`seed`</b>: A shape [2] integer Tensor of seeds to the random number generator.
* <b>`mean`</b>: A 0-D Tensor or Python value of type `dtype`. The mean of the
  truncated normal distribution.
* <b>`stddev`</b>: A 0-D Tensor or Python value of type `dtype`. The standard deviation
  of the normal distribution, before truncation.
* <b>`dtype`</b>: The type of the output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random truncated normal values.
