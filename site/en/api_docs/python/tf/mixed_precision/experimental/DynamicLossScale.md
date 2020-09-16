description: Loss scale that dynamically adjusts itself.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.mixed_precision.experimental.DynamicLossScale" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
<meta itemprop="property" content="update"/>
</div>

# tf.mixed_precision.experimental.DynamicLossScale

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L290-L418">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loss scale that dynamically adjusts itself.

Inherits From: [`LossScale`](../../../tf/mixed_precision/experimental/LossScale.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.train.experimental.DynamicLossScale`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.mixed_precision.experimental.DynamicLossScale`, `tf.compat.v1.train.experimental.DynamicLossScale`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.mixed_precision.experimental.DynamicLossScale(
    initial_loss_scale=(2 ** 15), increment_period=2000, multiplier=2.0
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`initial_loss_scale`
</td>
<td>
A Python float.  The loss scale to use at the
beginning. It's better to start this at a very high number, because a
loss scale that is too high gets lowered far more quickly than a loss
scale that is too low gets raised. The default is 2 ** 15, which is
approximately half the maximum float16 value.
</td>
</tr><tr>
<td>
`increment_period`
</td>
<td>
Increases loss scale every `increment_period`
consecutive steps that finite gradients are encountered. If a nonfinite
gradient is encountered, the count is reset back to zero.
</td>
</tr><tr>
<td>
`multiplier`
</td>
<td>
The multiplier to use when increasing or decreasing the loss
scale.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`increment_period`
</td>
<td>

</td>
</tr><tr>
<td>
`initial_loss_scale`
</td>
<td>

</td>
</tr><tr>
<td>
`multiplier`
</td>
<td>

</td>
</tr>
</table>



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L413-L418">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the config of this loss scale.


<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L353-L400">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update(
    grads
)
</code></pre>

Updates loss scale based on if gradients are finite in current step.


<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/experimental/loss_scale.py#L350-L351">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__()
</code></pre>

Returns the current loss scale as a scalar `float32` tensor.




