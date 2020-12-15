description: Outputs a Summary protocol buffer with a serialized tensor.proto.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.tensor_summary" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.tensor_summary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/summary/summary.py#L274-L327">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs a `Summary` protocol buffer with a serialized tensor.proto.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.tensor_summary(
    name, tensor, summary_description=None, collections=None, summary_metadata=None,
    family=None, display_name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the generated node. If display_name is not set, it will
also serve as the tag name in TensorBoard. (In that case, the tag
name will inherit tf name scopes.)
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A tensor of any type and shape to serialize.
</td>
</tr><tr>
<td>
`summary_description`
</td>
<td>
A long description of the summary sequence. Markdown
is supported.
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
`summary_metadata`
</td>
<td>
Optional SummaryMetadata proto (which describes which
plugins may use the summary value).
</td>
</tr><tr>
<td>
`family`
</td>
<td>
Optional; if provided, used as the prefix of the summary tag,
which controls the name used for display on TensorBoard when
display_name is not set.
</td>
</tr><tr>
<td>
`display_name`
</td>
<td>
A string used to name this data in TensorBoard. If this is
not set, then the node name will be used instead.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
</td>
</tr>

</table>

