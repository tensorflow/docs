description: Merge repeated labels into single labels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.collapse_repeated" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.collapse_repeated

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ctc_ops.py#L1058-L1118">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Merge repeated labels into single labels.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.collapse_repeated`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.collapse_repeated(
    labels, seq_length, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
Tensor of shape [batch, max value in seq_length]
</td>
</tr><tr>
<td>
`seq_length`
</td>
<td>
Tensor of shape [batch], sequence length of each batch element.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`. Defaults to "collapse_repeated_labels".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple `(collapsed_labels, new_seq_length)` where
</td>
</tr>
<tr>
<td>
`collapsed_labels`
</td>
<td>
Tensor of shape [batch, max_seq_length] with repeated
labels collapsed and padded to max_seq_length, eg:
`[[A, A, B, B, A], [A, B, C, D, E]] => [[A, B, A, 0, 0], [A, B, C, D, E]]`
</td>
</tr><tr>
<td>
`new_seq_length`
</td>
<td>
int tensor of shape [batch] with new sequence lengths.
</td>
</tr>
</table>

