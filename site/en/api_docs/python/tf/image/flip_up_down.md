

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.flip_up_down

``` python
tf.image.flip_up_down(image)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Flip an image vertically (upside down).

Outputs the contents of `image` flipped along the height dimension.

See also `reverse()`.

#### Args:

* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or
         3-D Tensor of shape `[height, width, channels]`.


#### Returns:

A tensor of the same type and shape as `image`.


#### Raises:

* <b>`ValueError`</b>: if the shape of `image` not supported.