page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.quantization.quantize_and_dequantize

``` python
tf.quantization.quantize_and_dequantize(
    input,
    input_min,
    input_max,
    signed_input=True,
    num_bits=8,
    range_given=False,
    round_mode='HALF_TO_EVEN',
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

Quantizes then dequantizes a tensor.

This op simulates the precision loss from the quantized forward pass by:

1. Quantizing the tensor to fixed point numbers, which should match the target
   quantization method when it is used in inference.
2. Dequantizing it back to floating point numbers for the following ops, most
   likely matmul.

There are different ways to quantize. This version uses only scaling, so 0.0
maps to 0.

From the specified 'num_bits' in the quantized output type, it determines
minimum and maximum representable quantized values.

e.g.

*   [-128, 127] for signed, num_bits = 8, or
*   [0, 255] for unsigned, num_bits = 8.

If range_given == False, the initial input_min, input_max will be determined
automatically as the minimum and maximum values in the input tensor, otherwise
the specified values of input_min, input_max are used.

Note: If the input_min, input_max are specified, they do not need to equal the
actual minimum and maximum values in the tensor. e.g. in some cases it may be
beneficial to specify these values such that the low probability extremes of the
input distribution are clipped.

This op determines the maximum scale_factor that would map the initial
[input_min, input_max] range to a range that lies within the representable
quantized range.

It determines the scale from one of input_min and input_max, then updates the
other one to maximize the respresentable range.

e.g.

*   if the output is signed, num_bits = 8, [input_min, input_max] = [-10.0,
    5.0]: it would use a scale_factor of -128 / -10.0 = 12.8 In this case, it
    would update input_max to be 127 / 12.8 = 9.921875
*   if the output is signed, num_bits = 8, [input_min, input_max] = [-10.0,
    10.0]: it would use a scale_factor of 127 / 10.0 = 12.7 In this case, it
    would update input_min to be 128.0 / 12.7 = -10.07874
*   if the output is unsigned, input_min is forced to be 0, and only the
    specified input_max is used.

After determining the scale_factor and updating the input range, it applies the
following to each value in the 'input' tensor.

output = round(clamp(value, input_min, input_max) * scale_factor) / scale_factor.

The above round function rounds the value based on the given round_mode.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
    Tensor to quantize and then dequantize.
* <b>`input_min`</b>: A `Tensor`. Must have the same type as `input`.
    If `range_given == True`, this specifies the minimum input value that needs to
    be represented, otherwise it is determined from the min value of the `input`
    tensor.
* <b>`input_max`</b>: A `Tensor`. Must have the same type as `input`.
    If `range_given == True`, this specifies the maximum input value that needs to
    be represented, otherwise it is determined from the max value of the `input`
    tensor.
* <b>`signed_input`</b>: An optional `bool`. Defaults to `True`.
    Whether the quantization is signed or unsigned. (actually this parameter should
    have been called <b>`signed_output`</b>)
* <b>`num_bits`</b>: An optional `int`. Defaults to `8`.
    The bitwidth of the quantization.
* <b>`range_given`</b>: An optional `bool`. Defaults to `False`.
    Whether the range is given or should be determined from the `input` tensor.
* <b>`round_mode`</b>: An optional `string` from: `"HALF_TO_EVEN", "HALF_UP"`. Defaults to `"HALF_TO_EVEN"`.
    The 'round_mode' attribute controls which rounding tie-breaking algorithm is
    used when rounding float values to their quantized equivalents. The following
    rounding modes are currently supported:

    *   HALF_TO_EVEN: this is the default round_mode.
    *   HALF_UP: round towards positive. In this mode 7.5 rounds up to 8 and -7.5
        rounds up to -7.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.