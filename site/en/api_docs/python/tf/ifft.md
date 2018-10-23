


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.ifft

### `tf.ifft`

```
tf.ifft(input, name=None)
```


See the guide: [Math > Fourier Transform Functions](../../../api_guides/python/math_ops#Fourier_Transform_Functions)

Compute the inverse 1-dimensional discrete Fourier Transform over the inner-most

dimension of `input`.

#### Args:

* <b>`input`</b>: A `Tensor` of type `complex64`. A complex64 tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `complex64`.
  A complex64 tensor of the same shape as `input`. The inner-most
  dimension of `input` is replaced with its inverse 1D Fourier Transform.

Defined in `tensorflow/python/ops/gen_math_ops.py`.

