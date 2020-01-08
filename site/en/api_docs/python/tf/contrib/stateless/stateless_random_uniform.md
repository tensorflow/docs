page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.stateless.stateless_random_uniform

``` python
tf.contrib.stateless.stateless_random_uniform(
    shape,
    seed,
    dtype=tf.float32,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_stateless_random_ops.py`.

Outputs deterministic pseudorandom random values from a uniform distribution.

The generated values follow a uniform distribution in the range `[0, 1)`. The
lower bound 0 is included in the range, while the upper bound 1 is excluded.

The outputs are a deterministic function of `shape` and `seed`.

#### Args:

* <b>`shape`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    The shape of the output tensor.
* <b>`seed`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    2 seeds (shape [2]).
* <b>`dtype`</b>: An optional <a href="../../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.half, tf.float32, tf.float64`. Defaults to <a href="../../../tf#float32"><code>tf.float32</code></a>.
    The type of the output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`.