page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.CosineDecayRestarts

## Class `CosineDecayRestarts`

A LearningRateSchedule that uses a cosine decay schedule with restarts.

Inherits From: [`LearningRateSchedule`](../../../tf/keras/optimizers/schedules/LearningRateSchedule)

### Aliases:

* Class `tf.compat.v1.keras.experimental.CosineDecayRestarts`
* Class `tf.compat.v2.keras.experimental.CosineDecayRestarts`
* Class `tf.keras.experimental.CosineDecayRestarts`



Defined in [`python/keras/optimizer_v2/learning_rate_schedule.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    initial_learning_rate,
    first_decay_steps,
    t_mul=2.0,
    m_mul=1.0,
    alpha=0.0,
    name=None
)
```

Applies cosine decay with restarts to the learning rate.

See [Loshchilov & Hutter, ICLR2016], SGDR: Stochastic Gradient Descent
with Warm Restarts. https://arxiv.org/abs/1608.03983

When training a model, it is often recommended to lower the learning rate as
the training progresses. This schedule applies a cosine decay function with
restarts to an optimizer step, given a provided initial learning rate.
It requires a `step` value to compute the decayed learning rate. You can
just pass a TensorFlow variable that you increment at each training step.

The schedule a 1-arg callable that produces a decayed learning
rate when passed the current optimizer step. This can be useful for changing
the learning rate value across different invocations of optimizer functions.

The learning rate multiplier first decays
from 1 to `alpha` for `first_decay_steps` steps. Then, a warm
restart is performed. Each new warm restart runs for `t_mul` times more
steps and with `m_mul` times smaller initial learning rate.

#### Example usage:


```python
first_decay_steps = 1000
lr_decayed_fn = (
  tf.keras.experimental.CosineDecayRestarts(
      initial_learning_rate,
      global_step,
      first_decay_steps))
```

You can pass this schedule directly into a <a href="../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a>
as the learning rate. The learning rate schedule is also serializable and
deserializable using <a href="../../../tf/keras/optimizers/schedules/serialize"><code>tf.keras.optimizers.schedules.serialize</code></a> and
<a href="../../../tf/keras/optimizers/schedules/deserialize"><code>tf.keras.optimizers.schedules.deserialize</code></a>.

#### Args:


* <b>`initial_learning_rate`</b>: A scalar `float32` or `float64` Tensor or a Python
  number. The initial learning rate.
* <b>`first_decay_steps`</b>: A scalar `int32` or `int64` `Tensor` or a Python
  number. Number of steps to decay over.
* <b>`t_mul`</b>: A scalar `float32` or `float64` `Tensor` or a Python number.
  Used to derive the number of iterations in the i-th period
* <b>`m_mul`</b>: A scalar `float32` or `float64` `Tensor` or a Python number.
  Used to derive the initial learning rate of the i-th period:
* <b>`alpha`</b>: A scalar `float32` or `float64` Tensor or a Python number.
  Minimum learning rate value as a fraction of the initial_learning_rate.
* <b>`name`</b>: String. Optional name of the operation.  Defaults to 'SGDRDecay'.

#### Returns:

A 1-arg callable learning rate schedule that takes the current optimizer
step and outputs the decayed learning rate, a scalar `Tensor` of the same
type as `initial_learning_rate`.


#### Raises:


* <b>`ValueError`</b>: if `global_step` is not supplied.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(step)
```




<h3 id="from_config"><code>from_config</code></h3>

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

``` python
get_config()
```






