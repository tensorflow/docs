description: Convert a Keras model to dot format.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.model_to_dot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.model_to_dot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/utils/vis_utils.py#L69-L277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convert a Keras model to dot format.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.model_to_dot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.model_to_dot(
    model, show_shapes=(False), show_dtype=(False), show_layer_names=(True),
    rankdir='TB', expand_nested=(False), dpi=96, subgraph=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`model`
</td>
<td>
A Keras model instance.
</td>
</tr><tr>
<td>
`show_shapes`
</td>
<td>
whether to display shape information.
</td>
</tr><tr>
<td>
`show_dtype`
</td>
<td>
whether to display layer dtypes.
</td>
</tr><tr>
<td>
`show_layer_names`
</td>
<td>
whether to display layer names.
</td>
</tr><tr>
<td>
`rankdir`
</td>
<td>
`rankdir` argument passed to PyDot,
a string specifying the format of the plot:
'TB' creates a vertical plot;
'LR' creates a horizontal plot.
</td>
</tr><tr>
<td>
`expand_nested`
</td>
<td>
whether to expand nested models into clusters.
</td>
</tr><tr>
<td>
`dpi`
</td>
<td>
Dots per inch.
</td>
</tr><tr>
<td>
`subgraph`
</td>
<td>
whether to return a `pydot.Cluster` instance.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `pydot.Dot` instance representing the Keras model or
a `pydot.Cluster` instance representing nested model if
`subgraph=True`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
if graphviz or pydot are not available.
</td>
</tr>
</table>

