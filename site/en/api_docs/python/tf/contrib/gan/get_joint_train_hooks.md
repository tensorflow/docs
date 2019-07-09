page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.get_joint_train_hooks

``` python
tf.contrib.gan.get_joint_train_hooks(train_steps=namedtuples.GANTrainSteps(1, 1))
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/gan/python/train.py).

Returns a hooks function for joint GAN training.

When using these train hooks, IT IS RECOMMENDED TO USE `use_locking=True` ON
ALL OPTIMIZERS TO AVOID RACE CONDITIONS.

The order of steps taken is:
1) Combined generator and discriminator steps
2) Generator only steps, if any remain
3) Discriminator only steps, if any remain

**NOTE**: Unlike `get_sequential_train_hooks`, this method performs updates
for the generator and discriminator simultaneously whenever possible. This
reduces the number of <a href="../../../tf/Session"><code>tf.Session</code></a> calls, and can also change the training
semantics.

To illustrate the difference look at the following example:

`train_steps=namedtuples.GANTrainSteps(3, 5)` will cause
`get_sequential_train_hooks` to make 8 session calls:
  1) 3 generator steps
  2) 5 discriminator steps

In contrast, `get_joint_train_steps` will make 5 session calls:
1) 3 generator + discriminator steps
2) 2 discriminator steps

#### Args:

* <b>`train_steps`</b>: A `GANTrainSteps` tuple that determines how many generator
    and discriminator training steps to take.


#### Returns:

A function that takes a GANTrainOps tuple and returns a list of hooks.