description: Imports the graph from graph_def into the current default Graph. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.graph_util.import_graph_def" />
<meta itemprop="path" content="Stable" />
</div>

# tf.graph_util.import_graph_def

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/importer.py#L347-L405">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Imports the graph from `graph_def` into the current default `Graph`. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.import_graph_def`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.graph_util.import_graph_def`, `tf.compat.v1.import_graph_def`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.graph_util.import_graph_def(
    graph_def, input_map=None, return_elements=None, name=None, op_dict=None,
    producer_op_list=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(op_dict)`. They will be removed in a future version.
Instructions for updating:
Please file an issue at https://github.com/tensorflow/tensorflow/issues if you depend on this feature.

This function provides a way to import a serialized TensorFlow
[`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto)
protocol buffer, and extract individual objects in the `GraphDef` as
<a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> and <a href="../../tf/Operation.md"><code>tf.Operation</code></a> objects. Once extracted,
these objects are placed into the current default `Graph`. See
<a href="../../tf/Graph.md#as_graph_def"><code>tf.Graph.as_graph_def</code></a> for a way to create a `GraphDef`
proto.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph_def`
</td>
<td>
A `GraphDef` proto containing operations to be imported into
the default graph.
</td>
</tr><tr>
<td>
`input_map`
</td>
<td>
A dictionary mapping input names (as strings) in `graph_def`
to `Tensor` objects. The values of the named input tensors in the
imported graph will be re-mapped to the respective `Tensor` values.
</td>
</tr><tr>
<td>
`return_elements`
</td>
<td>
A list of strings containing operation names in
`graph_def` that will be returned as `Operation` objects; and/or
tensor names in `graph_def` that will be returned as `Tensor` objects.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional.) A prefix that will be prepended to the names in
`graph_def`. Note that this does not apply to imported function names.
Defaults to `"import"`.
</td>
</tr><tr>
<td>
`op_dict`
</td>
<td>
(Optional.) Deprecated, do not use.
</td>
</tr><tr>
<td>
`producer_op_list`
</td>
<td>
(Optional.) An `OpList` proto with the (possibly stripped)
list of `OpDef`s used by the producer of the graph. If provided,
unrecognized attrs for ops in `graph_def` that have their default value
according to `producer_op_list` will be removed. This will allow some more
`GraphDef`s produced by later binaries to be accepted by earlier binaries.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of `Operation` and/or `Tensor` objects from the imported graph,
corresponding to the names in `return_elements`,
and None if `returns_elements` is None.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `graph_def` is not a `GraphDef` proto,
`input_map` is not a dictionary mapping strings to `Tensor` objects,
or `return_elements` is not a list of strings.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `input_map`, or `return_elements` contains names that
do not appear in `graph_def`, or `graph_def` is not well-formed (e.g.
it refers to an unknown tensor).
</td>
</tr>
</table>

