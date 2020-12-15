description: Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.quantize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.quantize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L5148-L5184">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.quantization.quantize`, `tf.compat.v1.quantize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantization.quantize(
    input, min_range, max_range, T, mode='MIN_COMBINED',
    round_mode='HALF_AWAY_FROM_ZERO', name=None, narrow_range=(False), axis=None,
    ensure_minimum_range=0.01
)
</code></pre>



<!-- Placeholder for "Used in" -->

[min_range, max_range] are scalar floats that specify the range for
the 'input' data. The 'mode' attribute controls exactly which calculations are
used to convert the float values to their quantized equivalents.  The
'round_mode' attribute controls which rounding tie-breaking algorithm is used
when rounding float values to their quantized equivalents.

In 'MIN_COMBINED' mode, each value of the tensor will undergo the following:

```
out[i] = (in[i] - min_range) * range(T) / (max_range - min_range)
if T == qint8: out[i] -= (range(T) + 1) / 2.0
```

here `range(T) = numeric_limits<T>::max() - numeric_limits<T>::min()`

*MIN_COMBINED Mode Example*

Assume the input is type float and has a possible range of [0.0, 6.0] and the
output type is quint8 ([0, 255]). The min_range and max_range values should be
specified as 0.0 and 6.0. Quantizing from float to quint8 will multiply each
value of the input by 255/6 and cast to quint8.

If the output type was qint8 ([-128, 127]), the operation will additionally
subtract each value by 128 prior to casting, so that the range of values aligns
with the range of qint8.

If the mode is 'MIN_FIRST', then this approach is used:

```
num_discrete_values = 1 << (# of bits in T)
range_adjust = num_discrete_values / (num_discrete_values - 1)
range = (range_max - range_min) * range_adjust
range_scale = num_discrete_values / range
quantized = round(input * range_scale) - round(range_min * range_scale) +
  numeric_limits<T>::min()
quantized = max(quantized, numeric_limits<T>::min())
quantized = min(quantized, numeric_limits<T>::max())
```

The biggest difference between this and MIN_COMBINED is that the minimum range
is rounded first, before it's subtracted from the rounded value. With
MIN_COMBINED, a small bias is introduced where repeated iterations of quantizing
and dequantizing will introduce a larger and larger error.

*SCALED mode Example*

`SCALED` mode matches the quantization approach used in
`QuantizeAndDequantize{V2|V3}`.

If the mode is `SCALED`, the quantization is performed by multiplying each
input value by a scaling_factor.
The scaling_factor is determined from `min_range` and `max_range` to be as large
as possible such that the range from `min_range` to `max_range` is representable
within values of type T.

```c++

  const int min_T = std::numeric_limits<T>::min();
  const int max_T = std::numeric_limits<T>::max();
  const float max_float = std::numeric_limits<float>::max();

  const float scale_factor_from_min_side =
      (min_T * min_range > 0) ? min_T / min_range : max_float;
  const float scale_factor_from_max_side =
      (max_T * max_range > 0) ? max_T / max_range : max_float;

  const float scale_factor = std::min(scale_factor_from_min_side,
                                      scale_factor_from_max_side);
```

We next use the scale_factor to adjust min_range and max_range as follows:

```c++
      min_range = min_T / scale_factor;
      max_range = max_T / scale_factor;
```


e.g. if T = qint8, and initially min_range = -10, and max_range = 9, we would
compare -128/-10.0 = 12.8 to 127/9.0 = 14.11, and set scaling_factor = 12.8
In this case, min_range would remain -10, but max_range would be adjusted to
127 / 12.8 = 9.921875

So we will quantize input values in the range (-10, 9.921875) to (-128, 127).

The input tensor can now be quantized by clipping values to the range
`min_range` to `max_range`, then multiplying by scale_factor as follows:

```c++
result = round(min(max_range, max(min_range, input)) * scale_factor)
```

The adjusted `min_range` and `max_range` are returned as outputs 2 and 3 of
this operation. These outputs should be used as the range for any further
calculations.


*narrow_range (bool) attribute*

If true, we do not use the minimum quantized value.
i.e. for int8 the quantized output, it would be restricted to the range
-127..127 instead of the full -128..127 range.
This is provided for compatibility with certain inference backends.
(Only applies to SCALED mode)


*axis (int) attribute*

An optional `axis` attribute can specify a dimension index of the input tensor,
such that quantization ranges will be calculated and applied separately for each
slice of the tensor along that dimension. This is useful for per-channel
quantization.

If axis is specified, min_range and max_range

if `axis`=None, per-tensor quantization is performed as normal.


*ensure_minimum_range (float) attribute*

Ensures the minimum quantization range is at least this value.
The legacy default value for this is 0.01, but it is strongly suggested to
set it to 0 for new uses.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`min_range`
</td>
<td>
A `Tensor` of type `float32`.
The minimum value of the quantization range. This value may be adjusted by the
op depending on other parameters. The adjusted value is written to `output_min`.
If the `axis` attribute is specified, this must be a 1-D tensor whose size
matches the `axis` dimension of the input and output tensors.
</td>
</tr><tr>
<td>
`max_range`
</td>
<td>
A `Tensor` of type `float32`.
The maximum value of the quantization range. This value may be adjusted by the
op depending on other parameters. The adjusted value is written to `output_max`.
If the `axis` attribute is specified, this must be a 1-D tensor whose size
matches the `axis` dimension of the input and output tensors.
</td>
</tr><tr>
<td>
`T`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`.
</td>
</tr><tr>
<td>
`mode`
</td>
<td>
An optional `string` from: `"MIN_COMBINED", "MIN_FIRST", "SCALED"`. Defaults to `"MIN_COMBINED"`.
</td>
</tr><tr>
<td>
`round_mode`
</td>
<td>
An optional `string` from: `"HALF_AWAY_FROM_ZERO", "HALF_TO_EVEN"`. Defaults to `"HALF_AWAY_FROM_ZERO"`.
</td>
</tr><tr>
<td>
`narrow_range`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An optional `int`. Defaults to `-1`.
</td>
</tr><tr>
<td>
`ensure_minimum_range`
</td>
<td>
An optional `float`. Defaults to `0.01`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple of `Tensor` objects (output, output_min, output_max).
</td>
</tr>
<tr>
<td>
`output`
</td>
<td>
A `Tensor` of type `T`.
</td>
</tr><tr>
<td>
`output_min`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`output_max`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

