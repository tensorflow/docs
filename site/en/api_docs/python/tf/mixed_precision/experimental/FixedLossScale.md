description: Loss scale with a fixed value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.mixed_precision.experimental.FixedLossScale" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="update"/>
</div>

# tf.mixed_precision.experimental.FixedLossScale

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/experimental/loss_scale.py#L222-L278">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loss scale with a fixed value.

Inherits From: [`LossScale`](../../../tf/mixed_precision/experimental/LossScale.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.train.experimental.FixedLossScale`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.mixed_precision.FixedLossScale`, `tf.compat.v1.mixed_precision.experimental.FixedLossScale`, `tf.compat.v1.train.experimental.FixedLossScale`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.mixed_precision.experimental.FixedLossScale(
    loss_scale_value
)
</code></pre>



<!-- Placeholder for "Used in" -->

WARNING: This class is deprecated and will be unexposed from the TF 2
namespace starting in TensorFlow 2.5. In TensorFlow 2.5, this class will only
be accessible as <a href="../../../tf/mixed_precision/experimental/FixedLossScale.md"><code>tf.compat.v1.mixed_precision.FixedLossScale</code></a>. Additionally
in 2.5, you will no longer be able to pass a `FixedLossScale` to a
<a href="../../../tf/keras/mixed_precision/Policy.md"><code>tf.keras.mixed_precision.Policy</code></a>. All the functionality in this class has
been merged into <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a>, so this class
is no longer needed.

The loss scale is not updated for the lifetime of instances of this class.
A given instance of this class always returns the same number when called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`loss_scale_value`
</td>
<td>
A Python float. Its ideal value varies depending on
models to run. Choosing a too small loss_scale might affect model
quality; a too big loss_scale might cause inf or nan. There is no single
right loss_scale to apply. There is no harm choosing a relatively big
number as long as no nan or inf is encountered in training.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If loss_scale_value is less than 1.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/experimental/loss_scale.py#L206-L209">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

Creates the LossScale from its config.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/experimental/loss_scale.py#L277-L278">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the config of this loss scale.


<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/experimental/loss_scale.py#L270-L272">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/experimental/loss_scale.py#L267-L268">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__()
</code></pre>

Returns the current loss scale as a scalar `float32` tensor.




