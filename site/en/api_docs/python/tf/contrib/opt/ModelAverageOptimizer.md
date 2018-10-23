

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.opt.ModelAverageOptimizer

## Class `ModelAverageOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/opt/python/training/model_average_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/opt/python/training/model_average_optimizer.py).

Wrapper optimizer that implements the Model Average algorithm.

This is a sync optimizer. During the training, each worker will update
the local variables and maintains its own local_step, which starts from 0
and is incremented by 1 after each update of local variables. Whenever the
interval_steps divides the local step, the local variables from all the
workers will be averaged and assigned to global center variables. Then the
local variables will be assigned by global center variables.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    opt,
    num_worker,
    is_chief,
    ma_custom_getter,
    interval_steps=100,
    use_locking=True,
    name='ModelAverageOptimizer'
)
```

Construct a new model average optimizer.

#### Args:

* <b>`opt`</b>: The actual optimizer that will be used to update local variables
* <b>`num_worker`</b>: The number of workers
* <b>`is_chief`</b>: whether chief worker
* <b>`ma_custom_getter`</b>: ModelAverageCustomGetter
* <b>`interval_steps`</b>: An int point value to controls the frequency of the
    average of local variables
* <b>`use_locking`</b>: If True use locks for update operations
* <b>`name`</b>: string. Optional name of the returned operation

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```

Apply gradients to variables.

This contains most of the synchronization implementation and also wraps the
apply_gradients() from the real optimizer. The chief work updates global
variables.

#### Args:

* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs as returned by
    compute_gradients().
* <b>`global_step`</b>: Optional Variable to increment by one after the
    variables have been updated.
* <b>`name`</b>: Optional name for the returned operation.  Default to the
    name passed to the Optimizer constructor.


#### Returns:

A conditional 'Operation' that update both local and global variables or
just local variables


#### Raises:

* <b>`ValueError`</b>: If the grads_and_vars is empty.
* <b>`ValueError`</b>: If global step is not provided, the staleness cannot be
    checked.

<h3 id="compute_gradients"><code>compute_gradients</code></h3>

``` python
compute_gradients(
    *args,
    **kwargs
)
```

Compute gradients of "loss" for the variables in "var_list".

This simply wraps the compute_gradients() from the real optimizer.

#### Args:

* <b>`*args`</b>: Arguments for compute_gradients().
* <b>`**kwargs`</b>: Keyword arguments for compute_gradients().


#### Returns:

A list of (gradient, variable) pairs.

<h3 id="get_init_op"><code>get_init_op</code></h3>

``` python
get_init_op()
```

Returns the op.

This method lets all the local variables equal to the global
variables before the training begins.

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

<h3 id="make_session_run_hook"><code>make_session_run_hook</code></h3>

``` python
make_session_run_hook()
```

Creates a hook to handle ModelAverage ops such as initialization.

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

