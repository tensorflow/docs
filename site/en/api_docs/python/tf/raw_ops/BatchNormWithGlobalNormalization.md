description: Batch normalization.

robots: noindex

# tf.raw_ops.BatchNormWithGlobalNormalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Batch normalization.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BatchNormWithGlobalNormalization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BatchNormWithGlobalNormalization(
    t, m, v, beta, gamma, variance_epsilon, scale_after_normalization, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op is deprecated. Prefer <a href="../../tf/nn/batch_normalization.md"><code>tf.nn.batch_normalization</code></a>.

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
A 4D input Tensor.
</td>
</tr><tr>
<td>
`m`
</td>
<td>
A `Tensor`. Must have the same type as `t`.
A 1D mean Tensor with size matching the last dimension of t.
This is the first output from tf.nn.moments,
or a saved moving average thereof.
</td>
</tr><tr>
<td>
`v`
</td>
<td>
A `Tensor`. Must have the same type as `t`.
A 1D variance Tensor with size matching the last dimension of t.
This is the second output from tf.nn.moments,
or a saved moving average thereof.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
A `Tensor`. Must have the same type as `t`.
A 1D beta Tensor with size matching the last dimension of t.
An offset to be added to the normalized tensor.
</td>
</tr><tr>
<td>
`gamma`
</td>
<td>
A `Tensor`. Must have the same type as `t`.
A 1D gamma Tensor with size matching the last dimension of t.
If "scale_after_normalization" is true, this tensor will be multiplied
with the normalized tensor.
</td>
</tr><tr>
<td>
`variance_epsilon`
</td>
<td>
A `float`. A small float number to avoid dividing by 0.
</td>
</tr><tr>
<td>
`scale_after_normalization`
</td>
<td>
A `bool`.
A bool indicating whether the resulted tensor
needs to be multiplied with gamma.
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

