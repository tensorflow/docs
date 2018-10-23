

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.scalar_mul

``` python
scalar_mul(
    scalar,
    x
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Arithmetic Operators](../../../api_guides/python/math_ops#Arithmetic_Operators)

Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

Intended for use in gradient code which might deal with `IndexedSlices`
objects, which are easy to multiply by a scalar but more expensive to
multiply with arbitrary tensors.

#### Args:

* <b>`scalar`</b>: A 0-D scalar `Tensor`. Must have known shape.
* <b>`x`</b>: A `Tensor` or `IndexedSlices` to be scaled.


#### Returns:

  `scalar * x` of the same type (`Tensor` or `IndexedSlices`) as `x`.


#### Raises:

* <b>`ValueError`</b>: if scalar is not a 0-D `scalar`.