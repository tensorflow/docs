description: Scatters tensor at indices in an input list.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TensorListScatterIntoExistingList" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TensorListScatterIntoExistingList

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Scatters tensor at indices in an input list.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorListScatterIntoExistingList`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListScatterIntoExistingList(
    input_handle, tensor, indices, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each member of the TensorList corresponds to one row of the input tensor,
specified by the given index (see <a href="../../tf/gather.md"><code>tf.gather</code></a>).

input_handle: The list to scatter into.
tensor: The input tensor.
indices: The indices used to index into the list.
output_handle: The TensorList.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_handle`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int32`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

