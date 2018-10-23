

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.stateless.stateless_random_normal

``` python
stateless_random_normal(
    shape,
    seed,
    dtype=tf.float32,
    name=None
)
```



Defined in `tensorflow/contrib/stateless/gen_stateless_random_ops.py`.

Outputs deterministic pseudorandom values from a normal distribution.

The generated values will have mean 0 and standard deviation 1.

The outputs are a deterministic function of `shape` and `seed`.

#### Args:

* <b>`shape`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    The shape of the output tensor.
* <b>`seed`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    2 seeds (shape [2]).
* <b>`dtype`</b>: An optional `tf.DType` from: `tf.half, tf.float32, tf.float64`. Defaults to `tf.float32`.
    The type of the output.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`. Random values with specified shape.