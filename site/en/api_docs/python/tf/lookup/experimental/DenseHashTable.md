description: A generic mutable hash table implementation using tensors as backing store.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lookup.experimental.DenseHashTable" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="erase"/>
<meta itemprop="property" content="export"/>
<meta itemprop="property" content="insert"/>
<meta itemprop="property" content="insert_or_assign"/>
<meta itemprop="property" content="lookup"/>
<meta itemprop="property" content="remove"/>
<meta itemprop="property" content="size"/>
</div>

# tf.lookup.experimental.DenseHashTable

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L1839-L2131">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A generic mutable hash table implementation using tensors as backing store.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lookup.experimental.DenseHashTable`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lookup.experimental.DenseHashTable(
    key_dtype, value_dtype, default_value, empty_key, deleted_key,
    initial_num_buckets=None, name='MutableDenseHashTable', checkpoint=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Data can be inserted by calling the insert method and removed by calling the
remove method. It does not support initialization via the init method.

It uses "open addressing" with quadratic reprobing to resolve collisions.
Compared to `MutableHashTable` the insert, remove and lookup operations in a
`DenseHashTable` are typically faster, but memory usage can be higher.
However, `DenseHashTable` does not require additional memory for
temporary tensors created during checkpointing and restore operations.

#### Example usage:



```python
table = tf.lookup.DenseHashTable(key_dtype=tf.int64,
                                 value_dtype=tf.int64,
                                 default_value=-1,
                                 empty_key=0,
                                 deleted_key=-1)

sess.run(table.insert(keys, values))
out = table.lookup(query_keys)
print(out.eval())
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key_dtype`
</td>
<td>
the type of the key tensors.
</td>
</tr><tr>
<td>
`value_dtype`
</td>
<td>
the type of the value tensors.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
The value to use if a key is missing in the table.
</td>
</tr><tr>
<td>
`empty_key`
</td>
<td>
the key to use to represent empty buckets internally. Must not
be used in insert, remove or lookup operations.
</td>
</tr><tr>
<td>
`deleted_key`
</td>
<td>
the key to use to represent deleted buckets internally. Must
not be used in insert, remove or lookup operations and be different from
the empty_key.
</td>
</tr><tr>
<td>
`initial_num_buckets`
</td>
<td>
the initial number of buckets.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`checkpoint`
</td>
<td>
if True, the contents of the table are saved to and restored
from checkpoints. If `shared_name` is empty for a checkpointed table, it
is shared using the table node name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If checkpoint is True and no name was specified.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`key_dtype`
</td>
<td>
The table key dtype.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the table.
</td>
</tr><tr>
<td>
`resource_handle`
</td>
<td>
Returns the resource handle associated with this Resource.
</td>
</tr><tr>
<td>
`value_dtype`
</td>
<td>
The table value dtype.
</td>
</tr>
</table>



## Methods

<h3 id="erase"><code>erase</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L2041-L2066">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>erase(
    keys, name=None
)
</code></pre>

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`keys`
</td>
<td>
Keys to remove. Can be a tensor of any shape. Must match the table's
key type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The created Operation.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when `keys` do not match the table data types.
</td>
</tr>
</table>



<h3 id="export"><code>export</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L2086-L2102">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>export(
    name=None
)
</code></pre>

Returns tensors of all keys and values in the table.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A pair of tensors with the first tensor containing all keys and the
second tensors containing all values in the table.
</td>
</tr>

</table>



<h3 id="insert"><code>insert</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L2022-L2039">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>insert(
    keys, values, name=None
)
</code></pre>

Associates `keys` with `values`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`keys`
</td>
<td>
Keys to insert. Can be a tensor of any shape. Must match the table's
key type.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
Values to be associated with keys. Must be a tensor of the same
shape as `keys` and match the table's value type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The created Operation.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when `keys` or `values` doesn't match the table data
types.
</td>
</tr>
</table>



<h3 id="insert_or_assign"><code>insert_or_assign</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L1995-L2020">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>insert_or_assign(
    keys, values, name=None
)
</code></pre>

Associates `keys` with `values`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`keys`
</td>
<td>
Keys to insert. Can be a tensor of any shape. Must match the table's
key type.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
Values to be associated with keys. Must be a tensor of the same
shape as `keys` and match the table's value type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The created Operation.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when `keys` or `values` doesn't match the table data
types.
</td>
</tr>
</table>



<h3 id="lookup"><code>lookup</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L1969-L1993">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>lookup(
    keys, name=None
)
</code></pre>

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`keys`
</td>
<td>
Keys to look up. Can be a tensor of any shape. Must match the
table's key_dtype.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor containing the values in the same shape as `keys` using the
table's value type.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when `keys` do not match the table data types.
</td>
</tr>
</table>



<h3 id="remove"><code>remove</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L2068-L2084">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>remove(
    keys, name=None
)
</code></pre>

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`keys`
</td>
<td>
Keys to remove. Can be a tensor of any shape. Must match the table's
key type.
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The created Operation.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
when `keys` do not match the table data types.
</td>
</tr>
</table>



<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/lookup_ops.py#L1956-L1967">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>size(
    name=None
)
</code></pre>

Compute the number of elements in this table.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
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
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar tensor containing the number of elements in this table.
</td>
</tr>

</table>





