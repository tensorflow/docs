description: A class wrapping information needed by an input function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.InputContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_per_replica_batch_size"/>
</div>

# tf.distribute.InputContext

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L454-L523">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A class wrapping information needed by an input function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.InputContext`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.InputContext(
    num_input_pipelines=1, input_pipeline_id=0, num_replicas_in_sync=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a context class that is passed to the user's input function and
contains information about the compute replicas and input pipelines. The
number of compute replicas (in sync training) helps compute the local batch
size from the desired global batch size for each replica. The input pipeline
information can be used to return a different subset of the input in each
replica (for e.g. shard the input pipeline, use a different input
source etc).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_input_pipelines`
</td>
<td>
the number of input pipelines in a cluster.
</td>
</tr><tr>
<td>
`input_pipeline_id`
</td>
<td>
the current input pipeline id, should be an int in
[0,`num_input_pipelines`).
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
the number of replicas that are in sync.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`input_pipeline_id`
</td>
<td>
Returns the input pipeline ID.
</td>
</tr><tr>
<td>
`num_input_pipelines`
</td>
<td>
Returns the number of input pipelines.
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
Returns the number of compute replicas in sync.
</td>
</tr>
</table>



## Methods

<h3 id="get_per_replica_batch_size"><code>get_per_replica_batch_size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L501-L519">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_per_replica_batch_size(
    global_batch_size
)
</code></pre>

Returns the per-replica batch size.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`global_batch_size`
</td>
<td>
the global batch size which should be divisible by
`num_replicas_in_sync`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
the per-replica batch size.
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
if `global_batch_size` not divisible by
`num_replicas_in_sync`.
</td>
</tr>
</table>





