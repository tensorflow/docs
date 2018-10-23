

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.flip_up_down

``` python
flip_up_down(image)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Flip an image vertically (upside down).

Outputs the contents of `image` flipped along the first dimension, which is
`height`.

See also `reverse()`.

#### Args:

* <b>`image`</b>: A 3-D tensor of shape `[height, width, channels].`


#### Returns:

  A 3-D tensor of the same type and shape as `image`.


#### Raises:

* <b>`ValueError`</b>: if the shape of `image` not supported.