description: Computes the inverse modified DCT of mdcts.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.inverse_mdct" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.inverse_mdct

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/spectral_ops.py#L373-L455">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the inverse modified DCT of `mdcts`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.inverse_mdct`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.inverse_mdct(
    mdcts, window_fn=tf.signal.vorbis_window, norm=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

To reconstruct an original waveform, the same window function should
be used with `mdct` and `inverse_mdct`.

#### Example usage:



```
>>> @tf.function
... def compare_round_trip():
...   samples = 1000
...   frame_length = 400
...   halflen = frame_length // 2
...   waveform = tf.random.normal(dtype=tf.float32, shape=[samples])
...   waveform_pad = tf.pad(waveform, [[halflen, 0],])
...   mdct = tf.signal.mdct(waveform_pad, frame_length, pad_end=True,
...                         window_fn=tf.signal.vorbis_window)
...   inverse_mdct = tf.signal.inverse_mdct(mdct,
...                                         window_fn=tf.signal.vorbis_window)
...   inverse_mdct = inverse_mdct[halflen: halflen + samples]
...   return waveform, inverse_mdct
>>> waveform, inverse_mdct = compare_round_trip()
>>> np.allclose(waveform.numpy(), inverse_mdct.numpy(), rtol=1e-3, atol=1e-4)
True
```

Implemented with TPU/GPU-compatible ops and supports gradients.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`mdcts`
</td>
<td>
A `float32`/`float64` `[..., frames, frame_length // 2]`
`Tensor` of MDCT bins representing a batch of `frame_length // 2`-point
MDCTs.
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
`norm`
</td>
<td>
If "ortho", orthonormal inverse DCT4 is performed, if it is None,
a regular dct4 followed by scaling of `1/frame_length` is performed.
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
A `[..., samples]` `Tensor` of `float32`/`float64` signals representing
the inverse MDCT for each input MDCT in `mdcts` where `samples` is
`(frames - 1) * (frame_length // 2) + frame_length`.
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
If `mdcts` is not at least rank 2.
</td>
</tr>
</table>


[mdct]: https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform