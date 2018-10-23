

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.get_sequential_train_steps

``` python
tf.contrib.gan.get_sequential_train_steps(train_steps=namedtuples.GANTrainSteps(1, 1))
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/gan/python/train.py).

Returns a thin wrapper around slim.learning.train_step, for GANs.

This function is to provide support for the Supervisor. For new code, please
use `MonitoredSession` and `get_sequential_train_hooks`.

#### Args:

* <b>`train_steps`</b>: A `GANTrainSteps` tuple that determines how many generator
    and discriminator training steps to take.


#### Returns:

A function that can be used for `train_step_fn` for GANs.