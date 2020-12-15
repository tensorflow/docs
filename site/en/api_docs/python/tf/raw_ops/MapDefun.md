description: Maps a function on the list of tensors unpacked from arguments on dimension 0.

robots: noindex

# tf.raw_ops.MapDefun

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Maps a function on the list of tensors unpacked from arguments on dimension 0.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MapDefun`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MapDefun(
    arguments, captured_inputs, output_types, output_shapes, f,
    max_intra_op_parallelism=1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
The function given by `f` is assumed to be stateless, and is executed
concurrently on all the slices; up to batch_size (i.e. the size of the 0th
dimension of each argument) functions will be scheduled at once.

The `max_intra_op_parallelism` attr, which defaults to 1, can be used to
limit the intra op parallelism. To limit inter-op parallelism, a user can
set a private threadpool on the dataset using <a href="../../tf/data/Options.md"><code>tf.data.Options</code></a>'s
`ThreadingOptions`.

Note that this op is not exposed to users directly, but is invoked in tf.data
rewrites.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors whose types are `Targuments`, corresponding to the inputs
the function should be mapped over.
</td>
</tr><tr>
<td>
`captured_inputs`
</td>
<td>
A list of `Tensor` objects.
A list of tensors whose types are `Tcaptured`, corresponding to the captured
inputs of the defun.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
A list of types.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
A list of shapes.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`max_intra_op_parallelism`
</td>
<td>
An optional `int`. Defaults to `1`.
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
A list of `Tensor` objects of type `output_types`.
</td>
</tr>

</table>

