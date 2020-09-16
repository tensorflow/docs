description: Generates a window function that can be used in inverse_stft.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.inverse_stft_window_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.inverse_stft_window_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/spectral_ops.py#L99-L158">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates a window function that can be used in `inverse_stft`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.inverse_stft_window_fn`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.inverse_stft_window_fn(
    frame_step, forward_window_fn=tf.signal.hann_window, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Constructs a window that is equal to the forward window with a further
pointwise amplitude correction.  `inverse_stft_window_fn` is equivalent to
`forward_window_fn` in the case where it would produce an exact inverse.

See examples in `inverse_stft` documentation for usage.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`frame_step`
</td>
<td>
An integer scalar `Tensor`. The number of samples to step.
</td>
</tr><tr>
<td>
`forward_window_fn`
</td>
<td>
window_fn used in the forward transform, `stft`.
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
A callable that takes a window length and a `dtype` keyword argument and
returns a `[window_length]` `Tensor` of samples in the provided datatype.
The returned window is suitable for reconstructing original waveform in
inverse_stft.
</td>
</tr>

</table>

