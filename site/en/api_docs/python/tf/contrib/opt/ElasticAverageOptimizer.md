page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.ElasticAverageOptimizer

## Class `ElasticAverageOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/opt/python/training/elastic_average_optimizer.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/opt/python/training/elastic_average_optimizer.py).

Wrapper optimizer that implements the Elastic Average SGD algorithm.
This is an async optimizer. During the training, Each worker will update
the local variables and maintains its own local_step, which starts from 0
and is incremented by 1 after each update of local variables. Whenever
the communication period divides the local step, the worker requests
the current global center variables and then computed the elastic difference
between global center variables and local variables. The elastic difference
then be used to update both local variables and global variables.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    opt,
    num_worker,
    ea_custom_getter,
    communication_period=10,
    moving_rate=None,
    rho=None,
    use_locking=True,
    synchronous=False,
    name='ElasticAverageOptimizer'
)
```

Construct a new gradient descent optimizer.

#### Args:

* <b>`opt`</b>: The actual optimizer that will be used to update local variables.
    Must be one of the Optimizer classes.
* <b>`num_worker`</b>: The number of workers
* <b>`ea_custom_getter`</b>: The ElasticAverageCustomGetter
* <b>`communication_period`</b>: An int point value to controls the frequency
    of the communication between every worker and the ps.
* <b>`moving_rate`</b>: A floating point value to control the elastic difference.
* <b>`rho`</b>: the amount of exploration we allow in the model. The default
    value is moving_rate/learning_rate
    rho=0.0 is suggested in async mode.
* <b>`use_locking`</b>: If True use locks for update operations.
* <b>`synchronous`</b>: Add_sync_queues_and_barrier or not.
          True: all workers will wait for each other before start training
          False: worker can start training when its initilization is done,
                 no need to wait for everyone is ready.
                 in case one worker is restarted, it can join and continue
                 training without being blocked.
* <b>`name`</b>: Optional name prefix for the operations created when applying
    gradients. Defaults to "ElasticAverageOptimizer".



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```

Apply gradients to global variables.

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
    gate_gradients=optimizer.Optimizer.GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    grad_loss=None
)
```

Compute gradients of `loss` for the variables in `var_list`.

Add rho*elastic_difference to loss to control the exploration
This is the first part of `minimize()`.  It returns a list
of (gradient, variable) pairs where "gradient" is the gradient
for "variable".  Note that "gradient" can be a `Tensor`, an
`IndexedSlices`, or `None` if there is no gradient for the
given variable.

#### Args:

* <b>`loss`</b>: A Tensor containing the value to minimize.
* <b>`var_list`</b>: Optional list or tuple of <a href="../../../tf/Variable"><code>tf.Variable</code></a> to update to minimize
    `loss`.  Defaults to the list of variables collected in the graph
    under the key `GraphKey.TRAINABLE_VARIABLES`.
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

<h3 id="get_init_op"><code>get_init_op</code></h3>

``` python
get_init_op(task_index)
```

Returns the op to let all the local variables and local center
variables equal to the global center variables before the training begins

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
make_session_run_hook(
    is_chief,
    task_index
)
```

Creates a hook to handle ElasticAverageOptimizerHook ops such as initialization.

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



<h3 id="swapping_saver"><code>swapping_saver</code></h3>

``` python
swapping_saver(
    var_list=None,
    name='swapping_saver',
    **kwargs
)
```

Create a saver copy global_center_variable to trainable variables
Please call this function after all your variables created with
ElasticAverageCustomGetter. For evaluations or inference, use this saver
during training.  It will save the global_center_variable of the trained
parameters under the original parameter names.
#### Args:

* <b>`var_list`</b>: List of variables to save, as per `Saver()`.
            If set to None, save all the trainable_variables that have
            been created before this call.
* <b>`name`</b>: The name of the saver.
* <b>`**kwargs`</b>: Keyword arguments of `Saver()`.

#### Returns:

A <a href="../../../tf/train/Saver"><code>tf.train.Saver</code></a> object.

#### Raises:

* <b>`RuntimeError`</b>: global_center_variable is empty, please make sure
                this is called after model created and
                ElasticAverageCustomGetter is used when declaring you model

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

<h3 id="BETA"><code>BETA</code></h3>

<h3 id="GATE_GRAPH"><code>GATE_GRAPH</code></h3>

<h3 id="GATE_NONE"><code>GATE_NONE</code></h3>

<h3 id="GATE_OP"><code>GATE_OP</code></h3>

