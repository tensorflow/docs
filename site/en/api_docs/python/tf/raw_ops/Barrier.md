description: Defines a barrier that persists across different graph executions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Barrier" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Barrier

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Defines a barrier that persists across different graph executions.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Barrier`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Barrier(
    component_types, shapes=[], capacity=-1, container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A barrier represents a key-value map, where each key is a string, and
each value is a tuple of tensors.

At runtime, the barrier contains 'complete' and 'incomplete'
elements. A complete element has defined tensors for all components of
its value tuple, and may be accessed using BarrierTakeMany. An
incomplete element has some undefined components in its value tuple,
and may be updated using BarrierInsertMany.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`component_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
The type of each component in a value.
</td>
</tr><tr>
<td>
`shapes`
</td>
<td>
An optional list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`). Defaults to `[]`.
The shape of each component in a value. Each shape must be 1 in the
first dimension. The length of this attr must be the same as the length of
component_types.
</td>
</tr><tr>
<td>
`capacity`
</td>
<td>
An optional `int`. Defaults to `-1`.
The capacity of the barrier.  The default capacity is MAX_INT32,
which is the largest capacity of the underlying queue.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this barrier is placed in the given container.
Otherwise, a default container is used.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this barrier will be shared under the given name
across multiple sessions.
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

