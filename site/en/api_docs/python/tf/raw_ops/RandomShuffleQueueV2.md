description: A queue that randomizes the order of elements.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RandomShuffleQueueV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RandomShuffleQueueV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A queue that randomizes the order of elements.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RandomShuffleQueueV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RandomShuffleQueueV2(
    component_types, shapes=[], capacity=-1, min_after_dequeue=0, seed=0, seed2=0,
    container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
The shape of each component in a value. The length of this attr must
be either 0 or the same as the length of component_types. If the length of
this attr is 0, the shapes of queue elements are not constrained, and
only one element may be dequeued at a time.
</td>
</tr><tr>
<td>
`capacity`
</td>
<td>
An optional `int`. Defaults to `-1`.
The upper bound on the number of elements in this queue.
Negative numbers mean no limit.
</td>
</tr><tr>
<td>
`min_after_dequeue`
</td>
<td>
An optional `int`. Defaults to `0`.
Dequeue will block unless there would be this
many elements after the dequeue or the queue is closed. This
ensures a minimum level of mixing of elements.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An optional `int`. Defaults to `0`.
If either seed or seed2 is set to be non-zero, the random number
generator is seeded by the given seed.  Otherwise, a random seed is used.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
An optional `int`. Defaults to `0`.
A second seed to avoid seed collision.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this queue is placed in the given container.
Otherwise, a default container is used.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this queue will be shared under the given name
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

