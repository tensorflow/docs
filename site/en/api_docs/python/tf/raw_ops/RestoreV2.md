description: Restores tensors from a V2 checkpoint.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RestoreV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RestoreV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Restores tensors from a V2 checkpoint.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RestoreV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RestoreV2(
    prefix, tensor_names, shape_and_slices, dtypes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For backward compatibility with the V1 format, this Op currently allows
restoring from a V1 checkpoint as well:
  - This Op first attempts to find the V2 index file pointed to by "prefix", and
    if found proceed to read it as a V2 checkpoint;
  - Otherwise the V1 read path is invoked.
Relying on this behavior is not recommended, as the ability to fall back to read
V1 might be deprecated and eventually removed.

By default, restores the named tensors in full.  If the caller wishes to restore
specific slices of stored tensors, "shape_and_slices" should be non-empty
strings and correspondingly well-formed.

Callers must ensure all the named tensors are indeed stored in the checkpoint.

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
Must have a single element.  The prefix of a V2 checkpoint.
</td>
</tr><tr>
<td>
`tensor_names`
</td>
<td>
A `Tensor` of type `string`.
shape {N}.  The names of the tensors to be restored.
</td>
</tr><tr>
<td>
`shape_and_slices`
</td>
<td>
A `Tensor` of type `string`.
shape {N}.  The slice specs of the tensors to be restored.
Empty strings indicate that they are non-partitioned tensors.
</td>
</tr><tr>
<td>
`dtypes`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
shape {N}.  The list of expected dtype for the tensors.  Must match
those stored in the checkpoint.
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
A list of `Tensor` objects of type `dtypes`.
</td>
</tr>

</table>

