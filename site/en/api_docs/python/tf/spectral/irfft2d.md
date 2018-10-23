

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.spectral.irfft2d

### `tf.spectral.irfft2d`

``` python
irfft2d(
    input_tensor,
    fft_length=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/spectral_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/spectral_ops.py).

See the guide: [Spectral Functions > Fourier Transform Functions](../../../../api_guides/python/spectral_ops#Fourier_Transform_Functions)

Inverse 2D real-valued fast Fourier transform.

Computes the inverse 2-dimensional discrete Fourier transform of a real-valued
signal over the inner-most 2 dimensions of `input`.

The inner-most 2 dimensions of `input` are assumed to be the result of `RFFT2D`:
The inner-most dimension contains the `fft_length / 2 + 1` unique components of
the DFT of a real-valued signal. If `fft_length` is not provided, it is computed
from the size of the inner-most 2 dimensions of `input`. If the FFT length used
to compute `input` is odd, it should be provided since it cannot be inferred
properly.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`fft_length`</b>: A `Tensor` of type `int32`.
    An int32 tensor of shape [2]. The FFT length for each dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `float32`.
  A float32 tensor of the same rank as `input`. The inner-most 2
    dimensions of `input` are replaced with the `fft_length` samples of their
    inverse 2D Fourier transform.



#### numpy compatibility
  Equivalent to np.fft.irfft2

