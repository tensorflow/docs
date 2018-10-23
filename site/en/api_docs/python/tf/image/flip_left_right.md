


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.image.flip_left_right

### `tf.image.flip_left_right`

```
tf.image.flip_left_right(image)
```


See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Flip an image horizontally (left to right).

Outputs the contents of `image` flipped along the second dimension, which is
`width`.

See also `reverse()`.

#### Args:

* <b>`image`</b>: A 3-D tensor of shape `[height, width, channels].`


#### Returns:

  A 3-D tensor of the same type and shape as `image`.


#### Raises:

* <b>`ValueError`</b>: if the shape of `image` not supported.

Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.tensorflow.org/code/tensorflow/python/ops/image_ops_impl.py).

