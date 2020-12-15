description: Gradient descent (with momentum) optimizer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.SGD" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.optimizers.SGD

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/gradient_descent.py#L30-L194">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Gradient descent (with momentum) optimizer.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.SGD`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.SGD`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.SGD(
    learning_rate=0.01, momentum=0.0, nesterov=(False), name='SGD', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Update rule for parameter `w` with gradient `g` when `momentum` is 0:

```python
w = w - learning_rate * g
```

Update rule when `momentum` is larger than 0:

```python
velocity = momentum * velocity - learning_rate * g
w = w + velocity
```

When `nesterov=True`, this rule becomes:

```python
velocity = momentum * velocity - learning_rate * g
w = w + momentum * velocity - learning_rate * g
```

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
that takes no arguments and returns the actual value to use. The
learning rate. Defaults to 0.01.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
float hyperparameter >= 0 that accelerates gradient descent
in the relevant
direction and dampens oscillations. Defaults to 0, i.e., vanilla gradient
descent.
</td>
</tr><tr>
<td>
`nesterov`
</td>
<td>
boolean. Whether to apply Nesterov momentum.
Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients.  Defaults to `"SGD"`.
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
>>> opt = tf.keras.optimizers.SGD(learning_rate=0.1)
>>> var = tf.Variable(1.0)
>>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
>>> step_count = opt.minimize(loss, [var]).numpy()
>>> # Step is `- learning_rate * grad`
>>> var.numpy()
0.9
```

```
>>> opt = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.9)
>>> var = tf.Variable(1.0)
>>> val0 = var.value()
>>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
>>> # First step is `- learning_rate * grad`
>>> step_count = opt.minimize(loss, [var]).numpy()
>>> val1 = var.value()
>>> (val0 - val1).numpy()
0.1
>>> # On later steps, step-size increases because of momentum
>>> step_count = opt.minimize(loss, [var]).numpy()
>>> val2 = var.value()
>>> (val1 - val2).numpy()
0.18
```

#### Reference:

- For `nesterov=True`, See [Sutskever et al., 2013](
  http://jmlr.org/proceedings/papers/v28/sutskever13.pdf).


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



