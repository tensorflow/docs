description: An Op to exchange data across TPU replicas.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.AllToAll" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.AllToAll

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An Op to exchange data across TPU replicas.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AllToAll`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AllToAll(
    input, group_assignment, concat_dimension, split_dimension, split_count,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

On each replica, the input is split into `split_count` blocks along
`split_dimension` and send to the other replicas given group_assignment. After
receiving `split_count` - 1 blocks from other replicas, we concatenate the
blocks along `concat_dimension` as the output.

For example, suppose there are 2 TPU replicas:
replica 0 receives input: `[[A, B]]`
replica 1 receives input: `[[C, D]]`

group_assignment=`[[0, 1]]`
concat_dimension=0
split_dimension=1
split_count=2

replica 0's output: `[[A], [C]]`
replica 1's output: `[[B], [D]]`

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
The local input to the sum.
</td>
</tr><tr>
<td>
`group_assignment`
</td>
<td>
A `Tensor` of type `int32`. An int32 tensor with shape
[num_groups, num_replicas_per_group]. `group_assignment[i]` represents the
replica ids in the ith subgroup.
</td>
</tr><tr>
<td>
`concat_dimension`
</td>
<td>
An `int`. The dimension number to concatenate.
</td>
</tr><tr>
<td>
`split_dimension`
</td>
<td>
An `int`. The dimension number to split.
</td>
</tr><tr>
<td>
`split_count`
</td>
<td>
An `int`.
The number of splits, this number must equal to the sub-group
size(group_assignment.get_shape()[1])
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

