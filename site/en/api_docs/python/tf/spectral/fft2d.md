page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.spectral.fft2d

### Aliases:

* `tf.fft2d`
* `tf.spectral.fft2d`

``` python
tf.spectral.fft2d(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_spectral_ops.py`.

2D fast Fourier transform.

Computes the 2-dimensional discrete Fourier transform over the inner-most
2 dimensions of `input`.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.