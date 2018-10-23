

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.image.rot90

### `tf.image.rot90`

``` python
rot90(
    image,
    k=1,
    name=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Rotate an image counter-clockwise by 90 degrees.

#### Args:

* <b>`image`</b>: A 3-D tensor of shape `[height, width, channels]`.
* <b>`k`</b>: A scalar integer. The number of times the image is rotated by 90 degrees.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

  A rotated 3-D tensor of the same type and shape as `image`.