

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.get_sequential_train_hooks

``` python
get_sequential_train_hooks(train_steps=namedtuples.GANTrainSteps(1, 1))
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/python/train.py).

Returns a hooks function for sequential GAN training.

#### Args:

* <b>`train_steps`</b>: A `GANTrainSteps` tuple that determines how many generator
    and discriminator training steps to take.


#### Returns:

A function that takes a GANTrainOps tuple and returns a list of hooks.