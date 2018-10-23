

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.fft3d

### `tf.fft3d`
### `tf.spectral.fft3d`

``` python
fft3d(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_spectral_ops.py`.

See the guide: [Spectral Functions > Fourier Transform Functions](../../../api_guides/python/spectral_ops#Fourier_Transform_Functions)

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



#### numpy compatibility
  Equivalent to np.fft.fftn with 3 dimensions.

