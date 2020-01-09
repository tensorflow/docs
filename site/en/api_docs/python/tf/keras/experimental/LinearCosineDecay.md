page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.LinearCosineDecay


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/experimental/LinearCosineDecay">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L730-L842">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `LinearCosineDecay`

A LearningRateSchedule that uses a linear cosine decay schedule.

Inherits From: [`LearningRateSchedule`](../../../tf/keras/optimizers/schedules/LearningRateSchedule)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/experimental/LinearCosineDecay"><code>tf.compat.v1.keras.experimental.LinearCosineDecay</code></a>
* Class <a href="/api_docs/python/tf/keras/experimental/LinearCosineDecay"><code>tf.compat.v2.keras.experimental.LinearCosineDecay</code></a>


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L733-L810">View source</a>

``` python
__init__(
    initial_learning_rate,
    decay_steps,
    num_periods=0.5,
    alpha=0.0,
    beta=0.001,
    name=None
)
```

Applies linear cosine decay to the learning rate.

See [Bello et al., ICML2017] Neural Optimizer Search with RL.
https://arxiv.org/abs/1709.07417

For the idea of warm starts here controlled by `num_periods`,
see [Loshchilov & Hutter, ICLR2016] SGDR: Stochastic Gradient Descent
with Warm Restarts. https://arxiv.org/abs/1608.03983

Note that linear cosine decay is more aggressive than cosine decay and
larger initial learning rates can typically be used.

When training a model, it is often recommended to lower the learning rate as
the training progresses. This schedule applies a linear cosine decay
function to an optimizer step, given a provided initial learning rate.
It requires a `step` value to compute the decayed learning rate. You can
just pass a TensorFlow variable that you increment at each training step.

The schedule a 1-arg callable that produces a decayed learning
rate when passed the current optimizer step. This can be useful for changing
the learning rate value across different invocations of optimizer functions.
It is computed as:

```python
def decayed_learning_rate(step):
  step = min(step, decay_steps)
  linear_decay = (decay_steps - step) / decay_steps
  cosine_decay = 0.5 * (
      1 + cos(pi * 2 * num_periods * step / decay_steps))
  decayed = (alpha + linear_decay) * cosine_decay + beta
  return initial_learning_rate * decayed
```

#### Example usage:


```python
decay_steps = 1000
lr_decayed_fn = (
  tf.keras.experimental.LinearCosineDecay(
    initial_learning_rate, decay_steps))
```

You can pass this schedule directly into a <a href="../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a>
as the learning rate. The learning rate schedule is also serializable and
deserializable using <a href="../../../tf/keras/optimizers/schedules/serialize"><code>tf.keras.optimizers.schedules.serialize</code></a> and
<a href="../../../tf/keras/optimizers/schedules/deserialize"><code>tf.keras.optimizers.schedules.deserialize</code></a>.

#### Args:


* <b>`initial_learning_rate`</b>: A scalar `float32` or `float64` Tensor or a Python
  number. The initial learning rate.
* <b>`decay_steps`</b>: A scalar `int32` or `int64` `Tensor` or a Python number.
  Number of steps to decay over.
* <b>`num_periods`</b>: Number of periods in the cosine part of the decay.
  See computation above.
* <b>`alpha`</b>: See computation above.
* <b>`beta`</b>: See computation above.
* <b>`name`</b>: String.  Optional name of the operation.  Defaults to
  'LinearCosineDecay'.

#### Returns:

A 1-arg callable learning rate schedule that takes the current optimizer
step and outputs the decayed learning rate, a scalar `Tensor` of the same
type as `initial_learning_rate`.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L812-L832">View source</a>

``` python
__call__(step)
```

Call self as a function.


<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L50-L60">View source</a>

``` python
from_config(
    cls,
    config
)
```

Instantiates a `LearningRateSchedule` from its config.


#### Args:


* <b>`config`</b>: Output of `get_config()`.


#### Returns:

A `LearningRateSchedule` instance.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py#L834-L842">View source</a>

``` python
get_config()
```
