


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.distributions.RegisterKL

### `class tf.contrib.distributions.RegisterKL`

See the guide: [Statistical Distributions (contrib) > Kullback-Leibler Divergence](../../../../../api_guides/python/contrib.distributions#Kullback_Leibler_Divergence)

Decorator to register a KL divergence implementation function.

Usage:

@distributions.RegisterKL(distributions.Normal, distributions.Normal)
def _kl_normal_mvn(norm_a, norm_b):
  # Return KL(norm_a || norm_b)

## Methods

<h3 id="__init__"><code>__init__(dist_cls_a, dist_cls_b)</code></h3>

Initialize the KL registrar.

#### Args:

* <b>`dist_cls_a`</b>: the class of the first argument of the KL divergence.
* <b>`dist_cls_b`</b>: the class of the second argument of the KL divergence.





Defined in [`tensorflow/contrib/distributions/python/ops/kullback_leibler.py`](https://www.tensorflow.org/code/tensorflow/contrib/distributions/python/ops/kullback_leibler.py).

