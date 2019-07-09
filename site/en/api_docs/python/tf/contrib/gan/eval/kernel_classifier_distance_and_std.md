page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.kernel_classifier_distance_and_std

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.kernel_classifier_distance_and_std`
* `tf.contrib.gan.eval.kernel_classifier_distance_and_std`

``` python
tf.contrib.gan.eval.kernel_classifier_distance_and_std(
    real_images,
    generated_images,
    classifier_fn,
    num_classifier_batches=1,
    max_block_size=1024,
    dtype=None
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Kernel "classifier" distance for evaluating a generative model.

This is based on the Kernel Inception distance, but for an arbitrary
embedding. Also returns an estimate of the standard error of the distance
estimator.

This technique is described in detail in https://arxiv.org/abs/1801.01401.
Given two distributions P and Q of activations, this function calculates

    E_{X, X' ~ P}[k(X, X')] + E_{Y, Y' ~ Q}[k(Y, Y')]
      - 2 E_{X ~ P, Y ~ Q}[k(X, Y)]

where k is the polynomial kernel

    k(x, y) = ( x^T y / dimension + 1 )^3.

This captures how different the distributions of real and generated images'
visual features are. Like the Frechet distance (and unlike the Inception
score), this is a true distance and incorporates information about the
target images. Unlike the Frechet score, this function computes an
*unbiased* and asymptotically normal estimator, which makes comparing
estimates across models much more intuitive.

The estimator used takes time quadratic in max_block_size. Larger values of
max_block_size will decrease the variance of the estimator but increase the
computational cost. This differs slightly from the estimator used by the
original paper; it is the block estimator of https://arxiv.org/abs/1307.1954.

NOTE: the blocking code assumes that real_activations and
generated_activations are both in random order. If either is sorted in a
meaningful order, the estimator will behave poorly.

NOTE: This function consumes images, computes their activations, and then
computes the classifier score. If you would like to precompute many
activations for real and generated images for large batches, or to compute
multiple scores based on the same images, please use
kernel_clasifier_distance_from_activations(), which this method also uses.

#### Args:

* <b>`real_images`</b>: Real images to use to compute Kernel Inception distance.
* <b>`generated_images`</b>: Generated images to use to compute Kernel Inception
    distance.
* <b>`classifier_fn`</b>: A function that takes images and produces activations based
    on a classifier.
* <b>`num_classifier_batches`</b>: Number of batches to split images in to in order to
    efficiently run them through the classifier network.
* <b>`max_estimator_block_size`</b>: integer, default 1024. The distance estimator
    splits samples into blocks for computational efficiency. Larger values are
    more computationally expensive but decrease the variance of the distance
    estimate. Having a smaller block size also gives a better estimate of the
    standard error.
* <b>`dtype`</b>: if not None, coerce activations to this dtype before computations.


#### Returns:

The Kernel Inception Distance. A floating-point scalar of the same type
  as the output of the activations.
An estimate of the standard error of the distance estimator (a scalar of
  the same type).