

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.AdamWOptimizer

## Class `AdamWOptimizer`

Inherits From: [`DecoupledWeightDecayExtension`](../../../tf/contrib/opt/DecoupledWeightDecayExtension), [`AdamOptimizer`](../../../tf/train/AdamOptimizer)



Defined in [`tensorflow/contrib/opt/python/training/weight_decay_optimizers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/opt/python/training/weight_decay_optimizers.py).

Optimizer that implements the Adam algorithm with weight decay.

This is an implementation of the AdamW optimizer described in "Fixing
Weight Decay Regularization in Adam" by Loshchilov & Hutter
(https://arxiv.org/abs/1711.05101)
([pdf])(https://arxiv.org/pdf/1711.05101.pdf).

It computes the update step of `train.AdamOptimizer` and additionally decays
the variable. Note that this is different from adding L2 regularization on
the variables to the loss: it regularizes variables with large
gradients more than L2 regularization would, which was shown to yield better
training loss and generalization error in the paper above.

For further information see the documentation of the Adam Optimizer.

Note that this optimizer can also be instantiated as

```python
extend_with_weight_decay(tf.train.AdamOptimizer, weight_decay=weight_decay)
```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    weight_decay,
    learning_rate=0.001,
    beta1=0.9,
    beta2=0.999,
    epsilon=1e-08,
    use_locking=False,
    name='AdamW'
)
```

Construct a new AdamW optimizer.

For further information see the documentation of the Adam Optimizer.

#### Args:

* <b>`weight_decay`</b>:  A `Tensor` or a floating point value.  The weight decay.
* <b>`learning_rate`</b>: A Tensor or a floating point value.  The learning rate.
* <b>`beta1`</b>: A float value or a constant float tensor.
    The exponential decay rate for the 1st moment estimates.
* <b>`beta2`</b>: A float value or a constant float tensor.
    The exponential decay rate for the 2nd moment estimates.
* <b>`epsilon`</b>: A small constant for numerical stability. This epsilon is
    "epsilon hat" in the Kingma and Ba paper (in the formula just before
    Section 2.1), not the epsilon in Algorithm 1 of the paper.
* <b>`use_locking`</b>: If True use locks for update operations.
* <b>`name`</b>: Optional name for the operations created when applying gradients.
    Defaults to "Adam".

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None,
    decay_var_list=None
)
```

Apply gradients to variables and decay the variables.

This function is the same as Optimizer.apply_gradients except that it
allows to specify the variables that should be decayed using
decay_var_list. If decay_var_list is None, all variables in var_list
are decayed.

For more information see the documentation of Optimizer.apply_gradients.

#### Args:

* <b>`grads_and_vars`</b>: List of (gradient, variable) pairs as returned by
    `compute_gradients()`.
* <b>`global_step`</b>: Optional `Variable` to increment by one after the
    variables have been updated.
* <b>`name`</b>: Optional name for the returned operation.  Default to the
    name passed to the `Optimizer` constructor.
* <b>`decay_var_list`</b>: Optional list of decay variables.


#### Returns:

An `Operation` that applies the specified gradients. If `global_step`
was not None, that operation also increments `global_step`.

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
    gate_gradients=optimizer.Optimizer.GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    name=None,
    grad_loss=None,
    decay_var_list=None
)
```

Add operations to minimize `loss` by updating `var_list` with decay.

This function is the same as Optimizer.minimize except that it allows to
specify the variables that should be decayed using decay_var_list.
If decay_var_list is None, all variables in var_list are decayed.

For more information see the documentation of Optimizer.minimize.

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
* <b>`decay_var_list`</b>: Optional list of decay variables.


#### Returns:

An Operation that updates the variables in `var_list`.  If `global_step`
was not `None`, that operation also increments `global_step`.

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

