description: Initializes a distributed TPU system for use with TensorFlow.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.initialize_system" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.initialize_system

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu.py#L98-L134">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Initializes a distributed TPU system for use with TensorFlow.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.initialize_system(
    embedding_config=None, job=None, compilation_failure_closes_chips=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`embedding_config`
</td>
<td>
If not None, a `TPUEmbeddingConfiguration` proto
describing the desired configuration of the hardware embedding lookup
tables. If embedding_config is None, no hardware embeddings can be used.
</td>
</tr><tr>
<td>
`job`
</td>
<td>
The job (the XXX in TensorFlow device specification /job:XXX) that
contains the TPU devices that will be initialized. If job=None it is
assumed there is only one job in the TensorFlow flock, and an error will
be returned if this assumption does not hold.
</td>
</tr><tr>
<td>
`compilation_failure_closes_chips`
</td>
<td>
Set the configuration whether
we want to close TPU chips when there is a compilation failure.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A serialized `TopologyProto` that describes the TPU system. Note:
the topology must be evaluated using `Session.run` before it can be used.
</td>
</tr>

</table>

