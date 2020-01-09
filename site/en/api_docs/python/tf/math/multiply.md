page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.multiply


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L328-L331">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns x * y element-wise.

### Aliases:

* `tf.RaggedTensor.__mul__`
* `tf.compat.v1.RaggedTensor.__mul__`
* `tf.compat.v1.math.multiply`
* `tf.compat.v1.multiply`
* `tf.compat.v2.RaggedTensor.__mul__`
* `tf.compat.v2.math.multiply`
* `tf.compat.v2.multiply`
* `tf.multiply`


``` python
tf.math.multiply(
    x,
    y,
    name=None
)
```



### Used in the guide:

* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)

### Used in the tutorials:

* [Automatic differentiation and gradient tape](https://www.tensorflow.org/tutorials/customization/autodiff)
* [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)



*NOTE*: <a href="../../tf/math/multiply"><code>tf.multiply</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
