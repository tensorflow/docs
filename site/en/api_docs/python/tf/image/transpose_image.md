page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.transpose_image

``` python
tf.image.transpose_image(image)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Transpose image(s) by swapping the height and width dimension.

See also `transpose()`.

#### Args:

* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or
         3-D Tensor of shape `[height, width, channels]`.


#### Returns:

 If `image` was 4-D, a 4-D float Tensor of shape
`[batch, width, height, channels]`
 If `image` was 3-D, a 3-D float Tensor of shape
`[width, height, channels]`


#### Raises:

* <b>`ValueError`</b>: if the shape of `image` not supported.