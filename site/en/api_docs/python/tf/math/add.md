page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.add


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns x + y element-wise.

### Aliases:

* `tf.RaggedTensor.__add__`
* `tf.add`
* `tf.compat.v1.RaggedTensor.__add__`
* `tf.compat.v1.add`
* `tf.compat.v1.math.add`
* `tf.compat.v2.RaggedTensor.__add__`
* `tf.compat.v2.add`
* `tf.compat.v2.math.add`


``` python
tf.math.add(
    x,
    y,
    name=None
)
```



### Used in the guide:

* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)

### Used in the tutorials:

* [Customization basics: tensors and operations](https://www.tensorflow.org/tutorials/customization/basics)



*NOTE*: <a href="../../tf/math/add"><code>math.add</code></a> supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `complex128`, `string`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
