

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.spectral.rfft

``` python
rfft(
    input_tensor,
    fft_length=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/spectral_ops.py).

See the guide: [Spectral Functions > Fourier Transform Functions](../../../../api_guides/python/spectral_ops#Fourier_Transform_Functions)

Real-valued fast Fourier transform.

Computes the 1-dimensional discrete Fourier transform of a real-valued signal
over the inner-most dimension of `input`.

Since the DFT of a real signal is Hermitian-symmetric, `RFFT` only returns the
`fft_length / 2 + 1` unique components of the FFT: the zero-frequency term,
followed by the `fft_length / 2` positive-frequency terms.

Along the axis `RFFT` is computed on, if `fft_length` is smaller than the
corresponding dimension of `input`, the dimension is cropped. If it is larger,
the dimension is padded with zeros.

#### Args:

* <b>`input`</b>: A `Tensor` of type `float32`. A float32 tensor.
* <b>`fft_length`</b>: A `Tensor` of type `int32`.
    An int32 tensor of shape [1]. The FFT length.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `complex64`.
  A complex64 tensor of the same rank as `input`. The inner-most
    dimension of `input` is replaced with the `fft_length / 2 + 1` unique
    frequency components of its 1D Fourier transform.



#### numpy compatibility
  Equivalent to np.fft.rfft

