page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.conj

### Aliases:

* `tf.conj`
* `tf.math.conj`

``` python
tf.math.conj(
    x,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/math_ops.py).

Returns the complex conjugate of a complex number.

Given a tensor `input` of complex numbers, this operation returns a tensor of
complex numbers that are the complex conjugate of each element in `input`. The
complex numbers in `input` must be of the form \\(a + bj\\), where *a* is the
real part and *b* is the imaginary part.

The complex conjugate returned by this operation is of the form \\(a - bj\\).

For example:

    # tensor 'input' is [-2.25 + 4.75j, 3.25 + 5.75j]
    tf.math.conj(input) ==> [-2.25 - 4.75j, 3.25 - 5.75j]

If `x` is real, it is returned unchanged.

#### Args:

* <b>`x`</b>: `Tensor` to conjugate.  Must have numeric or variant type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` that is the conjugate of `x` (with the same type).


#### Raises:

* <b>`TypeError`</b>: If `x` is not a numeric tensor.