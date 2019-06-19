page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.diagonal_only_frechet_classifier_distance_from_activations

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.diagonal_only_frechet_classifier_distance_from_activations`
* `tf.contrib.gan.eval.diagonal_only_frechet_classifier_distance_from_activations`

``` python
tf.contrib.gan.eval.diagonal_only_frechet_classifier_distance_from_activations(
    real_activations,
    generated_activations
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Classifier distance for evaluating a generative model.

This is based on the Frechet Inception distance, but for an arbitrary
classifier.

This technique is described in detail in https://arxiv.org/abs/1706.08500.
Given two Gaussian distribution with means m and m_w and covariance matrices
C and C_w, this function calcuates

        |m - m_w|^2 + (sigma + sigma_w - 2(sigma x sigma_w)^(1/2))

which captures how different the distributions of real images and generated
images (or more accurately, their visual features) are. Note that unlike the
Inception score, this is a true distance and utilizes information about real
world images. In this variant, we compute diagonal-only covariance matrices.
As a result, instead of computing an expensive matrix square root, we can do
something much simpler, and has O(n) vs O(n^2) space complexity.

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

The diagonal-only Frechet Inception distance. A floating-point scalar of
the same type as the output of the activations.


#### Raises:

* <b>`ValueError`</b>: If the shape of the variance and mean vectors are not equal.