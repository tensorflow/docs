page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.round


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L618-L643">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Rounds the values of a tensor to the nearest integer, element-wise.

### Aliases:

* `tf.compat.v1.math.round`
* `tf.compat.v1.round`
* `tf.compat.v2.math.round`
* `tf.compat.v2.round`
* `tf.round`


``` python
tf.math.round(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Rounds half to even.  Also known as bankers rounding. If you want to round
according to the current system rounding mode use tf::cint.
For example:

```python
x = tf.constant([0.9, 2.5, 2.3, 1.5, -4.5])
tf.round(x)  # [ 1.0, 2.0, 2.0, 2.0, -4.0 ]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, or `int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of same shape and type as `x`.
