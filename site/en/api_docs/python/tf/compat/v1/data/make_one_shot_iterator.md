description: Creates a <a href="../../../../tf/compat/v1/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> for enumerating dataset elements.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data.make_one_shot_iterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.data.make_one_shot_iterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/dataset_ops.py#L2527-L2545">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a <a href="../../../../tf/compat/v1/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> for enumerating dataset elements.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.data.make_one_shot_iterator(
    dataset
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note: The returned iterator will be initialized automatically.
A "one-shot" iterator does not support re-initialization.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dataset`
</td>
<td>
A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/compat/v1/data/Iterator.md"><code>tf.compat.v1.data.Iterator</code></a> over the elements of this dataset.
</td>
</tr>

</table>

