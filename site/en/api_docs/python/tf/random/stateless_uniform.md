page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.stateless_uniform

### Aliases:

* `tf.contrib.stateless.stateless_random_uniform`
* `tf.random.stateless_uniform`

``` python
tf.random.stateless_uniform(
    shape,
    seed,
    minval=0,
    maxval=None,
    dtype=tf.dtypes.float32,
    name=None
)
```



Defined in [`tensorflow/python/ops/stateless_random_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/stateless_random_ops.py).

Outputs deterministic pseudorandom values from a uniform distribution.

This is a stateless version of <a href="../../tf/random/uniform"><code>tf.random_uniform</code></a>: if run twice with the
same seeds, it will produce the same pseudorandom numbers.  The output is
consistent across multiple runs on the same hardware (and between CPU
and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
hardware.

The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while
the upper bound `maxval` is excluded.

For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
be specified explicitly.

In the integer case, the random integers are slightly biased unless
`maxval - minval` is an exact power of two.  The bias is small for values of
`maxval - minval` significantly smaller than the range of the output (either
`2**32` or `2**64`).

#### Args:

* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output tensor.
* <b>`seed`</b>: A shape [2] integer Tensor of seeds to the random number generator.
* <b>`minval`</b>: A 0-D Tensor or Python value of type `dtype`. The lower bound on the
    range of random values to generate.  Defaults to 0.
* <b>`maxval`</b>: A 0-D Tensor or Python value of type `dtype`. The upper bound on the
    range of random values to generate.  Defaults to 1 if `dtype` is floating
    point.
* <b>`dtype`</b>: The type of the output: `float16`, `float32`, `float64`, `int32`, or
    `int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random uniform values.


#### Raises:

* <b>`ValueError`</b>: If `dtype` is integral and `maxval` is not specified.