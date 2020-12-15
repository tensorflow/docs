description: Creates a dataset that computes a windowed group-by on input_dataset.

robots: noindex

# tf.raw_ops.GroupByWindowDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that computes a windowed group-by on `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GroupByWindowDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GroupByWindowDataset(
    input_dataset, key_func_other_arguments, reduce_func_other_arguments,
    window_size_func_other_arguments, key_func, reduce_func, window_size_func,
    output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

//

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`key_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`reduce_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`window_size_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`key_func`
</td>
<td>
A function decorated with @Defun.
A function mapping an element of `input_dataset`, concatenated
with `key_func_other_arguments` to a scalar value of type DT_INT64.
</td>
</tr><tr>
<td>
`reduce_func`
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`window_size_func`
</td>
<td>
A function decorated with @Defun.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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

