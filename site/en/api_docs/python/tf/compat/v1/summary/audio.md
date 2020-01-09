page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.summary.audio


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/summary/summary.py#L184-L230">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs a `Summary` protocol buffer with audio.

``` python
tf.compat.v1.summary.audio(
    name,
    tensor,
    sample_rate,
    max_outputs=3,
    collections=None,
    family=None
)
```



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

#### Args:


* <b>`name`</b>: A name for the generated node. Will also serve as a series name in
  TensorBoard.
* <b>`tensor`</b>: A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]`
  or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`.
* <b>`sample_rate`</b>: A Scalar `float32` `Tensor` indicating the sample rate of the
  signal in hertz.
* <b>`max_outputs`</b>: Max number of batch elements to generate audio for.
* <b>`collections`</b>: Optional list of ops.GraphKeys.  The collections to add the
  summary to.  Defaults to [_ops.GraphKeys.SUMMARIES]
* <b>`family`</b>: Optional; if provided, used as the prefix of the summary tag name,
  which controls the tab name used for display on Tensorboard.


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.
