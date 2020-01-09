page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.mixed_precision.ExponentialUpdateLossScaleManager


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L104-L200">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ExponentialUpdateLossScaleManager`

Loss scale manager uses an exponential update strategy.

Inherits From: [`LossScaleManager`](../../../tf/contrib/mixed_precision/LossScaleManager)

<!-- Placeholder for "Used in" -->

In general, the strategy increases loss scale by a greater-than-one factor
after encountering a consecutive series of steps with finite gradients;
Similarly, it decreases the loss scale by a factor when the accumulated number
of steps with non-finite (nan or inf) gradients are met. An update is not
applied if its result is less than 1 or overflows the float32 dynamic range.

The number of finite and non-finite steps are cleared every time the loss
scale is changed. The condition to decrease the loss scale is looser than to
increase it since the former does not require the steps to be consecutive.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L118-L148">View source</a>

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



## Methods

<h3 id="get_loss_scale"><code>get_loss_scale</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L155-L157">View source</a>

``` python
get_loss_scale()
```

Returns the loss scale.


<h3 id="update_loss_scale"><code>update_loss_scale</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L159-L200">View source</a>

``` python
update_loss_scale(finite_grads)
```

Updates loss scale based on if gradients are finite in current step.
