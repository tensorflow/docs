page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.kfac.fisher_blocks



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks_lib.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/fisher_blocks_lib.py).

FisherBlock definitions.

## Classes

[`class ConvDiagonalFB`](../../../tf/contrib/kfac/fisher_blocks/ConvDiagonalFB): FisherBlock for 2-D convolutional layers using a diagonal approx.

[`class ConvKFCBasicFB`](../../../tf/contrib/kfac/fisher_blocks/ConvKFCBasicFB): FisherBlock for convolutional layers using the basic KFC approx.

[`class EmbeddingKFACFB`](../../../tf/contrib/kfac/fisher_blocks/EmbeddingKFACFB): K-FAC FisherBlock for embedding layers.

[`class FisherBlock`](../../../tf/contrib/kfac/fisher_blocks/FisherBlock): Abstract base class for objects modeling approximate Fisher matrix blocks.

[`class FullFB`](../../../tf/contrib/kfac/fisher_blocks/FullFB): FisherBlock using a full matrix estimate (no approximations).

[`class FullyConnectedDiagonalFB`](../../../tf/contrib/kfac/fisher_blocks/FullyConnectedDiagonalFB): FisherBlock for fully-connected (dense) layers using a diagonal approx.

[`class FullyConnectedKFACBasicFB`](../../../tf/contrib/kfac/fisher_blocks/FullyConnectedKFACBasicFB): K-FAC FisherBlock for fully-connected (dense) layers.

[`class KroneckerProductFB`](../../../tf/contrib/kfac/fisher_blocks/KroneckerProductFB): A base class for blocks with separate input and output Kronecker factors.

[`class NaiveDiagonalFB`](../../../tf/contrib/kfac/fisher_blocks/NaiveDiagonalFB): FisherBlock using a diagonal matrix approximation.

## Functions

[`compute_pi_adjusted_damping(...)`](../../../tf/contrib/kfac/fisher_blocks/compute_pi_adjusted_damping)

[`compute_pi_tracenorm(...)`](../../../tf/contrib/kfac/fisher_blocks/compute_pi_tracenorm): Computes the scalar constant pi for Tikhonov regularization/damping.

[`normalize_damping(...)`](../../../tf/contrib/kfac/fisher_blocks/normalize_damping): Normalize damping after adjusting scale by NORMALIZE_DAMPING_POWER.

[`num_conv_locations(...)`](../../../tf/contrib/kfac/fisher_blocks/num_conv_locations): Returns the number of spatial locations a 2D Conv kernel is applied to.

[`set_global_constants(...)`](../../../tf/contrib/kfac/fisher_blocks/set_global_constants): Sets various global constants used by the classes in this module.

