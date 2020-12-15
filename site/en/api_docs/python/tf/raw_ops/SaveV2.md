description: Saves tensors in V2 checkpoint format.

robots: noindex

# tf.raw_ops.SaveV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Saves tensors in V2 checkpoint format.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SaveV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SaveV2(
    prefix, tensor_names, shape_and_slices, tensors, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, saves the named tensors in full.  If the caller wishes to save
specific slices of full tensors, "shape_and_slices" should be non-empty strings
and correspondingly well-formed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`prefix`
</td>
<td>
A `Tensor` of type `string`.
Must have a single element. The prefix of the V2 checkpoint to which we
write the tensors.
</td>
</tr><tr>
<td>
`tensor_names`
</td>
<td>
A `Tensor` of type `string`.
shape {N}. The names of the tensors to be saved.
</td>
</tr><tr>
<td>
`shape_and_slices`
</td>
<td>
A `Tensor` of type `string`.
shape {N}.  The slice specs of the tensors to be saved.
Empty strings indicate that they are non-partitioned tensors.
</td>
</tr><tr>
<td>
`tensors`
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

