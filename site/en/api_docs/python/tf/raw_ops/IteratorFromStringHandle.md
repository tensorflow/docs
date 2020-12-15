description: Converts the given string representing a handle to an iterator to a resource.

robots: noindex

# tf.raw_ops.IteratorFromStringHandle

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts the given string representing a handle to an iterator to a resource.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.IteratorFromStringHandle`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.IteratorFromStringHandle(
    string_handle, output_types=[], output_shapes=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`string_handle`
</td>
<td>
A `Tensor` of type `string`.
A string representation of the given handle.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
An optional list of `tf.DTypes`. Defaults to `[]`.
If specified, defines the type of each tuple component in an
element produced by the resulting iterator.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
If specified, defines the shape of each tuple component in an
element produced by the resulting iterator.
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

