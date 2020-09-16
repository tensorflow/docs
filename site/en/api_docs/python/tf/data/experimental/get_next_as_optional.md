description: Returns an Optional that contains the next value from the iterator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.get_next_as_optional" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.get_next_as_optional

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/ops/iterator_ops.py#L813-L833">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns an `Optional` that contains the next value from the iterator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.get_next_as_optional`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.get_next_as_optional(
    iterator
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `iterator` has reached the end of the sequence, the returned `Optional`
will have no value.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`iterator`
</td>
<td>
An iterator for an instance of <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An `Optional` object representing the next value from the iterator (if it
has one) or no value.
</td>
</tr>

</table>

