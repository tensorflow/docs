description: Outputs a Summary protocol buffer with images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.image" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.image

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/summary/summary.py#L87-L140">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs a `Summary` protocol buffer with images.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.image(
    name, tensor, max_outputs=3, collections=None, family=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The summary has up to `max_outputs` summary values containing images. The
images are built from `tensor` which must be 4-D with shape `[batch_size,
height, width, channels]` and where `channels` can be:

*  1: `tensor` is interpreted as Grayscale.
*  3: `tensor` is interpreted as RGB.
*  4: `tensor` is interpreted as RGBA.

The images have the same number of channels as the input tensor. For float
input, the values are normalized one image at a time to fit in the range
`[0, 255]`.  `uint8` values are unchanged.  The op uses two different
normalization algorithms:

*  If the input values are all positive, they are rescaled so the largest one
   is 255.

*  If any input value is negative, the values are shifted so input value 0.0
   is at 127.  They are then rescaled so that either the smallest value is 0,
   or the largest one is 255.

The `tag` in the outputted Summary.Value protobufs is generated based on the
name, with a suffix depending on the max_outputs setting:

*  If `max_outputs` is 1, the summary value tag is '*name*/image'.
*  If `max_outputs` is greater than 1, the summary value tags are
   generated sequentially as '*name*/image/0', '*name*/image/1', etc.

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
A 4-D `uint8` or `float32` `Tensor` of shape `[batch_size, height,
width, channels]` where `channels` is 1, 3, or 4.
</td>
</tr><tr>
<td>
`max_outputs`
</td>
<td>
Max number of batch elements to generate images for.
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

