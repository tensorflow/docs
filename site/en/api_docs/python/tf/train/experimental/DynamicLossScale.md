page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.experimental.DynamicLossScale


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/loss_scale.py#L270-L398">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `DynamicLossScale`

Loss scale that dynamically adjusts itself.

Inherits From: [`LossScale`](../../../tf/train/experimental/LossScale)

### Aliases:

* Class `tf.compat.v1.train.experimental.DynamicLossScale`
* Class `tf.compat.v2.train.experimental.DynamicLossScale`


<!-- Placeholder for "Used in" -->

Dynamic loss scaling works by adjusting the loss scale as training progresses.
The goal is to keep the loss scale as high as possible without overflowing the
gradients. As long as the gradients do not overflow, raising the loss scale
never hurts.

The algorithm starts by setting the loss scale to an initial value. Every N
steps that the gradients are finite, the loss scale is increased by some
factor. However, if a NaN or Inf gradient is found, the gradients for that
step are not applied, and the loss scale is decreased by the factor. This
process tends to keep the loss scale as high as possible without gradients
overflowing.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/loss_scale.py#L286-L316">View source</a>

``` python
__init__(
    initial_loss_scale=(2 ** 15),
    increment_period=2000,
    multiplier=2.0
)
```

Creates the dynamic loss scale.


#### Args:


* <b>`initial_loss_scale`</b>: A Python float.  The loss scale to use at the
  beginning. It's better to start this at a very high number, because a
  loss scale that is too high gets lowered far more quickly than a loss
  scale that is too low gets raised. The default is 2 ** 15, which is
  approximately half the maximum float16 value.
* <b>`increment_period`</b>: Increases loss scale every `increment_period`
  consecutive steps that finite gradients are encountered. If a nonfinite
  gradient is encountered, the count is reset back to zero.
* <b>`multiplier`</b>: The multiplier to use when increasing or decreasing the loss
  scale.



## Properties

<h3 id="increment_period"><code>increment_period</code></h3>




<h3 id="initial_loss_scale"><code>initial_loss_scale</code></h3>




<h3 id="multiplier"><code>multiplier</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/loss_scale.py#L330-L331">View source</a>

``` python
__call__()
```

Returns the current loss scale as a scalar `float32` tensor.


<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/loss_scale.py#L179-L182">View source</a>

``` python
from_config(
    cls,
    config
)
```

Creates the LossScale from its config.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/loss_scale.py#L393-L398">View source</a>

``` python
get_config()
```

Returns the config of this loss scale.


<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/experimental/loss_scale.py#L333-L380">View source</a>

``` python
update(grads)
```

Updates loss scale based on if gradients are finite in current step.
