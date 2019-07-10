page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.complex

Converts two real numbers to a complex number.

### Aliases:

* `tf.compat.v1.complex`
* `tf.compat.v1.dtypes.complex`
* `tf.compat.v2.complex`
* `tf.compat.v2.dtypes.complex`
* `tf.complex`
* `tf.dtypes.complex`

``` python
tf.dtypes.complex(
    real,
    imag,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Given a tensor `real` representing the real part of a complex number, and a
tensor `imag` representing the imaginary part of a complex number, this
operation returns complex numbers elementwise of the form \\(a + bj\\), where
*a* represents the `real` part and *b* represents the `imag` part.

The input tensors `real` and `imag` must have the same shape.

#### For example:



```python
real = tf.constant([2.25, 3.25])
imag = tf.constant([4.75, 5.75])
tf.complex(real, imag)  # [[2.25 + 4.75j], [3.25 + 5.75j]]
```

#### Args:


* <b>`real`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`imag`</b>: A `Tensor`. Must have the same type as `real`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `complex64` or `complex128`.
