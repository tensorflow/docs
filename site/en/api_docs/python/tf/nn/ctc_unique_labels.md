description: Get unique labels and indices for batched labels for <a href="../../tf/nn/ctc_loss.md"><code>tf.nn.ctc_loss</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.ctc_unique_labels" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.ctc_unique_labels

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ctc_ops.py#L1163-L1196">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get unique labels and indices for batched labels for <a href="../../tf/nn/ctc_loss.md"><code>tf.nn.ctc_loss</code></a>.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.ctc_unique_labels`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.ctc_unique_labels(
    labels, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For use with <a href="../../tf/nn/ctc_loss.md"><code>tf.nn.ctc_loss</code></a> optional argument `unique`: This op can be
used to preprocess labels in input pipeline to for better speed/memory use
computing the ctc loss on TPU.

#### Example:

ctc_unique_labels([[3, 4, 4, 3]]) ->
  unique labels padded with 0: [[3, 4, 0, 0]]
  indices of original labels in unique: [0, 1, 1, 0]



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
tensor of shape [batch_size, max_label_length] padded with 0.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this `Op`. Defaults to "ctc_unique_labels".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
tuple of
- unique labels, tensor of shape `[batch_size, max_label_length]`
- indices into unique labels, shape `[batch_size, max_label_length]`
</td>
</tr>

</table>

