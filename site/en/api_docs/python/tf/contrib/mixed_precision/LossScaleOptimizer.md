page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.mixed_precision.LossScaleOptimizer

## Class `LossScaleOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/mixed_precision/python/loss_scale_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/mixed_precision/python/loss_scale_optimizer.py).

An optimizer that applies loss scaling in backprop.

This class is useful for "mixed precision training" on GPUs (or other
potential accelerators), an approach to improve compute throughput without
compromising model quality.

The canonical way to perform mixed precision training is the following:
* Model variables are kept in high precision (e.g. float32).
* Computations are done in lower precision (e.g. float16), which enjoys
  performance speedup by virtue of hardware support. Variables are casted to
  lower precision before they're used.
* Final gradients are casted back to high precision dtype, then used to update
  variables.

The side-effect of performing computation in lower precision, is that it comes
with smaller numerical range. During backproping, small gradients might
underflow in the reduced numerical range, causing a model to converge at
suboptimal level.

To prevent underflow, this optimizer multiplies the loss by a factor before
backprop starts. Consequently, the gradients are linearly scaled up by the
same factor, thus not falling into the underflow zone. After that, to perserve
the correctness of backprop, the gradients are down-scaled by the same factor,
casted to the (higher) variable precision, then applied on the variables.

See [Nvidia's manual on mixed precision training](
https://docs.nvidia.com/deeplearning/sdk/mixed-precision-training/index.html)
for more details.

To use loss scale optimizer, one only needs choose a loss scale strategy and
wrap a regular optimizer. See examples below.

```
loss = loss_fn()
opt = tf.AdamOptimizer(learning_rate=...)

# Choose a loss scale manager which decides how to pick the right loss scale
# throughout the training process.
loss_scale_manger = tf.contrib.mixed_precision.FixedLossScaleManager(5000)

# Wraps the original optimizer in a LossScaleOptimizer.
loss_scale_optimizer = LossScaleOptimizer(opt, loss_scale_manager)

# Call minimize() on the loss scale optimizer.
train_op = loss_scale_optimizer.minimize(loss)
```

If gradients clipping is applied, one can call
`optimizer.compute_gradients()` and `optimizer.apply_gradients()`
separately.

Notice the following way of using LossScaleOptimizer is not intended. Always
use `loss_scale_optimizer.compute_gradients()` to compute gradients instead of
`tf.gradients()` if doing mixed precision training.

```
# The following is a wrong way to use LossScaleOptimizer along with
# tf.gradients().

# Always use loss_scale_optimizer.compute_gradients() to compute grads, or
# loss scale is not correctly applied.
grads = tf.gradients(loss, ...)

# Do some custom grad clipping.
grads = clip_grads(grads, ...)

loss_scale_optimizer.apply(grads_and_vars)
```

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    opt,
    loss_scale_manager
)
```

Construct a loss scaling optimizer.

#### Args:

* <b>`opt`</b>: The actual optimizer that will be used to compute and apply the
    gradients. Must be an implementation of the <a href="../../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a>
    interface.
* <b>`loss_scale_manager`</b>: A LossScaleManager object.

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```

Apply gradients. See base class <a href="../../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a>.

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

Compute gradients. See base class <a href="../../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a>.

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

