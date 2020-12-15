description: Reduction using NCCL all-reduce.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.NcclAllReduce" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="batch_reduce"/>
<meta itemprop="property" content="broadcast"/>
<meta itemprop="property" content="reduce"/>
</div>

# tf.distribute.NcclAllReduce

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cross_device_ops.py#L747-L769">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reduction using NCCL all-reduce.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.NcclAllReduce`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.NcclAllReduce(
    num_packs=1
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_packs`
</td>
<td>
values will be packed in this many splits.  `num_packs` should
be greater than or equals 0. When it is zero, no packing will be done.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
ValueError if `num_packs` is negative.
</td>
</tr>

</table>



## Methods

<h3 id="batch_reduce"><code>batch_reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cross_device_ops.py#L272-L322">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_reduce(
    reduce_op, value_destination_pairs, experimental_hints=None
)
</code></pre>

Reduce PerReplica objects in a batch.

Reduce each first element in `value_destination_pairs` to each second
element which indicates the destinations.

This can be faster than multiple individual `reduce`s because we can
fuse several tensors into one or multiple packs before reduction.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
An instance of <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> that indicates how the
`per_replica_value` will be reduced.
</td>
</tr><tr>
<td>
`value_destination_pairs`
</td>
<td>
A list or a tuple of PerReplica objects (or
tensors with device set if there is one device) and destinations.
</td>
</tr><tr>
<td>
`experimental_hints`
</td>
<td>
A `tf.distrbute.experimental.CollectiveHints`. Hints
to perform collective operations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a list of Mirrored objects.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `value_destination_pairs` is not an iterable of
tuples of PerReplica objects and destinations.
</td>
</tr>
</table>



<h3 id="broadcast"><code>broadcast</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cross_device_ops.py#L324-L335">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>broadcast(
    tensor, destinations
)
</code></pre>

Broadcast the `tensor` to destinations.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
the tensor to broadcast.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
the broadcast destinations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a Mirrored object.
</td>
</tr>

</table>



<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cross_device_ops.py#L228-L270">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, per_replica_value, destinations, experimental_hints=None
)
</code></pre>

Reduce `per_replica_value` to `destinations`.

It runs the reduction operation defined by `reduce_op` and put the
result on `destinations`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
An instance of <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> that indicates how
per_replica_value will be reduced.
</td>
</tr><tr>
<td>
`per_replica_value`
</td>
<td>
A <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> object or a tensor
with device set.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
the reduction destinations.
</td>
</tr><tr>
<td>
`experimental_hints`
</td>
<td>
A `tf.distrbute.experimental.CollectiveHints`. Hints
to perform collective operations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a Mirrored object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if per_replica_value can't be converted to a PerReplica
object or if destinations aren't strings, Variables or DistributedValues
</td>
</tr>
</table>





