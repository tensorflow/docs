

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.bayesflow.optimizers.VariationalSGDOptimizer

## Class `VariationalSGDOptimizer`

Inherits From: [`Optimizer`](../../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/bayesflow/python/ops/variational_sgd_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/bayesflow/python/ops/variational_sgd_optimizer.py).

An optimizer module for constant stochastic gradient descent.

This implements an optimizer module for the constant stochastic gradient
descent algorithm [1].  The optimization variable is regarded as an
approximate sample from the posterior .

Note: If a prior is included in the loss, it should be scaled by
`1/num_pseudo_batches`, where num_pseudo_batches is the number of minibatches
in the data.  I.e., it should be divided by the `num_pseudo_batches` term
described below.

[1]: "Stochastic Gradient Descent as Approximate Bayesian Inference
     Stephan Mandt, Matthew D. Hoffman, David M. Blei.
     ArXiv:1704.04289, 2017. https://arxiv.org/abs/1704.04289

#### Args:

* <b>`batch_size`</b>: Scalar `int`-like `Tensor`. The number of examples in a
    minibatch in the data set. Note: Assumes the loss is taken as the mean
    over a minibatch. Otherwise if the sum was taken set this to 1.
* <b>`total_num_examples`</b>: Scalar `int`-like `Tensor`. The total number of examples
    in the data set.
* <b>`max_learning_rate`</b>: Scalar `float`-like `Tensor`. A maximum allowable
    effective coordinate-wise learning rate. The algorithm scales down any
    effective learning rate (i.e. after preconditioning) that is larger than
    this. (Default: `1`)
* <b>`preconditioner_decay_rate`</b>: Scalar `float`-like `Tensor`. The exponential
    decay rate of the rescaling of the preconditioner (RMSprop). (This is
    "alpha" in [1]). Should be smaller than but nearly `1` to approximate
    sampling from the posterior. (Default: `0.95`)
* <b>`burnin`</b>: Scalar `int`-like `Tensor`. The number of iterations to collect
    gradient statistics to update the preconditioner before starting to draw
    noisy samples. (Default: `25`)
* <b>`burnin_max_learning_rate`</b>: Scalar `float`-like `Tensor`. Maximum learning
    rate to use during the burnin period.
    (Default: `1e-8`)
* <b>`use_single_learning_rate`</b>: Boolean Indicates whether one single learning
    rate is used or coordinate_wise learning rates are used.
    (Default: `False`)
* <b>`name`</b>: Python `str` describing ops managed by this function.
    (Default: `"VariationalSGDOptimizer"`)
* <b>`variable_scope`</b>: Variable scope used for calls to `tf.get_variable`.
    If `None`, a new variable scope is created using name
    `ops.get_default_graph().unique_name(name or default_name)`.


#### Raises:

* <b>`InvalidArgumentError`</b>: If preconditioner_decay_rate is a `Tensor` not in
    `(0,1]`.

## Properties

<h3 id="variable_scope"><code>variable_scope</code></h3>

Variable scope of all calls to `tf.get_variable`.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    batch_size,
    total_num_examples,
    max_learning_rate=1.0,
    preconditioner_decay_rate=0.95,
    burnin=25,
    burnin_max_learning_rate=1e-06,
    use_single_learning_rate=False,
    name=None,
    variable_scope=None
)
```



<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```

Apply gradients to variables.

This is the second part of `minimize()`. It returns an `Operation` that
applies gradients.

#### Args:

* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs as returned by
    `compute_gradients()`.
* <b>`global_step`</b>: Optional `Variable` to increment by one after the
    variables have been updated.
* <b>`name`</b>: Optional name for the returned operation.  Default to the
    name passed to the `Optimizer` constructor.


#### Returns:

An `Operation` that applies the specified gradients. If `global_step`
was not None, that operation also increments `global_step`.


#### Raises:

* <b>`TypeError`</b>: If `grads_and_vars` is malformed.
* <b>`ValueError`</b>: If none of the variables have gradients.

<h3 id="compute_gradients"><code>compute_gradients</code></h3>

``` python
compute_gradients(
    loss,
    var_list=None,
    gate_gradients=GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    grad_loss=None
)
```

Compute gradients of `loss` for the variables in `var_list`.

This is the first part of `minimize()`.  It returns a list
of (gradient, variable) pairs where "gradient" is the gradient
for "variable".  Note that "gradient" can be a `Tensor`, an
`IndexedSlices`, or `None` if there is no gradient for the
given variable.

#### Args:

* <b>`loss`</b>: A Tensor containing the value to minimize.
* <b>`var_list`</b>: Optional list or tuple of `tf.Variable` to update to minimize
    `loss`.  Defaults to the list of variables collected in the graph
    under the key `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`gate_gradients`</b>: How to gate the computation of gradients.  Can be
    `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`.
* <b>`aggregation_method`</b>: Specifies the method used to combine gradient terms.
    Valid values are defined in the class `AggregationMethod`.
* <b>`colocate_gradients_with_ops`</b>: If True, try colocating gradients with
    the corresponding op.
* <b>`grad_loss`</b>: Optional. A `Tensor` holding the gradient computed for `loss`.


#### Returns:

A list of (gradient, variable) pairs. Variable is always present, but
gradient can be `None`.


#### Raises:

* <b>`TypeError`</b>: If `var_list` contains anything else than `Variable` objects.
* <b>`ValueError`</b>: If some arguments are invalid.
* <b>`RuntimeError`</b>: If called with eager execution enabled and if `grad_loss`
    is not `None` or `loss` is not callable.



#### Eager Compatibility
When eager execution is enabled, `loss` should be a Python function that
takes elements of `var_list` as arguments and computes the value to be
minimized. If `var_list` is None, `loss` should take no arguments.
Gradient computation is done with respect to the elements of `var_list` if
not None, else with respect to any trainable variables created during the
execution of the `loss` function.
`gate_gradients`, `aggregation_method`, `colocate_gradients_with_ops` and
`grad_loss` are ignored when eager execution is enabled.



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

<h3 id="minimize"><code>minimize</code></h3>

``` python
minimize(
    loss,
    global_step=None,
    var_list=None,
    gate_gradients=GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    name=None,
    grad_loss=None
)
```

Add operations to minimize `loss` by updating `var_list`.

This method simply combines calls `compute_gradients()` and
`apply_gradients()`. If you want to process the gradient before applying
them call `compute_gradients()` and `apply_gradients()` explicitly instead
of using this function.

#### Args:

* <b>`loss`</b>: A `Tensor` containing the value to minimize.
* <b>`global_step`</b>: Optional `Variable` to increment by one after the
    variables have been updated.
* <b>`var_list`</b>: Optional list or tuple of `Variable` objects to update to
    minimize `loss`.  Defaults to the list of variables collected in
    the graph under the key `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`gate_gradients`</b>: How to gate the computation of gradients.  Can be
    `GATE_NONE`, `GATE_OP`, or  `GATE_GRAPH`.
* <b>`aggregation_method`</b>: Specifies the method used to combine gradient terms.
    Valid values are defined in the class `AggregationMethod`.
* <b>`colocate_gradients_with_ops`</b>: If True, try colocating gradients with
    the corresponding op.
* <b>`name`</b>: Optional name for the returned operation.
* <b>`grad_loss`</b>: Optional. A `Tensor` holding the gradient computed for `loss`.


#### Returns:

An Operation that updates the variables in `var_list`.  If `global_step`
was not `None`, that operation also increments `global_step`.


#### Raises:

* <b>`ValueError`</b>: If some of the variables are not `Variable` objects.



#### Eager Compatibility
When eager execution is enabled, `loss` should be a Python function that
takes elements of `var_list` as arguments and computes the value to be
minimized. If `var_list` is None, `loss` should take no arguments.
Minimization (and gradient computation) is done with respect to the
elements of `var_list` if not None, else with respect to any trainable
variables created during the execution of the `loss` function.
`gate_gradients`, `aggregation_method`, `colocate_gradients_with_ops` and
`grad_loss` are ignored when eager execution is enabled.



<h3 id="variables"><code>variables</code></h3>

``` python
variables()
```

A list of variables which encode the current state of `Optimizer`.

Includes slot variables and additional global variables created by the
optimizer in the current default graph.

#### Returns:

A list of variables.



## Class Members

<h3 id="GATE_GRAPH"><code>GATE_GRAPH</code></h3>

<h3 id="GATE_NONE"><code>GATE_NONE</code></h3>

<h3 id="GATE_OP"><code>GATE_OP</code></h3>

