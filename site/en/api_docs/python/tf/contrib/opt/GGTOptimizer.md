page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.GGTOptimizer

## Class `GGTOptimizer`

Inherits From: [`OptimizerV2`](../../../tf/contrib/optimizer_v2/OptimizerV2)



Defined in [`tensorflow/contrib/opt/python/training/ggt.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/opt/python/training/ggt.py).

Optimizer that implements the GGT algorithm.

GGT has an advantage over sgd and adam on large models with poor conditioning,
for example language models and CNNs,
see [[ABCHSZZ 2018]](https://arxiv.org/pdf/1806.02958.pdf).

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    learning_rate=0.001,
    beta1=0.9,
    use_locking=False,
    name='GGT',
    window=10,
    eps=0.0001,
    svd_eps=1e-06,
    sigma_eps=0.01
)
```

Construct a new GGT optimizer.

Initialization:

```
t <- 0 (Initialize timestep)
grad_buffer <- 0 (Initialize buffer for keeping past gradients)
flat_grad <- 0 (Initialize flattened gradient that contains gradients of all
                variables)
m_0 <- 0 (Initialize 1st moment vector)
```

Suppose all variables and their gradients are concatenated into vectors
`flat_vars` and `flat_grad`. The update rule for `flat_vars`
uses an optimization described at the beginning of section 2 of the paper:

```
t <- t + 1

m_t <- beta1 * m_{t-1} + (1 - beta1) * flat_grad
grad_buffer[(t-1) % window, :] <- m_t

M <- grad_buffer^T / sqrt(min(t, window))
U, sigma, _ <- SVD(M^TM + I * svd_eps)

sigma_sqrt_inv <- (sqrt(sigma) + sigma_eps)^(-3)
sigma_sqrt_min <- min(sqrt(sigma))

if sigma_sqrt_min > eps:
  new_step <- M U diag(sigma_sqrt_inv) U^T M^T m_t +
              (m_t - M U diag(1/sigma) U^T M^T m_t) / sigma_sqrt_min
else:
  new_step <- M U diag(sigma_sqrt_inv) U^T M^T m_t

flat_vars <- flat_vars - learning_rate * new_step
```

GGT provides the power of full-matrix adaptive regularization at a cost not
much larger than SGD. As a result it is suited for large models where the
gradient covariance matrix has a poor condition number that slows down first
order methods.
GGT uses the preconditioner from full-matrix AdaGrad, with gradient history
attenuated exponentially as in Adam, and truncated to a window parameter.
It has provable guarantees even for non-convex optimization that is never
significantly worse than SGD and in some cases better.

#### Args:

* <b>`learning_rate`</b>: A float hyperparameter. The learning rate.
* <b>`beta1`</b>: A float hyperparameter. The exponential decay rate for the 1st
    moment estimates.
* <b>`use_locking`</b>: If True use locks for update operations.
* <b>`name`</b>: Optional name for the operations created when applying gradients.
    Defaults to "GGT".
* <b>`window`</b>: An integer hyperparameter. The number of first moments to keep in
    computing the adaptive preconditioner.
* <b>`eps`</b>: A float hyperparameter. Used to truncate small eigenvalues of the
    gradient covariance matrix.
* <b>`svd_eps`</b>: A float hyperparameter. Used to stabilize SVD.
* <b>`sigma_eps`</b>: A float hyperparameter. Used to regularize matrix inversion.



## Methods

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
* <b>`global_step`</b>: Optional `Variable` to increment by one after the variables
    have been updated.
* <b>`name`</b>: Optional name for the returned operation.  Default to the name
    passed to the `Optimizer` constructor.


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
    grad_loss=None,
    stop_gradients=None,
    scale_loss_by_num_replicas=None
)
```

Compute gradients of `loss` for the variables in `var_list`.

This is the first part of `minimize()`.  It returns a list
of (gradient, variable) pairs where "gradient" is the gradient
for "variable".  Note that "gradient" can be a `Tensor`, an
`IndexedSlices`, or `None` if there is no gradient for the
given variable.

#### Args:

* <b>`loss`</b>: A Tensor containing the value to minimize or a callable taking no
    arguments which returns the value to minimize. When eager execution is
    enabled it must be a callable.
* <b>`var_list`</b>: Optional list or tuple of <a href="../../../tf/Variable"><code>tf.Variable</code></a> to update to minimize
    `loss`.  Defaults to the list of variables collected in the graph under
    the key `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`gate_gradients`</b>: How to gate the computation of gradients.  Can be
    `GATE_NONE`, `GATE_OP`, or `GATE_GRAPH`.
* <b>`aggregation_method`</b>: Specifies the method used to combine gradient terms.
    Valid values are defined in the class `AggregationMethod`.
* <b>`grad_loss`</b>: Optional. A `Tensor` holding the gradient computed for `loss`.
* <b>`stop_gradients`</b>: Optional. A Tensor or list of tensors not to differentiate
    through.
* <b>`scale_loss_by_num_replicas`</b>: Optional boolean. If true, scale the loss down
    by the number of replicas. By default, auto-detects whether this is
    needed.


#### Returns:

A list of (gradient, variable) pairs. Variable is always present, but
gradient can be `None`.


#### Raises:

* <b>`TypeError`</b>: If `var_list` contains anything else than `Variable` objects.
* <b>`ValueError`</b>: If some arguments are invalid.
* <b>`RuntimeError`</b>: If called with eager execution enabled and `loss` is
    not callable.



#### Eager Compatibility
When eager execution is enabled, `gate_gradients`, and `aggregation_method`
are ignored.



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
    name=None,
    grad_loss=None,
    stop_gradients=None,
    scale_loss_by_num_replicas=None
)
```

Add operations to minimize `loss` by updating `var_list`.

This method simply combines calls `compute_gradients()` and
`apply_gradients()`. If you want to process the gradient before applying
them call `compute_gradients()` and `apply_gradients()` explicitly instead
of using this function.

#### Args:

* <b>`loss`</b>: A `Tensor` containing the value to minimize.
* <b>`global_step`</b>: Optional `Variable` to increment by one after the variables
    have been updated.
* <b>`var_list`</b>: Optional list or tuple of `Variable` objects to update to
    minimize `loss`.  Defaults to the list of variables collected in the
    graph under the key `GraphKeys.TRAINABLE_VARIABLES`.
* <b>`gate_gradients`</b>: How to gate the computation of gradients.  Can be
    `GATE_NONE`, `GATE_OP`, or  `GATE_GRAPH`.
* <b>`aggregation_method`</b>: Specifies the method used to combine gradient terms.
    Valid values are defined in the class `AggregationMethod`.
* <b>`name`</b>: Optional name for the returned operation.
* <b>`grad_loss`</b>: Optional. A `Tensor` holding the gradient computed for `loss`.
* <b>`stop_gradients`</b>: Optional. A Tensor or list of tensors not to differentiate
    through.
* <b>`scale_loss_by_num_replicas`</b>: Optional boolean. If true, scale the loss down
    by the number of replicas. By default, auto-detects whether this is
    needed.


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
`gate_gradients`, `aggregation_method`, and `grad_loss` are ignored when
eager execution is enabled.



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

