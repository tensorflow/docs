description: Returns the list of input tensors necessary to compute tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.get_source_inputs" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.get_source_inputs

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/utils/layer_utils.py#L32-L68">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the list of input tensors necessary to compute `tensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.get_source_inputs`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.get_source_inputs(
    tensor, layer=None, node_index=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Output will always be a list of tensors
(potentially with 1 element).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
The tensor to start from.
</td>
</tr><tr>
<td>
`layer`
</td>
<td>
Origin layer of the tensor. Will be
determined via tensor._keras_history if not provided.
</td>
</tr><tr>
<td>
`node_index`
</td>
<td>
Origin node index of the tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
List of input tensors.
</td>
</tr>

</table>

