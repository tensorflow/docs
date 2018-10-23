

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.optimizer.KfacOptimizer

## Class `KfacOptimizer`

Inherits From: [`GradientDescentOptimizer`](../../../../tf/train/GradientDescentOptimizer)



Defined in [`tensorflow/contrib/kfac/python/ops/optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/optimizer.py).

The KFAC Optimizer (https://arxiv.org/abs/1503.05671).

## Properties

<h3 id="damping"><code>damping</code></h3>



<h3 id="variables"><code>variables</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    learning_rate,
    cov_ema_decay,
    damping,
    layer_collection,
    momentum=0.0,
    momentum_type='regular',
    norm_constraint=None,
    name='KFAC'
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
      (Higher damping means the update looks more like a standard gradient
      update - see Tikhonov regularization.)
* <b>`layer_collection`</b>: The layer collection object, which holds the fisher
      blocks, kronecker factors, and losses associated with the
      graph.  The layer_collection cannot be modified after KfacOptimizer's
      initialization.
* <b>`momentum`</b>: The momentum value for this optimizer. Only applies when
      momentum_type is 'regular' or 'adam'. (Default: 0)
* <b>`momentum_type`</b>: The type of momentum to use in this optimizer, one of
      'regular', 'adam', or 'qmodel'. (Default: 'regular')
* <b>`norm_constraint`</b>: float or Tensor. If specified, the update is scaled down
      so that its approximate squared Fisher norm v^T F v is at most the
      specified value. May only be used with momentum type 'regular'.
      (Default: None)
* <b>`name`</b>: The name for this optimizer. (Default: 'KFAC')


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
    *args,
    **kwargs
)
```





## Class Members

<h3 id="GATE_GRAPH"><code>GATE_GRAPH</code></h3>

<h3 id="GATE_NONE"><code>GATE_NONE</code></h3>

<h3 id="GATE_OP"><code>GATE_OP</code></h3>

