page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.signal

Signal processing operations.

<!-- Placeholder for "Used in" -->

See the [tf.signal](https://tensorflow.org/api_guides/python/contrib.signal)
guide.


[hamming]: https://en.wikipedia.org/wiki/Window_function#Hamming_window
[hann]: https://en.wikipedia.org/wiki/Window_function#Hann_window
[mel]: https://en.wikipedia.org/wiki/Mel_scale
[mfcc]: https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
[stft]: https://en.wikipedia.org/wiki/Short-time_Fourier_transform

## Functions

[`dct(...)`](../../../tf/signal/dct): Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

[`fft(...)`](../../../tf/signal/fft): Fast Fourier transform.

[`fft2d(...)`](../../../tf/signal/fft2d): 2D fast Fourier transform.

[`fft3d(...)`](../../../tf/signal/fft3d): 3D fast Fourier transform.

[`frame(...)`](../../../tf/signal/frame): Expands `signal`'s `axis` dimension into frames of `frame_length`.

[`hamming_window(...)`](../../../tf/signal/hamming_window): Generate a [Hamming][hamming] window.

[`hann_window(...)`](../../../tf/signal/hann_window): Generate a [Hann window][hann].

[`idct(...)`](../../../tf/signal/idct): Computes the 1D [Inverse Discrete Cosine Transform (DCT)][idct] of `input`.

[`ifft(...)`](../../../tf/signal/ifft): Inverse fast Fourier transform.

[`ifft2d(...)`](../../../tf/signal/ifft2d): Inverse 2D fast Fourier transform.

[`ifft3d(...)`](../../../tf/signal/ifft3d): Inverse 3D fast Fourier transform.

[`inverse_stft(...)`](../../../tf/signal/inverse_stft): Computes the inverse [Short-time Fourier Transform][stft] of `stfts`.

[`inverse_stft_window_fn(...)`](../../../tf/signal/inverse_stft_window_fn): Generates a window function that can be used in `inverse_stft`.

[`irfft(...)`](../../../tf/signal/irfft): Inverse real-valued fast Fourier transform.

[`irfft2d(...)`](../../../tf/signal/irfft2d): Inverse 2D real-valued fast Fourier transform.

[`irfft3d(...)`](../../../tf/signal/irfft3d): Inverse 3D real-valued fast Fourier transform.

[`linear_to_mel_weight_matrix(...)`](../../../tf/signal/linear_to_mel_weight_matrix): Returns a matrix to warp linear scale spectrograms to the [mel scale][mel].

[`mfccs_from_log_mel_spectrograms(...)`](../../../tf/signal/mfccs_from_log_mel_spectrograms): Computes [MFCCs][mfcc] of `log_mel_spectrograms`.

[`overlap_and_add(...)`](../../../tf/signal/overlap_and_add): Reconstructs a signal from a framed representation.

[`rfft(...)`](../../../tf/signal/rfft): Real-valued fast Fourier transform.

[`rfft2d(...)`](../../../tf/signal/rfft2d): 2D real-valued fast Fourier transform.

[`rfft3d(...)`](../../../tf/signal/rfft3d): 3D real-valued fast Fourier transform.

[`stft(...)`](../../../tf/signal/stft): Computes the [Short-time Fourier Transform][stft] of `signals`.

