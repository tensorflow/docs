description: An array of Tensors of given size.

robots: noindex

# tf.raw_ops.TensorArrayV3

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An array of Tensors of given size.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorArrayV3`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorArrayV3(
    size, dtype, element_shape=None, dynamic_size=(False), clear_after_read=(True),
    identical_element_shapes=(False), tensor_array_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Write data via Write and read via Read or Pack.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`size`
</td>
<td>
A `Tensor` of type `int32`. The size of the array.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. The type of the elements on the tensor_array.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
An optional <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `None`.
The expected shape of an element, if known. Used to
validate the shapes of TensorArray elements. If this shape is not
fully specified, gathering zero-size TensorArrays is an error.
</td>
</tr><tr>
<td>
`dynamic_size`
</td>
<td>
An optional `bool`. Defaults to `False`.
A boolean that determines whether writes to the TensorArray
are allowed to grow the size.  By default, this is not allowed.
</td>
</tr><tr>
<td>
`clear_after_read`
</td>
<td>
An optional `bool`. Defaults to `True`.
If true (default), Tensors in the TensorArray are cleared
after being read.  This disables multiple read semantics but allows early
release of memory.
</td>
</tr><tr>
<td>
`identical_element_shapes`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true (default is false), then all
elements in the TensorArray will be expected to have have identical shapes.
This allows certain behaviors, like dynamically checking for
consistent shapes on write, and being able to fill in properly
shaped zero tensors on stack -- even if the element_shape attribute
is not fully defined.
</td>
</tr><tr>
<td>
`tensor_array_name`
</td>
<td>
An optional `string`. Defaults to `""`.
Overrides the name used for the temporary tensor_array
resource. Default value is the name of the 'TensorArray' op (which
is guaranteed unique).
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
A tuple of `Tensor` objects (handle, flow).
</td>
</tr>
<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type `resource`.
</td>
</tr><tr>
<td>
`flow`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

