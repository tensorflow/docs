description: Optimizer that implements the RMSprop algorithm.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.RMSprop" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.keras.optimizers.RMSprop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/rmsprop.py#L35-L299">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Optimizer that implements the RMSprop algorithm.

Inherits From: [`Optimizer`](../../../tf/keras/optimizers/Optimizer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.RMSprop`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.RMSprop`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.RMSprop(
    learning_rate=0.001, rho=0.9, momentum=0.0, epsilon=1e-07, centered=(False),
    name='RMSprop', **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

The gist of RMSprop is to:

- Maintain a moving (discounted) average of the square of gradients
- Divide the gradient by the root of this average

This implementation of RMSprop uses plain momentum, not Nesterov momentum.

The centered version additionally maintains a moving average of the
gradients, and uses that average to estimate the variance.

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
learning rate. Defaults to 0.001.
</td>
</tr><tr>
<td>
`rho`
</td>
<td>
Discounting factor for the history/coming gradient. Defaults to 0.9.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
A scalar or a scalar `Tensor`. Defaults to 0.0.
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
`centered`
</td>
<td>
Boolean. If `True`, gradients are normalized by the estimated
variance of the gradient; if False, by the uncentered second moment.
Setting this to `True` may help with training, but is slightly more
expensive in terms of computation and memory. Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients. Defaults to `"RMSprop"`.
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


Note that in the dense implementation of this algorithm, variables and their
corresponding accumulators (momentum, gradient moving average, square
gradient moving average) will be updated even if the gradient is zero
(i.e. accumulators will decay, momentum will be applied). The sparse
implementation (used when the gradient is an `IndexedSlices` object,
typically because of <a href="../../../tf/gather.md"><code>tf.gather</code></a> or an embedding lookup in the forward pass)
will not update variable slices or their accumulators unless those slices
were used in the forward pass (nor is there an "eventual" correction to
account for these omitted updates). This leads to more efficient updates for
large embedding lookup tables (where most of the slices are not accessed in
a particular graph execution), but differs from the published algorithm.

#### Usage:



```
>>> opt = tf.keras.optimizers.RMSprop(learning_rate=0.1)
>>> var1 = tf.Variable(10.0)
>>> loss = lambda: (var1 ** 2) / 2.0    # d(loss) / d(var1) = var1
>>> step_count = opt.minimize(loss, [var1]).numpy()
>>> var1.numpy()
9.683772
```

#### Reference:

- [Hinton, 2012](
  http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)


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
learning rate. Defaults to 0.001.
</td>
</tr><tr>
<td>
`rho`
</td>
<td>
Discounting factor for the history/coming gradient. Defaults to 0.9.
</td>
</tr><tr>
<td>
`momentum`
</td>
<td>
A scalar or a scalar `Tensor`. Defaults to 0.0.
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
`centered`
</td>
<td>
Boolean. If `True`, gradients are normalized by the estimated
variance of the gradient; if False, by the uncentered second moment.
Setting this to `True` may help with training, but is slightly more
expensive in terms of computation and memory. Defaults to `False`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name prefix for the operations created when applying
gradients. Defaults to "RMSprop".
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
`decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
gradients by value, `decay` is included for backward compatibility to
allow time inverse decay of learning rate. `lr` is included for backward
compatibility, recommended to use `learning_rate` instead.
</td>
</tr>
</table>



