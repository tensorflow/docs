description: Computes the [Modified Discrete Cosine Transform][mdct] of signals.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.mdct" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.mdct

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/spectral_ops.py#L297-L370">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the [Modified Discrete Cosine Transform][mdct] of `signals`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.mdct`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.mdct(
    signals, frame_length, window_fn=tf.signal.vorbis_window, pad_end=(False),
    norm=None, name=None
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
An integer scalar `Tensor`. The window length in samples
which must be divisible by 4.
</td>
</tr><tr>
<td>
`window_fn`
</td>
<td>
A callable that takes a frame_length and a `dtype` keyword
argument and returns a `[frame_length]` `Tensor` of samples in the
provided datatype. If set to `None`, a rectangular window with a scale of
1/sqrt(2) is used. For perfect reconstruction of a signal from `mdct`
followed by `inverse_mdct`, please use <a href="../../tf/signal/vorbis_window.md"><code>tf.signal.vorbis_window</code></a>,
<a href="../../tf/signal/kaiser_bessel_derived_window.md"><code>tf.signal.kaiser_bessel_derived_window</code></a> or `None`. If using another
window function, make sure that w[n]^2 + w[n + frame_length // 2]^2 = 1
and w[n] = w[frame_length - n - 1] for n = 0,...,frame_length // 2 - 1 to
achieve perfect reconstruction.
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
`norm`
</td>
<td>
If it is None, unnormalized dct4 is used, if it is "ortho"
orthonormal dct4 is used.
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
A `[..., frames, frame_length // 2]` `Tensor` of `float32`/`float64`
MDCT values where `frames` is roughly `samples // (frame_length // 2)`
when `pad_end=False`.
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
not scalar, or `frame_length` is not a multiple of `4`.
</td>
</tr>
</table>


[mdct]: https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform