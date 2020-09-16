description: Creates a dataset that computes a group-by on input_dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.GroupByReducerDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.GroupByReducerDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that computes a group-by on `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.GroupByReducerDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.GroupByReducerDataset(
    input_dataset, key_func_other_arguments, init_func_other_arguments,
    reduce_func_other_arguments, finalize_func_other_arguments, key_func, init_func,
    reduce_func, finalize_func, output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a dataset that computes a group-by on `input_dataset`.

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
A variant tensor representing the input dataset.
</td>
</tr><tr>
<td>
`key_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors, typically values that were captured when
building a closure for `key_func`.
</td>
</tr><tr>
<td>
`init_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors, typically values that were captured when
building a closure for `init_func`.
</td>
</tr><tr>
<td>
`reduce_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors, typically values that were captured when
building a closure for `reduce_func`.
</td>
</tr><tr>
<td>
`finalize_func_other_arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors, typically values that were captured when
building a closure for `finalize_func`.
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
`init_func`
</td>
<td>
A function decorated with @Defun.
A function mapping a key of type DT_INT64, concatenated with
`init_func_other_arguments` to the initial reducer state.
</td>
</tr><tr>
<td>
`reduce_func`
</td>
<td>
A function decorated with @Defun.
A function mapping the current reducer state and an element of `input_dataset`,
concatenated with `reduce_func_other_arguments` to a new reducer state.
</td>
</tr><tr>
<td>
`finalize_func`
</td>
<td>
A function decorated with @Defun.
A function mapping the final reducer state to an output element.
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

