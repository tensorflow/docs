page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.linear_to_mel_weight_matrix


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/signal/mel_ops.py#L91-L213">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a matrix to warp linear scale spectrograms to the [mel scale][mel].

### Aliases:

* `tf.compat.v1.signal.linear_to_mel_weight_matrix`
* `tf.compat.v2.signal.linear_to_mel_weight_matrix`


``` python
tf.signal.linear_to_mel_weight_matrix(
    num_mel_bins=20,
    num_spectrogram_bins=129,
    sample_rate=8000,
    lower_edge_hertz=125.0,
    upper_edge_hertz=3800.0,
    dtype=tf.dtypes.float32,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Returns a weight matrix that can be used to re-weight a `Tensor` containing
`num_spectrogram_bins` linearly sampled frequency information from
`[0, sample_rate / 2]` into `num_mel_bins` frequency information from
`[lower_edge_hertz, upper_edge_hertz]` on the [mel scale][mel].

For example, the returned matrix `A` can be used to right-multiply a
spectrogram `S` of shape `[frames, num_spectrogram_bins]` of linear
scale spectrum values (e.g. STFT magnitudes) to generate a "mel spectrogram"
`M` of shape `[frames, num_mel_bins]`.

    # `S` has shape [frames, num_spectrogram_bins]
    # `M` has shape [frames, num_mel_bins]
    M = tf.matmul(S, A)

The matrix can be used with <a href="../../tf/tensordot"><code>tf.tensordot</code></a> to convert an arbitrary rank
`Tensor` of linear-scale spectral bins into the mel scale.

    # S has shape [..., num_spectrogram_bins].
    # M has shape [..., num_mel_bins].
    M = tf.tensordot(S, A, 1)
    # tf.tensordot does not support shape inference for this case yet.
    M.set_shape(S.shape[:-1].concatenate(A.shape[-1:]))

#### Args:


* <b>`num_mel_bins`</b>: Python int. How many bands in the resulting mel spectrum.
* <b>`num_spectrogram_bins`</b>: An integer `Tensor`. How many bins there are in the
  source spectrogram data, which is understood to be `fft_size // 2 + 1`,
  i.e. the spectrogram only contains the nonredundant FFT bins.
* <b>`sample_rate`</b>: Python float. Samples per second of the input signal used to
  create the spectrogram. We need this to figure out the actual frequencies
  for each spectrogram bin, which dictates how they are mapped into the mel
  scale.
* <b>`lower_edge_hertz`</b>: Python float. Lower bound on the frequencies to be
  included in the mel spectrum. This corresponds to the lower edge of the
  lowest triangular band.
* <b>`upper_edge_hertz`</b>: Python float. The desired top edge of the highest
  frequency band.
* <b>`dtype`</b>: The `DType` of the result matrix. Must be a floating point type.
* <b>`name`</b>: An optional name for the operation.


#### Returns:

A `Tensor` of shape `[num_spectrogram_bins, num_mel_bins]`.



#### Raises:


* <b>`ValueError`</b>: If `num_mel_bins`/`num_spectrogram_bins`/`sample_rate` are not
  positive, `lower_edge_hertz` is negative, frequency edges are incorrectly
  ordered, `upper_edge_hertz` is larger than the Nyquist frequency, or
  `sample_rate` is neither a Python float nor a constant Tensor.

[mel]: https://en.wikipedia.org/wiki/Mel_scale
