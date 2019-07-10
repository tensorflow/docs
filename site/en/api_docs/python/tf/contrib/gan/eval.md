page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.gan.eval

TF-GAN evaluation module.



Defined in [`contrib/gan/python/eval/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/eval/__init__.py).

<!-- Placeholder for "Used in" -->

This module supports techniques such as Inception Score, Frechet Inception
distance, and Sliced Wasserstein distance.

## Modules

[`classifier_metrics`](../../../tf/contrib/gan/eval/classifier_metrics) module: Model evaluation tools for TF-GAN.

[`eval_utils`](../../../tf/contrib/gan/eval/eval_utils) module: Utility file for visualizing generated images.

[`summaries`](../../../tf/contrib/gan/eval/summaries) module: Common TF-GAN summaries.

## Functions

[`add_cyclegan_image_summaries(...)`](../../../tf/contrib/gan/eval/add_cyclegan_image_summaries): Adds image summaries for CycleGAN.

[`add_gan_model_image_summaries(...)`](../../../tf/contrib/gan/eval/add_gan_model_image_summaries): Adds image summaries for real and fake images.

[`add_gan_model_summaries(...)`](../../../tf/contrib/gan/eval/add_gan_model_summaries): Adds typical GANModel summaries.

[`add_image_comparison_summaries(...)`](../../../tf/contrib/gan/eval/add_image_comparison_summaries): Adds image summaries to compare triplets of images.

[`add_regularization_loss_summaries(...)`](../../../tf/contrib/gan/eval/add_regularization_loss_summaries): Adds summaries for a regularization losses..

[`add_stargan_image_summaries(...)`](../../../tf/contrib/gan/eval/add_stargan_image_summaries): Adds image summaries to see StarGAN image results.

[`classifier_score(...)`](../../../tf/contrib/gan/eval/classifier_score): Classifier score for evaluating a conditional generative model.

[`classifier_score_from_logits(...)`](../../../tf/contrib/gan/eval/classifier_score_from_logits): Classifier score for evaluating a generative model from logits.

[`diagonal_only_frechet_classifier_distance_from_activations(...)`](../../../tf/contrib/gan/eval/diagonal_only_frechet_classifier_distance_from_activations): Classifier distance for evaluating a generative model.

[`frechet_classifier_distance(...)`](../../../tf/contrib/gan/eval/frechet_classifier_distance): Classifier distance for evaluating a generative model.

[`frechet_classifier_distance_from_activations(...)`](../../../tf/contrib/gan/eval/frechet_classifier_distance_from_activations): Classifier distance for evaluating a generative model.

[`get_graph_def_from_disk(...)`](../../../tf/contrib/gan/eval/get_graph_def_from_disk): Get a GraphDef proto from a disk location.

[`get_graph_def_from_resource(...)`](../../../tf/contrib/gan/eval/get_graph_def_from_resource): Get a GraphDef proto from within a .par file.

[`get_graph_def_from_url_tarball(...)`](../../../tf/contrib/gan/eval/get_graph_def_from_url_tarball): Get a GraphDef proto from a tarball on the web.

[`image_grid(...)`](../../../tf/contrib/gan/eval/image_grid): Arrange a minibatch of images into a grid to form a single image.

[`image_reshaper(...)`](../../../tf/contrib/gan/eval/image_reshaper): A reshaped summary image.

[`kernel_classifier_distance(...)`](../../../tf/contrib/gan/eval/kernel_classifier_distance): Kernel "classifier" distance for evaluating a generative model.

[`kernel_classifier_distance_and_std(...)`](../../../tf/contrib/gan/eval/kernel_classifier_distance_and_std): Kernel "classifier" distance for evaluating a generative model.

[`kernel_classifier_distance_and_std_from_activations(...)`](../../../tf/contrib/gan/eval/kernel_classifier_distance_and_std_from_activations): Kernel "classifier" distance for evaluating a generative model.

[`kernel_classifier_distance_from_activations(...)`](../../../tf/contrib/gan/eval/kernel_classifier_distance_from_activations): Kernel "classifier" distance for evaluating a generative model.

[`mean_only_frechet_classifier_distance_from_activations(...)`](../../../tf/contrib/gan/eval/mean_only_frechet_classifier_distance_from_activations): Classifier distance for evaluating a generative model from activations.

[`preprocess_image(...)`](../../../tf/contrib/gan/eval/preprocess_image): Prepare a batch of images for evaluation.

[`run_image_classifier(...)`](../../../tf/contrib/gan/eval/run_image_classifier): Runs a network from a frozen graph.

[`run_inception(...)`](../../../tf/contrib/gan/eval/run_inception): Run images through a pretrained Inception classifier.

[`sliced_wasserstein_distance(...)`](../../../tf/contrib/gan/eval/sliced_wasserstein_distance): Compute the Wasserstein distance between two distributions of images.

## Other Members

* `INCEPTION_DEFAULT_IMAGE_SIZE = 299` <a id="INCEPTION_DEFAULT_IMAGE_SIZE"></a>
* `frechet_inception_distance` <a id="frechet_inception_distance"></a>
* `inception_score` <a id="inception_score"></a>
* `kernel_inception_distance` <a id="kernel_inception_distance"></a>
* `kernel_inception_distance_and_std` <a id="kernel_inception_distance_and_std"></a>
