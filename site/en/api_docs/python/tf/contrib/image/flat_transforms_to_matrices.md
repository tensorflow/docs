page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.flat_transforms_to_matrices


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/image/python/ops/image_ops.py#L334-L363">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts <a href="../../../tf/contrib/image"><code>tf.contrib.image</code></a> projective transforms to affine matrices.

``` python
tf.contrib.image.flat_transforms_to_matrices(transforms)
```



<!-- Placeholder for "Used in" -->

Note that the output matrices map output coordinates to input coordinates. For
the forward transformation matrix, call <a href="../../../tf/linalg/inv"><code>tf.linalg.inv</code></a> on the result.

#### Args:


* <b>`transforms`</b>: Vector of length 8, or batches of transforms with shape
  `(N, 8)`.


#### Returns:

3D tensor of matrices with shape `(N, 3, 3)`. The output matrices map the
  *output coordinates* (in homogeneous coordinates) of each transform to the
  corresponding *input coordinates*.



#### Raises:


* <b>`ValueError`</b>: If `transforms` have an invalid shape.
