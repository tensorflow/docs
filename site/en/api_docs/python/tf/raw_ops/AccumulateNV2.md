description: Returns the element-wise sum of a list of tensors.

robots: noindex

# tf.raw_ops.AccumulateNV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the element-wise sum of a list of tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AccumulateNV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AccumulateNV2(
    inputs, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`tf.accumulate_n_v2` performs the same operation as <a href="../../tf/math/add_n.md"><code>tf.add_n</code></a>, but does not
wait for all of its inputs to be ready before beginning to sum. This can
save memory if inputs are ready at different times, since minimum temporary
storage is proportional to the output size rather than the inputs size.

Unlike the original `accumulate_n`, `accumulate_n_v2` is differentiable.

Returns a `Tensor` of same shape and type as the elements of `inputs`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
A list of `Tensor` objects, each with same shape and type.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`.
Shape of elements of `inputs`.
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
A `Tensor`. Has the same type as `inputs`.
</td>
</tr>

</table>

