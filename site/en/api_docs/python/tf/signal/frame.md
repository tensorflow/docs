page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.frame

Expands `signal`'s `axis` dimension into frames of `frame_length`.

### Aliases:

* `tf.compat.v1.signal.frame`
* `tf.compat.v2.signal.frame`
* `tf.contrib.signal.frame`
* `tf.signal.frame`

``` python
tf.signal.frame(
    signal,
    frame_length,
    frame_step,
    pad_end=False,
    pad_value=0,
    axis=-1,
    name=None
)
```



Defined in [`python/ops/signal/shape_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/signal/shape_ops.py).

<!-- Placeholder for "Used in" -->

Slides a window of size `frame_length` over `signal`'s `axis` dimension
with a stride of `frame_step`, replacing the `axis` dimension with
`[frames, frame_length]` frames.

If `pad_end` is True, window positions that are past the end of the `axis`
dimension are padded with `pad_value` until the window moves fully past the
end of the dimension. Otherwise, only window positions that fully overlap the
`axis` dimension are produced.

#### For example:



```python
pcm = tf.compat.v1.placeholder(tf.float32, [None, 9152])
frames = tf.signal.frame(pcm, 512, 180)
magspec = tf.abs(tf.signal.rfft(frames, [512]))
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


* <b>`ValueError`</b>: If `frame_length`, `frame_step`, `pad_value`, or `axis` are not
  scalar.