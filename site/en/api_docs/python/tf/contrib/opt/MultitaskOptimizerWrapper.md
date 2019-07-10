page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.MultitaskOptimizerWrapper

## Class `MultitaskOptimizerWrapper`

Optimizer wrapper making all-zero gradients harmless.





Defined in [`contrib/opt/python/training/multitask_optimizer_wrapper.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/opt/python/training/multitask_optimizer_wrapper.py).

<!-- Placeholder for "Used in" -->

This might be useful when a multi-task loss is used,
and some components of the loss might be
not present (e.g. masked out) in some training batches.
Technically their gradient would be zero,
which would normally affect the optimizer state
(e.g. push running average to zero).
However this is not the desired behaviour,
since the missing loss component
should be treated as unknown rather than zero.

This wrapper filters out all-zero gradient tensors,
therefore preserving the optimizer state.

If gradient clipping by global norm is used,
the provided function clip_gradients_by_global_norm
should be used (and specified explicitly by the user).
Otherwise the global norm would be underestimated
because of all-zero tensors that should be ignored.

The gradient calculation and application
are delegated to an underlying optimizer.
The gradient application is altered only for all-zero tensors.

#### Example:


```python
momentum_optimizer = tf.compat.v1.train.MomentumOptimizer(
  learning_rate, momentum=0.9)
multitask_momentum_optimizer = tf.contrib.opt.MultitaskOptimizerWrapper(
  momentum_optimizer)
gradvars = multitask_momentum_optimizer.compute_gradients(
  loss)
gradvars_clipped, _ = tf.contrib.opt.clip_gradients_by_global_norm(
  gradvars, 15.0)
train_op = multitask_momentum_optimizer.apply_gradients(
  gradvars_clipped, global_step=batch)
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(opt)
```

Constructor.


#### Args:


* <b>`opt`</b>: an instance of a class that implements tf.train.Optimizer.



