

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.optimizer.KfacOptimizer

## Class `KfacOptimizer`

Inherits From: [`GradientDescentOptimizer`](../../../../tf/train/GradientDescentOptimizer)



Defined in [`tensorflow/contrib/kfac/python/ops/optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/optimizer.py).

The KFAC Optimizer (https://arxiv.org/abs/1503.05671).

## Properties

<h3 id="damping"><code>damping</code></h3>



<h3 id="damping_adaptation_interval"><code>damping_adaptation_interval</code></h3>



<h3 id="variables"><code>variables</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    learning_rate,
    cov_ema_decay,
    damping,
    layer_collection,
    var_list=None,
    momentum=0.9,
    momentum_type='regular',
    norm_constraint=None,
    name='KFAC',
    estimation_mode='gradients',
    colocate_gradients_with_ops=True,
    batch_size=None,
    placement_strategy=None,
    **kwargs
)
```

Initializes the KFAC optimizer with the given settings.

#### Args:

* <b>`learning_rate`</b>: The base learning rate for the optimizer.  Should probably
      be set to 1.0 when using momentum_type = 'qmodel', but can still be
      set lowered if desired (effectively lowering the trust in the
      quadratic model.)
* <b>`cov_ema_decay`</b>: The decay factor used when calculating the covariance
      estimate moving averages.
* <b>`damping`</b>: The damping factor used to stabilize training due to errors in
      the local approximation with the Fisher information matrix, and to
      regularize the update direction by making it closer to the gradient.
      If damping is adapted during training then this value is used for
      initializing damping variable.
      (Higher damping means the update looks more like a standard gradient
      update - see Tikhonov regularization.)
* <b>`layer_collection`</b>: The layer collection object, which holds the fisher
      blocks, kronecker factors, and losses associated with the
      graph.  The layer_collection cannot be modified after KfacOptimizer's
      initialization.
* <b>`var_list`</b>: Optional list or tuple of variables to train. Defaults to the
      list of variables collected in the graph under the key
      `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`momentum`</b>: The momentum decay constant to use. Only applies when
      momentum_type is 'regular' or 'adam'. (Default: 0.9)
* <b>`momentum_type`</b>: The type of momentum to use in this optimizer, one of
      'regular', 'adam', or 'qmodel'. (Default: 'regular')
* <b>`norm_constraint`</b>: float or Tensor. If specified, the update is scaled down
      so that its approximate squared Fisher norm v^T F v is at most the
      specified value. May only be used with momentum type 'regular'.
      (Default: None)
* <b>`name`</b>: The name for this optimizer. (Default: 'KFAC')
* <b>`estimation_mode`</b>: The type of estimator to use for the Fishers.  Can be
      'gradients', 'empirical', 'curvature_propagation', or 'exact'.
      (Default: 'gradients'). See the doc-string for FisherEstimator for
      more a more detailed description of these options.
* <b>`colocate_gradients_with_ops`</b>: Whether we should request gradients we
      compute in the estimator be colocated with their respective ops.
      (Default: True)
* <b>`batch_size`</b>: The size of the mini-batch. Only needed when momentum_type
      == 'qmodel' or when automatic adjustment is used.  (Default: None)
* <b>`placement_strategy`</b>: string, Device placement strategy used when creating
    covariance variables, covariance ops, and inverse ops.
    (Default: `None`)
* <b>`**kwargs`</b>: Arguments to be passesd to specific placement
    strategy mixin. Check `placement.RoundRobinPlacementMixin` for example.


#### Raises:

* <b>`ValueError`</b>: If the momentum type is unsupported.
* <b>`ValueError`</b>: If clipping is used with momentum type other than 'regular'.
* <b>`ValueError`</b>: If no losses have been registered with layer_collection.
* <b>`ValueError`</b>: If momentum is non-zero and momentum_type is not 'regular'
      or 'adam'.

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    *args,
    **kwargs
)
```

Applies gradients to variables.

#### Args:

* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs.
* <b>`*args`</b>: Additional arguments for super.apply_gradients.
* <b>`**kwargs`</b>: Additional keyword arguments for super.apply_gradients.


#### Returns:

An `Operation` that applies the specified gradients.

<h3 id="compute_gradients"><code>compute_gradients</code></h3>

``` python
compute_gradients(
    *args,
    **kwargs
)
```



<h3 id="create_ops_and_vars_thunks"><code>create_ops_and_vars_thunks</code></h3>

``` python
create_ops_and_vars_thunks()
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

#### Returns:

* <b>`cov_variable_thunks`</b>: A list of thunks that make the cov variables.
* <b>`cov_update_thunks`</b>: A list of thunks that make the cov update ops.
* <b>`inv_variable_thunks`</b>: A list of thunks that make the inv variables.
* <b>`inv_update_thunks`</b>: A list of thunks that make the inv update ops.

<h3 id="get_name"><code>get_name</code></h3>

``` python
get_name()
```



<h3 id="get_slot"><code>get_slot</code></h3>

``` python
get_slot(
    var,
    name
)
```

Return a slot named `name` created for `var` by the Optimizer.

Some `Optimizer` subclasses use additional variables.  For example
`Momentum` and `Adagrad` use variables to accumulate updates.  This method
gives access to these `Variable` objects if for some reason you need them.

Use `get_slot_names()` to get the list of slot names created by the
`Optimizer`.

#### Args:

* <b>`var`</b>: A variable passed to `minimize()` or `apply_gradients()`.
* <b>`name`</b>: A string.


#### Returns:

The `Variable` for the slot if it was created, `None` otherwise.

<h3 id="get_slot_names"><code>get_slot_names</code></h3>

``` python
get_slot_names()
```

Return a list of the names of slots created by the `Optimizer`.

See `get_slot()`.

#### Returns:

A list of strings.

<h3 id="make_vars_and_create_op_thunks"><code>make_vars_and_create_op_thunks</code></h3>

``` python
make_vars_and_create_op_thunks()
```

Make vars and create op thunks.

#### Returns:

* <b>`cov_update_thunks`</b>: List of cov update thunks. Corresponds one-to-one with
    the list of factors given by the "factors" property.
* <b>`inv_update_thunks`</b>: List of inv update thunks. Corresponds one-to-one with
    the list of factors given by the "factors" property.

<h3 id="minimize"><code>minimize</code></h3>

``` python
minimize(
    *args,
    **kwargs
)
```



<h3 id="set_damping_adaptation_params"><code>set_damping_adaptation_params</code></h3>

``` python
set_damping_adaptation_params(
    is_chief,
    prev_train_batch,
    loss_fn,
    min_damping=1e-05,
    damping_adaptation_decay=0.99,
    damping_adaptation_interval=5
)
```

Sets parameters required to adapt damping during training.

When called, enables damping adaptation according to the Levenberg-Marquardt
style rule described in Section 6.5 of "Optimizing Neural Networks with
Kronecker-factored Approximate Curvature".

Note that this function creates Tensorflow variables which store a few
scalars and are accessed by the ops which update the damping (as part
of the training op returned by the minimize() method).

#### Args:

* <b>`is_chief`</b>: `Boolean`, `True` if the worker is chief.
* <b>`prev_train_batch`</b>: Training data used to minimize loss in the previous
    step. This will be used to evaluate loss by calling
    `loss_fn(prev_train_batch)`.
* <b>`loss_fn`</b>: `function` that takes as input training data tensor and returns
    a scalar loss.
* <b>`min_damping`</b>: `float`(Optional), Minimum value the damping parameter
    can take. Default value 1e-5.
* <b>`damping_adaptation_decay`</b>: `float`(Optional), The `damping` parameter is
    multiplied by the `damping_adaptation_decay` every
    `damping_adaptation_interval` number of iterations. Default value 0.99.
* <b>`damping_adaptation_interval`</b>: `int`(Optional), Number of steps in between
    updating the `damping` parameter. Default value 5.


#### Raises:

* <b>`ValueError`</b>: If `set_damping_adaptation_params` is already called and the
    the `adapt_damping` is `True`.



## Class Members

<h3 id="GATE_GRAPH"><code>GATE_GRAPH</code></h3>

<h3 id="GATE_NONE"><code>GATE_NONE</code></h3>

<h3 id="GATE_OP"><code>GATE_OP</code></h3>

