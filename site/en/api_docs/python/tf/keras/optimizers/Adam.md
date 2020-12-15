description: Optimizer that implements the Adam algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.Adam" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.optimizers.Adam

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/adam.py#L34-L253">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the Adam algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.Adam`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.Adam`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.Adam(
    learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, amsgrad=(False),
    name='Adam', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Adam optimization is a stochastic gradient descent method that is based on
adaptive estimation of first-order and second-order moments.

According to
[Kingma et al., 2014](http://arxiv.org/abs/1412.6980),
the method is "*computationally
efficient, has little memory requirement, invariant to diagonal rescaling of
gradients, and is well suited for problems that are large in terms of
data/parameters*".

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
<a href="../../../tf/keras/optimizers/schedules/LearningRateSchedule.md"><code>tf.keras.optimizers.schedules.LearningRateSchedule</code></a>, or a callable
that takes no arguments and returns the actual value to use, The
learning rate. Defaults to 0.001.
</td>
</tr><tr>
<td>
`beta_1`
</td>
<td>
A float value or a constant float tensor, or a callable
that takes no arguments and returns the actual value to use. The
exponential decay rate for the 1st moment estimates. Defaults to 0.9.
</td>
</tr><tr>
<td>
`beta_2`
</td>
<td>
A float value or a constant float tensor, or a callable
that takes no arguments and returns the actual value to use, The
exponential decay rate for the 2nd moment estimates. Defaults to 0.999.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small constant for numerical stability. This epsilon is
"epsilon hat" in the Kingma and Ba paper (in the formula just before
Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
1e-7.
</td>
</tr><tr>
<td>
`amsgrad`
</td>
<td>
Boolean. Whether to apply AMSGrad variant of this algorithm from
the paper "On the Convergence of Adam and beyond". Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operations created when applying gradients.
Defaults to `"Adam"`.
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



#### Usage:



```
>>> opt = tf.keras.optimizers.Adam(learning_rate=0.1)
>>> var1 = tf.Variable(10.0)
>>> loss = lambda: (var1 ** 2)/2.0       # d(loss)/d(var1) == var1
>>> step_count = opt.minimize(loss, [var1]).numpy()
>>> # The first step is `-learning_rate*sign(grad)`
>>> var1.numpy()
9.9
```

#### Reference:

- [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
- [Reddi et al., 2018](
    https://openreview.net/pdf?id=ryQu7f-RZ) for `amsgrad`.



#### Notes:



The default value of 1e-7 for epsilon might not be a good default in
general. For example, when training an Inception network on ImageNet a
current good choice is 1.0 or 0.1. Note that since Adam uses the
formulation just before Section 2.1 of the Kingma and Ba paper rather than
the formulation in Algorithm 1, the "epsilon" referred to here is "epsilon
hat" in the paper.

The sparse implementation of this algorithm (used when the gradient is an
IndexedSlices object, typically because of <a href="../../../tf/gather.md"><code>tf.gather</code></a> or an embedding
lookup in the forward pass) does apply momentum to variable slices even if
they were not used in the forward pass (meaning they have a gradient equal
to zero). Momentum decay (beta1) is also applied to the entire momentum
accumulator. This means that the sparse behavior is equivalent to the dense
behavior (in contrast to some momentum implementations which ignore momentum
unless a variable slice was actually used).

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



