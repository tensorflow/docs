page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.angle

### Aliases:

* `tf.angle`
* `tf.math.angle`

``` python
tf.math.angle(
    input,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/math_ops.py).

Returns the element-wise argument of a complex (or real) tensor.

Given a tensor `input`, this operation returns a tensor of type `float` that
is the argument of each element in `input` considered as a complex number.

The elements in `input` are considered to be complex numbers of the form
\\(a + bj\\), where *a* is the real part and *b* is the imaginary part.
If `input` is real then *b* is zero by definition.

The argument returned by this function is of the form \\(atan2(b, a)\\).
If `input` is real, a tensor of all zeros is returned.

For example:

```
# tensor 'input' is [-2.25 + 4.75j, 3.25 + 5.75j]
tf.angle(input) ==> [2.0132, 1.056]
```

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float`, `double`,
    `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.