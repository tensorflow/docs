description: Restores a tensor from checkpoint files.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RestoreSlice" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RestoreSlice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Restores a tensor from checkpoint files.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RestoreSlice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RestoreSlice(
    file_pattern, tensor_name, shape_and_slice, dt, preferred_shard=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is like `Restore` except that restored tensor can be listed as filling
only a slice of a larger tensor.  `shape_and_slice` specifies the shape of the
larger tensor and the slice that the restored tensor covers.

The `shape_and_slice` input has the same format as the
elements of the `shapes_and_slices` input of the `SaveSlices` op.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`file_pattern`
</td>
<td>
A `Tensor` of type `string`.
Must have a single element. The pattern of the files from
which we read the tensor.
</td>
</tr><tr>
<td>
`tensor_name`
</td>
<td>
A `Tensor` of type `string`.
Must have a single element. The name of the tensor to be
restored.
</td>
</tr><tr>
<td>
`shape_and_slice`
</td>
<td>
A `Tensor` of type `string`.
Scalar. The shapes and slice specifications to use when
restoring a tensors.
</td>
</tr><tr>
<td>
`dt`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. The type of the tensor to be restored.
</td>
</tr><tr>
<td>
`preferred_shard`
</td>
<td>
An optional `int`. Defaults to `-1`.
Index of file to open first if multiple files match
`file_pattern`. See the documentation for `Restore`.
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
A `Tensor` of type `dt`.
</td>
</tr>

</table>

