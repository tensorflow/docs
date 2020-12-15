description: Public API for tf.quantization namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.quantization" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.quantization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.quantization namespace.



## Functions

[`dequantize(...)`](../../../tf/quantization/dequantize.md): Dequantize the 'input' tensor into a float or bfloat16 Tensor.

[`fake_quant_with_min_max_args(...)`](../../../tf/quantization/fake_quant_with_min_max_args.md): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`fake_quant_with_min_max_args_gradient(...)`](../../../tf/quantization/fake_quant_with_min_max_args_gradient.md): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`fake_quant_with_min_max_vars(...)`](../../../tf/quantization/fake_quant_with_min_max_vars.md): Fake-quantize the 'inputs' tensor of type float via global float scalars

[`fake_quant_with_min_max_vars_gradient(...)`](../../../tf/quantization/fake_quant_with_min_max_vars_gradient.md): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`fake_quant_with_min_max_vars_per_channel(...)`](../../../tf/quantization/fake_quant_with_min_max_vars_per_channel.md): Fake-quantize the 'inputs' tensor of type float via per-channel floats

[`fake_quant_with_min_max_vars_per_channel_gradient(...)`](../../../tf/quantization/fake_quant_with_min_max_vars_per_channel_gradient.md): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`quantize(...)`](../../../tf/quantization/quantize.md): Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`quantize_and_dequantize(...)`](../../../tf/quantization/quantize_and_dequantize.md): Quantizes then dequantizes a tensor. (deprecated)

[`quantize_and_dequantize_v2(...)`](../../../tf/quantization/quantize_and_dequantize_v2.md): Quantizes then dequantizes a tensor.

[`quantized_concat(...)`](../../../tf/quantization/quantized_concat.md): Concatenates quantized tensors along one dimension.

