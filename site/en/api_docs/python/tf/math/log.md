page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.log


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes natural logarithm of x element-wise.

### Aliases:

* `tf.compat.v1.log`
* `tf.compat.v1.math.log`
* `tf.compat.v2.math.log`


``` python
tf.math.log(
    x,
    name=None
)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)

### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)



I.e., \\(y = \log_e x\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
