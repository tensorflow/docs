description: Returns the type signature for elements of the input dataset / iterator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.get_structure" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.get_structure

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/dataset_ops.py#L2738-L2759">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the type signature for elements of the input dataset / iterator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.get_structure`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.get_structure(
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
A <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> or an <a href="../../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of <a href="../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> objects matching the structure of an
element of `dataset_or_iterator` and specifying the type of individual
components.
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
If input is not a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> or an <a href="../../../tf/data/Iterator.md"><code>tf.data.Iterator</code></a>
object.
</td>
</tr>
</table>

