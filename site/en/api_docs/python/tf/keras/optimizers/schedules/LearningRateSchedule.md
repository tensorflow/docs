page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.schedules.LearningRateSchedule

## Class `LearningRateSchedule`

A serializable learning rate decay schedule.



### Aliases:

* Class `tf.compat.v1.keras.optimizers.schedules.LearningRateSchedule`
* Class `tf.compat.v2.keras.optimizers.schedules.LearningRateSchedule`
* Class `tf.compat.v2.optimizers.schedules.LearningRateSchedule`
* Class `tf.keras.optimizers.schedules.LearningRateSchedule`



Defined in [`python/keras/optimizer_v2/learning_rate_schedule.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py).

<!-- Placeholder for "Used in" -->

`LearningRateSchedule`s can be passed in as the learning rate of optimizers in
<a href="../../../../tf/keras/optimizers"><code>tf.keras.optimizers</code></a>. They can be serialized and deserialized using
<a href="../../../../tf/keras/optimizers/schedules/serialize"><code>tf.keras.optimizers.schedules.serialize</code></a> and
<a href="../../../../tf/keras/optimizers/schedules/deserialize"><code>tf.keras.optimizers.schedules.deserialize</code></a>.

## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(step)
```




<h3 id="from_config"><code>from_config</code></h3>

``` python
@classmethod
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






