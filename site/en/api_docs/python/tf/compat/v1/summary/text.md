description: Summarizes textual data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.text" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.text

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/summary/summary.py#L233-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Summarizes textual data.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.text(
    name, tensor, collections=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Text data summarized via this plugin will be visible in the Text Dashboard
in TensorBoard. The standard TensorBoard Text Dashboard will render markdown
in the strings, and will automatically organize 1d and 2d tensors into tables.
If a tensor with more than 2 dimensions is provided, a 2d subarray will be
displayed along with a warning message. (Note that this behavior is not
intrinsic to the text summary api, but rather to the default TensorBoard text
plugin.)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the generated node. Will also serve as a series name in
TensorBoard.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
a string-type Tensor to summarize.
</td>
</tr><tr>
<td>
`collections`
</td>
<td>
Optional list of ops.GraphKeys.  The collections to add the
summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A TensorSummary op that is configured so that TensorBoard will recognize
that it contains textual data. The TensorSummary is a scalar `Tensor` of
type `string` which contains `Summary` protobufs.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If tensor has the wrong type.
</td>
</tr>
</table>

