page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.polyval

Computes the elementwise value of a polynomial.

### Aliases:

* `tf.compat.v1.math.polyval`
* `tf.compat.v2.math.polyval`
* `tf.math.polyval`

``` python
tf.math.polyval(
    coeffs,
    x,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

If `x` is a tensor and `coeffs` is a list n + 1 tensors, this function returns
the value of the n-th order polynomial

   p(x) = coeffs[n-1] + coeffs[n-2] * x + ...  + coeffs[0] * x**(n-1)

evaluated using Horner's method, i.e.

   p(x) = coeffs[n-1] + x * (coeffs[n-2] + ... + x * (coeffs[1] +
          x * coeffs[0]))

#### Args:


* <b>`coeffs`</b>: A list of `Tensor` representing the coefficients of the polynomial.
* <b>`x`</b>: A `Tensor` representing the variable of the polynomial.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `tensor` of the shape as the expression p(x) with usual broadcasting rules
for element-wise addition and multiplication applied.




#### Numpy Compatibility
Equivalent to numpy.polyval.

