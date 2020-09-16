description: Describes some metadata about the TPU system.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tpu.experimental.TPUSystemMetadata" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="devices"/>
<meta itemprop="property" content="num_cores"/>
<meta itemprop="property" content="num_hosts"/>
<meta itemprop="property" content="num_of_cores_per_host"/>
<meta itemprop="property" content="topology"/>
</div>

# tf.tpu.experimental.TPUSystemMetadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu_system_metadata.py#L45-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Describes some metadata about the TPU system.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.tpu.experimental.TPUSystemMetadata`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tpu.experimental.TPUSystemMetadata(
    num_cores, num_hosts, num_of_cores_per_host, topology, devices
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`num_cores`
</td>
<td>
interger. Total number of TPU cores in the TPU system.
</td>
</tr><tr>
<td>
`num_hosts`
</td>
<td>
interger. Total number of hosts (TPU workers) in the TPU system.
</td>
</tr><tr>
<td>
`num_of_cores_per_host`
</td>
<td>
interger. Number of TPU cores per host (TPU worker).
</td>
</tr><tr>
<td>
`topology`
</td>
<td>
an instance of <a href="../../../tf/tpu/experimental/Topology.md"><code>tf.tpu.experimental.Topology</code></a>, which describes the
physical topology of TPU system.
</td>
</tr><tr>
<td>
`devices`
</td>
<td>
a tuple of strings, which describes all the TPU devices in the
system.
</td>
</tr>
</table>



## Class Variables

* `devices` <a id="devices"></a>
* `num_cores` <a id="num_cores"></a>
* `num_hosts` <a id="num_hosts"></a>
* `num_of_cores_per_host` <a id="num_of_cores_per_host"></a>
* `topology` <a id="topology"></a>
