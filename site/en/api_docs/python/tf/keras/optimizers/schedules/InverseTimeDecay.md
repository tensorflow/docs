page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.schedules.InverseTimeDecay

## Class `InverseTimeDecay`

A LearningRateSchedule that uses an inverse time decay schedule.

Inherits From: [`LearningRateSchedule`](../../../../tf/keras/optimizers/schedules/LearningRateSchedule)

### Aliases:

* Class `tf.compat.v1.keras.optimizers.schedules.InverseTimeDecay`
* Class `tf.compat.v2.keras.optimizers.schedules.InverseTimeDecay`
* Class `tf.compat.v2.optimizers.schedules.InverseTimeDecay`
* Class `tf.keras.optimizers.schedules.InverseTimeDecay`



Defined in [`python/keras/optimizer_v2/learning_rate_schedule.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    initial_learning_rate,
    decay_steps,
    decay_rate,
    staircase=False,
    name=None
)
```

Applies inverse time decay to the initial learning rate.

When training a model, it is often recommended to lower the learning rate as
the training progresses. This schedule applies the inverse decay function
to an optimizer step, given a provided initial learning rate.
It requires a `step` value to compute the decayed learning rate. You can
just pass a TensorFlow variable that you increment at each training step.

The schedule a 1-arg callable that produces a decayed learning
rate when passed the current optimizer step. This can be useful for changing
the learning rate value across different invocations of optimizer functions.
It is computed as:

```python
def decayed_learning_rate(step):
  return initial_learning_rate / (1 + decay_rate * step / decay_step)
```

or, if `staircase` is `True`, as:

```python
def decayed_learning_rate(step):
  return initial_learning_rate / (1 + decay_rate * floor(step / decay_step))
```

You can pass this schedule directly into a <a href="../../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a>
as the learning rate.
Example: Fit a Keras model when decaying 1/t with a rate of 0.5:

```python
...
initial_learning_rate = 0.1
decay_steps = 1.0
decay_rate = 0.5
learning_rate_fn = keras.optimizers.schedules.InverseTimeDecay(
  initial_learning_rate, global_step, decay_steps, decay_rate)

model.compile(optimizer=tf.keras.optimizers.SGD(
                  learning_rate=learning_rate_fn),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels, epochs=5)
```

#### Args:


* <b>`initial_learning_rate`</b>: A scalar `float32` or `float64` `Tensor` or a
  Python number.  The initial learning rate.
* <b>`decay_steps`</b>: How often to apply decay.
* <b>`decay_rate`</b>: A Python number.  The decay rate.
* <b>`staircase`</b>: Whether to apply decay in a discrete staircase, as opposed to
  continuous, fashion.
* <b>`name`</b>: String.  Optional name of the operation.  Defaults to
  'InverseTimeDecay'.


#### Returns:

A 1-arg callable learning rate schedule that takes the current optimizer
step and outputs the decayed learning rate, a scalar `Tensor` of the same
type as `initial_learning_rate`.




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






