page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.TowerOptimizer

## Class `TowerOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)

Gathers gradients from all towers and reduces them in the last one.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(optimizer_or_optimizer_fn)
```

Wrap an existing optimizer for gathering gradients across towers. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2018-05-31.
Instructions for updating:
Please use <a href="../../../tf/contrib/distribute/MirroredStrategy"><code>tf.contrib.distribute.MirroredStrategy</code></a> instead.

Each invocation of model_fn has to call the same optimizers in the same
order.

Multiple optimizers that use the same or different losses are supported.

If TowerOptimizer is used but `replicate_model_fn` isn't, then no
aggregation will happen.  All calls will simply be forwarded to the
underlying optimizer. The behavior is similar if there is only one tower.

If TowerOptimizer is used together with SyncReplicasOptimizer that wraps
the user's optimizer, then it's the SyncReplicasOptimizer that needs to be
wrapped with TowerOptimizer.

#### Args:

* <b>`optimizer_or_optimizer_fn`</b>: an instance of optimizer to wrap.  That
    instance is going to be used for optimizer-specific logic.  This can
    also be a no-argument function that returns such an optimizer instance.



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    **kwargs
)
```

Collect gradients updates to apply them with the last tower.

<h3 id="compute_gradients"><code>compute_gradients</code></h3>

``` python
compute_gradients(
    loss,
    *args,
    **kwargs
)
```

Compute gradients, but first, if needed, scale the loss.

<h3 id="get_name"><code>get_name</code></h3>

``` python
get_name(
    *args,
    **kwargs
)
```



<h3 id="get_slot"><code>get_slot</code></h3>

``` python
get_slot(
    *args,
    **kwargs
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
get_slot_names(
    *args,
    **kwargs
)
```

Return a list of the names of slots created by the `Optimizer`.

See `get_slot()`.

#### Returns:

A list of strings.

<h3 id="has_been_used"><code>has_been_used</code></h3>

``` python
@staticmethod
has_been_used()
```



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
takes no arguments and computes the value to be minimized. Minimization (and
gradient computation) is done with respect to the elements of `var_list` if
not None, else with respect to any trainable variables created during the
execution of the `loss` function. `gate_gradients`, `aggregation_method`,
`colocate_gradients_with_ops` and `grad_loss` are ignored when eager
execution is enabled.



<h3 id="variables"><code>variables</code></h3>

``` python
variables(
    *args,
    **kwargs
)
```

A list of variables which encode the current state of `Optimizer`.

Includes slot variables and additional global variables created by the
optimizer in the current default graph.

#### Returns:

A list of variables.



## Class Members

<h3 id="COLLECTION_FOR_GRAPH_STATES"><code>COLLECTION_FOR_GRAPH_STATES</code></h3>

<h3 id="GATE_GRAPH"><code>GATE_GRAPH</code></h3>

<h3 id="GATE_NONE"><code>GATE_NONE</code></h3>

<h3 id="GATE_OP"><code>GATE_OP</code></h3>

