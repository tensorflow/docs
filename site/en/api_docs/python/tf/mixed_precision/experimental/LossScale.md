description: Base class for all loss scales.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.mixed_precision.experimental.LossScale" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="update"/>
</div>

# tf.mixed_precision.experimental.LossScale

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L43-L198">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for all loss scales.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.train.experimental.LossScale`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.mixed_precision.experimental.LossScale`, `tf.compat.v1.train.experimental.LossScale`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.mixed_precision.experimental.LossScale()
</code></pre>



<!-- Placeholder for "Used in" -->

This is an abstract base class, so you cannot instantiate it directly.
Instead, use one of its concrete subclasses:
  * <a href="../../../tf/mixed_precision/experimental/DynamicLossScale.md"><code>tf.mixed_precision.experimental.DynamicLossScale</code></a> (recommended)
  * <a href="../../../tf/mixed_precision/experimental/FixedLossScale.md"><code>tf.mixed_precision.experimental.FixedLossScale</code></a>

It's recommended to use a loss scale with a
<a href="../../../tf/keras/mixed_precision/experimental/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.experimental.LossScaleOptimizer</code></a>, as its easier than
using a loss scale directly.

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

In most functions that accept a LossScale, you can also pass an int (such as
8) to create a `FixedLossScale` or the string `"dynamic"` to create a dynamic
loss scale.

## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L195-L198">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

Creates the LossScale from its config.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L190-L193">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>get_config()
</code></pre>

Returns the config of this loss scale.


<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L90-L125">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>update(
    grads
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads`
</td>
<td>
A nested structure of unscaled gradients, each which is the
gradient of the loss with respect to a weight. The gradients should have
already been divided by the loss scale being before passed to this
function. 'None' gradients are accepted, and are ignored.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>

<tr>
<td>
`update_op`
</td>
<td>
In eager mode, None. In graph mode, an op to update the loss
scale.
</td>
</tr><tr>
<td>
`should_apply_gradients`
</td>
<td>
Either a bool or a scalar boolean tensor. If
False, the caller should skip applying `grads` to the variables this
step.
</td>
</tr>
</table>



<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L85-L88">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>__call__()
</code></pre>

Returns the current loss scale as a scalar `float32` tensor.




