page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.quantization.fake_quant_with_min_max_vars_per_channel_gradient


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

### Aliases:

* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient"><code>tf.compat.v1.fake_quant_with_min_max_vars_per_channel_gradient</code></a>
* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient"><code>tf.compat.v1.quantization.fake_quant_with_min_max_vars_per_channel_gradient</code></a>
* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient"><code>tf.compat.v2.quantization.fake_quant_with_min_max_vars_per_channel_gradient</code></a>
* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient"><code>tf.fake_quant_with_min_max_vars_per_channel_gradient</code></a>


``` python
tf.quantization.fake_quant_with_min_max_vars_per_channel_gradient(
    gradients,
    inputs,
    min,
    max,
    num_bits=8,
    narrow_range=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gradients`</b>: A `Tensor` of type `float32`.
  Backpropagated gradients above the FakeQuantWithMinMaxVars operation,
  shape one of: `[d]`, `[b, d]`,  `[b, h, w, d]`.
* <b>`inputs`</b>: A `Tensor` of type `float32`.
  Values passed as inputs to the FakeQuantWithMinMaxVars operation, shape
    same as `gradients`.
  min, max: Quantization interval, floats of shape `[d]`.
* <b>`min`</b>: A `Tensor` of type `float32`.
* <b>`max`</b>: A `Tensor` of type `float32`.
* <b>`num_bits`</b>: An optional `int`. Defaults to `8`.
  The bitwidth of the quantization; between 2 and 16, inclusive.
* <b>`narrow_range`</b>: An optional `bool`. Defaults to `False`.
  Whether to quantize into 2^num_bits - 1 distinct values.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (backprops_wrt_input, backprop_wrt_min, backprop_wrt_max).


* <b>`backprops_wrt_input`</b>: A `Tensor` of type `float32`.
* <b>`backprop_wrt_min`</b>: A `Tensor` of type `float32`.
* <b>`backprop_wrt_max`</b>: A `Tensor` of type `float32`.
