page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.image_gradients

``` python
tf.image.image_gradients(image)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/image_ops_impl.py).

Returns image gradients (dy, dx) for each color channel.

Both output tensors have the same shape as the input: [batch_size, h, w,
d]. The gradient values are organized so that [I(x+1, y) - I(x, y)] is in
location (x, y). That means that dy will always have zeros in the last row,
and dx will always have zeros in the last column.

#### Arguments:

* <b>`image`</b>: Tensor with shape [batch_size, h, w, d].


#### Returns:

Pair of tensors (dy, dx) holding the vertical and horizontal image
gradients (1-step finite difference).


#### Raises:

* <b>`ValueError`</b>: If `image` is not a 4D tensor.