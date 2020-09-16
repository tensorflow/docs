description: Restores a tensor from checkpoint files.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Restore" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Restore

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
<p>`tf.compat.v1.raw_ops.Restore`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Restore(
    file_pattern, tensor_name, dt, preferred_shard=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reads a tensor stored in one or several files. If there are several files (for
instance because a tensor was saved as slices), `file_pattern` may contain
wildcard symbols (`*` and `?`) in the filename portion only, not in the
directory portion.

If a `file_pattern` matches several files, `preferred_shard` can be used to hint
in which file the requested tensor is likely to be found. This op will first
open the file at index `preferred_shard` in the list of matching files and try
to restore tensors from that file.  Only if some tensors or tensor slices are
not found in that first file, then the Op opens all the files. Setting
`preferred_shard` to match the value passed as the `shard` input
of a matching `Save` Op may speed up Restore.  This attribute only affects
performance, not correctness.  The default value -1 means files are processed in
order.

See also `RestoreSlice`.

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
`file_pattern`.
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

