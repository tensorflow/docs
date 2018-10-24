

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.sparse_image_warp

``` python
tf.contrib.image.sparse_image_warp(
    image,
    source_control_point_locations,
    dest_control_point_locations,
    interpolation_order=2,
    regularization_weight=0.0,
    num_boundary_points=0,
    name='sparse_image_warp'
)
```



Defined in [`tensorflow/contrib/image/python/ops/sparse_image_warp.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/image/python/ops/sparse_image_warp.py).

Image warping using correspondences between sparse control points.

Apply a non-linear warp to the image, where the warp is specified by
the source and destination locations of a (potentially small) number of
control points. First, we use a polyharmonic spline
(<a href="../../../tf/contrib/image/interpolate_spline"><code>tf.contrib.image.interpolate_spline</code></a>) to interpolate the displacements
between the corresponding control points to a dense flow field.
Then, we warp the image using this dense flow field
(<a href="../../../tf/contrib/image/dense_image_warp"><code>tf.contrib.image.dense_image_warp</code></a>).

Let t index our control points. For regularization_weight=0, we have:
warped_image[b, dest_control_point_locations[b, t, 0],
                dest_control_point_locations[b, t, 1], :] =
image[b, source_control_point_locations[b, t, 0],
         source_control_point_locations[b, t, 1], :].

For regularization_weight > 0, this condition is met approximately, since
regularized interpolation trades off smoothness of the interpolant vs.
reconstruction of the interpolant at the control points.
See <a href="../../../tf/contrib/image/interpolate_spline"><code>tf.contrib.image.interpolate_spline</code></a> for further documentation of the
interpolation_order and regularization_weight arguments.


#### Args:

* <b>`image`</b>: `[batch, height, width, channels]` float `Tensor`
* <b>`source_control_point_locations`</b>: `[batch, num_control_points, 2]` float
    `Tensor`
* <b>`dest_control_point_locations`</b>: `[batch, num_control_points, 2]` float
    `Tensor`
* <b>`interpolation_order`</b>: polynomial order used by the spline interpolation
* <b>`regularization_weight`</b>: weight on smoothness regularizer in interpolation
* <b>`num_boundary_points`</b>: How many zero-flow boundary points to include at
    each image edge.Usage:
      num_boundary_points=0: don't add zero-flow points
      num_boundary_points=1: 4 corners of the image
      num_boundary_points=2: 4 corners and one in the middle of each edge
        (8 points total)
      num_boundary_points=n: 4 corners and n-1 along each edge
* <b>`name`</b>: A name for the operation (optional).

  Note that image and offsets can be of type tf.half, tf.float32, or
  tf.float64, and do not necessarily have to be the same type.


#### Returns:

* <b>`warped_image`</b>: `[batch, height, width, channels]` float `Tensor` with same
    type as input image.
* <b>`flow_field`</b>: `[batch, height, width, 2]` float `Tensor` containing the dense
    flow field produced by the interpolation.