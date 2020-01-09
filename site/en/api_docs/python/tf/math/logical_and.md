page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.logical_and


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns the truth value of x AND y element-wise.

### Aliases:

* `tf.RaggedTensor.__and__`
* `tf.compat.v1.RaggedTensor.__and__`
* `tf.compat.v1.logical_and`
* `tf.compat.v1.math.logical_and`
* `tf.compat.v2.RaggedTensor.__and__`
* `tf.compat.v2.logical_and`
* `tf.compat.v2.math.logical_and`
* `tf.logical_and`


``` python
tf.math.logical_and(
    x,
    y,
    name=None
)
```



### Used in the tutorials:

* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



*NOTE*: <a href="../../tf/math/logical_and"><code>math.logical_and</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.
