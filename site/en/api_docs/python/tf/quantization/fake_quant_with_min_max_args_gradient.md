page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.quantization.fake_quant_with_min_max_args_gradient


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Compute gradients for a FakeQuantWithMinMaxArgs operation.

### Aliases:

* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient"><code>tf.compat.v1.fake_quant_with_min_max_args_gradient</code></a>
* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient"><code>tf.compat.v1.quantization.fake_quant_with_min_max_args_gradient</code></a>
* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient"><code>tf.compat.v2.quantization.fake_quant_with_min_max_args_gradient</code></a>
* <a href="/api_docs/python/tf/quantization/fake_quant_with_min_max_args_gradient"><code>tf.fake_quant_with_min_max_args_gradient</code></a>


``` python
tf.quantization.fake_quant_with_min_max_args_gradient(
    gradients,
    inputs,
    min=-6,
    max=6,
    num_bits=8,
    narrow_range=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gradients`</b>: A `Tensor` of type `float32`.
  Backpropagated gradients above the FakeQuantWithMinMaxArgs operation.
* <b>`inputs`</b>: A `Tensor` of type `float32`.
  Values passed as inputs to the FakeQuantWithMinMaxArgs operation.
* <b>`min`</b>: An optional `float`. Defaults to `-6`.
* <b>`max`</b>: An optional `float`. Defaults to `6`.
* <b>`num_bits`</b>: An optional `int`. Defaults to `8`.
* <b>`narrow_range`</b>: An optional `bool`. Defaults to `False`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32`.
