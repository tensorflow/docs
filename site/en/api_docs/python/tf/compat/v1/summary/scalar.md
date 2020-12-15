description: Outputs a Summary protocol buffer containing a single scalar value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.scalar" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.scalar

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/summary/summary.py#L57-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs a `Summary` protocol buffer containing a single scalar value.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.scalar(
    name, tensor, collections=None, family=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The generated Summary has a Tensor.proto containing the input Tensor.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the generated node. Will also serve as the series name in
TensorBoard.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A real numeric Tensor containing a single value.
</td>
</tr><tr>
<td>
`collections`
</td>
<td>
Optional list of graph collections keys. The new summary op is
added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
</td>
</tr><tr>
<td>
`family`
</td>
<td>
Optional; if provided, used as the prefix of the summary tag name,
which controls the tab name used for display on Tensorboard.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` of type `string`. Which contains a `Summary` protobuf.
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
If tensor has the wrong shape or type.
</td>
</tr>
</table>

