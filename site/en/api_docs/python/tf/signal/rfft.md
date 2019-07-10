page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.rfft

Real-valued fast Fourier transform.

### Aliases:

* `tf.compat.v1.signal.rfft`
* `tf.compat.v1.spectral.rfft`
* `tf.compat.v2.signal.rfft`
* `tf.signal.rfft`
* `tf.spectral.rfft`

``` python
tf.signal.rfft(
    input_tensor,
    fft_length=None,
    name=None
)
```



Defined in [`python/ops/signal/fft_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/signal/fft_ops.py).

<!-- Placeholder for "Used in" -->

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
