page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.signal.overlap_and_add

``` python
tf.contrib.signal.overlap_and_add(
    signal,
    frame_step,
    name=None
)
```



Defined in [`tensorflow/contrib/signal/python/ops/reconstruction_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/signal/python/ops/reconstruction_ops.py).

See the guide: [Signal Processing (contrib) > Reconstructing framed sequences and applying a tapering window](../../../../../api_guides/python/contrib.signal#Reconstructing_framed_sequences_and_applying_a_tapering_window)

Reconstructs a signal from a framed representation.

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

* <b>`ValueError`</b>: If `signal`'s rank is less than 2, `frame_step` is not a scalar
    integer or `frame_step` is greater than `frame_length`.