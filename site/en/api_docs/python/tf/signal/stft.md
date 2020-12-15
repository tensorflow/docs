description: Computes the [Short-time Fourier Transform][stft] of signals.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.stft" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.stft

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/signal/spectral_ops.py#L38-L96">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the [Short-time Fourier Transform][stft] of `signals`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.stft`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.stft(
    signals, frame_length, frame_step, fft_length=None,
    window_fn=tf.signal.hann_window, pad_end=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Implemented with TPU/GPU-compatible ops and supports gradients.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`signals`
</td>
<td>
A `[..., samples]` `float32`/`float64` `Tensor` of real-valued
signals.
</td>
</tr><tr>
<td>
`frame_length`
</td>
<td>
An integer scalar `Tensor`. The window length in samples.
</td>
</tr><tr>
<td>
`frame_step`
</td>
<td>
An integer scalar `Tensor`. The number of samples to step.
</td>
</tr><tr>
<td>
`fft_length`
</td>
<td>
An integer scalar `Tensor`. The size of the FFT to apply.
If not provided, uses the smallest power of 2 enclosing `frame_length`.
</td>
</tr><tr>
<td>
`window_fn`
</td>
<td>
A callable that takes a window length and a `dtype` keyword
argument and returns a `[window_length]` `Tensor` of samples in the
provided datatype. If set to `None`, no windowing is used.
</td>
</tr><tr>
<td>
`pad_end`
</td>
<td>
Whether to pad the end of `signals` with zeros when the provided
frame length and step produces a frame that lies partially past its end.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `[..., frames, fft_unique_bins]` `Tensor` of `complex64`/`complex128`
STFT values where `fft_unique_bins` is `fft_length // 2 + 1` (the unique
components of the FFT).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `signals` is not at least rank 1, `frame_length` is
not scalar, or `frame_step` is not scalar.
</td>
</tr>
</table>


[stft]: https://en.wikipedia.org/wiki/Short-time_Fourier_transform