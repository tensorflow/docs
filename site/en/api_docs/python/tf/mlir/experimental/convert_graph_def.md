description: Import a GraphDef and convert it to a textual MLIR module.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.mlir.experimental.convert_graph_def" />
<meta itemprop="path" content="Stable" />
</div>

# tf.mlir.experimental.convert_graph_def

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/compiler/mlir/mlir.py#L25-L41">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Import a GraphDef and convert it to a textual MLIR module.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.mlir.experimental.convert_graph_def`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.mlir.experimental.convert_graph_def(
    graph_def, pass_pipeline='tf-standard-pipeline'
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph_def`
</td>
<td>
An object of type graph_pb2.GraphDef or a textual proto
representation of a valid GraphDef.
</td>
</tr><tr>
<td>
`pass_pipeline`
</td>
<td>
A textual description of an MLIR Pass Pipeline to run on the
module, see MLIR documentation for the
[textual pass pipeline syntax](https://github.com/tensorflow/mlir/blob/master/g3doc/WritingAPass.md#textual-pass-pipeline-specification).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A textual representation of the MLIR module corresponding to the graphdef.
Raises a RuntimeError on error.
</td>
</tr>

</table>

