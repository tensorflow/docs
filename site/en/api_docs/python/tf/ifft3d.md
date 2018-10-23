


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.ifft3d

### `tf.ifft3d`

```
tf.ifft3d(input, name=None)
```


See the guide: [Math > Fourier Transform Functions](../../../api_guides/python/math_ops#Fourier_Transform_Functions)

Compute the inverse 3-dimensional discrete Fourier Transform over the inner-most

3 dimensions of `input`.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `complex64`.
  A complex64 tensor of the same shape as `input`. The inner-most 3
    dimensions of `input` are replaced with their inverse 3D Fourier Transform.



#### numpy compatibility
  Equivalent to np.fft3



Defined in `tensorflow/python/ops/gen_math_ops.py`.

