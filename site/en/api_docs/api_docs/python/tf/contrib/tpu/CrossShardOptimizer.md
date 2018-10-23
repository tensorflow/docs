

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.CrossShardOptimizer

## Class `CrossShardOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/tpu/python/tpu/tpu_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/tpu/python/tpu/tpu_optimizer.py).

An optimizer that averages gradients across TPU shards.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    opt,
    reduction=losses.Reduction.MEAN,
    name='CrossShardOptimizer'
)
```

Construct a new cross-shard optimizer.

#### Args:

* <b>`opt`</b>: An existing `Optimizer` to encapsulate.
* <b>`reduction`</b>: The reduction to apply to the shard losses.
* <b>`name`</b>: Optional name prefix for the operations created when applying
    gradients. Defaults to "CrossShardOptimizer".


#### Raises:

* <b>`ValueError`</b>: If reduction is not a valid cross-shard reduction.

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```

Apply gradients to variables.

Calls tpu_ops.cross_replica_sum() to sum gradient contributions across
replicas, and then applies the real optimizer.

#### Args:

* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs as returned by
    compute_gradients().
* <b>`global_step`</b>: Optional Variable to increment by one after the
    variables have been updated.
* <b>`name`</b>: Optional name for the returned operation.  Default to the
    name passed to the Optimizer constructor.


#### Returns:

An `Operation` that applies the gradients. If `global_step` was not None,
that operation also increments `global_step`.


#### Raises:

* <b>`ValueError`</b>: If the grads_and_vars is malformed.

<h3 id="compute_gradients"><code>compute_gradients</code></h3>

``` python
compute_gradients(
    loss,
    var_list=None,
    **kwargs
)
```

Compute gradients of "loss" for the variables in "var_list".

This simply wraps the compute_gradients() from the real optimizer. The
gradients will be aggregated in the apply_gradients() so that user can
modify the gradients like clipping with per replica global norm if needed.
The global norm with aggregated gradients can be bad as one replica's huge
gradients can hurt the gradients from other replicas.

#### Args:

* <b>`loss`</b>: A Tensor containing the value to minimize.
* <b>`var_list`</b>: Optional list or tuple of `tf.Variable` to update to minimize
    `loss`.  Defaults to the list of variables collected in the graph
    under the key `GraphKey.TRAINABLE_VARIABLES`.
* <b>`**kwargs`</b>: Keyword arguments for compute_gradients().


#### Returns:

A list of (gradient, variable) pairs.


#### Raises:

* <b>`ValueError`</b>: If not within a tpu_shard_context.

<h3 id="get_name"><code>get_name</code></h3>

``` python
get_name()
```



<h3 id="get_slot"><code>get_slot</code></h3>

``` python
get_slot(
    *args,
    **kwargs
)
```

Return a slot named "name" created for "var" by the Optimizer.

This simply wraps the get_slot() from the actual optimizer.

#### Args:

* <b>`*args`</b>: Arguments for get_slot().
* <b>`**kwargs`</b>: Keyword arguments for get_slot().


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

This simply wraps the get_slot_names() from the actual optimizer.

#### Args:

* <b>`*args`</b>: Arguments for get_slot().
* <b>`**kwargs`</b>: Keyword arguments for get_slot().


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



## Class Members

<h3 id="GATE_GRAPH"><code>GATE_GRAPH</code></h3>

<h3 id="GATE_NONE"><code>GATE_NONE</code></h3>

<h3 id="GATE_OP"><code>GATE_OP</code></h3>

