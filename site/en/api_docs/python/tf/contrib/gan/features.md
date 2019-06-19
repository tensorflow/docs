

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.gan.features



Defined in [`tensorflow/contrib/gan/python/features/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/gan/python/features/__init__.py).

TFGAN features module.

This module includes support for virtual batch normalization, buffer replay,
conditioning, etc.

## Classes

[`class VBN`](../../../tf/contrib/gan/features/VBN): A class to perform virtual batch normalization.

## Functions

[`clip_discriminator_weights(...)`](../../../tf/contrib/gan/features/clip_discriminator_weights): Modifies an optimizer so it clips weights to a certain value.

[`clip_variables(...)`](../../../tf/contrib/gan/features/clip_variables): Modifies an optimizer so it clips weights to a certain value.

[`condition_tensor(...)`](../../../tf/contrib/gan/features/condition_tensor): Condition the value of a tensor.

[`condition_tensor_from_onehot(...)`](../../../tf/contrib/gan/features/condition_tensor_from_onehot): Condition a tensor based on a one-hot tensor.

[`tensor_pool(...)`](../../../tf/contrib/gan/features/tensor_pool): Queue storing input values and returning random previously stored ones.

