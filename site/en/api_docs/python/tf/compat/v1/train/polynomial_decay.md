description: Applies a polynomial decay to the learning rate.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.polynomial_decay" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.polynomial_decay

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/learning_rate_decay.py#L182-L280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Applies a polynomial decay to the learning rate.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.polynomial_decay(
    learning_rate, global_step, decay_steps, end_learning_rate=0.0001, power=1.0,
    cycle=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It is commonly observed that a monotonically decreasing learning rate, whose
degree of change is carefully chosen, results in a better performing model.
This function applies a polynomial decay function to a provided initial
`learning_rate` to reach an `end_learning_rate` in the given `decay_steps`.

It requires a `global_step` value to compute the decayed learning rate.  You
can just pass a TensorFlow variable that you increment at each training step.

The function returns the decayed learning rate.  It is computed as:

```python
global_step = min(global_step, decay_steps)
decayed_learning_rate = (learning_rate - end_learning_rate) *
                        (1 - global_step / decay_steps) ^ (power) +
                        end_learning_rate

```

If `cycle` is True then a multiple of `decay_steps` is used, the first one
that is bigger than `global_steps`.

```python
decay_steps = decay_steps * ceil(global_step / decay_steps)
decayed_learning_rate = (learning_rate - end_learning_rate) *
                        (1 - global_step / decay_steps) ^ (power) +
                        end_learning_rate

```

Example: decay from 0.1 to 0.01 in 10000 steps using sqrt (i.e. power=0.5):

```python
...
global_step = tf.Variable(0, trainable=False)
starter_learning_rate = 0.1
end_learning_rate = 0.01
decay_steps = 10000
learning_rate = tf.compat.v1.train.polynomial_decay(starter_learning_rate,
global_step,
                                          decay_steps, end_learning_rate,
                                          power=0.5)
# Passing global_step to minimize() will increment it at each step.
learning_step = (
    tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
    .minimize(...my loss..., global_step=global_step)
)
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
A scalar `float32` or `float64` `Tensor` or a Python number.
The initial learning rate.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number. Global
step to use for the decay computation.  Must not be negative.
</td>
</tr><tr>
<td>
`decay_steps`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number. Must
be positive.  See the decay computation above.
</td>
</tr><tr>
<td>
`end_learning_rate`
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a Python
number.  The minimal end learning rate.
</td>
</tr><tr>
<td>
`power`
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a Python number.  The
power of the polynomial. Defaults to linear, 1.0.
</td>
</tr><tr>
<td>
`cycle`
</td>
<td>
A boolean, whether or not it should cycle beyond decay_steps.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String.  Optional name of the operation. Defaults to
'PolynomialDecay'.
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




#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.

