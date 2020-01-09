page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.maximum


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns the max of x and y (i.e. x > y ? x : y) element-wise.

### Aliases:

* `tf.compat.v1.math.maximum`
* `tf.compat.v1.maximum`
* `tf.compat.v2.math.maximum`
* `tf.compat.v2.maximum`
* `tf.maximum`


``` python
tf.math.maximum(
    x,
    y,
    name=None
)
```



### Used in the tutorials:

* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



*NOTE*: <a href="../../tf/math/maximum"><code>math.maximum</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
