description: Transforms input_dataset containing Example protos as vectors of DT_STRING into a dataset of Tensor or SparseTensor objects representing the parsed features.

robots: noindex

# tf.raw_ops.ExperimentalParseExampleDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ExperimentalParseExampleDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ExperimentalParseExampleDataset(
    input_dataset, num_parallel_calls, dense_defaults, sparse_keys, dense_keys,
    sparse_types, dense_shapes, output_types, output_shapes, sloppy=(False),
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
`num_parallel_calls`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`dense_defaults`
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
A dict mapping string keys to `Tensor`s.
The keys of the dict must match the dense_keys of the feature.
</td>
</tr><tr>
<td>
`sparse_keys`
</td>
<td>
A list of `strings`.
A list of string keys in the examples features.
The results for these keys will be returned as `SparseTensor` objects.
</td>
</tr><tr>
<td>
`dense_keys`
</td>
<td>
A list of `strings`.
A list of Ndense string Tensors (scalars).
The keys expected in the Examples features associated with dense values.
</td>
</tr><tr>
<td>
`sparse_types`
</td>
<td>
A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
A list of `DTypes` of the same length as `sparse_keys`.
Only <a href="../../tf.md#float32"><code>tf.float32</code></a> (`FloatList`), <a href="../../tf.md#int64"><code>tf.int64</code></a> (`Int64List`),
and <a href="../../tf.md#string"><code>tf.string</code></a> (`BytesList`) are supported.
</td>
</tr><tr>
<td>
`dense_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
List of tuples with the same length as `dense_keys`.
The shape of the data for each dense feature referenced by `dense_keys`.
Required for any input tensors identified by `dense_keys`.  Must be
either fully defined, or may contain an unknown first dimension.
An unknown first dimension means the feature is treated as having
a variable number of blocks, and the output shape along this dimension
is considered unknown at graph build time.  Padding is applied for
minibatch elements smaller than the maximum number of blocks for the
given feature along this dimension.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
The type list for the return values.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
The list of shapes being produced.
</td>
</tr><tr>
<td>
`sloppy`
</td>
<td>
An optional `bool`. Defaults to `False`.
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

