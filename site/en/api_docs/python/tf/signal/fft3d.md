page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.fft3d


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_spectral_ops.py`



3D fast Fourier transform.

### Aliases:

* `tf.compat.v1.fft3d`
* `tf.compat.v1.signal.fft3d`
* `tf.compat.v1.spectral.fft3d`
* `tf.compat.v2.signal.fft3d`


``` python
tf.signal.fft3d(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Computes the 3-dimensional discrete Fourier transform over the inner-most 3
dimensions of `input`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
  A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
