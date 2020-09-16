description: A general quantization scheme is being developed in tf.contrib.quantize. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.do_quantize_training_on_graphdef" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.do_quantize_training_on_graphdef

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/quantize_training.py#L27-L50">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A general quantization scheme is being developed in `tf.contrib.quantize`. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.do_quantize_training_on_graphdef(
    input_graph, num_bits
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
GraphDef quantized training rewriter is deprecated in the long term.

Consider using that instead, though since it is in the tf.contrib namespace,
it is not subject to backward compatibility guarantees.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_graph`
</td>
<td>
A `GraphDef`.
</td>
</tr><tr>
<td>
`num_bits`
</td>
<td>
The number of bits for quantize training.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The graph with quantize training done.
</td>
</tr>

</table>

