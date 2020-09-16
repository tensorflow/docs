description: Returns the last element of the input list as well as a list with all but that element.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TensorListPopBack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TensorListPopBack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the last element of the input list as well as a list with all but that element.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorListPopBack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListPopBack(
    input_handle, element_shape, element_dtype, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Fails if the list is empty.

input_handle: the input list
tensor: the withdrawn last element of the list
element_dtype: the type of elements in the list
element_shape: the shape of the output tensor

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
A tuple of `Tensor` objects (output_handle, tensor).
</td>
</tr>
<tr>
<td>
`output_handle`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A `Tensor` of type `element_dtype`.
</td>
</tr>
</table>

