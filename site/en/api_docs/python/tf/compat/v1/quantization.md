page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.quantization

Public API for tf.quantization namespace.

<!-- Placeholder for "Used in" -->


## Functions

[`dequantize(...)`](../../../tf/quantization/dequantize): Dequantize the 'input' tensor into a float Tensor.

[`fake_quant_with_min_max_args(...)`](../../../tf/quantization/fake_quant_with_min_max_args): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`fake_quant_with_min_max_args_gradient(...)`](../../../tf/quantization/fake_quant_with_min_max_args_gradient): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](../../../tf/quantization/fake_quant_with_min_max_vars): Fake-quantize the 'inputs' tensor of type float via global float scalars `min`

[`fake_quant_with_min_max_vars_gradient(...)`](../../../tf/quantization/fake_quant_with_min_max_vars_gradient): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](../../../tf/quantization/fake_quant_with_min_max_vars_per_channel): Fake-quantize the 'inputs' tensor of type float and one of the shapes: `[d]`,

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](../../../tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`quantize(...)`](../../../tf/quantization/quantize): Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`quantize_and_dequantize(...)`](../../../tf/quantization/quantize_and_dequantize): Quantizes then dequantizes a tensor.

[`quantized_concat(...)`](../../../tf/quantization/quantized_concat): Concatenates quantized tensors along one dimension.

