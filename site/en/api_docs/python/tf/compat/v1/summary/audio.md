description: Outputs a Summary protocol buffer with audio.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.audio" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.audio

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/summary/summary.py#L184-L230">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs a `Summary` protocol buffer with audio.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.audio(
    name, tensor, sample_rate, max_outputs=3, collections=None, family=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The summary has up to `max_outputs` summary values containing audio. The
audio is built from `tensor` which must be 3-D with shape `[batch_size,
frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
assumed to be in the range of `[-1.0, 1.0]` with a sample rate of
`sample_rate`.

The `tag` in the outputted Summary.Value protobufs is generated based on the
name, with a suffix depending on the max_outputs setting:

*  If `max_outputs` is 1, the summary value tag is '*name*/audio'.
*  If `max_outputs` is greater than 1, the summary value tags are
   generated sequentially as '*name*/audio/0', '*name*/audio/1', etc

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
A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]`
or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`.
</td>
</tr><tr>
<td>
`sample_rate`
</td>
<td>
A Scalar `float32` `Tensor` indicating the sample rate of the
signal in hertz.
</td>
</tr><tr>
<td>
`max_outputs`
</td>
<td>
Max number of batch elements to generate audio for.
</td>
</tr><tr>
<td>
`collections`
</td>
<td>
Optional list of ops.GraphKeys.  The collections to add the
summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]
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
A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
</td>
</tr>

</table>

