description: Transforms a tf.Example proto (as a string) into typed tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ParseSingleExample" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ParseSingleExample

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a tf.Example proto (as a string) into typed tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParseSingleExample`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParseSingleExample(
    serialized, dense_defaults, num_sparse, sparse_keys, dense_keys, sparse_types,
    dense_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`
</td>
<td>
A `Tensor` of type `string`.
A vector containing a batch of binary serialized Example protos.
</td>
</tr><tr>
<td>
`dense_defaults`
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
A list of Tensors (some may be empty), whose length matches
the length of `dense_keys`. dense_defaults[j] provides default values
when the example's feature_map lacks dense_key[j].  If an empty Tensor is
provided for dense_defaults[j], then the Feature dense_keys[j] is required.
The input type is inferred from dense_defaults[j], even when it's empty.
If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
then the shape of dense_defaults[j] must match that of dense_shapes[j].
If dense_shapes[j] has an undefined major dimension (variable strides dense
feature), dense_defaults[j] must contain a single element:
the padding element.
</td>
</tr><tr>
<td>
`num_sparse`
</td>
<td>
An `int` that is `>= 0`.
The number of sparse features to be parsed from the example. This
must match the lengths of `sparse_keys` and `sparse_types`.
</td>
</tr><tr>
<td>
`sparse_keys`
</td>
<td>
A list of `strings`. A list of `num_sparse` strings.
The keys expected in the Examples' features associated with sparse values.
</td>
</tr><tr>
<td>
`dense_keys`
</td>
<td>
A list of `strings`.
The keys expected in the Examples' features associated with dense
values.
</td>
</tr><tr>
<td>
`sparse_types`
</td>
<td>
A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
A list of `num_sparse` types; the data types of data in each
Feature given in sparse_keys.
Currently the ParseSingleExample op supports DT_FLOAT (FloatList),
DT_INT64 (Int64List), and DT_STRING (BytesList).
</td>
</tr><tr>
<td>
`dense_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
The shapes of data in each Feature given in dense_keys.
The length of this list must match the length of `dense_keys`.  The
number of elements in the Feature corresponding to dense_key[j] must
always equal dense_shapes[j].NumEntries().  If dense_shapes[j] ==
(D0, D1, ..., DN) then the shape of output Tensor dense_values[j]
will be (D0, D1, ..., DN): In the case dense_shapes[j] = (-1, D1,
..., DN), the shape of the output Tensor dense_values[j] will be (M,
D1, .., DN), where M is the number of blocks of elements of length
D1 * .... * DN, in the input.
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
A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values).
</td>
</tr>
<tr>
<td>
`sparse_indices`
</td>
<td>
A list of `num_sparse` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A list of `Tensor` objects of type `sparse_types`.
</td>
</tr><tr>
<td>
`sparse_shapes`
</td>
<td>
A list of `num_sparse` `Tensor` objects with type `int64`.
</td>
</tr><tr>
<td>
`dense_values`
</td>
<td>
A list of `Tensor` objects. Has the same type as `dense_defaults`.
</td>
</tr>
</table>

