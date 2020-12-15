description: Clips tensor values to a specified min and max.

robots: noindex

# tf.raw_ops.ClipByValue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Clips tensor values to a specified min and max.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ClipByValue`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ClipByValue(
    t, clip_value_min, clip_value_max, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a tensor `t`, this operation returns a tensor of the same type and
shape as `t` with its values clipped to `clip_value_min` and `clip_value_max`.
Any values less than `clip_value_min` are set to `clip_value_min`. Any values
greater than `clip_value_max` are set to `clip_value_max`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`t`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
A `Tensor`.
</td>
</tr><tr>
<td>
`clip_value_min`
</td>
<td>
A `Tensor`. Must have the same type as `t`.
A 0-D (scalar) `Tensor`, or a `Tensor` with the same shape
as `t`. The minimum value to clip by.
</td>
</tr><tr>
<td>
`clip_value_max`
</td>
<td>
A `Tensor`. Must have the same type as `t`.
A 0-D (scalar) `Tensor`, or a `Tensor` with the same shape
as `t`. The maximum value to clip by.
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
A `Tensor`. Has the same type as `t`.
</td>
</tr>

</table>

