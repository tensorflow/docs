page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.matrices_to_flat_transforms

Converts affine matrices to <a href="../../../tf/contrib/image"><code>tf.contrib.image</code></a> projective transforms.

``` python
tf.contrib.image.matrices_to_flat_transforms(transform_matrices)
```



Defined in [`contrib/image/python/ops/image_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/image/python/ops/image_ops.py).

<!-- Placeholder for "Used in" -->

Note that we expect matrices that map output coordinates to input coordinates.
To convert forward transformation matrices, call <a href="../../../tf/linalg/inv"><code>tf.linalg.inv</code></a> on the
matrices and use the result here.

#### Args:


* <b>`transform_matrices`</b>: One or more affine transformation matrices, for the
  reverse transformation in homogeneous coordinates. Shape `(3, 3)` or
  `(N, 3, 3)`.


#### Returns:

2D tensor of flat transforms with shape `(N, 8)`, which may be passed into
  <a href="../../../tf/contrib/image/transform"><code>tf.contrib.image.transform</code></a>.



#### Raises:


* <b>`ValueError`</b>: If `transform_matrices` have an invalid shape.