page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distributions.RegisterKL

## Class `RegisterKL`



### Aliases:

* Class `tf.contrib.distributions.RegisterKL`
* Class `tf.distributions.RegisterKL`



Defined in [`tensorflow/python/ops/distributions/kullback_leibler.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/distributions/kullback_leibler.py).

Decorator to register a KL divergence implementation function.

Usage:

@distributions.RegisterKL(distributions.Normal, distributions.Normal)
def _kl_normal_mvn(norm_a, norm_b):
  # Return KL(norm_a || norm_b)

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dist_cls_a,
    dist_cls_b
)
```

Initialize the KL registrar. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2019-01-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../tf/distributions"><code>tf.distributions</code></a>.

#### Args:

* <b>`dist_cls_a`</b>: the class of the first argument of the KL divergence.
* <b>`dist_cls_b`</b>: the class of the second argument of the KL divergence.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(kl_fn)
```

Perform the KL registration.

#### Args:

* <b>`kl_fn`</b>: The function to use for the KL divergence.


#### Returns:

kl_fn


#### Raises:

* <b>`TypeError`</b>: if kl_fn is not a callable.
* <b>`ValueError`</b>: if a KL divergence function has already been registered for
    the given argument classes.



