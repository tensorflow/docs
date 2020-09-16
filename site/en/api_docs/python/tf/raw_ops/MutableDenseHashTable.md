description: Creates an empty hash table that uses tensors as the backing store.

robots: noindex

# tf.raw_ops.MutableDenseHashTable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates an empty hash table that uses tensors as the backing store.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MutableDenseHashTable`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MutableDenseHashTable(
    empty_key, value_dtype, container='', shared_name='',
    use_node_name_sharing=(False), value_shape=[], initial_num_buckets=131072,
    max_load_factor=0.8, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It uses "open addressing" with quadratic reprobing to resolve
collisions.

This op creates a mutable hash table, specifying the type of its keys and
values. Each value must be a scalar. Data can be inserted into the table using
the insert operations. It does not support the initialization operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`empty_key`
</td>
<td>
A `Tensor`.
The key used to represent empty key buckets internally. Must not
be used in insert or lookup operations.
</td>
</tr><tr>
<td>
`value_dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. Type of the table values.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this table is placed in the given container.
Otherwise, a default container is used.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this table is shared under the given name across
multiple sessions.
</td>
</tr><tr>
<td>
`use_node_name_sharing`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`value_shape`
</td>
<td>
An optional <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `[]`.
The shape of each value.
</td>
</tr><tr>
<td>
`initial_num_buckets`
</td>
<td>
An optional `int`. Defaults to `131072`.
The initial number of hash table buckets. Must be a power
to 2.
</td>
</tr><tr>
<td>
`max_load_factor`
</td>
<td>
An optional `float`. Defaults to `0.8`.
The maximum ratio between number of entries and number of
buckets before growing the table. Must be between 0 and 1.
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
A `Tensor` of type mutable `string`.
</td>
</tr>

</table>

