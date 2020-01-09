page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.bias_add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/bias_add">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L2685-L2718">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds `bias` to `value`.

### Aliases:

* <a href="/api_docs/python/tf/nn/bias_add"><code>tf.compat.v1.nn.bias_add</code></a>
* <a href="/api_docs/python/tf/nn/bias_add"><code>tf.compat.v2.nn.bias_add</code></a>


``` python
tf.nn.bias_add(
    value,
    bias,
    data_format=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This is (mostly) a special case of <a href="../../tf/math/add"><code>tf.add</code></a> where `bias` is restricted to 1-D.
Broadcasting is supported, so `value` may have any number of dimensions.
Unlike <a href="../../tf/math/add"><code>tf.add</code></a>, the type of `bias` is allowed to differ from `value` in the
case where both types are quantized.

#### Args:


* <b>`value`</b>: A `Tensor` with type `float`, `double`, `int64`, `int32`, `uint8`,
  `int16`, `int8`, `complex64`, or `complex128`.
* <b>`bias`</b>: A 1-D `Tensor` with size matching the channel dimension of `value`.
  Must be the same type as `value` unless `value` is a quantized type,
  in which case a different quantized type may be used.
* <b>`data_format`</b>: A string. 'N...C' and 'NC...' are supported.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with the same type as `value`.
