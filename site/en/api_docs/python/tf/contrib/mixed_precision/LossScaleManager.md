page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.mixed_precision.LossScaleManager


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L33-L70">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LossScaleManager`

Abstract loss scale manager class.



<!-- Placeholder for "Used in" -->

Loss scale managers with a different strategy should subclass this class.
Loss scaling is a process that:

1) Applies a multiplier on the loss before computing gradients, and
2) Applies the reciprocal of the multiplier on the gradients before they are
   applied on variables.

This class is used together with
<a href="../../../tf/contrib/mixed_precision/LossScaleOptimizer"><code>tf.contrib.mixed_precision.LossScaleOptimizer</code></a> for mixed precision training
(float32 variables and float16 ops) on Nvidia GPUs in order to achieve the
same model quality as single precision training, with the benefits of
potential higher throughput.

See <a href="../../../tf/contrib/mixed_precision/LossScaleOptimizer"><code>tf.contrib.mixed_precision.LossScaleOptimizer</code></a> for more details.

## Methods

<h3 id="get_loss_scale"><code>get_loss_scale</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L52-L55">View source</a>

``` python
get_loss_scale()
```

Returns the loss scale as a scalar `float32` tensor.


<h3 id="update_loss_scale"><code>update_loss_scale</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L57-L70">View source</a>

``` python
update_loss_scale(finite_grads)
```

Updates loss scale based on if gradients are finite in current step.


#### Args:


* <b>`finite_grads`</b>: bool scalar tensor indicating if all gradients are
  finite (i.e., not inf or nan).


#### Returns:

An op, when executed updates the loss scale. If eager execution is
enabled, does not return anything.
