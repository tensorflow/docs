page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.train

``` python
tf.contrib.training.train(
    train_op,
    logdir,
    master='',
    is_chief=True,
    scaffold=None,
    hooks=None,
    chief_only_hooks=None,
    save_checkpoint_secs=600,
    save_summaries_steps=100,
    config=None,
    max_wait_secs=7200,
    run_metadata=None
)
```



Defined in [`tensorflow/contrib/training/python/training/training.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/training/python/training/training.py).

Runs the training loop.

#### Args:

* <b>`train_op`</b>: A `Tensor` that, when executed, will apply the gradients and
    return the loss value.
* <b>`logdir`</b>: The directory where the graph and checkpoints are saved.
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
* <b>`max_wait_secs`</b>: Maximum time workers should wait for the session to
    become available. This should be kept relatively short to help detect
    incorrect code, but sometimes may need to be increased if the chief takes
    a while to start up.
* <b>`run_metadata`</b>: A [`RunMetadata`] protocol buffer.


#### Returns:

the value of the loss function after training.


#### Raises:

* <b>`ValueError`</b>: if `logdir` is `None` and either `save_checkpoint_secs` or
  `save_summaries_steps` are `None.