

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.fft2d

### `tf.fft2d`
### `tf.spectral.fft2d`

``` python
fft2d(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_spectral_ops.py`.

See the guide: [Spectral Functions > Fourier Transform Functions](../../../api_guides/python/spectral_ops#Fourier_Transform_Functions)

Compute the 2-dimensional discrete Fourier Transform over the inner-most

2 dimensions of `input`.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `complex64`.
  A complex64 tensor of the same shape as `input`. The inner-most 2
    dimensions of `input` are replaced with their 2D Fourier Transform.



#### numpy compatibility
  Equivalent to np.fft.fft2

