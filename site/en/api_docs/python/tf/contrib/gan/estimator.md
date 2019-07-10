page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.gan.estimator

TF-GAN estimator module.



Defined in [`contrib/gan/python/estimator/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/estimator/__init__.py).

<!-- Placeholder for "Used in" -->

GANEstimator provides all the infrastructure support of a TensorFlow Estimator
with the feature support of TF-GAN.

## Modules

[`gan_estimator`](../../../tf/contrib/gan/estimator/gan_estimator) module: `tf.Learn` components for `GANEstimator`.

[`head`](../../../tf/contrib/gan/estimator/head) module: `tf.Learn` components for `GANEstimator`'s loss.

[`latent_gan_estimator`](../../../tf/contrib/gan/estimator/latent_gan_estimator) module: `tf.Learn` components for `Train Input Estimator`.

[`stargan_estimator`](../../../tf/contrib/gan/estimator/stargan_estimator) module: `tf.Learn` components for `GANEstimator`.

[`tpu_gan_estimator`](../../../tf/contrib/gan/estimator/tpu_gan_estimator) module: `tf.Learn` components for `TPUGANEstimator`.

## Classes

[`class GANEstimator`](../../../tf/contrib/gan/estimator/GANEstimator): An estimator for Generative Adversarial Networks (GANs).

[`class GANHead`](../../../tf/contrib/gan/estimator/GANHead): `Head` for a GAN.

[`class StarGANEstimator`](../../../tf/contrib/gan/estimator/StarGANEstimator): An estimator for Generative Adversarial Networks (GANs).

[`class SummaryType`](../../../tf/contrib/gan/estimator/SummaryType)

[`class TPUGANEstimator`](../../../tf/contrib/gan/estimator/TPUGANEstimator): An estimator for Generative Adversarial Networks (GANs) on TPU.

## Functions

[`gan_head(...)`](../../../tf/contrib/gan/estimator/gan_head): Creates a `GANHead`. (deprecated)

[`get_latent_gan_estimator(...)`](../../../tf/contrib/gan/estimator/get_latent_gan_estimator): Gets an estimator that passes gradients to the input.

