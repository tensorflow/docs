page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.mixed_precision.ExponentialUpdateLossScaleManager

## Class `ExponentialUpdateLossScaleManager`

Inherits From: [`LossScaleManager`](../../../tf/contrib/mixed_precision/LossScaleManager)



Defined in [`tensorflow/contrib/mixed_precision/python/loss_scale_manager.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py).

Loss scale manager uses an exponential update strategy.

In general, the strategy increases loss scale by a greater-than-one factor
after encountering a consecutive series of steps with finite gradients;
Similarly, it decreases the loss scale by a factor when the accumulated number
of steps with non-finite (nan or inf) gradients are met. An update is not
applied if its result is less than 1 or overflows the float32 dynamic range.

The number of finite and non-finite steps are cleared every time the loss
scale is changed. The condition to decrease the loss scale is looser than to
increase it since the former does not require the steps to be consecutive.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    init_loss_scale,
    incr_every_n_steps,
    decr_every_n_nan_or_inf=2,
    incr_ratio=2,
    decr_ratio=0.8
)
```

Constructor of exponential-update loss scale manager.

#### Args:

* <b>`init_loss_scale`</b>: A Python float.  The loss scale to use at the beginning.
* <b>`incr_every_n_steps`</b>: Increases loss scale every n consecutive steps with
    finite gradients.
* <b>`decr_every_n_nan_or_inf`</b>: Decreases loss scale every n accumulated steps
    with nan or inf gradients.
* <b>`incr_ratio`</b>: The multiplier to use when increasing the loss scale.
* <b>`decr_ratio`</b>: The less-than-one-multiplier to use when decreasing the loss
    scale.

<h3 id="get_loss_scale"><code>get_loss_scale</code></h3>

``` python
get_loss_scale()
```

Returns the loss scale.

<h3 id="update_loss_scale"><code>update_loss_scale</code></h3>

``` python
update_loss_scale(finite_grads)
```

Updates loss scale based on if gradients are finite in current step.



