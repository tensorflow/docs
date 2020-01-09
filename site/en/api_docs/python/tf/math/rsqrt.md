page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.rsqrt


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes reciprocal of square root of x element-wise.

### Aliases:

* `tf.compat.v1.math.rsqrt`
* `tf.compat.v1.rsqrt`
* `tf.compat.v2.math.rsqrt`


``` python
tf.math.rsqrt(
    x,
    name=None
)
```



### Used in the tutorials:

* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



I.e., \\(y = 1 / \sqrt{x}\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
