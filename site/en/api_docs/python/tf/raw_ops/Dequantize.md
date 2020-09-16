description: Dequantize the 'input' tensor into a float or bfloat16 Tensor.

robots: noindex

# tf.raw_ops.Dequantize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Dequantize the 'input' tensor into a float or bfloat16 Tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Dequantize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Dequantize(
    input, min_range, max_range, mode='MIN_COMBINED', narrow_range=(False), axis=-1,
    dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

[min_range, max_range] are scalar floats that specify the range for
the output. The 'mode' attribute controls exactly which calculations are
used to convert the float values to their quantized equivalents.

In 'MIN_COMBINED' mode, each value of the tensor will undergo the following:

```
if T == qint8: in[i] += (range(T) + 1)/ 2.0
out[i] = min_range + (in[i]* (max_range - min_range) / range(T))
```
here `range(T) = numeric_limits<T>::max() - numeric_limits<T>::min()`

*MIN_COMBINED Mode Example*

If the input comes from a QuantizedRelu6, the output type is
quint8 (range of 0-255) but the possible range of QuantizedRelu6 is
0-6.  The min_range and max_range values are therefore 0.0 and 6.0.
Dequantize on quint8 will take each value, cast to float, and multiply
by 6 / 255.
Note that if quantizedtype is qint8, the operation will additionally add
each value by 128 prior to casting.

If the mode is 'MIN_FIRST', then this approach is used:

```c++
num_discrete_values = 1 << (# of bits in T)
range_adjust = num_discrete_values / (num_discrete_values - 1)
range = (range_max - range_min) * range_adjust
range_scale = range / num_discrete_values
const double offset_input = static_cast<double>(input) - lowest_quantized;
result = range_min + ((input - numeric_limits<T>::min()) * range_scale)
```

If the mode is `SCALED`, dequantization is performed by multiplying each
input value by a scaling_factor. (Thus an input of 0 always maps to 0.0).

The scaling_factor is determined from `min_range`, `max_range`, and
`narrow_range` in a way that is compatible with `QuantizeAndDequantize{V2|V3}`
and `QuantizeV2`, using the following algorithm:

```c++

  const int min_expected_T = std::numeric_limits<T>::min() +
    (narrow_range ? 1 : 0);
  const int max_expected_T = std::numeric_limits<T>::max();
  const float max_expected_T = std::numeric_limits<float>::max();

  const float scale_factor =
    (std::numeric_limits<T>::min() == 0) ? (max_range / max_expected_T)
                                         : std::max(min_range / min_expected_T,
                                                    max_range / max_expected_T);
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
</td>
</tr><tr>
<td>
`min_range`
</td>
<td>
A `Tensor` of type `float32`.
The minimum scalar value possibly produced for the input.
</td>
</tr><tr>
<td>
`max_range`
</td>
<td>
A `Tensor` of type `float32`.
The maximum scalar value possibly produced for the input.
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
`dtype`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.bfloat16, tf.float32`. Defaults to <a href="../../tf.md#float32"><code>tf.float32</code></a>.
Type of the output tensor. Currently Dequantize supports float and bfloat16.
If 'dtype' is 'bfloat16', it only supports 'MIN_COMBINED' mode.
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
A `Tensor` of type `dtype`.
</td>
</tr>

</table>

