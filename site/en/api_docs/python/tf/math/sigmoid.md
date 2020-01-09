page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sigmoid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L3112-L3132">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes sigmoid of `x` element-wise.

### Aliases:

* `tf.compat.v1.math.sigmoid`
* `tf.compat.v1.nn.sigmoid`
* `tf.compat.v1.sigmoid`
* `tf.compat.v2.math.sigmoid`
* `tf.compat.v2.nn.sigmoid`
* `tf.compat.v2.sigmoid`
* `tf.nn.sigmoid`
* `tf.sigmoid`


``` python
tf.math.sigmoid(
    x,
    name=None
)
```



### Used in the tutorials:

* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)



Specifically, `y = 1 / (1 + exp(-x))`.

#### Args:


* <b>`x`</b>: A Tensor with type `float16`, `float32`, `float64`, `complex64`, or
  `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor with the same type as `x`.




#### Scipy Compatibility
Equivalent to scipy.special.expit
