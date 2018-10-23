

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.fft

### Aliases:

* `tf.fft`
* `tf.spectral.fft`

``` python
tf.fft(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_spectral_ops.py`.

See the guide: [Spectral Functions > Discrete Fourier Transforms](../../../api_guides/python/spectral_ops#Discrete_Fourier_Transforms)

Fast Fourier transform.

Computes the 1-dimensional discrete Fourier transform over the inner-most
dimension of `input`.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `complex64`.