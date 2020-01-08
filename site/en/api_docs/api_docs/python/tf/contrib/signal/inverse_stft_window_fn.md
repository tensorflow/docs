

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.signal.inverse_stft_window_fn

``` python
tf.contrib.signal.inverse_stft_window_fn(
    frame_step,
    forward_window_fn=functools.partial(window_ops.hann_window, periodic=True),
    name=None
)
```



Defined in [`tensorflow/contrib/signal/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/signal/python/ops/spectral_ops.py).

Generates a window function that can be used in `inverse_stft`.

Constructs a window that is equal to the forward window with a further
pointwise amplitude correction.  `inverse_stft_window_fn` is equivalent to
`forward_window_fn` in the case where it would produce an exact inverse.

See examples in `inverse_stft` documentation for usage.

#### Args:

* <b>`frame_step`</b>: An integer scalar `Tensor`. The number of samples to step.
* <b>`forward_window_fn`</b>: window_fn used in the forward transform, `stft`.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A callable that takes a window length and a `dtype` keyword argument and
  returns a `[window_length]` `Tensor` of samples in the provided datatype.
  The returned window is suitable for reconstructing original waveform in
  inverse_stft.