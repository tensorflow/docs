page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.gan_train

``` python
tf.contrib.gan.gan_train(
    train_ops,
    logdir,
    get_hooks_fn=get_sequential_train_hooks(),
    master='',
    is_chief=True,
    scaffold=None,
    hooks=None,
    chief_only_hooks=None,
    save_checkpoint_secs=600,
    save_summaries_steps=100,
    config=None
)
```



Defined in [`tensorflow/contrib/gan/python/train.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/train.py).

A wrapper around `contrib.training.train` that uses GAN hooks.

#### Args:

* <b>`train_ops`</b>: A GANTrainOps named tuple.
* <b>`logdir`</b>: The directory where the graph and checkpoints are saved.
* <b>`get_hooks_fn`</b>: A function that takes a GANTrainOps tuple and returns a list
    of hooks.
* <b>`master`</b>: The URL of the master.
* <b>`is_chief`</b>: Specifies whether or not the training is being run by the primary
    replica during replica training.
* <b>`scaffold`</b>: An tf.train.Scaffold instance.
* <b>`hooks`</b>: List of <a href="../../../tf/train/SessionRunHook"><code>tf.train.SessionRunHook</code></a> callbacks which are run inside the
    training loop.
* <b>`chief_only_hooks`</b>: List of <a href="../../../tf/train/SessionRunHook"><code>tf.train.SessionRunHook</code></a> instances which are run
    inside the training loop for the chief trainer only.
* <b>`save_checkpoint_secs`</b>: The frequency, in seconds, that a checkpoint is saved
    using a default checkpoint saver. If `save_checkpoint_secs` is set to
    `None`, then the default checkpoint saver isn't used.
* <b>`save_summaries_steps`</b>: The frequency, in number of global steps, that the
    summaries are written to disk using a default summary saver. If
    `save_summaries_steps` is set to `None`, then the default summary saver
    isn't used.
* <b>`config`</b>: An instance of <a href="../../../tf/ConfigProto"><code>tf.ConfigProto</code></a>.


#### Returns:

Output of the call to `training.train`.