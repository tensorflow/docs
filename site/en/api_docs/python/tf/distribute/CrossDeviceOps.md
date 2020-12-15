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
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L231-L522">
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

The main purpose of this class is to be passed to
<a href="../../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a> in order to choose among different cross
device communication implementations. Prefer using the methods of
<a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> instead of the ones of this class.

#### Implementations:


* <a href="../../tf/distribute/ReductionToOneDevice.md"><code>tf.distribute.ReductionToOneDevice</code></a>
* <a href="../../tf/distribute/NcclAllReduce.md"><code>tf.distribute.NcclAllReduce</code></a>
* <a href="../../tf/distribute/HierarchicalCopyAllReduce.md"><code>tf.distribute.HierarchicalCopyAllReduce</code></a>

## Methods

<h3 id="batch_reduce"><code>batch_reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L379-L426">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_reduce(
    reduce_op, value_destination_pairs, options=None
)
</code></pre>

Reduce values to destinations in batches.

See <a href="../../tf/distribute/StrategyExtended.md#batch_reduce_to"><code>tf.distribute.StrategyExtended.batch_reduce_to</code></a>. This can only be
called in the cross-replica context.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
a <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> specifying how values should be
combined.
</td>
</tr><tr>
<td>
`value_destination_pairs`
</td>
<td>
a sequence of (value, destinations) pairs. See
<a href="../../tf/distribute/CrossDeviceOps.md#reduce"><code>tf.distribute.CrossDeviceOps.reduce</code></a> for descriptions.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
a <a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a>. See
<a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a> for details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, one per pair
in `value_destination_pairs`.
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
tuples of <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> and destinations.
</td>
</tr>
</table>



<h3 id="batch_reduce_implementation"><code>batch_reduce_implementation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L479-L504">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_reduce_implementation(
    reduce_op, value_destination_pairs, options
)
</code></pre>

Implementation of `batch_reduce`.

Overriding this method is useful for subclass implementers.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
a <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> specifying how values should be
combined.
</td>
</tr><tr>
<td>
`value_destination_pairs`
</td>
<td>
a sequence of (value, destinations) pairs. See
`reduce` for descriptions.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
a <a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a>. See
<a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a> for details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, one per pair
in `value_destination_pairs`.
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
tuples of <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> and destinations.
</td>
</tr>
</table>



<h3 id="broadcast"><code>broadcast</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L428-L445">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>broadcast(
    tensor, destinations
)
</code></pre>

Broadcast `tensor` to `destinations`.

This can only be called in the cross-replica context.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> like object. The value to broadcast.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, a
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> alike object, or a device string. It specifies the devices
to broadcast to. Note that if it's a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, the value is
broadcasted to the devices of that variable, this method doesn't update
the variable.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr>

</table>



<h3 id="broadcast_implementation"><code>broadcast_implementation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L506-L522">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>broadcast_implementation(
    tensor, destinations
)
</code></pre>

Implementation of `broadcast`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> like object. The value to broadcast.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, a
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> alike object, or a device string. It specifies the devices
to broadcast to.
`destinations`. Note that if it's a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, the value is
broadcasted to the devices of that variable, this method doesn't update
the variable.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr>

</table>



<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L253-L299">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, per_replica_value, destinations, options=None
)
</code></pre>

Reduce `per_replica_value` to `destinations`.

See <a href="../../tf/distribute/StrategyExtended.md#reduce_to"><code>tf.distribute.StrategyExtended.reduce_to</code></a>. This can only be called in
the cross-replica context.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
a <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> specifying how values should be
combined.
</td>
</tr><tr>
<td>
`per_replica_value`
</td>
<td>
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, or a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>
like object.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, a
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> alike object, or a device string. It specifies the devices
to reduce to. To perform an all-reduce, pass the same to `value` and
`destinations`. Note that if it's a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, the value is reduced
to the devices of that variable, and this method doesn't update the
variable.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
a <a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a>. See
<a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a> for details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
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
if per_replica_value can't be converted to a
<a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> or if destinations is not a string,
<a href="../../tf/Variable.md"><code>tf.Variable</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr>
</table>



<h3 id="reduce_implementation"><code>reduce_implementation</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cross_device_ops.py#L447-L477">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce_implementation(
    reduce_op, per_replica_value, destinations, options
)
</code></pre>

Implementation of `reduce`.

Overriding this method is useful for subclass implementers.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
a <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> specifying how values should be
combined.
</td>
</tr><tr>
<td>
`per_replica_value`
</td>
<td>
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, or a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>
like object.
</td>
</tr><tr>
<td>
`destinations`
</td>
<td>
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, a
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> alike object, or a device string. It specifies the devices
to reduce to. To perform an all-reduce, pass the same to `value` and
`destinations`. Note that if it's a <a href="../../tf/Variable.md"><code>tf.Variable</code></a>, the value is reduced
to the devices of that variable, this method doesn't update the
variable.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
a <a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a>. See
<a href="../../tf/distribute/experimental/CommunicationOptions.md"><code>tf.distribute.experimental.CommunicationOptions</code></a> for details.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
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
if per_replica_value can't be converted to a
<a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> or if destinations is not a string,
<a href="../../tf/Variable.md"><code>tf.Variable</code></a> or <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr>
</table>





