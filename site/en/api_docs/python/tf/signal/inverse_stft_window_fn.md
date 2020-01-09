page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.inverse_stft_window_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/signal/inverse_stft_window_fn">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/signal/spectral_ops.py#L95-L153">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Generates a window function that can be used in `inverse_stft`.

### Aliases:

* <a href="/api_docs/python/tf/signal/inverse_stft_window_fn"><code>tf.compat.v1.signal.inverse_stft_window_fn</code></a>
* <a href="/api_docs/python/tf/signal/inverse_stft_window_fn"><code>tf.compat.v2.signal.inverse_stft_window_fn</code></a>
* <a href="/api_docs/python/tf/signal/inverse_stft_window_fn"><code>tf.contrib.signal.inverse_stft_window_fn</code></a>


``` python
tf.signal.inverse_stft_window_fn(
    frame_step,
    forward_window_fn=tf.signal.hann_window,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
