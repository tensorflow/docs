description: Signal processing operations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.signal" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.signal

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Signal processing operations.


See the [tf.signal](https://tensorflow.org/api_guides/python/contrib.signal)
guide.


[hamming]: https://en.wikipedia.org/wiki/Window_function#Hamming_window
[hann]: https://en.wikipedia.org/wiki/Window_function#Hann_window
[mel]: https://en.wikipedia.org/wiki/Mel_scale
[mfcc]: https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
[stft]: https://en.wikipedia.org/wiki/Short-time_Fourier_transform

## Functions

[`dct(...)`](../tf/signal/dct.md): Computes the 1D [Discrete Cosine Transform (DCT)][dct] of `input`.

[`fft(...)`](../tf/signal/fft.md): Fast Fourier transform.

[`fft2d(...)`](../tf/signal/fft2d.md): 2D fast Fourier transform.

[`fft3d(...)`](../tf/signal/fft3d.md): 3D fast Fourier transform.

[`fftshift(...)`](../tf/signal/fftshift.md): Shift the zero-frequency component to the center of the spectrum.

[`frame(...)`](../tf/signal/frame.md): Expands `signal`'s `axis` dimension into frames of `frame_length`.

[`hamming_window(...)`](../tf/signal/hamming_window.md): Generate a [Hamming][hamming] window.

[`hann_window(...)`](../tf/signal/hann_window.md): Generate a [Hann window][hann].

[`idct(...)`](../tf/signal/idct.md): Computes the 1D [Inverse Discrete Cosine Transform (DCT)][idct] of `input`.

[`ifft(...)`](../tf/signal/ifft.md): Inverse fast Fourier transform.

[`ifft2d(...)`](../tf/signal/ifft2d.md): Inverse 2D fast Fourier transform.

[`ifft3d(...)`](../tf/signal/ifft3d.md): Inverse 3D fast Fourier transform.

[`ifftshift(...)`](../tf/signal/ifftshift.md): The inverse of fftshift.

[`inverse_mdct(...)`](../tf/signal/inverse_mdct.md): Computes the inverse modified DCT of `mdcts`.

[`inverse_stft(...)`](../tf/signal/inverse_stft.md): Computes the inverse [Short-time Fourier Transform][stft] of `stfts`.

[`inverse_stft_window_fn(...)`](../tf/signal/inverse_stft_window_fn.md): Generates a window function that can be used in `inverse_stft`.

[`irfft(...)`](../tf/signal/irfft.md): Inverse real-valued fast Fourier transform.

[`irfft2d(...)`](../tf/signal/irfft2d.md): Inverse 2D real-valued fast Fourier transform.

[`irfft3d(...)`](../tf/signal/irfft3d.md): Inverse 3D real-valued fast Fourier transform.

[`kaiser_bessel_derived_window(...)`](../tf/signal/kaiser_bessel_derived_window.md): Generate a [Kaiser Bessel derived window][kbd].

[`kaiser_window(...)`](../tf/signal/kaiser_window.md): Generate a [Kaiser window][kaiser].

[`linear_to_mel_weight_matrix(...)`](../tf/signal/linear_to_mel_weight_matrix.md): Returns a matrix to warp linear scale spectrograms to the [mel scale][mel].

[`mdct(...)`](../tf/signal/mdct.md): Computes the [Modified Discrete Cosine Transform][mdct] of `signals`.

[`mfccs_from_log_mel_spectrograms(...)`](../tf/signal/mfccs_from_log_mel_spectrograms.md): Computes [MFCCs][mfcc] of `log_mel_spectrograms`.

[`overlap_and_add(...)`](../tf/signal/overlap_and_add.md): Reconstructs a signal from a framed representation.

[`rfft(...)`](../tf/signal/rfft.md): Real-valued fast Fourier transform.

[`rfft2d(...)`](../tf/signal/rfft2d.md): 2D real-valued fast Fourier transform.

[`rfft3d(...)`](../tf/signal/rfft3d.md): 3D real-valued fast Fourier transform.

[`stft(...)`](../tf/signal/stft.md): Computes the [Short-time Fourier Transform][stft] of `signals`.

[`vorbis_window(...)`](../tf/signal/vorbis_window.md): Generate a [Vorbis power complementary window][vorbis].

