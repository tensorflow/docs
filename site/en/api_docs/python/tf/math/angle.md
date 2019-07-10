page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.angle

Returns the element-wise argument of a complex (or real) tensor.

### Aliases:

* `tf.angle`
* `tf.compat.v1.angle`
* `tf.compat.v1.math.angle`
* `tf.compat.v2.math.angle`
* `tf.math.angle`

``` python
tf.math.angle(
    input,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation returns a tensor of type `float` that
is the argument of each element in `input` considered as a complex number.

The elements in `input` are considered to be complex numbers of the form
\\(a + bj\\), where *a* is the real part and *b* is the imaginary part.
If `input` is real then *b* is zero by definition.

The argument returned by this function is of the form \\(atan2(b, a)\\).
If `input` is real, a tensor of all zeros is returned.

#### For example:



```
input = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j], dtype=tf.complex64)
tf.math.angle(input).numpy()
# ==> array([2.0131705, 1.056345 ], dtype=float32)
```

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float`, `double`,
  `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.
