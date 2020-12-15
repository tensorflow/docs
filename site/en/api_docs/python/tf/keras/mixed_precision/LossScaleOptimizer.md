description: An optimizer that applies loss scaling to prevent numeric underflow.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.mixed_precision.LossScaleOptimizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_scaled_loss"/>
<meta itemprop="property" content="get_unscaled_gradients"/>
</div>

# tf.keras.mixed_precision.LossScaleOptimizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py#L397-L922">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An optimizer that applies loss scaling to prevent numeric underflow.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.mixed_precision.LossScaleOptimizer`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.mixed_precision.LossScaleOptimizer(
    inner_optimizer, dynamic=(True), initial_scale=None, dynamic_growth_steps=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Loss scaling is a technique to prevent numeric underflow in intermediate
gradients when float16 is used. To prevent underflow, the loss is multiplied
(or "scaled") by a certain factor called the "loss scale", which causes
intermediate gradients to be scaled by the loss scale as well. The final
gradients are divided (or "unscaled") by the loss scale to bring them back to
their original value.

`LossScaleOptimizer` wraps another optimizer and applies loss scaling to it.
By default, the loss scale is dynamically updated over time so you do not have
to choose the loss scale. The `minimize` method automatically scales the loss,
unscales the gradients, and updates the loss scale so all you have to do is
wrap your optimizer with a `LossScaleOptimizer` if you use `minimize`. For
example:

```
>>> opt = tf.keras.optimizers.SGD(0.25)
>>> opt = tf.keras.mixed_precision.LossScaleOptimizer(opt)
>>> var = tf.Variable(1.)
>>> loss_fn = lambda: var ** 2
>>> # 'minimize' applies loss scaling and updates the loss sale.
>>> opt.minimize(loss_fn, var_list=var)
>>> var.numpy()
0.5
```

If a <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a> is used to compute gradients instead of `minimize`, you
must scale the loss and gradients manually. This can be done with the
<a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#get_scaled_loss"><code>LossScaleOptimizer.get_scaled_loss</code></a> and
<a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#get_unscaled_gradients"><code>LossScaleOptimizer.get_unscaled_gradients</code></a> methods. For example:

```
>>> with tf.GradientTape() as tape:
...   loss = loss_fn()
...   scaled_loss = opt.get_scaled_loss(loss)
>>> scaled_grad = tape.gradient(scaled_loss, var)
>>> (grad,) = opt.get_unscaled_gradients([scaled_grad])
>>> opt.apply_gradients([(grad, var)])  # Loss scale is updated here
>>> var.numpy()
0.25
```

Warning: If you forget to call `get_scaled_loss` or `get_unscaled_gradients`
(or both) when using a <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>, the model will likely converge to a
worse quality. Please make sure you call each function exactly once.

When mixed precision with float16 is used, there is typically no risk of
underflow affecting model quality if loss scaling is properly used. See
[the mixed precision guide](
https://www.tensorflow.org/guide/keras/mixed_precision) for more information
on how to use mixed precision.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inner_optimizer`
</td>
<td>
The <a href="../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a> instance to wrap.
</td>
</tr><tr>
<td>
`dynamic`
</td>
<td>
Bool indicating whether dynamic loss scaling is used. Defaults to
True. If True, the loss scale will be dynamically updated over time using
an algorithm that keeps the loss scale at approximately its optimal value.
If False, a single fixed loss scale is used and `initial_scale` must be
specified, which is used as the loss scale. Recommended to keep as True,
as choosing a fixed loss scale can be tricky. Currently, there is a small
performance overhead to dynamic loss scaling compared to fixed loss
scaling.
</td>
</tr><tr>
<td>
`initial_scale`
</td>
<td>
The initial loss scale. If `dynamic` is True, this defaults
to `2 ** 15`. If `dynamic` is False, this must be specified and acts as
the sole loss scale, as the loss scale does not change over time. When
dynamic loss scaling is used, is better for this to be a very high number,
because a loss scale that is too high gets lowered far more quickly than a
loss scale that is too low gets raised.
</td>
</tr><tr>
<td>
`dynamic_growth_steps`
</td>
<td>
With dynamic loss scaling, every
`dynamic_growth_steps` steps with finite gradients, the loss scale is
doubled. Defaults to 2000. If a nonfinite gradient is encountered, the
count is reset back to zero, gradients are skipped that step, and the loss
scale is halved. The count can be queried with
<a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic_counter"><code>LossScaleOptimizer.dynamic_counter</code></a>. This argument can only be specified
if `dynamic` is True.
</td>
</tr>
</table>


`LossScaleOptimizer` will occasionally skip applying gradients to the
variables, in which case the trainable variables will not change that step.
This is done because the dynamic loss scale will sometimes be raised too
high, causing overflow in the gradients. Typically, the first 2 to 15 steps of
the model are skipped as the initial loss scale is very high, but afterwards
steps will only be skipped on average 0.05% of the time (the fraction of steps
skipped is `1 / dynamic_growth_steps`).

`LossScaleOptimizer` delegates all public `Optimizer` methods to the inner
optimizer. Additionally, in methods `minimize` and `get_gradients, it scales
the loss and unscales the gradients. In methods `minimize` and
`apply_gradients`, it additionally updates the loss scale and skips applying
gradients if any gradient has a nonfinite value.

### Hyperparameters

Hyperparameters can be accessed and set on the LossScaleOptimizer, which will
be delegated to the wrapped optimizer.

```
>>> opt = tf.keras.optimizers.Adam(beta_1=0.8, epsilon=1e-5)
>>> opt = tf.keras.mixed_precision.LossScaleOptimizer(opt)
>>> opt.beta_1  # Equivalent to `opt.inner_optimizer.beta_1`
0.8
>>> opt.beta_1 = 0.7  # Equivalent to `opt.inner_optimizer.beta_1 = 0.7`
>>> opt.beta_1
0.7
>>> opt.inner_optimizer.beta_1
0.7
```

However, accessing or setting non-hyperparameters is not delegated to the
LossScaleOptimizer. In an Adam optimizer, `beta_1` is a hyperparameter but
`epsilon` is not, as the Adam optimizer only calls `Optimizer._set_hyper` on
`beta_1`.

```
>>> opt.inner_optimizer.epsilon
1e-5
>>> opt.epsilon
Traceback (most recent call last):
...
AttributeError: 'LossScaleOptimizer' object has no attribute 'epsilon'
>>> opt.epsilon = 1e-4  # This does NOT set epsilon on `opt.inner_optimizer`
>>> opt.inner_optimizer.epsilon
>>> 1e-5
```

In the above example, despite epsilon being set on the LossScaleOptimizer, the
old epsilon value will still be used when training as epsilon was not set on
the inner optimizer.

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
devices (when using <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>). If `None`, defaults to
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

This is None if <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic"><code>LossScaleOptimizer.dynamic</code></a> is False.

The counter is incremented every step. Once it reaches
<a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic_growth_steps"><code>LossScaleOptimizer.dynamic_growth_steps</code></a>, the loss scale will be doubled
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

This is None if <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic"><code>LossScaleOptimizer.dynamic</code></a> is False.

Every `dynamic_growth_steps` consecutive steps with finite gradients, the
loss scale is increased.
</td>
</tr><tr>
<td>
`initial_scale`
</td>
<td>
The initial loss scale.

If <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#dynamic"><code>LossScaleOptimizer.dynamic</code></a> is False, this is the same number as
<a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale</code></a>, as the loss scale never changes.
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
<a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. In that case, call this method to scale the loss before
passing the loss to <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If you use
<a href="../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, loss
scaling is automatically applied and this method is unneeded.

If this method is called, `get_unscaled_gradients` should also be called.
See the <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> doc for
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
`loss` multiplied by <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale</code></a>.
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
<a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. In that case, call this method to unscale the gradients
after computing them with <a href="../../../tf/GradientTape.md"><code>tf.GradientTape</code></a>. If you use
<a href="../../../tf/keras/optimizers/Optimizer.md#minimize"><code>LossScaleOptimizer.minimize</code></a> or <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#get_gradients"><code>LossScaleOptimizer.get_gradients</code></a>, loss
scaling is automatically applied and this method is unneeded.

If this method is called, `get_scaled_loss` should also be called. See
the <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md"><code>tf.keras.mixed_precision.LossScaleOptimizer</code></a> doc for an
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
is divided by <a href="../../../tf/keras/mixed_precision/LossScaleOptimizer.md#loss_scale"><code>LossScaleOptimizer.loss_scale</code></a>.
</td>
</tr>

</table>





