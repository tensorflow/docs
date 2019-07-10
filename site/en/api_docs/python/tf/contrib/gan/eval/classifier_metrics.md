page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.gan.eval.classifier_metrics

Model evaluation tools for TF-GAN.



Defined in [`contrib/gan/python/eval/python/classifier_metrics.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/eval/python/classifier_metrics.py).

<!-- Placeholder for "Used in" -->


## Functions

[`classifier_score(...)`](../../../../tf/contrib/gan/eval/classifier_score): Classifier score for evaluating a conditional generative model.

[`classifier_score_from_logits(...)`](../../../../tf/contrib/gan/eval/classifier_score_from_logits): Classifier score for evaluating a generative model from logits.

[`diagonal_only_frechet_classifier_distance_from_activations(...)`](../../../../tf/contrib/gan/eval/diagonal_only_frechet_classifier_distance_from_activations): Classifier distance for evaluating a generative model.

[`frechet_classifier_distance(...)`](../../../../tf/contrib/gan/eval/frechet_classifier_distance): Classifier distance for evaluating a generative model.

[`frechet_classifier_distance_from_activations(...)`](../../../../tf/contrib/gan/eval/frechet_classifier_distance_from_activations): Classifier distance for evaluating a generative model.

[`get_graph_def_from_disk(...)`](../../../../tf/contrib/gan/eval/get_graph_def_from_disk): Get a GraphDef proto from a disk location.

[`get_graph_def_from_resource(...)`](../../../../tf/contrib/gan/eval/get_graph_def_from_resource): Get a GraphDef proto from within a .par file.

[`get_graph_def_from_url_tarball(...)`](../../../../tf/contrib/gan/eval/get_graph_def_from_url_tarball): Get a GraphDef proto from a tarball on the web.

[`kernel_classifier_distance(...)`](../../../../tf/contrib/gan/eval/kernel_classifier_distance): Kernel "classifier" distance for evaluating a generative model.

[`kernel_classifier_distance_and_std(...)`](../../../../tf/contrib/gan/eval/kernel_classifier_distance_and_std): Kernel "classifier" distance for evaluating a generative model.

[`kernel_classifier_distance_and_std_from_activations(...)`](../../../../tf/contrib/gan/eval/kernel_classifier_distance_and_std_from_activations): Kernel "classifier" distance for evaluating a generative model.

[`kernel_classifier_distance_from_activations(...)`](../../../../tf/contrib/gan/eval/kernel_classifier_distance_from_activations): Kernel "classifier" distance for evaluating a generative model.

[`mean_only_frechet_classifier_distance_from_activations(...)`](../../../../tf/contrib/gan/eval/mean_only_frechet_classifier_distance_from_activations): Classifier distance for evaluating a generative model from activations.

[`preprocess_image(...)`](../../../../tf/contrib/gan/eval/preprocess_image): Prepare a batch of images for evaluation.

[`run_image_classifier(...)`](../../../../tf/contrib/gan/eval/run_image_classifier): Runs a network from a frozen graph.

[`run_inception(...)`](../../../../tf/contrib/gan/eval/run_inception): Run images through a pretrained Inception classifier.

## Other Members

* `INCEPTION_DEFAULT_IMAGE_SIZE = 299` <a id="INCEPTION_DEFAULT_IMAGE_SIZE"></a>
* `frechet_inception_distance` <a id="frechet_inception_distance"></a>
* `inception_score` <a id="inception_score"></a>
* `kernel_inception_distance` <a id="kernel_inception_distance"></a>
* `kernel_inception_distance_and_std` <a id="kernel_inception_distance_and_std"></a>
