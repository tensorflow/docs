

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.model_pruning.train

``` python
tf.contrib.model_pruning.train(
    train_op,
    logdir,
    mask_update_op,
    train_step_fn=train_step,
    train_step_kwargs=_USE_DEFAULT,
    log_every_n_steps=1,
    graph=None,
    master='',
    is_chief=True,
    global_step=None,
    number_of_steps=None,
    init_op=_USE_DEFAULT,
    init_feed_dict=None,
    local_init_op=_USE_DEFAULT,
    init_fn=None,
    ready_op=_USE_DEFAULT,
    summary_op=_USE_DEFAULT,
    save_summaries_secs=600,
    summary_writer=_USE_DEFAULT,
    startup_delay_steps=0,
    saver=None,
    save_interval_secs=600,
    sync_optimizer=None,
    session_config=None,
    trace_every_n_steps=None
)
```



Defined in [`tensorflow/contrib/model_pruning/python/learning.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/model_pruning/python/learning.py).

Wrapper around tf-slim's train function.

Runs a training loop using a TensorFlow supervisor.
When the sync_optimizer is supplied, gradient updates are applied
synchronously. Otherwise, gradient updates are applied asynchronous.

#### Args:

* <b>`train_op`</b>: A `Tensor` that, when executed, will apply the gradients and
    return the loss value.
* <b>`logdir`</b>: The directory where training logs are written to. If None, model
    checkpoints and summaries will not be written.
* <b>`mask_update_op`</b>: Operation that upon execution updates the weight masks and
    thresholds.
* <b>`train_step_fn`</b>: The function to call in order to execute a single gradient
    step. The function must have take exactly four arguments: the current
    session, the `train_op` `Tensor`, a global step `Tensor` and a dictionary.
* <b>`train_step_kwargs`</b>: A dictionary which is passed to the `train_step_fn`. By
    default, two `Boolean`, scalar ops called "should_stop" and "should_log"
    are provided.
* <b>`log_every_n_steps`</b>: The frequency, in terms of global steps, that the loss
    and global step and logged.
* <b>`graph`</b>: The graph to pass to the supervisor. If no graph is supplied the
    default graph is used.
* <b>`master`</b>: The address of the tensorflow master.
* <b>`is_chief`</b>: Specifies whether or not the training is being run by the primary
    replica during replica training.
* <b>`global_step`</b>: The `Tensor` representing the global step. If left as `None`,
    then slim.variables.get_or_create_global_step() is used.
* <b>`number_of_steps`</b>: The max number of gradient steps to take during training,
    as measured by 'global_step': training will stop if global_step is
    greater than 'number_of_steps'. If the value is left as None, training
    proceeds indefinitely.
* <b>`init_op`</b>: The initialization operation. If left to its default value, then
    the session is initialized by calling `tf.global_variables_initializer()`.
* <b>`init_feed_dict`</b>: A feed dictionary to use when executing the `init_op`.
* <b>`local_init_op`</b>: The local initialization operation. If left to its default
    value, then the session is initialized by calling
    `tf.local_variables_initializer()` and `tf.tables_initializer()`.
* <b>`init_fn`</b>: An optional callable to be executed after `init_op` is called. The
    callable must accept one argument, the session being initialized.
* <b>`ready_op`</b>: Operation to check if the model is ready to use. If left to its
    default value, then the session checks for readiness by calling
    `tf.report_uninitialized_variables()`.
* <b>`summary_op`</b>: The summary operation.
* <b>`save_summaries_secs`</b>: How often, in seconds, to save summaries.
* <b>`summary_writer`</b>: `SummaryWriter` to use.  Can be `None`
    to indicate that no summaries should be written. If unset, we
    create a SummaryWriter.
* <b>`startup_delay_steps`</b>: The number of steps to wait for before beginning. Note
    that this must be 0 if a sync_optimizer is supplied.
* <b>`saver`</b>: Saver to save checkpoints. If None, a default one will be created
    and used.
* <b>`save_interval_secs`</b>: How often, in seconds, to save the model to `logdir`.
* <b>`sync_optimizer`</b>: an instance of tf.train.SyncReplicasOptimizer, or a list of
    them. If the argument is supplied, gradient updates will be synchronous.
    If left as `None`, gradient updates will be asynchronous.
* <b>`session_config`</b>: An instance of <a href="../../../tf/ConfigProto"><code>tf.ConfigProto</code></a> that will be used to
    configure the `Session`. If left as `None`, the default will be used.
* <b>`trace_every_n_steps`</b>: produce and save a `Timeline` in Chrome trace format
    and add it to the summaries every `trace_every_n_steps`. If None, no trace
    information will be produced or saved.


#### Returns:

the value of the loss function after training.


#### Raises:

* <b>`ValueError`</b>: if `train_op` is empty or if `startup_delay_steps` is
    non-zero when `sync_optimizer` is supplied, if `number_of_steps` is
    negative, or if `trace_every_n_steps` is not `None` and no `logdir` is
    provided.