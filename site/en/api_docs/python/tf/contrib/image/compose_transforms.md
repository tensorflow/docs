

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.image.compose_transforms

### `tf.contrib.image.compose_transforms`

``` python
compose_transforms(*transforms)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/image/python/ops/image_ops.py).

Composes the transforms tensors.

#### Args:

  *transforms: List of image projective transforms to be composed. Each
      transform is length 8 (single transform) or shape (N, 8) (batched
      transforms). The shapes of all inputs must be equal, and at least one
      input must be given.


#### Returns:

  A composed transform tensor. When passed to `tf.contrib.image.transform`,
      equivalent to applying each of the given transforms to the image in
      order.