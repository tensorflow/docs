page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.div

Divides x / y elementwise (using Python 2 division operator semantics). (deprecated)

### Aliases:

* `tf.RaggedTensor.__div__`
* `tf.compat.v1.RaggedTensor.__div__`
* `tf.compat.v1.div`
* `tf.compat.v2.RaggedTensor.__div__`
* `tf.div`

``` python
tf.div(
    x,
    y,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.

NOTE: Prefer using the Tensor division operator or tf.divide which obey Python
3 division operator semantics.

This function divides `x` and `y`, forcing Python 2 semantics. That is, if `x`
and `y` are both integers then the result will be an integer. This is in
contrast to Python 3, where division with `/` is always a float while division
with `//` is always an integer.

#### Args:


* <b>`x`</b>: `Tensor` numerator of real numeric type.
* <b>`y`</b>: `Tensor` denominator of real numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`x / y` returns the quotient of x and y.
