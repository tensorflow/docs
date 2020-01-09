page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.square


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes square of x element-wise.

### Aliases:

* `tf.compat.v1.math.square`
* `tf.compat.v1.square`
* `tf.compat.v2.math.square`
* `tf.compat.v2.square`
* `tf.square`


``` python
tf.math.square(
    x,
    name=None
)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)
* [Custom training: basics](https://www.tensorflow.org/tutorials/customization/custom_training)
* [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)



I.e., \\(y = x * x = x^2\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.square(x.values, ...), x.dense_shape)`
