

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.spectral.irfft

### `tf.spectral.irfft`

``` python
irfft(
    input_tensor,
    fft_length=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/spectral_ops.py).

See the guide: [Spectral Functions > Fourier Transform Functions](../../../../api_guides/python/spectral_ops#Fourier_Transform_Functions)

Compute the inverse 1-dimensional discrete Fourier Transform of a real-valued

signal over the inner-most dimension of `input`.

The inner-most dimension of `input` is assumed to be the result of `RFFT`: the
`fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If
`fft_length` is not provided, it is computed from the size of the inner-most
dimension of `input` (`fft_length = 2 * (inner - 1)`). If the FFT length used to
compute `input` is odd, it should be provided since it cannot be inferred
properly.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`fft_length`</b>: A `Tensor` of type `int32`.
    An int32 tensor of shape [1]. The FFT length.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `float32`.
  A float32 tensor of the same rank as `input`. The inner-most
    dimension of `input` is replaced with the `fft_length` samples of its inverse
    1D Fourier Transform.



#### numpy compatibility
  Equivalent to np.fft.irfft

