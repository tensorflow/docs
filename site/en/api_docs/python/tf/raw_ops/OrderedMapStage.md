description: Stage (key, values) in the underlying container which behaves like a ordered

robots: noindex

# tf.raw_ops.OrderedMapStage

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Stage (key, values) in the underlying container which behaves like a ordered

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OrderedMapStage`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OrderedMapStage(
    key, indices, values, dtypes, capacity=0, memory_limit=0, container='',
    shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

associative container.   Elements are ordered by key.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`key`
</td>
<td>
A `Tensor` of type `int64`. int64
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of `Tensor` objects. a list of tensors
dtypes A list of data types that inserted values should adhere to.
</td>
</tr><tr>
<td>
`dtypes`
</td>
<td>
A list of `tf.DTypes`.
</td>
</tr><tr>
<td>
`capacity`
</td>
<td>
An optional `int` that is `>= 0`. Defaults to `0`.
Maximum number of elements in the Staging Area. If > 0, inserts
on the container will block when the capacity is reached.
</td>
</tr><tr>
<td>
`memory_limit`
</td>
<td>
An optional `int` that is `>= 0`. Defaults to `0`.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this queue is placed in the given container. Otherwise,
a default container is used.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
It is necessary to match this name to the matching Unstage Op.
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
The created Operation.
</td>
</tr>

</table>

