description: Replaces all the variables in a graph with constants of the same values. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.graph_util.convert_variables_to_constants" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.graph_util.convert_variables_to_constants

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/graph_util_impl.py#L243-L284">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Replaces all the variables in a graph with constants of the same values. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.graph_util.convert_variables_to_constants(
    sess, input_graph_def, output_node_names, variable_names_whitelist=None,
    variable_names_blacklist=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/compat/v1/graph_util/convert_variables_to_constants.md"><code>tf.compat.v1.graph_util.convert_variables_to_constants</code></a>

If you have a trained graph containing Variable ops, it can be convenient to
convert them all to Const ops holding the same values. This makes it possible
to describe the network fully with a single GraphDef file, and allows the
removal of a lot of ops related to loading and saving the variables.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sess`
</td>
<td>
Active TensorFlow session containing the variables.
</td>
</tr><tr>
<td>
`input_graph_def`
</td>
<td>
GraphDef object holding the network.
</td>
</tr><tr>
<td>
`output_node_names`
</td>
<td>
List of name strings for the result nodes of the graph.
</td>
</tr><tr>
<td>
`variable_names_whitelist`
</td>
<td>
The set of variable names to convert (by default,
all variables are converted).
</td>
</tr><tr>
<td>
`variable_names_blacklist`
</td>
<td>
The set of variable names to omit converting
to constants.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
GraphDef containing a simplified version of the original.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
if a DT_RESOURCE op is found whose ancestor Variables are both
blacklisted AND whitelisted for freezing.
</td>
</tr>
</table>

