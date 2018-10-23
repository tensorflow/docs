

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.signal.frame

``` python
frame(
    signal,
    frame_length,
    frame_step,
    pad_end=False,
    pad_value=0,
    axis=-1,
    name=None
)
```



Defined in [`tensorflow/contrib/signal/python/ops/shape_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/signal/python/ops/shape_ops.py).

Expands `signal`'s `axis` dimension into frames of `frame_length`.

Slides a window of size `frame_length` over `signal`s `axis` dimension
with a stride of `frame_step`, replacing the `axis` dimension with
`[frames, frame_length]` frames.

If `pad_end` is True, window positions that are past the end of the `axis`
dimension are padded with `pad_value` until the window moves fully past the
end of the dimension. Otherwise, only window positions that fully overlap the
`axis` dimension are produced.

For example:

```python
pcm = tf.placeholder(tf.float32, [None, 9152])
frames = tf.contrib.signal.frame(pcm, 512, 180)
magspec = tf.abs(tf.spectral.rfft(frames, [512]))
image = tf.expand_dims(magspec, 3)
```

#### Args:

* <b>`signal`</b>: A `[..., samples, ...]` `Tensor`. The rank and dimensions
    may be unknown. Rank must be at least 1.
* <b>`frame_length`</b>: The frame length in samples. An integer or scalar `Tensor`.
* <b>`frame_step`</b>: The frame hop size in samples. An integer or scalar `Tensor`.
* <b>`pad_end`</b>: Whether to pad the end of `signal` with `pad_value`.
* <b>`pad_value`</b>: An optional scalar `Tensor` to use where the input signal
    does not exist when `pad_end` is True.
* <b>`axis`</b>: A scalar integer `Tensor` indicating the axis to frame. Defaults to
    the last axis. Supports negative values for indexing from the end.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

  A `Tensor` of frames with shape `[..., frames, frame_length, ...]`.


#### Raises:

* <b>`ValueError`</b>: If `frame_length`, `frame_step`, or `pad_value` are not scalar.