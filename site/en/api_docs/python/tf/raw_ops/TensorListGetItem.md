description: Returns the item in the list with the given index.

robots: noindex

# tf.raw_ops.TensorListGetItem

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the item in the list with the given index.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorListGetItem`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListGetItem(
    input_handle, index, element_shape, element_dtype, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

input_handle: the list
index: the position in the list from which an element will be retrieved
item: the element at that position

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
`index`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`element_dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
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
A `Tensor` of type `element_dtype`.
</td>
</tr>

</table>

