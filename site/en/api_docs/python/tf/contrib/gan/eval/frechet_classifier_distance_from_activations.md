

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.eval.frechet_classifier_distance_from_activations

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.frechet_classifier_distance_from_activations`
* `tf.contrib.gan.eval.frechet_classifier_distance_from_activations`

``` python
frechet_classifier_distance_from_activations(
    real_activations,
    generated_activations
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Classifier distance for evaluating a generative model.

This is based on the Frechet Inception distance, but for an arbitrary
classifier.

This technique is described in detail in https://arxiv.org/abs/1706.08500.
Given two Gaussian distribution with means m and m_w and covariance matrices
C and C_w, this function calcuates

|m - m_w|^2 + Tr(C + C_w - 2(C * C_w)^(1/2))

which captures how different the distributions of real images and generated
images (or more accurately, their visual features) are. Note that unlike the
Inception score, this is a true distance and utilizes information about real
world images.

Note that when computed using sample means and sample covariance matrices,
Frechet distance is biased. It is more biased for small sample sizes. (e.g.
even if the two distributions are the same, for a small sample size, the
expected Frechet distance is large). It is important to use the same
sample size to compute frechet classifier distance when comparing two
generative models.

#### Args:

* <b>`real_activations`</b>: Real images to use to compute Frechet Inception distance.
* <b>`generated_activations`</b>: Generated images to use to compute Frechet Inception
    distance.


#### Returns:

The Frechet Inception distance. A floating-point scalar of the same type
as the output of the activations.