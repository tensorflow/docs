description: Describes a set of TPU devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.Topology" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="cpu_device_name_at_coordinates"/>
<meta itemprop="property" content="serialized"/>
<meta itemprop="property" content="task_ordinal_at_coordinates"/>
<meta itemprop="property" content="tpu_device_name_at_coordinates"/>
<meta itemprop="property" content="tpu_device_ordinal_at_coordinates"/>
</div>

# tf.tpu.experimental.Topology

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/topology.py#L45-L235">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Describes a set of TPU devices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.Topology`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.Topology(
    serialized=None, mesh_shape=None, device_coordinates=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Represents both the shape of the physical mesh, and the mapping between
TensorFlow TPU devices to physical mesh coordinates.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`
</td>
<td>
A serialized `TopologyProto`, or `None`. If not `None`, the
serialized proto is parsed to discover the topology.
</td>
</tr><tr>
<td>
`mesh_shape`
</td>
<td>
A sequence of 4 positive integers, or `None`. If not `None`,
the shape of the TPU topology, in number of cores. Ignored if
`serialized` is not `None`.
</td>
</tr><tr>
<td>
`device_coordinates`
</td>
<td>
A rank 4 numpy array that describes the mapping from
TensorFlow TPU devices to TPU fabric coordinates, or `None`. Ignored
if `serialized is not `None`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `serialized` does not describe a well-formed topology.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `serialized` is `None` and `mesh_shape` is not a sequence
of 4 positive integers.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `serialized` is `None` and `device_coordinates` is not a
rank 4 numpy int32 array that describes a valid coordinate mapping.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`device_coordinates`
</td>
<td>
Describes the mapping from TPU devices to topology coordinates.
</td>
</tr><tr>
<td>
`mesh_rank`
</td>
<td>
Returns the number of dimensions in the mesh.
</td>
</tr><tr>
<td>
`mesh_shape`
</td>
<td>
A rank 1 int32 array describing the shape of the TPU topology.
</td>
</tr><tr>
<td>
`missing_devices`
</td>
<td>
Array of indices of missing devices.
</td>
</tr><tr>
<td>
`num_tasks`
</td>
<td>
Returns the number of TensorFlow tasks in the TPU slice.
</td>
</tr><tr>
<td>
`num_tpus_per_task`
</td>
<td>
Returns the number of TPU devices per task in the TPU slice.
</td>
</tr>
</table>



## Methods

<h3 id="cpu_device_name_at_coordinates"><code>cpu_device_name_at_coordinates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/topology.py#L204-L207">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cpu_device_name_at_coordinates(
    device_coordinates, job=None
)
</code></pre>

Returns the CPU device attached to a logical core.


<h3 id="serialized"><code>serialized</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/topology.py#L225-L235">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>serialized()
</code></pre>

Returns the serialized form of the topology.


<h3 id="task_ordinal_at_coordinates"><code>task_ordinal_at_coordinates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/topology.py#L178-L189">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>task_ordinal_at_coordinates(
    device_coordinates
)
</code></pre>

Returns the TensorFlow task number attached to `device_coordinates`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`device_coordinates`
</td>
<td>
An integer sequence describing a device's physical
coordinates in the TPU fabric.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Returns the TensorFlow task number that contains the TPU device with those
physical coordinates.
</td>
</tr>

</table>



<h3 id="tpu_device_name_at_coordinates"><code>tpu_device_name_at_coordinates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/topology.py#L209-L213">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tpu_device_name_at_coordinates(
    device_coordinates, job=None
)
</code></pre>

Returns the name of the TPU device assigned to a logical core.


<h3 id="tpu_device_ordinal_at_coordinates"><code>tpu_device_ordinal_at_coordinates</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/topology.py#L191-L202">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tpu_device_ordinal_at_coordinates(
    device_coordinates
)
</code></pre>

Returns the TensorFlow device number at `device_coordinates`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`device_coordinates`
</td>
<td>
An integer sequence describing a device's physical
coordinates in the TPU fabric.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Returns the TensorFlow device number within the task corresponding to
attached to the device with those physical coordinates.
</td>
</tr>

</table>





