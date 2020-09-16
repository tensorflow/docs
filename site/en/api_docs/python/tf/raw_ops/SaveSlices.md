description: Saves input tensors slices to disk.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SaveSlices" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SaveSlices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Saves input tensors slices to disk.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SaveSlices`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SaveSlices(
    filename, tensor_names, shapes_and_slices, data, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is like `Save` except that tensors can be listed in the saved file as being
a slice of a larger tensor.  `shapes_and_slices` specifies the shape of the
larger tensor and the slice that this tensor covers. `shapes_and_slices` must
have as many elements as `tensor_names`.

Elements of the `shapes_and_slices` input must either be:

*  The empty string, in which case the corresponding tensor is
   saved normally.
*  A string of the form `dim0 dim1 ... dimN-1 slice-spec` where the
   `dimI` are the dimensions of the larger tensor and `slice-spec`
   specifies what part is covered by the tensor to save.

`slice-spec` itself is a `:`-separated list: `slice0:slice1:...:sliceN-1`
where each `sliceI` is either:

*  The string `-` meaning that the slice covers all indices of this dimension
*  `start,length` where `start` and `length` are integers.  In that
   case the slice covers `length` indices starting at `start`.

See also `Save`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`filename`
</td>
<td>
A `Tensor` of type `string`.
Must have a single element. The name of the file to which we write the
tensor.
</td>
</tr><tr>
<td>
`tensor_names`
</td>
<td>
A `Tensor` of type `string`.
Shape `[N]`. The names of the tensors to be saved.
</td>
</tr><tr>
<td>
`shapes_and_slices`
</td>
<td>
A `Tensor` of type `string`.
Shape `[N]`.  The shapes and slice specifications to use when
saving the tensors.
</td>
</tr><tr>
<td>
`data`
</td>
<td>
A list of `Tensor` objects. `N` tensors to save.
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
The created Operation.
</td>
</tr>

</table>

