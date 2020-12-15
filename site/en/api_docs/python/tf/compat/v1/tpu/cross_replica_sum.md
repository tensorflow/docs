description: Sum the input tensor across replicas according to group_assignment.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.cross_replica_sum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.cross_replica_sum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/ops/tpu_ops.py#L93-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sum the input tensor across replicas according to group_assignment.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.cross_replica_sum(
    x, group_assignment=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
The local tensor to the sum.
</td>
</tr><tr>
<td>
`group_assignment`
</td>
<td>
Optional 2d int32 lists with shape [num_groups,
num_replicas_per_group]. `group_assignment[i]` represents the replica
ids in the ith subgroup.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional op name.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` which is summed across replicas.
</td>
</tr>

</table>

