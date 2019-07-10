page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.matrices_to_flat_transforms

``` python
tf.contrib.image.matrices_to_flat_transforms(transform_matrices)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/image/python/ops/image_ops.py).

Converts affine matrices to <a href="../../../tf/contrib/image"><code>tf.contrib.image</code></a> projective transforms.

Note that we expect matrices that map output coordinates to input coordinates.
To convert forward transformation matrices, call <a href="../../../tf/matrix_inverse"><code>tf.linalg.inv</code></a> on the
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