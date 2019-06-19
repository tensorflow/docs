page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.PowerSignOptimizer

## Class `PowerSignOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/opt/python/training/powersign.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/opt/python/training/powersign.py).

Optimizer that implements the PowerSign update.

See [Bello et al., ICML2017],
[Neural Optimizer Search with RL](https://arxiv.org/abs/1709.07417).

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    learning_rate=0.1,
    base=math.e,
    beta=0.9,
    sign_decay_fn=None,
    use_locking=False,
    name='PowerSignOptimizer'
)
```

Constructs a new PowerSignOptimizer object.

Initialization:

```
m_0 <- 0 (Initialize initial 1st moment vector)
t <- 0 (Initialize timestep)
```

Update:

```
t <- t + 1
m_t <- beta1 * m_{t-1} + (1 - beta1) * g
sign_decay <- sign_decay_fn(t)
update <- base ** (sign_decay * sign(g) * sign(m)) * g
variable <- variable - lr_t * update
```

Example usage for PowerSign-cd (PowerSign with cosine sign decay)

```
decay_steps = 1000
linear_decay_fn = sign_decays.get_linear_decay_fn(decay_steps)
opt = PowerSignOptimizer(learning_rate=0.1, sign_decay_fn=linear_decay_fn)
```

#### Args:

* <b>`learning_rate`</b>: learning_rate used when taking a step.
* <b>`base`</b>: base used in optimizer.
* <b>`beta`</b>: decay used for computing the moving average m.
* <b>`sign_decay_fn`</b>: decay function applied to the sign(g) sign(m) quantity.
      Takes global_step as an argument. See sign_decay.py for some examples.
* <b>`use_locking`</b>: If True, use locks for update operations.
* <b>`name`</b>: Optional name for the operations created iwhen applying gradients.
    Defaults to "PowerSignOptimizer".

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```



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

* <b>`loss`</b>: A Tensor containing the value to minimize or a callable taking
    no arguments which returns the value to minimize. When eager execution
    is enabled it must be a callable.
* <b>`var_list`</b>: Optional list or tuple of <a href="../../../tf/Variable"><code>tf.Variable</code></a> to update to minimize
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
* <b>`RuntimeError`</b>: If called with eager execution enabled and `loss` is
    not callable.



#### Eager Compatibility
When eager execution is enabled, `gate_gradients`, `aggregation_method`,
and `colocate_gradients_with_ops` are ignored.



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

