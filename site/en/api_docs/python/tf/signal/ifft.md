page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.signal.ifft

### Aliases:

* `tf.ifft`
* `tf.signal.ifft`
* `tf.spectral.ifft`

``` python
tf.signal.ifft(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_spectral_ops.py`.

Inverse fast Fourier transform.

Computes the inverse 1-dimensional discrete Fourier transform over the
inner-most dimension of `input`.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    A complex tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.