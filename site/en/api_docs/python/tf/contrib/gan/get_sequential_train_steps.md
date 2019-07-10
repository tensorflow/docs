page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.get_sequential_train_steps

Returns a thin wrapper around slim.learning.train_step, for GANs.

``` python
tf.contrib.gan.get_sequential_train_steps(train_steps=namedtuples.GANTrainSteps(1, 1))
```



Defined in [`contrib/gan/python/train.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/train.py).

<!-- Placeholder for "Used in" -->

This function is to provide support for the Supervisor. For new code, please
use `MonitoredSession` and `get_sequential_train_hooks`.

#### Args:


* <b>`train_steps`</b>: A `GANTrainSteps` tuple that determines how many generator and
  discriminator training steps to take.


#### Returns:

A function that can be used for `train_step_fn` for GANs.
