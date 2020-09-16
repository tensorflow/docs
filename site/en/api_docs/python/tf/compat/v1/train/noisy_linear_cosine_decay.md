description: Applies noisy linear cosine decay to the learning rate.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.noisy_linear_cosine_decay" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.noisy_linear_cosine_decay

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/learning_rate_decay.py#L679-L771">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies noisy linear cosine decay to the learning rate.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.noisy_linear_cosine_decay(
    learning_rate, global_step, decay_steps, initial_variance=1.0,
    variance_decay=0.55, num_periods=0.5, alpha=0.0, beta=0.001, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that linear cosine decay is more aggressive than cosine decay and
larger initial learning rates can typically be used.

When training a model, it is often recommended to lower the learning rate as
the training progresses.  This function applies a noisy linear
cosine decay function to a provided initial learning rate.
It requires a `global_step` value to compute the decayed learning rate.
You can just pass a TensorFlow variable that you increment at each
training step.

The function returns the decayed learning rate.  It is computed as:
```python
global_step = min(global_step, decay_steps)
linear_decay = (decay_steps - global_step) / decay_steps)
cosine_decay = 0.5 * (
    1 + cos(pi * 2 * num_periods * global_step / decay_steps))
decayed = (alpha + linear_decay + eps_t) * cosine_decay + beta
decayed_learning_rate = learning_rate * decayed
```
where eps_t is 0-centered gaussian noise with variance
initial_variance / (1 + global_step) ** variance_decay

#### Example usage:


```python
decay_steps = 1000
lr_decayed = noisy_linear_cosine_decay(
  learning_rate, global_step, decay_steps)
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
A scalar `float32` or `float64` Tensor or a Python number.
The initial learning rate.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number. Global
step to use for the decay computation.
</td>
</tr><tr>
<td>
`decay_steps`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number. Number
of steps to decay over.
</td>
</tr><tr>
<td>
`initial_variance`
</td>
<td>
initial variance for the noise. See computation above.
</td>
</tr><tr>
<td>
`variance_decay`
</td>
<td>
decay for the noise's variance. See computation above.
</td>
</tr><tr>
<td>
`num_periods`
</td>
<td>
Number of periods in the cosine part of the decay. See
computation above.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
See computation above.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
See computation above.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String.  Optional name of the operation.  Defaults to
'NoisyLinearCosineDecay'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A scalar `Tensor` of the same type as `learning_rate`.  The decayed
learning rate.
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
if `global_step` is not supplied.
</td>
</tr>
</table>



#### References:

Neural Optimizer Search with Reinforcement Learning:
  [Bello et al., 2017](http://proceedings.mlr.press/v70/bello17a.html)
  ([pdf](http://proceedings.mlr.press/v70/bello17a/bello17a.pdf))
Stochastic Gradient Descent with Warm Restarts:
  [Loshchilov et al., 2017]
  (https://openreview.net/forum?id=Skq89Scxx&noteId=Skq89Scxx)
  ([pdf](https://openreview.net/pdf?id=Skq89Scxx))




#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.

