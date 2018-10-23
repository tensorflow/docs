

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.estimator.FisherEstimator

## Class `FisherEstimator`





Defined in [`tensorflow/contrib/kfac/python/ops/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/estimator.py).

Fisher estimator class supporting various approximations of the Fisher.

## Properties

<h3 id="damping"><code>damping</code></h3>



<h3 id="variables"><code>variables</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    variables,
    cov_ema_decay,
    damping,
    layer_collection,
    estimation_mode='gradients'
)
```

Create a FisherEstimator object.

#### Args:

* <b>`variables`</b>: A list of the variables for which to estimate the Fisher. This
      must match the variables registered in layer_collection (if it is not
      None).
* <b>`cov_ema_decay`</b>: The decay factor used when calculating the covariance
      estimate moving averages.
* <b>`damping`</b>: The damping factor used to stabilize training due to errors in
      the local approximation with the Fisher information matrix, and to
      regularize the update direction by making it closer to the gradient.
      (Higher damping means the update looks more like a standard gradient
      update - see Tikhonov regularization.)
* <b>`layer_collection`</b>: The layer collection object, which holds the fisher
      blocks, kronecker factors, and losses associated with the
      graph.
* <b>`estimation_mode`</b>: The type of estimator to use for the Fishers.  Can be
      'gradients', 'empirical', 'curvature_propagation', or 'exact'.
      (Default: 'gradients').  'gradients' is the basic estimation approach
      from the original K-FAC paper.  'empirical' computes the 'empirical'
      Fisher information matrix (which uses the data's distribution for the
      targets, as opposed to the true Fisher which uses the model's
      distribution) and requires that each registered loss have specified
      targets. 'curvature_propagation' is a method which estimates the
      Fisher using self-products of random 1/-1 vectors times "half-factors"
      of the Fisher, as described here: https://arxiv.org/abs/1206.6464 .
      Finally, 'exact' is the obvious generalization of Curvature
      Propagation to compute the exact Fisher (modulo any additional
      diagonal or Kronecker approximations) by looping over one-hot vectors
      for each coordinate of the output instead of using 1/-1 vectors.  It
      is more expensive to compute than the other three options by a factor
      equal to the output dimension, roughly speaking.


#### Raises:

* <b>`ValueError`</b>: If no losses have been registered with layer_collection.

<h3 id="multiply"><code>multiply</code></h3>

``` python
multiply(vecs_and_vars)
```

Multiplies the vectors by the corresponding (damped) blocks.

#### Args:

* <b>`vecs_and_vars`</b>: List of (vector, variable) pairs.


#### Returns:

A list of (transformed vector, var) pairs in the same order as
vecs_and_vars.

<h3 id="multiply_inverse"><code>multiply_inverse</code></h3>

``` python
multiply_inverse(vecs_and_vars)
```

Multiplies the vecs by the corresponding (damped) inverses of the blocks.

#### Args:

* <b>`vecs_and_vars`</b>: List of (vector, variable) pairs.


#### Returns:

A list of (transformed vector, var) pairs in the same order as
vecs_and_vars.



