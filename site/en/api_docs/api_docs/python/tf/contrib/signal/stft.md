

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.signal.stft

``` python
stft(
    signal,
    frame_length,
    frame_step,
    fft_length=None,
    window_fn=functools.partial(window_ops.hann_window, periodic=True),
    pad_end=False,
    name=None
)
```



Defined in [`tensorflow/contrib/signal/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/signal/python/ops/spectral_ops.py).

Computes the Short-time Fourier Transform of a batch of real signals.

https://en.wikipedia.org/wiki/Short-time_Fourier_transform

Implemented with GPU-compatible ops and supports gradients.

#### Args:

* <b>`signal`</b>: A `[..., samples]` `float32` `Tensor` of real-valued signals.
* <b>`frame_length`</b>: An integer scalar `Tensor`. The window length in samples.
* <b>`frame_step`</b>: An integer scalar `Tensor`. The number of samples to step.
* <b>`fft_length`</b>: An integer scalar `Tensor`. The size of the FFT to apply.
    If not provided, uses the smallest power of 2 enclosing `frame_length`.
* <b>`window_fn`</b>: A callable that takes a window length and a `dtype` keyword
    argument and returns a `[window_length]` `Tensor` of samples in the
    provided datatype. If set to `None`, no windowing is used.
* <b>`pad_end`</b>: Whether to pad the end of signal with zeros when the provided
    frame length and step produces a frame that lies partially past the end
    of `signal`.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

  A `[..., frames, fft_unique_bins]` `Tensor` of `complex64` STFT values where
  `fft_unique_bins` is `fft_length / 2 + 1` (the unique components of the
  FFT).


#### Raises:

* <b>`ValueError`</b>: If `signal` is not at least rank 1, `frame_length` is
    not scalar, `frame_step` is not scalar, or `frame_length`
    is greater than `fft_length`.