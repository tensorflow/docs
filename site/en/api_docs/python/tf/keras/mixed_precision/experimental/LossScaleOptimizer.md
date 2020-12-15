description: An deprecated optimizer that applies loss scaling.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.experimental.LossScaleOptimizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_scaled_loss"/>
<meta itemprop="property" content="get_unscaled_gradients"/>
</div>

# tf.keras.mixed_precision.experimental.LossScaleOptimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py#L940-L1110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An deprecated optimizer that applies loss scaling.

Inherits From: [`LossScaleOptimizer`](../../../../tf/keras/mixed_precision/LossScaleOptimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.mixed_precision.experimental.LossScaleOptimizer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.experimental.LossScaleOptimizer(
    optimizer, loss_scale
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: This class is deprecated and will be removed in TensorFlow 2.5.
Please use the non-experimental class
<a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> instead.

This class is identical to the non-experimental
<a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>keras.mixed_precision.LossScaleOptimizer</code></a> except its constructor takes
different arguments. For this class (the experimental version), the
constructor takes a `loss_scale` argument.  For the non-experimental class,
the constructor encodes the loss scaling information in multiple arguments.
Note that unlike this class, the non-experimental class does not accept a
<a href="../../../../tf/mixed_precision/experimental/LossScale.md"><code>tf.compat.v1.mixed_precision.LossScale</code></a>, which is deprecated.

If you currently use this class, you should switch to the non-experimental
<a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> instead. We show several
examples of converting the use of the experimental class to the equivalent
non-experimental class.

```
>>> # In all of the the examples below, `opt1` and `opt2` are identical
>>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
...     tf.keras.optimizers.SGD(), loss_scale='dynamic')
>>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
...     tf.keras.optimizers.SGD())
>>> assert opt1.get_config() == opt2.get_config()
```

```
>>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
...     tf.keras.optimizers.SGD(), loss_scale=123)
>>> # dynamic=False indicates to use fixed loss scaling. initial_scale=123
>>> # refers to the initial loss scale, which is the single fixed loss scale
>>> # when dynamic=False.
>>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
...     tf.keras.optimizers.SGD(), dynamic=False, initial_scale=123)
>>> assert opt1.get_config() == opt2.get_config()
```

```
>>> loss_scale = tf.compat.v1.mixed_precision.experimental.DynamicLossScale(
...     initial_loss_scale=2048, increment_period=500)
>>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
...     tf.keras.optimizers.SGD(), loss_scale=loss_scale)
>>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
...     tf.keras.optimizers.SGD(), initial_scale=2048,
...     dynamic_growth_steps=500)
>>> assert opt1.get_config() == opt2.get_config()
```

Make sure to also switch from this class to the non-experimental class in
isinstance checks, if you have any. If you do not do this, your model may run
into hard-to-debug issues, as the experimental `LossScaleOptimizer` subclasses
the non-experimental `LossScaleOptimizer`, but not vice versa. It is safe to
switch isinstance checks to the non-experimental `LossScaleOptimizer` even
before using the non-experimental `LossScaleOptimizer`.

```
>>> opt1 = tf.keras.mixed_precision.experimental.LossScaleOptimizer(
...     tf.keras.optimizers.SGD(), loss_scale='dynamic')
>>> # The experimental class subclasses the non-experimental class
>>> isinstance(opt1, tf.keras.mixed_precision.LossScaleOptimizer)
True
>>> opt2 = tf.keras.mixed_precision.LossScaleOptimizer(
...     tf.keras.optimizers.SGD())
>>> # The non-experimental class does NOT subclass the experimental class.
>>> isinstance(opt2, tf.keras.mixed_precision.experimental.LossScaleOptimizer)
False
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`optimizer`
</td>
<td>
The Optimizer instance to wrap.
</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
The loss scale to scale the loss and gradients. This can
either be an int/float to use a fixed loss scale, the string "dynamic"
to use dynamic loss scaling, or an instance of a LossScale. The string
"dynamic" equivalent to passing `DynamicLossScale()`, and passing an
int/float is equivalent to passing a FixedLossScale with the given loss
scale. If a DynamicLossScale is passed, DynamicLossScale.multiplier must
be 2 (the default).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
String. The name to use for momentum accumulator weights created
by the optimizer.
</td>
</tr><tr>
<td>
`gradient_aggregator`
</td>
<td>
The function to use to aggregate gradients across
devices (when using <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>). If `None`, defaults to
summing the gradients across devices. The function should accept and
return a list of `(gradient, variable)` tuples.
</td>
</tr><tr>
<td>
`gradient_transformers`
</td>
<td>
Optional. List of functions to use to transform
gradients before applying updates to Variables. The functions are
applied after `gradient_aggregator`. The functions should accept and
return a list of `(gradient, variable)` tuples.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
keyword arguments. Allowed arguments are `clipvalue`,
`clipnorm`, `global_clipnorm`.
If `clipvalue` (float) is set, the gradient of each weight
is clipped to be no higher than this value.
If `clipnorm` (float) is set, the gradient of each weight
is individually clipped so that its norm is no higher than this value.
If `global_clipnorm` (float) is set the gradient of all weights is
clipped so that their global norm is no higher than this value.
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
in case of any invalid argument.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dynamic`
</td>
<td>
Bool indicating whether dynamic loss scaling is used.
</td>
</tr><tr>
<td>
`dynamic_counter`
</td>
<td>
The number of steps since the loss scale was last increased or decreased.

This is None if <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic"><code>LossScaleOptimizer.dynamic</code></a> is False.

The counter is incremented every step. Once it reaches
<a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic_growth_steps"><code>LossScaleOptimizer.dynamic_growth_steps</code></a>, the loss scale will be doubled
and the counter will be reset back to zero. If nonfinite gradients are
encountered, the loss scale will be halved and the counter will be reset
back to zero.
</td>
</tr><tr>
<td>
`dynamic_growth_steps`
</td>
<td>
The number of steps it takes to increase the loss scale.

This is None if <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic"><code>LossScaleOptimizer.dynamic</code></a> is False.

Every `dynamic_growth_steps` consecutive steps with finite gradients, the
loss scale is increased.
</td>
</tr><tr>
<td>
`initial_scale`
</td>
<td>
The initial loss scale.

If <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic"><code>LossScaleOptimizer.dynamic</code></a> is False, this is the same number as
<a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale</code></a>, as the loss scale never changes.
</td>
</tr><tr>
<td>
`inner_optimizer`
</td>
<td>
The optimizer that this LossScaleOptimizer is wrapping.
</td>
</tr><tr>
<td>
`loss_scale`
</td>
<td>
The current loss scale as a float32 scalar tensor.
</td>
</tr>
</table>



## Methods

<h3 id="get_scaled_loss"><code>get_scaled_loss</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py#L622-L648">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_scaled_loss(
    loss
)
</code></pre>

Scales the loss by the loss scale.

This method is only needed if you compute gradients manually, e.g. with
<a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. In that case, call this method to scale the loss before
passing the loss to <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If you use
<a href="../../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, loss
scaling is automatically applied and this method is unneeded.

If this method is called, `get_unscaled_gradients` should also be called.
See the <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> doc for
an example.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`loss`
</td>
<td>
The loss, which will be multiplied by the loss scale. Can either be
a tensor or a callable returning a tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`loss` multiplied by <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale</code></a>.
</td>
</tr>

</table>



<h3 id="get_unscaled_gradients"><code>get_unscaled_gradients</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py#L650-L675">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_unscaled_gradients(
    grads
)
</code></pre>

Unscales the gradients by the loss scale.

This method is only needed if you compute gradients manually, e.g. with
<a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. In that case, call this method to unscale the gradients
after computing them with <a href="../../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If you use
<a href="../../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, loss
scaling is automatically applied and this method is unneeded.

If this method is called, `get_scaled_loss` should also be called. See
the <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> doc for an
example.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`grads`
</td>
<td>
A list of tensors, each which will be divided by the loss scale.
Can have None values, which are ignored.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A new list the same size as `grads`, where every non-None value in `grads`
is divided by <a href="../../../../tf/keras/mixed_precision/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale</code></a>.
</td>
</tr>

</table>





