

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.image



Defined in [`tensorflow/contrib/image/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/image/__init__.py).

Ops for image manipulation.

### API

This module provides functions for image manipulation; currently, chrominance
transforms (including changing saturation and hue) in YIQ space and
projective transforms (including rotation) are supported.

## Image Transformation `Ops`


## Image Segmentation `Ops`


## Matching `Ops`


## Random Dot Stereogram `Ops`


## Functions

[`angles_to_projective_transforms(...)`](../../tf/contrib/image/angles_to_projective_transforms): Returns projective transform(s) for the given angle(s).

[`compose_transforms(...)`](../../tf/contrib/image/compose_transforms): Composes the transforms tensors.

[`connected_components(...)`](../../tf/contrib/image/connected_components): Labels the connected components in a batch of images.

[`dense_image_warp(...)`](../../tf/contrib/image/dense_image_warp): Image warping using per-pixel flow vectors.

[`flat_transforms_to_matrices(...)`](../../tf/contrib/image/flat_transforms_to_matrices): Converts <a href="../../tf/contrib/image"><code>tf.contrib.image</code></a> projective transforms to affine matrices.

[`interpolate_spline(...)`](../../tf/contrib/image/interpolate_spline): Interpolate signal using polyharmonic interpolation.

[`matrices_to_flat_transforms(...)`](../../tf/contrib/image/matrices_to_flat_transforms): Converts affine matrices to <a href="../../tf/contrib/image"><code>tf.contrib.image</code></a> projective transforms.

[`rotate(...)`](../../tf/contrib/image/rotate): Rotate image(s) counterclockwise by the passed angle(s) in radians.

[`single_image_random_dot_stereograms(...)`](../../tf/contrib/image/single_image_random_dot_stereograms): Output a RandomDotStereogram Tensor for export via encode_PNG/JPG OP.

[`sparse_image_warp(...)`](../../tf/contrib/image/sparse_image_warp): Image warping using correspondences between sparse control points.

[`transform(...)`](../../tf/contrib/image/transform): Applies the given transform(s) to the image(s).

[`translate(...)`](../../tf/contrib/image/translate): Translate image(s) by the passed vectors(s).

[`translations_to_projective_transforms(...)`](../../tf/contrib/image/translations_to_projective_transforms): Returns projective transform(s) for the given translation(s).

