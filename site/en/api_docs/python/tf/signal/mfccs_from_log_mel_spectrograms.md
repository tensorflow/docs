description: Computes [MFCCs][mfcc] of log_mel_spectrograms.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal.mfccs_from_log_mel_spectrograms" />
<meta itemprop="path" content="Stable" />
</div>

# tf.signal.mfccs_from_log_mel_spectrograms

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/signal/mfcc_ops.py#L28-L109">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes [MFCCs][mfcc] of `log_mel_spectrograms`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.signal.mfccs_from_log_mel_spectrograms`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.signal.mfccs_from_log_mel_spectrograms(
    log_mel_spectrograms, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Implemented with GPU-compatible ops and supports gradients.

[Mel-Frequency Cepstral Coefficient (MFCC)][mfcc] calculation consists of
taking the DCT-II of a log-magnitude mel-scale spectrogram. [HTK][htk]'s MFCCs
use a particular scaling of the DCT-II which is almost orthogonal
normalization. We follow this convention.

All `num_mel_bins` MFCCs are returned and it is up to the caller to select
a subset of the MFCCs based on their application. For example, it is typical
to only use the first few for speech recognition, as this results in
an approximately pitch-invariant representation of the signal.

#### For example:



```python
batch_size, num_samples, sample_rate = 32, 32000, 16000.0
# A Tensor of [batch_size, num_samples] mono PCM samples in the range [-1, 1].
pcm = tf.random.normal([batch_size, num_samples], dtype=tf.float32)

# A 1024-point STFT with frames of 64 ms and 75% overlap.
stfts = tf.signal.stft(pcm, frame_length=1024, frame_step=256,
                       fft_length=1024)
spectrograms = tf.abs(stfts)

# Warp the linear scale spectrograms into the mel-scale.
num_spectrogram_bins = stfts.shape[-1].value
lower_edge_hertz, upper_edge_hertz, num_mel_bins = 80.0, 7600.0, 80
linear_to_mel_weight_matrix = tf.signal.linear_to_mel_weight_matrix(
  num_mel_bins, num_spectrogram_bins, sample_rate, lower_edge_hertz,
  upper_edge_hertz)
mel_spectrograms = tf.tensordot(
  spectrograms, linear_to_mel_weight_matrix, 1)
mel_spectrograms.set_shape(spectrograms.shape[:-1].concatenate(
  linear_to_mel_weight_matrix.shape[-1:]))

# Compute a stabilized log to get log-magnitude mel-scale spectrograms.
log_mel_spectrograms = tf.math.log(mel_spectrograms + 1e-6)

# Compute MFCCs from log_mel_spectrograms and take the first 13.
mfccs = tf.signal.mfccs_from_log_mel_spectrograms(
  log_mel_spectrograms)[..., :13]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`log_mel_spectrograms`
</td>
<td>
A `[..., num_mel_bins]` `float32`/`float64` `Tensor`
of log-magnitude mel-scale spectrograms.
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
A `[..., num_mel_bins]` `float32`/`float64` `Tensor` of the MFCCs of
`log_mel_spectrograms`.
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
If `num_mel_bins` is not positive.
</td>
</tr>
</table>


[mfcc]: https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
[htk]: https://en.wikipedia.org/wiki/HTK_(software)