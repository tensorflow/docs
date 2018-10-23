

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.spectral.rfft2d

``` python
rfft2d(
    input_tensor,
    fft_length=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/spectral_ops.py).

See the guide: [Spectral Functions > Discrete Fourier Transforms](../../../../api_guides/python/spectral_ops#Discrete_Fourier_Transforms)

2D real-valued fast Fourier transform.

Computes the 2-dimensional discrete Fourier transform of a real-valued signal
over the inner-most 2 dimensions of `input`.

Since the DFT of a real signal is Hermitian-symmetric, `RFFT2D` only returns the
`fft_length / 2 + 1` unique components of the FFT for the inner-most dimension
of `output`: the zero-frequency term, followed by the `fft_length / 2`
positive-frequency terms.

Along each axis `RFFT2D` is computed on, if `fft_length` is smaller than the
corresponding dimension of `input`, the dimension is cropped. If it is larger,
the dimension is padded with zeros.

#### Args:

* <b>`input`</b>: A `Tensor` of type `float32`. A float32 tensor.
* <b>`fft_length`</b>: A `Tensor` of type `int32`.
    An int32 tensor of shape [2]. The FFT length for each dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `complex64`.
A complex64 tensor of the same rank as `input`. The inner-most 2
  dimensions of `input` are replaced with their 2D Fourier transform. The
  inner-most dimension contains `fft_length / 2 + 1` unique frequency
  components.



#### Numpy Compatibility
Equivalent to np.fft.rfft2

