description: A queue that produces elements in first-in first-out order.

robots: noindex

# tf.raw_ops.PaddingFIFOQueueV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A queue that produces elements in first-in first-out order.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.PaddingFIFOQueueV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.PaddingFIFOQueueV2(
    component_types, shapes=[], capacity=-1, container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Variable-size shapes are allowed by setting the corresponding shape dimensions
to 0 in the shape attr.  In this case DequeueMany will pad up to the maximum
size of any given element in the minibatch.  See below for details.

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
be either 0 or the same as the length of component_types.
Shapes of fixed rank but variable size are allowed by setting
any shape dimension to -1.  In this case, the inputs' shape may vary along
the given dimension, and DequeueMany will pad the given dimension with
zeros up to the maximum shape of all elements in the given batch.
If the length of this attr is 0, different queue elements may have
different ranks and shapes, but only one element may be dequeued at a time.
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

