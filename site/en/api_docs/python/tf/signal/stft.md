page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.stft

### Aliases:

* `tf.contrib.signal.stft`
* `tf.signal.stft`

``` python
tf.signal.stft(
    signals,
    frame_length,
    frame_step,
    fft_length=None,
    window_fn=tf.signal.hann_window,
    pad_end=False,
    name=None
)
```



Defined in [`tensorflow/python/ops/signal/spectral_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/signal/spectral_ops.py).

Computes the [Short-time Fourier Transform][stft] of `signals`.

Implemented with GPU-compatible ops and supports gradients.

#### Args:

* <b>`signals`</b>: A `[..., samples]` `float32` `Tensor` of real-valued signals.
* <b>`frame_length`</b>: An integer scalar `Tensor`. The window length in samples.
* <b>`frame_step`</b>: An integer scalar `Tensor`. The number of samples to step.
* <b>`fft_length`</b>: An integer scalar `Tensor`. The size of the FFT to apply.
    If not provided, uses the smallest power of 2 enclosing `frame_length`.
* <b>`window_fn`</b>: A callable that takes a window length and a `dtype` keyword
    argument and returns a `[window_length]` `Tensor` of samples in the
    provided datatype. If set to `None`, no windowing is used.
* <b>`pad_end`</b>: Whether to pad the end of `signals` with zeros when the provided
    frame length and step produces a frame that lies partially past its end.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `[..., frames, fft_unique_bins]` `Tensor` of `complex64` STFT values where
`fft_unique_bins` is `fft_length // 2 + 1` (the unique components of the
FFT).


#### Raises:

* <b>`ValueError`</b>: If `signals` is not at least rank 1, `frame_length` is
    not scalar, or `frame_step` is not scalar.

[stft]: https://en.wikipedia.org/wiki/Short-time_Fourier_transform