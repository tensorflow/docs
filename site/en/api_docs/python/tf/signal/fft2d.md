page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.fft2d

2D fast Fourier transform.

### Aliases:

* `tf.compat.v1.fft2d`
* `tf.compat.v1.signal.fft2d`
* `tf.compat.v1.spectral.fft2d`
* `tf.compat.v2.signal.fft2d`
* `tf.fft2d`
* `tf.signal.fft2d`
* `tf.spectral.fft2d`

``` python
tf.signal.fft2d(
    input,
    name=None
)
```



Defined in generated file: `python/ops/gen_spectral_ops.py`.

<!-- Placeholder for "Used in" -->

Computes the 2-dimensional discrete Fourier transform over the inner-most
2 dimensions of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
