

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.quantization



Defined in [`tensorflow/quantization/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/quantization/__init__.py).

Public API for tf.quantization namespace.

## Functions

[`dequantize(...)`](../tf/dequantize): Dequantize the 'input' tensor into a float Tensor.

[`fake_quant_with_min_max_args(...)`](../tf/fake_quant_with_min_max_args): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`fake_quant_with_min_max_args_gradient(...)`](../tf/fake_quant_with_min_max_args_gradient): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](../tf/fake_quant_with_min_max_vars): Fake-quantize the 'inputs' tensor of type float via global float scalars `min`

[`fake_quant_with_min_max_vars_gradient(...)`](../tf/fake_quant_with_min_max_vars_gradient): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](../tf/fake_quant_with_min_max_vars_per_channel): Fake-quantize the 'inputs' tensor of type float and one of the shapes: `[d]`,

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](../tf/fake_quant_with_min_max_vars_per_channel_gradient): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`quantized_concat(...)`](../tf/quantized_concat): Concatenates quantized tensors along one dimension.

