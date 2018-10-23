

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.estimator.FisherEstimator

## Class `FisherEstimator`





Defined in [`tensorflow/contrib/kfac/python/ops/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/kfac/python/ops/estimator.py).

Fisher estimator class supporting various approximations of the Fisher.

#### Attributes:

* <b>`cov_update_thunks`</b>: list of no-arg functions. Executing a function adds
    covariance update ops for a single FisherFactor to the graph.
* <b>`cov_update_ops`</b>: List of Ops. Running an op updates covariance matrices for a
    single FisherFactor.
* <b>`cov_update_op`</b>: Op. Running updates covariance matrices for all
    FisherFactors.
* <b>`inv_update_thunks`</b>: list of no-arg functions.  Executing a function adds
    inverse update ops for a single FisherFactor to the graph.
* <b>`inv_update_ops`</b>: List of Ops. Running an op updates inverse matrices for a
    single FisherFactor.
* <b>`inv_update_op`</b>: Op. Running updates inverse matrices for all FisherFactors.

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
    estimation_mode='gradients',
    colocate_gradients_with_ops=True,
    cov_devices=None,
    inv_devices=None
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
      'gradients', 'empirical', 'curvature_prop', or 'exact'.
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
* <b>`colocate_gradients_with_ops`</b>: Whether we should request gradients be
      colocated with their respective ops. (Default: True)
* <b>`cov_devices`</b>: Iterable of device strings (e.g. '/gpu:0'). Covariance
      computations will be placed on these devices in a round-robin fashion.
      Can be None, which means that no devices are specified.
* <b>`inv_devices`</b>: Iterable of device strings (e.g. '/gpu:0'). Inversion
      computations will be placed on these devices in a round-robin fashion.
      Can be None, which means that no devices are specified.


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



