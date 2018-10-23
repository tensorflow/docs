

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.bayesflow.layers



Defined in [`tensorflow/contrib/bayesflow/python/ops/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/layers.py).

Probabilistic neural layers.

See ${python/contrib.bayesflow.layers}.

## Classes

[`class Conv1DFlipout`](../../../tf/contrib/bayesflow/layers/Conv1DFlipout): 1D convolution layer (e.g. temporal convolution) with Flipout.

[`class Conv1DReparameterization`](../../../tf/contrib/bayesflow/layers/Conv1DReparameterization): 1D convolution layer (e.g. temporal convolution).

[`class Conv2DFlipout`](../../../tf/contrib/bayesflow/layers/Conv2DFlipout): 2D convolution layer (e.g. spatial convolution over images) with Flipout.

[`class Conv2DReparameterization`](../../../tf/contrib/bayesflow/layers/Conv2DReparameterization): 2D convolution layer (e.g. spatial convolution over images).

[`class Conv3DFlipout`](../../../tf/contrib/bayesflow/layers/Conv3DFlipout): 3D convolution layer (e.g. spatial convolution over volumes) with Flipout.

[`class Conv3DReparameterization`](../../../tf/contrib/bayesflow/layers/Conv3DReparameterization): 3D convolution layer (e.g. spatial convolution over volumes).

[`class Convolution1DFlipout`](../../../tf/contrib/bayesflow/layers/Conv1DFlipout): 1D convolution layer (e.g. temporal convolution) with Flipout.

[`class Convolution1DReparameterization`](../../../tf/contrib/bayesflow/layers/Conv1DReparameterization): 1D convolution layer (e.g. temporal convolution).

[`class Convolution2DFlipout`](../../../tf/contrib/bayesflow/layers/Conv2DFlipout): 2D convolution layer (e.g. spatial convolution over images) with Flipout.

[`class Convolution2DReparameterization`](../../../tf/contrib/bayesflow/layers/Conv2DReparameterization): 2D convolution layer (e.g. spatial convolution over images).

[`class Convolution3DFlipout`](../../../tf/contrib/bayesflow/layers/Conv3DFlipout): 3D convolution layer (e.g. spatial convolution over volumes) with Flipout.

[`class Convolution3DReparameterization`](../../../tf/contrib/bayesflow/layers/Conv3DReparameterization): 3D convolution layer (e.g. spatial convolution over volumes).

[`class DenseFlipout`](../../../tf/contrib/bayesflow/layers/DenseFlipout): Densely-connected layer class with Flipout estimator.

[`class DenseLocalReparameterization`](../../../tf/contrib/bayesflow/layers/DenseLocalReparameterization): Densely-connected layer class with local reparameterization estimator.

[`class DenseReparameterization`](../../../tf/contrib/bayesflow/layers/DenseReparameterization): Densely-connected layer class with reparameterization estimator.

## Functions

[`conv1d_flipout(...)`](../../../tf/contrib/bayesflow/layers/conv1d_flipout): Functional interface for 1D convolution layer (e.g. temporal convolution).

[`conv1d_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/conv1d_reparameterization): Functional interface for 1D convolution layer (e.g. temporal convolution).

[`conv2d_flipout(...)`](../../../tf/contrib/bayesflow/layers/conv2d_flipout): Functional interface for the 2D convolution layer.

[`conv2d_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/conv2d_reparameterization): Functional interface for the 2D convolution layer.

[`conv3d_flipout(...)`](../../../tf/contrib/bayesflow/layers/conv3d_flipout): Functional interface for the 3D convolution layer.

[`conv3d_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/conv3d_reparameterization): Functional interface for the 3D convolution layer.

[`convolution1d_flipout(...)`](../../../tf/contrib/bayesflow/layers/conv1d_flipout): Functional interface for 1D convolution layer (e.g. temporal convolution).

[`convolution1d_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/conv1d_reparameterization): Functional interface for 1D convolution layer (e.g. temporal convolution).

[`convolution2d_flipout(...)`](../../../tf/contrib/bayesflow/layers/conv2d_flipout): Functional interface for the 2D convolution layer.

[`convolution2d_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/conv2d_reparameterization): Functional interface for the 2D convolution layer.

[`convolution3d_flipout(...)`](../../../tf/contrib/bayesflow/layers/conv3d_flipout): Functional interface for the 3D convolution layer.

[`convolution3d_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/conv3d_reparameterization): Functional interface for the 3D convolution layer.

[`default_loc_scale_fn(...)`](../../../tf/contrib/bayesflow/layers/default_loc_scale_fn): Makes closure which creates `loc`, `scale` params from `tf.get_variable`.

[`default_mean_field_normal_fn(...)`](../../../tf/contrib/bayesflow/layers/default_mean_field_normal_fn): Creates a function to build Normal distributions with trainable params.

[`dense_flipout(...)`](../../../tf/contrib/bayesflow/layers/dense_flipout): Densely-connected layer with Flipout estimator.

[`dense_local_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/dense_local_reparameterization): Densely-connected layer with local reparameterization estimator.

[`dense_reparameterization(...)`](../../../tf/contrib/bayesflow/layers/dense_reparameterization): Densely-connected layer with reparameterization estimator.

