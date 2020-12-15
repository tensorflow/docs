description: Optimizer that implements the FTRL algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.Ftrl" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.optimizers.Ftrl

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/ftrl.py#L30-L250">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the FTRL algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.Ftrl`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.Ftrl`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.Ftrl(
    learning_rate=0.001, learning_rate_power=-0.5, initial_accumulator_value=0.1,
    l1_regularization_strength=0.0, l2_regularization_strength=0.0, name='Ftrl',
    l2_shrinkage_regularization_strength=0.0, beta=0.0, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

See Algorithm 1 of this
[paper](https://research.google.com/pubs/archive/41159.pdf).
This version has support for both online L2 (the L2 penalty given in the paper
above) and shrinkage-type L2 (which is the addition of an L2 penalty to the
loss function).

#### Initialization:


$$t = 0$$
$$n_{0} = 0$$
$$\sigma_{0} = 0$$
$$z_{0} = 0$$

Update ($$i$$ is variable index, $$\alpha$$ is the learning rate):
$$t = t + 1$$
$$n_{t,i} = n_{t-1,i} + g_{t,i}^{2}$$
$$\sigma_{t,i} = (\sqrt{n_{t,i}} - \sqrt{n_{t-1,i}}) / \alpha$$
$$z_{t,i} = z_{t-1,i} + g_{t,i} - \sigma_{t,i} * w_{t,i}$$
$$w_{t,i} = - ((\beta+\sqrt{n_{t,i}}) / \alpha + 2 * \lambda_{2})^{-1} *
            (z_{i} - sgn(z_{i}) * \lambda_{1}) if \abs{z_{i}} > \lambda_{i}
                                               else 0$$

Check the documentation for the l2_shrinkage_regularization_strength
parameter for more details when shrinkage is enabled, in which case gradient
is replaced with gradient_with_shrinkage.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`learning_rate`
</td>
<td>
A `Tensor`, floating point value, or a schedule that is a
<a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>. The learning rate.
</td>
</tr><tr>
<td>
`learning_rate_power`
</td>
<td>
A float value, must be less or equal to zero.
Controls how the learning rate decreases during training. Use zero for
a fixed learning rate.
</td>
</tr><tr>
<td>
`initial_accumulator_value`
</td>
<td>
The starting value for accumulators.
Only zero or positive values are allowed.
</td>
</tr><tr>
<td>
`l1_regularization_strength`
</td>
<td>
A float value, must be greater than or
equal to zero.
</td>
</tr><tr>
<td>
`l2_regularization_strength`
</td>
<td>
A float value, must be greater than or
equal to zero.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients.  Defaults to `"Ftrl"`.
</td>
</tr><tr>
<td>
`l2_shrinkage_regularization_strength`
</td>
<td>
A float value, must be greater than
or equal to zero. This differs from L2 above in that the L2 above is a
stabilization penalty, whereas this L2 shrinkage is a magnitude penalty.
When input is sparse shrinkage will only happen on the active weights.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
A float value, representing the beta value from the paper.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments. Allowed to be one of
`"clipnorm"` or `"clipvalue"`.
`"clipnorm"` (float) clips gradients by norm; `"clipvalue"` (float) clips
gradients by value.
</td>
</tr>
</table>



#### Reference:

- [paper](
  https://www.eecs.tufts.edu/~dsculley/papers/ad-click-prediction.pdf)


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



