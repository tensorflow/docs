page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.pow

``` python
tf.pow(
    x,
    y,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Basic Math Functions](../../../api_guides/python/math_ops#Basic_Math_Functions)

Computes the power of one value to another.

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

#### Args:

* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
   `complex64`, or `complex128`.
* <b>`y`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
   `complex64`, or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.