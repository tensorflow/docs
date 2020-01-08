page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.DecoupledWeightDecayExtension

## Class `DecoupledWeightDecayExtension`





Defined in [`tensorflow/contrib/opt/python/training/weight_decay_optimizers.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/opt/python/training/weight_decay_optimizers.py).

This class allows to extend optimizers with decoupled weight decay.

It implements the decoupled weight decay described by Loshchilov & Hutter
(https://arxiv.org/pdf/1711.05101.pdf), in which the weight decay is
decoupled from the optimization steps w.r.t. to the loss function.
For SGD variants, this simplifies hyperparameter search since it decouples
the settings of weight decay and learning rate.
For adaptive gradient algorithms, it regularizes variables with large
gradients more than L2 regularization would, which was shown to yield better
training loss and generalization error in the paper above.

This class alone is not an optimizer but rather extends existing
optimizers with decoupled weight decay. We explicitly define the two examples
used in the above paper (SGDW and AdamW), but in general this can extend
any OptimizerX by using
`extend_with_weight_decay(OptimizerX, weight_decay=weight_decay)`.
In order for it to work, it must be the first class the Optimizer with
weight decay inherits from, e.g.

```python
class AdamWOptimizer(DecoupledWeightDecayExtension, adam.AdamOptimizer):
  def __init__(self, weight_decay, *args, **kwargs):
    super(AdamWOptimizer, self).__init__(weight_decay, *args, **kwargs).
```

Note that this extension decays weights BEFORE applying the update based
on the gradient, i.e. this extension only has the desired behaviour for
optimizers which do not depend on the value of'var' in the update step!

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    weight_decay,
    **kwargs
)
```

Construct the extension class that adds weight decay to an optimizer.

#### Args:

* <b>`weight_decay`</b>: A `Tensor` or a floating point value, the factor by which
    a variable is decayed in the update step.
* <b>`**kwargs`</b>: Optional list or tuple or set of `Variable` objects to
    decay.



## Methods

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



