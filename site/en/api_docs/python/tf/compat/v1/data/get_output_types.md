description: Returns the output shapes for elements of the input dataset / iterator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data.get_output_types" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.data.get_output_types

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/data/ops/dataset_ops.py#L2917-L2931">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the output shapes for elements of the input dataset / iterator.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.data.get_output_types(
    dataset_or_iterator
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset_or_iterator`
</td>
<td>
A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> or <a href="../../../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> objects objects matching the structure of
dataset / iterator elements and specifying the shape of the individual
components.
</td>
</tr>

</table>

