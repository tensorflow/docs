

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.deprecated.audio_summary

``` python
tf.contrib.deprecated.audio_summary(
    tag,
    tensor,
    sample_rate,
    max_outputs=3,
    collections=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/logging_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/logging_ops.py).

Outputs a `Summary` protocol buffer with audio. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.audio. Note that tf.summary.audio uses the node name instead of the tag. This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in.

This op is deprecated. Please switch to tf.summary.audio.
For an explanation of why this op was deprecated, and information on how to
migrate, look ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

The summary has up to `max_outputs` summary values containing audio. The
audio is built from `tensor` which must be 3-D with shape `[batch_size,
frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
assumed to be in the range of `[-1.0, 1.0]` with a sample rate of
`sample_rate`.

The `tag` argument is a scalar `Tensor` of type `string`.  It is used to
build the `tag` of the summary values:

*  If `max_outputs` is 1, the summary value tag is '*tag*/audio'.
*  If `max_outputs` is greater than 1, the summary value tags are
   generated sequentially as '*tag*/audio/0', '*tag*/audio/1', etc.

#### Args:

* <b>`tag`</b>: A scalar `Tensor` of type `string`. Used to build the `tag`
    of the summary values.
* <b>`tensor`</b>: A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]`
    or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`.
* <b>`sample_rate`</b>: A Scalar `float32` `Tensor` indicating the sample rate of the
    signal in hertz.
* <b>`max_outputs`</b>: Max number of batch elements to generate audio for.
* <b>`collections`</b>: Optional list of ops.GraphKeys.  The collections to add the
    summary to.  Defaults to [ops.GraphKeys.SUMMARIES]
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar `Tensor` of type `string`. The serialized `Summary` protocol
buffer.