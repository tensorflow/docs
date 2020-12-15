description: Extracts the average sparse gradient in a SparseConditionalAccumulator.

robots: noindex

# tf.raw_ops.SparseAccumulatorTakeGradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Extracts the average sparse gradient in a SparseConditionalAccumulator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseAccumulatorTakeGradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseAccumulatorTakeGradient(
    handle, num_required, dtype, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The op will blocks until sufficient (i.e., more than num_required)
gradients have been accumulated. If the accumulator has already
aggregated more than num_required gradients, it will return its
average of the accumulated gradients.  Also automatically increments
the recorded global_step in the accumulator by 1, and resets the
aggregate to 0.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type mutable `string`.
The handle to a SparseConditionalAccumulator.
</td>
</tr><tr>
<td>
`num_required`
</td>
<td>
A `Tensor` of type `int32`.
Number of gradients required before we return an aggregate.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64, tf.int32, tf.uint8, tf.int16, tf.int8, tf.complex64, tf.int64, tf.qint8, tf.quint8, tf.qint32, tf.bfloat16, tf.uint16, tf.complex128, tf.half, tf.uint32, tf.uint64`.
The data type of accumulated gradients. Needs to correspond to the type
of the accumulator.
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
A tuple of `Tensor` objects (indices, values, shape).
</td>
</tr>
<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor` of type `dtype`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

