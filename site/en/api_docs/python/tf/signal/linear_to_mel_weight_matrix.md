description: Returns a matrix to warp linear scale spectrograms to the [mel scale][mel].

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.linear_to_mel_weight_matrix" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.linear_to_mel_weight_matrix

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/signal/mel_ops.py#L93-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a matrix to warp linear scale spectrograms to the [mel scale][mel].

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.linear_to_mel_weight_matrix`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.linear_to_mel_weight_matrix(
    num_mel_bins=20, num_spectrogram_bins=129, sample_rate=8000,
    lower_edge_hertz=125.0, upper_edge_hertz=3800.0, dtype=tf.dtypes.float32,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a weight matrix that can be used to re-weight a `Tensor` containing
`num_spectrogram_bins` linearly sampled frequency information from
`[0, sample_rate / 2]` into `num_mel_bins` frequency information from
`[lower_edge_hertz, upper_edge_hertz]` on the [mel scale][mel].

This function follows the [Hidden Markov Model Toolkit
(HTK)](http://htk.eng.cam.ac.uk/) convention, defining the mel scale in
terms of a frequency in hertz according to the following formula:

    $$        extrm{mel}(f) = 2595 *  extrm{log}_{10}(1 + 
rac{f}{700})$$

In the returned matrix, all the triangles (filterbanks) have a peak value
of 1.0.

For example, the returned matrix `A` can be used to right-multiply a
spectrogram `S` of shape `[frames, num_spectrogram_bins]` of linear
scale spectrum values (e.g. STFT magnitudes) to generate a "mel spectrogram"
`M` of shape `[frames, num_mel_bins]`.

    # `S` has shape [frames, num_spectrogram_bins]
    # `M` has shape [frames, num_mel_bins]
    M = tf.matmul(S, A)

The matrix can be used with <a href="../../tf/tensordot.md"><code>tf.tensordot</code></a> to convert an arbitrary rank
`Tensor` of linear-scale spectral bins into the mel scale.

    # S has shape [..., num_spectrogram_bins].
    # M has shape [..., num_mel_bins].
    M = tf.tensordot(S, A, 1)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_mel_bins`
</td>
<td>
Python int. How many bands in the resulting mel spectrum.
</td>
</tr><tr>
<td>
`num_spectrogram_bins`
</td>
<td>
An integer `Tensor`. How many bins there are in the
source spectrogram data, which is understood to be `fft_size // 2 + 1`,
i.e. the spectrogram only contains the nonredundant FFT bins.
</td>
</tr><tr>
<td>
`sample_rate`
</td>
<td>
An integer or float `Tensor`. Samples per second of the input
signal used to create the spectrogram. Used to figure out the frequencies
corresponding to each spectrogram bin, which dictates how they are mapped
into the mel scale.
</td>
</tr><tr>
<td>
`lower_edge_hertz`
</td>
<td>
Python float. Lower bound on the frequencies to be
included in the mel spectrum. This corresponds to the lower edge of the
lowest triangular band.
</td>
</tr><tr>
<td>
`upper_edge_hertz`
</td>
<td>
Python float. The desired top edge of the highest
frequency band.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The `DType` of the result matrix. Must be a floating point type.
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
A `Tensor` of shape `[num_spectrogram_bins, num_mel_bins]`.
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
If `num_mel_bins`/`num_spectrogram_bins`/`sample_rate` are not
positive, `lower_edge_hertz` is negative, frequency edges are incorrectly
ordered, `upper_edge_hertz` is larger than the Nyquist frequency.
</td>
</tr>
</table>


[mel]: https://en.wikipedia.org/wiki/Mel_scale