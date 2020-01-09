page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.overlap_and_add


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/overlap_and_add">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/signal/reconstruction_ops.py#L29-L155">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Reconstructs a signal from a framed representation.

### Aliases:

* <a href="/api_docs/python/tf/signal/overlap_and_add"><code>tf.compat.v1.signal.overlap_and_add</code></a>
* <a href="/api_docs/python/tf/signal/overlap_and_add"><code>tf.compat.v2.signal.overlap_and_add</code></a>
* <a href="/api_docs/python/tf/signal/overlap_and_add"><code>tf.contrib.signal.overlap_and_add</code></a>


``` python
tf.signal.overlap_and_add(
    signal,
    frame_step,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Adds potentially overlapping frames of a signal with shape
`[..., frames, frame_length]`, offsetting subsequent frames by `frame_step`.
The resulting tensor has shape `[..., output_size]` where

    output_size = (frames - 1) * frame_step + frame_length

#### Args:


* <b>`signal`</b>: A [..., frames, frame_length] `Tensor`. All dimensions may be
  unknown, and rank must be at least 2.
* <b>`frame_step`</b>: An integer or scalar `Tensor` denoting overlap offsets. Must be
  less than or equal to `frame_length`.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `Tensor` with shape `[..., output_size]` containing the overlap-added
frames of `signal`'s inner-most two dimensions.



#### Raises:


* <b>`ValueError`</b>: If `signal`'s rank is less than 2, or `frame_step` is not a
  scalar integer.
