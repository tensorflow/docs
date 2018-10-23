

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.fft3d

### Aliases:

* `tf.fft3d`
* `tf.spectral.fft3d`

``` python
fft3d(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_spectral_ops.py`.

See the guide: [Spectral Functions > Discrete Fourier Transforms](../../../api_guides/python/spectral_ops#Discrete_Fourier_Transforms)

3D fast Fourier transform.

Computes the 3-dimensional discrete Fourier transform over the inner-most 3
dimensions of `input`.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `complex64`.
A complex64 tensor of the same shape as `input`. The inner-most 3
  dimensions of `input` are replaced with their 3D Fourier transform.



#### Numpy Compatibility
Equivalent to np.fft.fftn with 3 dimensions.

