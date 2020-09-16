description: Saves the input tensors to disk.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Save" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Save

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Saves the input tensors to disk.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Save`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Save(
    filename, tensor_names, data, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The size of `tensor_names` must match the number of tensors in `data`. `data[i]`
is written to `filename` with name `tensor_names[i]`.

See also `SaveSlices`.

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
Must have a single element. The name of the file to which we write
the tensor.
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

