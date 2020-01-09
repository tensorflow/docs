page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.experimental.LossScale


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/train/experimental/LossScale">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/experimental/loss_scale.py#L40-L182">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LossScale`

Loss scale base class.

Inherits From: [`CheckpointableBase`](../../../tf/contrib/checkpoint/CheckpointableBase)

### Aliases:

* Class <a href="/api_docs/python/tf/train/experimental/LossScale"><code>tf.compat.v1.train.experimental.LossScale</code></a>
* Class <a href="/api_docs/python/tf/train/experimental/LossScale"><code>tf.compat.v2.train.experimental.LossScale</code></a>


<!-- Placeholder for "Used in" -->

Loss scaling is a process that multiplies the loss by a multiplier called the
loss scale, and divides each gradient by the same multiplier. The pseudocode
for this process is:

```
loss = ...
loss *= loss_scale
grads = gradients(loss, vars)
grads /= loss_scale
```

Mathematically, loss scaling has no effect, but can help avoid numerical
underflow in intermediate gradients when float16 tensors are used for mixed
precision training. By multiplying the loss, each intermediate gradient will
have the same multiplier applied.

Instances of this class represent a loss scale. Calling instances of this
class returns the loss scale as a scalar float32 tensor, while method
`update()` updates the loss scale depending on the values of the gradients.
Optimizers use instances of this class to scale loss and gradients.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/experimental/loss_scale.py#L65-L67">View source</a>

``` python
__init__()
```

Initializes the loss scale class.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/experimental/loss_scale.py#L69-L72">View source</a>

``` python
__call__()
```

Returns the current loss scale as a scalar `float32` tensor.


<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/experimental/loss_scale.py#L179-L182">View source</a>

``` python
@classmethod
from_config(
    cls,
    config
)
```

Creates the LossScale from its config.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/experimental/loss_scale.py#L174-L177">View source</a>

``` python
get_config()
```

Returns the config of this loss scale.


<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/experimental/loss_scale.py#L74-L109">View source</a>

``` python
update(grads)
```

Updates the value of the loss scale.

The loss scale will be potentially updated, based on the value of `grads`.
The tensor returned by calling this class is only updated when this function
is evaluated.

In eager mode, this directly updates the loss scale, so that calling
`__call__` will return the newly updated loss scale. In graph mode,
this returns an op that, when evaluated, updates the loss scale.

This function also returns a `should_apply_gradients` bool. If False,
gradients should not be applied to the variables that step, as nonfinite
gradients were found, and the loss scale has been be updated to reduce the
chance of finding nonfinite gradients in the next step. Some loss scale
classes will always return True, as they cannot adjust themselves in
response to nonfinite gradients.

When a DistributionStrategy is used, this function may only be called in a
cross-replica context.

#### Args:


* <b>`grads`</b>: A nested structure of unscaled gradients, each which is the
  gradient of the loss with respect to a weight. The gradients should have
  already been divided by the loss scale being before passed to this
  function. 'None' gradients are accepted, and are ignored.


#### Returns:


* <b>`update_op`</b>: In eager mode, None. In graph mode, an op to update the loss
  scale.
* <b>`should_apply_gradients`</b>: Either a bool or a scalar boolean tensor. If
  False, the caller should skip applying `grads` to the variables this
  step.
