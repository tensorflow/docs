page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.ifft3d

Inverse 3D fast Fourier transform.

### Aliases:

* `tf.compat.v1.ifft3d`
* `tf.compat.v1.signal.ifft3d`
* `tf.compat.v1.spectral.ifft3d`
* `tf.compat.v2.signal.ifft3d`
* `tf.ifft3d`
* `tf.signal.ifft3d`
* `tf.spectral.ifft3d`

``` python
tf.signal.ifft3d(
    input,
    name=None
)
```



Defined in generated file: `python/ops/gen_spectral_ops.py`.

<!-- Placeholder for "Used in" -->

Computes the inverse 3-dimensional discrete Fourier transform over the
inner-most 3 dimensions of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
