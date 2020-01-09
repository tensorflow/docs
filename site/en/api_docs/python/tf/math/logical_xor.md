page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.logical_xor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L1234-L1265">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Logical XOR function.

### Aliases:

* `tf.RaggedTensor.__xor__`
* `tf.compat.v1.RaggedTensor.__xor__`
* `tf.compat.v1.logical_xor`
* `tf.compat.v1.math.logical_xor`
* `tf.compat.v2.RaggedTensor.__xor__`
* `tf.compat.v2.math.logical_xor`


``` python
tf.math.logical_xor(
    x,
    y,
    name='LogicalXor'
)
```



<!-- Placeholder for "Used in" -->

x ^ y = (x | y) & ~(x & y)

Inputs are tensor and if the tensors contains more than one element, an
element-wise logical XOR is computed.

#### Usage:



```python
x = tf.constant([False, False, True, True], dtype = tf.bool)
y = tf.constant([False, True, False, True], dtype = tf.bool)
z = tf.logical_xor(x, y, name="LogicalXor")
#  here z = [False  True  True False]
```

#### Args:


* <b>`x`</b>: A `Tensor` type bool.
* <b>`y`</b>: A `Tensor` of type bool.


#### Returns:

A `Tensor` of type bool with the same size as that of x or y.
