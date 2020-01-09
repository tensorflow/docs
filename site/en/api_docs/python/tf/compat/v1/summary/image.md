page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.image


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/summary.py#L87-L140">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs a `Summary` protocol buffer with images.

``` python
tf.compat.v1.summary.image(
    name,
    tensor,
    max_outputs=3,
    collections=None,
    family=None
)
```



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

#### Args:


* <b>`name`</b>: A name for the generated node. Will also serve as a series name in
  TensorBoard.
* <b>`tensor`</b>: A 4-D `uint8` or `float32` `Tensor` of shape `[batch_size, height,
  width, channels]` where `channels` is 1, 3, or 4.
* <b>`max_outputs`</b>: Max number of batch elements to generate images for.
* <b>`collections`</b>: Optional list of ops.GraphKeys.  The collections to add the
  summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag name,
  which controls the tab name used for display on Tensorboard.


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
