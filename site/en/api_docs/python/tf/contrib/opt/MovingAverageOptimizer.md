

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.opt.MovingAverageOptimizer

## Class `MovingAverageOptimizer`

Inherits From: [`Optimizer`](../../../tf/train/Optimizer)



Defined in [`tensorflow/contrib/opt/python/training/moving_average_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/opt/python/training/moving_average_optimizer.py).

Optimizer that computes a moving average of the variables.

Empirically it has been found that using the moving average of the trained
parameters of a deep network is better than using its trained parameters
directly. This optimizer allows you to compute this moving average and swap
the variables at save time so that any code outside of the training loop will
use by default the averaged values instead of the original ones.

Example of usage:

```python

// Encapsulate your favorite optimizer (here the momentum one)
// inside the MovingAverageOptimizer.
opt = tf.train.MomentumOptimizer(learning_rate, FLAGS.momentum)
opt = tf.contrib.opt.MovingAverageOptimizer(opt)
// Then create your model and all its variables.
model = build_model()
// Add the training op that optimizes using opt.
// This needs to be called before swapping_saver().
opt.minimize(cost, var_list)
// Then create your saver like this:
saver = opt.swapping_saver()
// Pass it to your training loop.
    slim.learning.train(
        model,
        ...
        saver=saver)
```

Note that for evaluation, the normal saver should be used instead of
swapping_saver().

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    opt,
    average_decay=0.9999,
    num_updates=None,
    sequential_update=True
)
```

Construct a new MovingAverageOptimizer.

#### Args:

* <b>`opt`</b>: A tf.Optimizer that will be used to compute and apply gradients.
* <b>`average_decay`</b>: Float.  Decay to use to maintain the moving averages
                 of trained variables.
                 See tf.train.ExponentialMovingAverage for details.
* <b>`num_updates`</b>: Optional count of number of updates applied to variables.
               See tf.train.ExponentialMovingAverage for details.
* <b>`sequential_update`</b>: Bool. If False, will compute the moving average at the
                     same time as the model is updated, potentially doing
                     benign data races.
                     If True, will update the moving average after gradient
                     updates.

<h3 id="apply_gradients"><code>apply_gradients</code></h3>

``` python
apply_gradients(
    grads_and_vars,
    global_step=None,
    name=None
)
```



<h3 id="compute_gradients"><code>compute_gradients</code></h3>

``` python
compute_gradients(
    *args,
    **kwargs
)
```



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



<h3 id="swapping_saver"><code>swapping_saver</code></h3>

``` python
swapping_saver(
    var_list=None,
    name='swapping_saver',
    **kwargs
)
```

Create a saver swapping moving averages and variables.

You should use this saver during training.  It will save the moving averages
of the trained parameters under the original parameter names.  For
evaluations or inference you should use a regular saver and it will
automatically use the moving averages for the trained variable.

You must call this function after all variables have been created and after
you have called Optimizer.minimize().

#### Args:

* <b>`var_list`</b>: List of variables to save, as per `Saver()`.
            If set to None, will save all the variables that have been
            created before this call.
* <b>`name`</b>: The name of the saver.
* <b>`**kwargs`</b>: Keyword arguments of `Saver()`.


#### Returns:

A `tf.train.Saver` object.


#### Raises:

* <b>`RuntimeError`</b>: If apply_gradients or minimize has not been called before.

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

