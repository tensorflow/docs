description: Optimizer that implements the Adamax algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.Adamax" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.optimizers.Adamax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/adamax.py#L33-L188">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the Adamax algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.Adamax`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.Adamax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.Adamax(
    learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, name='Adamax',
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It is a variant of Adam based on the infinity norm.
Default parameters follow those provided in the paper.
Adamax is sometimes superior to adam, specially in models with embeddings.

#### Initialization:



```python
m = 0  # Initialize initial 1st moment vector
v = 0  # Initialize the exponentially weighted infinity norm
t = 0  # Initialize timestep
```

The update rule for parameter `w` with gradient `g` is
described at the end of section 7.1 of the paper:

```python
t += 1
m = beta1 * m + (1 - beta) * g
v = max(beta2 * v, abs(g))
current_lr = learning_rate / (1 - beta1 ** t)
w = w - current_lr * m / (v + epsilon)
```

Similarly to `Adam`, the epsilon is added for numerical stability
(especially to get rid of division by zero when `v_t == 0`).

In contrast to `Adam`, the sparse implementation of this algorithm
(used when the gradient is an IndexedSlices object, typically because of
<a href="../../../tf/gather.md"><code>tf.gather</code></a> or an embedding lookup in the forward pass) only updates
variable slices and corresponding `m_t`, `v_t` terms when that part of
the variable was used in the forward pass. This means that the sparse
behavior is contrast to the dense behavior (similar to some momentum
implementations which ignore momentum unless a variable slice was actually
used).

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
`beta_1`
</td>
<td>
A float value or a constant float tensor. The exponential decay
rate for the 1st moment estimates.
</td>
</tr><tr>
<td>
`beta_2`
</td>
<td>
A float value or a constant float tensor. The exponential decay
rate for the exponentially weighted infinity norm.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A small constant for numerical stability.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operations created when applying gradients.
Defaults to `"Adamax"`.
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

- [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)


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



