description: Base class for cross-device reduction and broadcasting algorithms.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.CrossDeviceOps" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="batch_reduce"/>
<meta itemprop="property" content="batch_reduce_implementation"/>
<meta itemprop="property" content="broadcast"/>
<meta itemprop="property" content="broadcast_implementation"/>
<meta itemprop="property" content="reduce"/>
<meta itemprop="property" content="reduce_implementation"/>
</div>

# tf.distribute.CrossDeviceOps

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L215-L402">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for cross-device reduction and broadcasting algorithms.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.CrossDeviceOps`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.CrossDeviceOps()
</code></pre>



<!-- Placeholder for "Used in" -->


## Methods

<h3 id="batch_reduce"><code>batch_reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L269-L319">View source</a>

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



<h3 id="batch_reduce_implementation"><code>batch_reduce_implementation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L362-L389">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_reduce_implementation(
    reduce_op, value_destination_pairs, experimental_hints
)
</code></pre>

Implementation of reduce PerReplica objects in a batch.

Overriding this method is useful for subclass implementers.

Reduce each first element in `value_destination_pairs` to each second
element which indicates the destinations.

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
`value_destination_pairs`
</td>
<td>
An iterable of tuples of PerReplica objects
(or tensors with device set if there is one device) and destinations.
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
tuples of PerReplica objects and destinations
</td>
</tr>
</table>



<h3 id="broadcast"><code>broadcast</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L321-L332">View source</a>

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



<h3 id="broadcast_implementation"><code>broadcast_implementation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L391-L402">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>broadcast_implementation(
    tensor, destinations
)
</code></pre>

Implementation of broadcast the `tensor` to destinations.


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L226-L267">View source</a>

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
A PerReplica object or a tensor with device set.
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



<h3 id="reduce_implementation"><code>reduce_implementation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cross_device_ops.py#L334-L360">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce_implementation(
    reduce_op, per_replica_value, destinations, experimental_hints
)
</code></pre>

The implementation of reduce of `per_replica_value` to `destinations`.

Overriding this method is useful for subclass implementers.

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
An instance <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> that indicates of how
per_replica_value will be reduced.
</td>
</tr><tr>
<td>
`per_replica_value`
</td>
<td>
A PerReplica object or a tensor with device set.
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
object.
</td>
</tr>
</table>





