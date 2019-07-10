page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.ifft2d

Inverse 2D fast Fourier transform.

### Aliases:

* `tf.compat.v1.ifft2d`
* `tf.compat.v1.signal.ifft2d`
* `tf.compat.v1.spectral.ifft2d`
* `tf.compat.v2.signal.ifft2d`
* `tf.ifft2d`
* `tf.signal.ifft2d`
* `tf.spectral.ifft2d`

``` python
tf.signal.ifft2d(
    input,
    name=None
)
```



Defined in generated file: `python/ops/gen_spectral_ops.py`.

<!-- Placeholder for "Used in" -->

Computes the inverse 2-dimensional discrete Fourier transform over the
inner-most 2 dimensions of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
