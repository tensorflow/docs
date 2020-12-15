description: A LearningRateSchedule that uses an exponential decay schedule.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.schedules.ExponentialDecay" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.optimizers.schedules.ExponentialDecay

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L65-L166">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A LearningRateSchedule that uses an exponential decay schedule.

Inherits From: [`LearningRateSchedule`](../../../../tf/keras/optimizers/schedules/LearningRateSchedule.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.optimizers.schedules.ExponentialDecay`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.optimizers.schedules.ExponentialDecay`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate, decay_steps, decay_rate, staircase=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

When training a model, it is often recommended to lower the learning rate as
the training progresses. This schedule applies an exponential decay function
to an optimizer step, given a provided initial learning rate.

The schedule a 1-arg callable that produces a decayed learning
rate when passed the current optimizer step. This can be useful for changing
the learning rate value across different invocations of optimizer functions.
It is computed as:

```python
def decayed_learning_rate(step):
  return initial_learning_rate * decay_rate ^ (step / decay_steps)
```

If the argument `staircase` is `True`, then `step / decay_steps` is
an integer division and the decayed learning rate follows a
staircase function.

You can pass this schedule directly into a <a href="../../../../tf/keras/optimizers/Optimizer.md"><code>tf.keras.optimizers.Optimizer</code></a>
as the learning rate.
Example: When fitting a Keras model, decay every 100000 steps with a base
of 0.96:

```python
initial_learning_rate = 0.1
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=100000,
    decay_rate=0.96,
    staircase=True)

model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=lr_schedule),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels, epochs=5)
```

The learning rate schedule is also serializable and deserializable using
<a href="../../../../tf/keras/optimizers/schedules/serialize.md"><code>tf.keras.optimizers.schedules.serialize</code></a> and
<a href="../../../../tf/keras/optimizers/schedules/deserialize.md"><code>tf.keras.optimizers.schedules.deserialize</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 1-arg callable learning rate schedule that takes the current optimizer
step and outputs the decayed learning rate, a scalar `Tensor` of the same
type as `initial_learning_rate`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`initial_learning_rate`
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a
Python number.  The initial learning rate.
</td>
</tr><tr>
<td>
`decay_steps`
</td>
<td>
A scalar `int32` or `int64` `Tensor` or a Python number.
Must be positive.  See the decay computation above.
</td>
</tr><tr>
<td>
`decay_rate`
</td>
<td>
A scalar `float32` or `float64` `Tensor` or a
Python number.  The decay rate.
</td>
</tr><tr>
<td>
`staircase`
</td>
<td>
Boolean.  If `True` decay the learning rate at discrete
intervals
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String.  Optional name of the operation.  Defaults to
'ExponentialDecay'.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L51-L61">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

Instantiates a `LearningRateSchedule` from its config.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config`
</td>
<td>
Output of `get_config()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `LearningRateSchedule` instance.
</td>
</tr>

</table>



<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L159-L166">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>




<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L144-L157">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    step
)
</code></pre>

Call self as a function.




