

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.frechet_classifier_distance

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.frechet_classifier_distance`
* `tf.contrib.gan.eval.frechet_classifier_distance`

``` python
tf.contrib.gan.eval.frechet_classifier_distance(
    real_images,
    generated_images,
    classifier_fn,
    num_batches=1
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Classifier distance for evaluating a generative model.

This is based on the Frechet Inception distance, but for an arbitrary
classifier.

This technique is described in detail in https://arxiv.org/abs/1706.08500.
Given two Gaussian distribution with means m and m_w and covariance matrices
C and C_w, this function calculates

            |m - m_w|^2 + Tr(C + C_w - 2(C * C_w)^(1/2))

which captures how different the distributions of real images and generated
images (or more accurately, their visual features) are. Note that unlike the
Inception score, this is a true distance and utilizes information about real
world images.

Note that when computed using sample means and sample covariance matrices,
Frechet distance is biased. It is more biased for small sample sizes. (e.g.
even if the two distributions are the same, for a small sample size, the
expected Frechet distance is large). It is important to use the same
sample size to compute Frechet classifier distance when comparing two
generative models.

NOTE: This function consumes images, computes their activations, and then
computes the classifier score. If you would like to precompute many
activations for real and generated images for large batches, please use
frechet_clasifier_distance_from_activations(), which this method also uses.

#### Args:

* <b>`real_images`</b>: Real images to use to compute Frechet Inception distance.
* <b>`generated_images`</b>: Generated images to use to compute Frechet Inception
    distance.
* <b>`classifier_fn`</b>: A function that takes images and produces activations
    based on a classifier.
* <b>`num_batches`</b>: Number of batches to split images in to in order to
    efficiently run them through the classifier network.


#### Returns:

The Frechet Inception distance. A floating-point scalar of the same type
as the output of `classifier_fn`.