

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.estimator.FisherEstimator

## Class `FisherEstimator`





Defined in [`tensorflow/contrib/kfac/python/ops/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/estimator.py).

Fisher estimator class supporting various approximations of the Fisher.

This is an abstract base class which does not implement a strategy for
placing covariance variables, covariance update ops and inverse update ops.
The placement strategies are implemented in `placement.py`. See
`FisherEstimatorRoundRobin` for example of a concrete subclass with
a round-robin placement strategy.

## Properties

<h3 id="blocks"><code>blocks</code></h3>

All registered FisherBlocks.

<h3 id="damping"><code>damping</code></h3>



<h3 id="factors"><code>factors</code></h3>

All registered FisherFactors.

<h3 id="name"><code>name</code></h3>



<h3 id="variables"><code>variables</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    variables,
    cov_ema_decay,
    damping,
    layer_collection,
    exps=(-1,),
    estimation_mode='gradients',
    colocate_gradients_with_ops=True,
    name='FisherEstimator'
)
```

Create a FisherEstimator object.

#### Args:

* <b>`variables`</b>: A `list` of variables or `callable` which returns the variables
      for which to estimate the Fisher. This must match the variables
      registered in layer_collection (if it is not None).
* <b>`cov_ema_decay`</b>: The decay factor used when calculating the covariance
      estimate moving averages.
* <b>`damping`</b>: float. The damping factor used to stabilize training due to
      errors in the local approximation with the Fisher information matrix,
      and to regularize the update direction by making it closer to the
      gradient. (Higher damping means the update looks more like a standard
      gradient update - see Tikhonov regularization.)
* <b>`layer_collection`</b>: The layer collection object, which holds the fisher
      blocks, kronecker factors, and losses associated with the
      graph.
* <b>`exps`</b>: List of floats or ints. These represent the different matrix
      powers of the approximate Fisher that the FisherEstimator will be able
      to multiply vectors by. If the user asks for a matrix power other
      one of these (or 1, which is always supported), there will be a
      failure. (Default: (-1,))
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
* <b>`name`</b>: A string. A name given to this estimator, which is added to the
      variable scope when constructing variables and ops.
      (Default: "FisherEstimator")

#### Raises:

* <b>`ValueError`</b>: If no losses have been registered with layer_collection.

<h3 id="create_ops_and_vars_thunks"><code>create_ops_and_vars_thunks</code></h3>

``` python
create_ops_and_vars_thunks(scope=None)
```

Create thunks that make the ops and vars on demand.

This function returns 4 lists of thunks: cov_variable_thunks,
cov_update_thunks, inv_variable_thunks, and inv_update_thunks.

The length of each list is the number of factors and the i-th element of
each list corresponds to the i-th factor (given by the "factors" property).

Note that the execution of these thunks must happen in a certain
partial order.  The i-th element of cov_variable_thunks must execute
before the i-th element of cov_update_thunks (and also the i-th element
of inv_update_thunks).  Similarly, the i-th element of inv_variable_thunks
must execute before the i-th element of inv_update_thunks.

TL;DR (oversimplified): Execute the thunks according to the order that
they are returned.

#### Args:

* <b>`scope`</b>: A string or None.  If None it will be set to the name of this
    estimator (given by the name property). All thunks will execute inside
    of a variable scope of the given name. (Default: None)

#### Returns:

* <b>`cov_variable_thunks`</b>: A list of thunks that make the cov variables.
* <b>`cov_update_thunks`</b>: A list of thunks that make the cov update ops.
* <b>`inv_variable_thunks`</b>: A list of thunks that make the inv variables.
* <b>`inv_update_thunks`</b>: A list of thunks that make the inv update ops.

<h3 id="made_vars"><code>made_vars</code></h3>

``` python
made_vars()
```



<h3 id="make_ops_and_vars"><code>make_ops_and_vars</code></h3>

``` python
make_ops_and_vars(scope=None)
```

Make ops and vars with a specific placement strategy.

For each factor, all of that factor's cov variables and their associated
update ops will be placed on a particular device.  For example in case of
round robin placement a new device is chosen for each factor by cycling
through list of devices in the cov_devices argument. If cov_devices is None
then no explicit device placement occurs.

An analogous strategy is followed for inverse update ops, with the list of
devices being given by the inv_devices argument.

Inverse variables on the other hand are not placed on any specific device
(they will just use the current the device placement context, whatever
that happens to be).  The idea is that the inverse variable belong where
they will be accessed most often, which is the device that actually applies
the preconditioner to the gradient. The user will be responsible for setting
the device context for this.

#### Args:

* <b>`scope`</b>: A string or None.  If None it will be set to the name of this
    estimator (given by the name property). All variables will be created,
    and all ops will execute, inside of a variable scope of the given
    name. (Default: None)


#### Returns:

* <b>`cov_update_ops`</b>: List of ops that compute the cov updates. Corresponds
    one-to-one with the list of factors given by the "factors" property.
* <b>`cov_update_op`</b>: cov_update_ops grouped into a single op.
* <b>`inv_update_ops`</b>: List of ops that compute the inv updates. Corresponds
    one-to-one with the list of factors given by the "factors" property.
* <b>`inv_update_op`</b>: inv_update_ops grouped into a single op.
* <b>`cov_update_thunks`</b>: Thunks that make the ops in cov_update_ops.
* <b>`inv_update_thunks`</b>: Thunks that make the ops in inv_update_ops.

<h3 id="make_vars_and_create_op_thunks"><code>make_vars_and_create_op_thunks</code></h3>

``` python
make_vars_and_create_op_thunks(scope=None)
```

Make vars and create op thunks with a specific placement strategy.

For each factor, all of that factor's cov variables and their associated
update ops will be placed on a particular device.  A new device is chosen
for each factor by cycling through list of devices in the cov_devices
argument. If cov_devices is None then no explicit device placement occurs.

An analogous strategy is followed for inverse update ops, with the list of
devices being given by the inv_devices argument.

Inverse variables on the other hand are not placed on any specific device
(they will just use the current the device placement context, whatever
that happens to be).  The idea is that the inverse variable belong where
they will be accessed most often, which is the device that actually applies
the preconditioner to the gradient. The user will be responsible for setting
the device context for this.

#### Args:

* <b>`scope`</b>: A string or None.  If None it will be set to the name of this
    estimator (given by the name property). All variables will be created,
    and all thunks will execute, inside of a variable scope of the given
    name. (Default: None)


#### Returns:

* <b>`cov_update_thunks`</b>: List of cov update thunks. Corresponds one-to-one with
    the list of factors given by the "factors" property.
* <b>`inv_update_thunks`</b>: List of inv update thunks. Corresponds one-to-one with
    the list of factors given by the "factors" property.

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

<h3 id="multiply_matpower"><code>multiply_matpower</code></h3>

``` python
multiply_matpower(
    exp,
    vecs_and_vars
)
```

Multiplies the vecs by the corresponding matrix powers of the blocks.

#### Args:

* <b>`exp`</b>: A float representing the power to raise the blocks by before
    multiplying it by the vector.
* <b>`vecs_and_vars`</b>: List of (vector, variable) pairs.


#### Returns:

A list of (transformed vector, var) pairs in the same order as
vecs_and_vars.



