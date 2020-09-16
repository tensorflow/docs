description: Creates a dataset containing elements of input_dataset matching predicate.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.FilterDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.FilterDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset containing elements of `input_dataset` matching `predicate`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FilterDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FilterDataset(
    input_dataset, other_arguments, predicate, output_types, output_shapes,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `predicate` function must return a scalar boolean and accept the
following arguments:

* One tensor for each component of an element of `input_dataset`.
* One tensor for each value in `other_arguments`.

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
`other_arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors, typically values that were captured when
building a closure for `predicate`.
</td>
</tr><tr>
<td>
`predicate`
</td>
<td>
A function decorated with @Defun.
A function returning a scalar boolean.
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

