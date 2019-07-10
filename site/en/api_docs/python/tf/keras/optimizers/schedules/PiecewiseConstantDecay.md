page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.schedules.PiecewiseConstantDecay

## Class `PiecewiseConstantDecay`

A LearningRateSchedule that uses a piecewise constant decay schedule.

Inherits From: [`LearningRateSchedule`](../../../../tf/keras/optimizers/schedules/LearningRateSchedule)

### Aliases:

* Class `tf.compat.v1.keras.optimizers.schedules.PiecewiseConstantDecay`
* Class `tf.compat.v2.keras.optimizers.schedules.PiecewiseConstantDecay`
* Class `tf.compat.v2.optimizers.schedules.PiecewiseConstantDecay`
* Class `tf.keras.optimizers.schedules.PiecewiseConstantDecay`



Defined in [`python/keras/optimizer_v2/learning_rate_schedule.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    boundaries,
    values,
    name=None
)
```

Piecewise constant from boundaries and interval values.

The function returns a 1-arg callable to compute the piecewise constant
when passed the current optimizer step. This can be useful for changing the
learning rate value across different invocations of optimizer functions.

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5
  for the next 10000 steps, and 0.1 for any additional steps.

```python
step = tf.Variable(0, trainable=False)
boundaries = [100000, 110000]
values = [1.0, 0.5, 0.1]
learning_rate_fn = keras.optimizers.schedules.PiecewiseConstantDecay(
    boundaries, values)

# Later, whenever we perform an optimization step, we pass in the step.
learning_rate = learning_rate_fn(step)
```

You can pass this schedule directly into a <a href="../../../../tf/keras/optimizers/Optimizer"><code>tf.keras.optimizers.Optimizer</code></a>
as the learning rate. The learning rate schedule is also serializable and
deserializable using <a href="../../../../tf/keras/optimizers/schedules/serialize"><code>tf.keras.optimizers.schedules.serialize</code></a> and
<a href="../../../../tf/keras/optimizers/schedules/deserialize"><code>tf.keras.optimizers.schedules.deserialize</code></a>.

#### Args:


* <b>`boundaries`</b>: A list of `Tensor`s or `int`s or `float`s with strictly
  increasing entries, and with all elements having the same type as the
  optimizer step.
* <b>`values`</b>: A list of `Tensor`s or `float`s or `int`s that specifies the
  values for the intervals defined by `boundaries`. It should have one
  more element than `boundaries`, and all elements should have the same
  type.
* <b>`name`</b>: A string. Optional name of the operation. Defaults to
  'PiecewiseConstant'.


#### Returns:

A 1-arg callable learning rate schedule that takes the current optimizer
step and outputs the decayed learning rate, a scalar `Tensor` of the same
type as the boundary tensors.

The output of the 1-arg function that takes the `step`
is `values[0]` when `step <= boundaries[0]`,
`values[1]` when `step > boundaries[0]` and `step <= boundaries[1]`, ...,
and values[-1] when `step > boundaries[-1]`.



#### Raises:


* <b>`ValueError`</b>: if types of all `values` do not match or
    the number of elements in the lists does not match.



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






