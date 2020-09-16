description: Sets up the centralized structures for a distributed TPU system.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ConfigureDistributedTPU" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ConfigureDistributedTPU

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Sets up the centralized structures for a distributed TPU system.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ConfigureDistributedTPU`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ConfigureDistributedTPU(
    embedding_config='', tpu_embedding_config='', is_global_init=(False),
    enable_whole_mesh_compilations=(False), compilation_failure_closes_chips=(True),
    name=None
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
An optional `string`. Defaults to `""`.
Reserved. Do not use.
</td>
</tr><tr>
<td>
`tpu_embedding_config`
</td>
<td>
An optional `string`. Defaults to `""`.
Serialized tensorflow.tpu.TPUEmbeddingConfiguration that
describes the embedding lookups of the program.
</td>
</tr><tr>
<td>
`is_global_init`
</td>
<td>
An optional `bool`. Defaults to `False`.
Reserved. Do not use.
</td>
</tr><tr>
<td>
`enable_whole_mesh_compilations`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`compilation_failure_closes_chips`
</td>
<td>
An optional `bool`. Defaults to `True`.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

