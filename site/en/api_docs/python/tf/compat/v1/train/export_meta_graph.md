description: Returns MetaGraphDef proto.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.export_meta_graph" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.export_meta_graph

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/saver.py#L1517-L1599">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns `MetaGraphDef` proto.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.export_meta_graph(
    filename=None, meta_info_def=None, graph_def=None, saver_def=None,
    collection_list=None, as_text=(False), graph=None, export_scope=None,
    clear_devices=(False), clear_extraneous_savers=(False),
    strip_default_attrs=(False), save_debug_info=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Optionally writes it to filename.

This function exports the graph, saver, and collection objects into
`MetaGraphDef` protocol buffer with the intention of it being imported
at a later time or location to restart training, run inference, or be
a subgraph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`filename`
</td>
<td>
Optional filename including the path for writing the generated
`MetaGraphDef` protocol buffer.
</td>
</tr><tr>
<td>
`meta_info_def`
</td>
<td>
`MetaInfoDef` protocol buffer.
</td>
</tr><tr>
<td>
`graph_def`
</td>
<td>
`GraphDef` protocol buffer.
</td>
</tr><tr>
<td>
`saver_def`
</td>
<td>
`SaverDef` protocol buffer.
</td>
</tr><tr>
<td>
`collection_list`
</td>
<td>
List of string keys to collect.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
If `True`, writes the `MetaGraphDef` as an ASCII proto.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
The `Graph` to export. If `None`, use the default graph.
</td>
</tr><tr>
<td>
`export_scope`
</td>
<td>
Optional `string`. Name scope under which to extract the
subgraph. The scope name will be striped from the node definitions for
easy import later into new name scopes. If `None`, the whole graph is
exported. graph_def and export_scope cannot both be specified.
</td>
</tr><tr>
<td>
`clear_devices`
</td>
<td>
Whether or not to clear the device field for an `Operation`
or `Tensor` during export.
</td>
</tr><tr>
<td>
`clear_extraneous_savers`
</td>
<td>
Remove any Saver-related information from the graph
(both Save/Restore ops and SaverDefs) that are not associated with the
provided SaverDef.
</td>
</tr><tr>
<td>
`strip_default_attrs`
</td>
<td>
Boolean. If `True`, default-valued attributes will be
removed from the NodeDefs. For a detailed guide, see
[Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
</td>
</tr><tr>
<td>
`save_debug_info`
</td>
<td>
If `True`, save the GraphDebugInfo to a separate file,
which in the same directory of filename and with `_debug` added before the
file extend.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Optional keyed arguments.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `MetaGraphDef` proto.
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
When the `GraphDef` is larger than 2GB.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called with eager execution enabled.
</td>
</tr>
</table>




#### Eager Compatibility
Exporting/importing meta graphs is not supported unless both `graph_def` and
`graph` are provided. No graph exists when eager execution is enabled.

