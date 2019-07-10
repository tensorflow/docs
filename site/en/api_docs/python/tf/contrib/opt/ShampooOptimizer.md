page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.ShampooOptimizer

## Class `ShampooOptimizer`

The Shampoo Optimizer

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`contrib/opt/python/training/shampoo.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/opt/python/training/shampoo.py).

<!-- Placeholder for "Used in" -->

Variant of Adagrad using one preconditioner matrix per variable dimension.
For details, see https://arxiv.org/abs/1802.09568

gbar is time-weighted accumulated gradient:
gbar[t] = gbar_decay[t] * gbar[t-1] + gbar_weight[t] * g[t]

mat_gbar is time-weighted accumulated gradient square:
mat_gbar_j[t] = mat_gbar_decay[t] * mat_gbar_j[t-1]
                + mat_gbar_weight[t] * gg_j[t]
where if g[t] = g_abcd then gg_a[t] = g_abcd g_a'bcd (Einstein notation)

#### Update rule:


w[t+1] = w[t] - learning_rate[t] * Prod_j mat_gbar_j[t]^(-alpha/n) gbar[t]
   Again, mat_gbar_j[t]^(-alpha) gbar[t] is a tensor contraction along the
   j'th dimension of gbar[t] with the first dimension of
   mat_gbar_j[t]^(-alpha/n), where alpha is a hyperparameter,
   and n = rank of the variable.
   Prod_j represents doing this contraction for all j in 0..n-1.

Typically learning_rate is constant, but could be time dependent by passing
a lambda function that depends on step.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    global_step=0,
    max_matrix_size=768,
    gbar_decay=0.0,
    gbar_weight=1.0,
    mat_gbar_decay=1.0,
    mat_gbar_weight=1.0,
    learning_rate=1.0,
    svd_interval=1,
    precond_update_interval=1,
    epsilon=0.0001,
    alpha=0.5,
    use_iterative_root=False,
    use_locking=False,
    name='Shampoo'
)
```

Default values of the various hyper-parameters.

gbar_decay, gbar_weight etc. can be a float or a time varying parameter.
For time-varying parameters use e.g. "lambda T: T / (T + 1.0)"
where the expression in the lambda is a tensorflow expression

#### Args:


* <b>`global_step`</b>: tensorflow variable indicating the step.
* <b>`max_matrix_size`</b>: We do not perform SVD for matrices larger than this.
* <b>`gbar_decay`</b>: * <b>`gbar_weight`</b>:  Used to update gbar:
      gbar[t] = gbar_decay[t] * gbar[t-1] + gbar_weight[t] * g[t]
* <b>`mat_gbar_decay`</b>: * <b>`mat_gbar_weight`</b>:  Used to update mat_gbar:
     mat_gbar_j[t] = mat_gbar_decay[t] * mat_gbar_j[t-1]
                     + mat_gbar_weight[t] * gg_j[t]
* <b>`learning_rate`</b>: Similar to SGD
* <b>`svd_interval`</b>: We should do SVD after this many steps. Default = 1, i.e.
              every step. Usually 20 leads to no loss of accuracy, and
              50 or 100 is also OK. May also want more often early,
              and less often later - set in caller as for example:
              "svd_interval = lambda(T): tf.cond(
                  T < 2000, lambda: 20.0, lambda: 1000.0)"
* <b>`precond_update_interval`</b>: We should update the preconditioners after
                         this many steps. Default = 1. Usually less than
                         svd_interval.
* <b>`epsilon`</b>:  epsilon * I_n is added to each mat_gbar_j for stability for
          non-diagonal version of shampoo.
* <b>`alpha`</b>:  total power of the preconditioners.
* <b>`use_iterative_root`</b>: should the optimizer use SVD (faster) or the
                    iterative root method (for TPU) for finding the
                    roots of PSD matrices.
* <b>`use_locking`</b>: * <b>`name`</b>: name of optimizer.



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
takes no arguments and computes the value to be minimized. Minimization (and
gradient computation) is done with respect to the elements of `var_list` if
not None, else with respect to any trainable variables created during the
execution of the `loss` function. `gate_gradients`, `aggregation_method`,
`colocate_gradients_with_ops` and `grad_loss` are ignored when eager
execution is enabled.



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

* `GATE_GRAPH = 2` <a id="GATE_GRAPH"></a>
* `GATE_NONE = 0` <a id="GATE_NONE"></a>
* `GATE_OP = 1` <a id="GATE_OP"></a>
