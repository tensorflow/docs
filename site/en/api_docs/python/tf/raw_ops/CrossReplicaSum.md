description: An Op to sum inputs across replicated TPU instances.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CrossReplicaSum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CrossReplicaSum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



An Op to sum inputs across replicated TPU instances.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CrossReplicaSum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CrossReplicaSum(
    input, group_assignment, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Each instance supplies its own input.

For example, suppose there are 8 TPU instances: `[A, B, C, D, E, F, G, H]`.
Passing group_assignment=`[[0,2,4,6],[1,3,5,7]]` sets `A, C, E, G` as group 0,
and `B, D, F, H` as group 1. Thus we get the outputs:
`[A+C+E+G, B+D+F+H, A+C+E+G, B+D+F+H, A+C+E+G, B+D+F+H, A+C+E+G, B+D+F+H]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `int32`, `uint32`.
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

