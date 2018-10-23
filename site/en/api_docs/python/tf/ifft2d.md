

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.ifft2d

### Aliases:

* `tf.ifft2d`
* `tf.spectral.ifft2d`

``` python
tf.ifft2d(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_spectral_ops.py`.

See the guide: [Spectral Functions > Discrete Fourier Transforms](../../../api_guides/python/spectral_ops#Discrete_Fourier_Transforms)

Inverse 2D fast Fourier transform.

Computes the inverse 2-dimensional discrete Fourier transform over the
inner-most 2 dimensions of `input`.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `complex64`.