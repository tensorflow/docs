page_type: reference
<style> table img { max-width: 100%; } </style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.atan2

``` python
tf.atan2(
    y,
    x,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_math_ops.py`.

Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

This is the angle \( \theta \in [-\pi, \pi] \) such that
\[ x = r \cos(\theta) \]
and
\[ y = r \sin(\theta) \]
where \(r = \sqrt(x^2 + y^2) \).

#### Args:

* <b>`y`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `y`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `y`.