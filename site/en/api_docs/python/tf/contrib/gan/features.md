page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.gan.features

TFGAN features module.



Defined in [`contrib/gan/python/features/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/features/__init__.py).

<!-- Placeholder for "Used in" -->

This module includes support for virtual batch normalization, buffer replay,
conditioning, etc.

## Classes

[`class VBN`](../../../tf/contrib/gan/features/VBN): A class to perform virtual batch normalization.

## Functions

[`clip_discriminator_weights(...)`](../../../tf/contrib/gan/features/clip_discriminator_weights): Modifies an optimizer so it clips weights to a certain value.

[`clip_variables(...)`](../../../tf/contrib/gan/features/clip_variables): Modifies an optimizer so it clips weights to a certain value.

[`compute_spectral_norm(...)`](../../../tf/contrib/gan/features/compute_spectral_norm): Estimates the largest singular value in the weight tensor.

[`condition_tensor(...)`](../../../tf/contrib/gan/features/condition_tensor): Condition the value of a tensor.

[`condition_tensor_from_onehot(...)`](../../../tf/contrib/gan/features/condition_tensor_from_onehot): Condition a tensor based on a one-hot tensor.

[`keras_spectral_normalization(...)`](../../../tf/contrib/gan/features/keras_spectral_normalization): A context manager that enables Spectral Normalization for Keras.

[`spectral_norm_regularizer(...)`](../../../tf/contrib/gan/features/spectral_norm_regularizer): Returns a functions that can be used to apply spectral norm regularization.

[`spectral_normalization_custom_getter(...)`](../../../tf/contrib/gan/features/spectral_normalization_custom_getter): Custom getter that performs Spectral Normalization on a weight tensor.

[`spectral_normalize(...)`](../../../tf/contrib/gan/features/spectral_normalize): Normalizes a weight matrix by its spectral norm.

[`tensor_pool(...)`](../../../tf/contrib/gan/features/tensor_pool): Queue storing input values and returning random previously stored ones.

