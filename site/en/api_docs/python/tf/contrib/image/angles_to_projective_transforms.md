

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.image.angles_to_projective_transforms

### `tf.contrib.image.angles_to_projective_transforms`

``` python
angles_to_projective_transforms(
    angles,
    image_height,
    image_width
)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/image/python/ops/image_ops.py).

Returns projective transform(s) for the given angle(s).

#### Args:

* <b>`angles`</b>: A scalar angle to rotate all images by, or (for batches of images)
    a vector with an angle to rotate each image in the batch.
* <b>`image_height`</b>: Height of the image(s) to be transformed.
* <b>`image_width`</b>: Width of the image(s) to be transformed.


#### Returns:

  A tensor of shape (num_images, 8). Projective transforms which can be given
    to `tf.contrib.image.transform`.