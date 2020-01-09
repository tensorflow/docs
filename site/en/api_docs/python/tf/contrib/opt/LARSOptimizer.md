page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.LARSOptimizer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/lars_optimizer.py#L29-L178">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LARSOptimizer`

Layer-wise Adaptive Rate Scaling for large batch training.

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)

<!-- Placeholder for "Used in" -->

Introduced by "Large Batch Training of Convolutional Networks" by Y. You,
I. Gitman, and B. Ginsburg. (https://arxiv.org/abs/1708.03888)

Implements the LARS learning rate scheme presented in the paper above. This
optimizer is useful when scaling the batch size to up to 32K without
significant performance degradation. It is recommended to use the optimizer
in conjunction with:
    - Gradual learning rate warm-up
    - Linear learning rate scaling
    - Poly rule learning rate decay

Note, LARS scaling is currently only enabled for dense tensors. Sparse tensors
use the default momentum optimizer.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/lars_optimizer.py#L47-L96">View source</a>

``` python
__init__(
    learning_rate,
    momentum=0.9,
    weight_decay=0.0001,
    eeta=0.001,
    epsilon=0.0,
    name='LARSOptimizer',
    skip_list=None,
    use_nesterov=False
)
```

Construct a new LARS Optimizer.


#### Args:


* <b>`learning_rate`</b>: A `Tensor` or floating point value. The base learning rate.
* <b>`momentum`</b>: A floating point value. Momentum hyperparameter.
* <b>`weight_decay`</b>: A floating point value. Weight decay hyperparameter.
* <b>`eeta`</b>: LARS coefficient as used in the paper. Dfault set to LARS
  coefficient from the paper. (eeta / weight_decay) determines the highest
  scaling factor in LARS.
* <b>`epsilon`</b>: Optional epsilon parameter to be set in models that have very
  small gradients. Default set to 0.0.
* <b>`name`</b>: Optional name prefix for variables and ops created by LARSOptimizer.
* <b>`skip_list`</b>: List of strings to enable skipping variables from LARS scaling.
  If any of the strings in skip_list is a subset of var.name, variable
  'var' is skipped from LARS scaling. For a typical classification model
  with batch normalization, the skip_list is ['batch_normalization',
  'bias']
* <b>`use_nesterov`</b>: when set to True, nesterov momentum will be enabled


#### Raises:


* <b>`ValueError`</b>: If a hyperparameter is set to a non-sensical value.



## Methods

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L531-L638">View source</a>

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
* <b>`RuntimeError`</b>: If you should use `_distributed_apply()` instead.

<h3 id="compute_gradients"><code>compute_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L415-L519">View source</a>

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
  under the key <a href="/api_docs/python/tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a>.
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



<h3 id="compute_lr"><code>compute_lr</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/lars_optimizer.py#L102-L118">View source</a>

``` python
compute_lr(
    grad,
    var
)
```




<h3 id="get_name"><code>get_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L352-L353">View source</a>

``` python
get_name()
```




<h3 id="get_slot"><code>get_slot</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L735-L771">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L773-L781">View source</a>

``` python
get_slot_names()
```

Return a list of the names of slots created by the `Optimizer`.

See `get_slot()`.

#### Returns:

A list of strings.


<h3 id="minimize"><code>minimize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L355-L413">View source</a>

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
  the graph under the key <a href="/api_docs/python/tf/GraphKeys#TRAINABLE_VARIABLES"><code>GraphKeys.TRAINABLE_VARIABLES</code></a>.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/optimizer.py#L783-L809">View source</a>

``` python
variables()
```

A list of variables which encode the current state of `Optimizer`.

Includes slot variables and additional global variables created by the
optimizer in the current default graph.

#### Returns:

A list of variables.




## Class Members

* `GATE_GRAPH = 2` <a id="GATE_GRAPH"></a>
* `GATE_NONE = 0` <a id="GATE_NONE"></a>
* `GATE_OP = 1` <a id="GATE_OP"></a>
