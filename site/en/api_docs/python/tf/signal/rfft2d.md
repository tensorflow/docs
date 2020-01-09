page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.rfft2d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/signal/fft_ops.py#L114-L125">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



2D real-valued fast Fourier transform.

### Aliases:

* `tf.compat.v1.signal.rfft2d`
* `tf.compat.v1.spectral.rfft2d`
* `tf.compat.v2.signal.rfft2d`


``` python
tf.signal.rfft2d(
    input_tensor,
    fft_length=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
