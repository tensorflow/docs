

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random_uniform

``` python
tf.random_uniform(
    shape,
    minval=0,
    maxval=None,
    dtype=tf.float32,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/random_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/random_ops.py).

See the guide: [Constants, Sequences, and Random Values > Random Tensors](../../../api_guides/python/constant_op#Random_Tensors)

Outputs random values from a uniform distribution.

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
* <b>`minval`</b>: A 0-D Tensor or Python value of type `dtype`. The lower bound on the
    range of random values to generate.  Defaults to 0.
* <b>`maxval`</b>: A 0-D Tensor or Python value of type `dtype`. The upper bound on
    the range of random values to generate.  Defaults to 1 if `dtype` is
    floating point.
* <b>`dtype`</b>: The type of the output: `float16`, `float32`, `float64`, `int32`,
    or `int64`.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
    See <a href="../tf/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random uniform values.


#### Raises:

* <b>`ValueError`</b>: If `dtype` is integral and `maxval` is not specified.