


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.train.SingularMonitoredSession

### `class tf.train.SingularMonitoredSession`

See the guide: [Training > Distributed execution](../../../../api_guides/python/train#Distributed_execution)

Session-like object that handles initialization, restoring, and hooks.

Please note that this utility is not recommended for distributed settings.
For distributed settings, please use `tf.train.MonitoredSession`. The
differences between `MonitoredSession` and `SingularMonitoredSession` are:
* `MonitoredSession` handles `AbortedError` for distributed settings,
  but `SingularMonitoredSession` does not.
* `MonitoredSession` can be created in `chief` or `worker` modes.
  `SingularMonitoredSession` is always created as `chief`.
* You can access the raw `tf.Session` object used by
  `SingularMonitoredSession`, whereas in MonitoredSession the raw session is
  private. This can be used:
  - To `run` without hooks.
  - To save and restore.
* All other functionality is identical.

Example usage:
```python
saver_hook = CheckpointSaverHook(...)
summary_hook = SummaryHook(...)
with SingularMonitoredSession(hooks=[saver_hook, summary_hook]) as sess:
  while not sess.should_stop():
    sess.run(train_op)
```

Initialization: At creation time the hooked session does following things
in given order:

* calls `hook.begin()` for each given hook
* finalizes the graph via `scaffold.finalize()`
* create session
* initializes the model via initialization ops provided by `Scaffold`
* restores variables if a checkpoint exists
* launches queue runners

Run: When `run()` is called, the hooked session does following things:

* calls `hook.before_run()`
* calls TensorFlow `session.run()` with merged fetches and feed_dict
* calls `hook.after_run()`
* returns result of `session.run()` asked by user

Exit: At the `close()`, the hooked session does following things in order:

* calls `hook.end()`
* closes the queue runners and the session
* surpresses `OutOfRange` error which indicates that all inputs have been
  processed if the `SingularMonitoredSession` is used as a context.

## Properties

<h3 id="graph"><code>graph</code></h3>

The graph that was launched in this session.



## Methods

<h3 id="__init__"><code>__init__(hooks=None, scaffold=None, master='', config=None, checkpoint_dir=None)</code></h3>

Creates a SingularMonitoredSession.

#### Args:

* <b>`hooks`</b>: An iterable of `SessionRunHook' objects.
* <b>`scaffold`</b>: A `Scaffold` used for gathering or building supportive ops. If
    not specified a default one is created. It's used to finalize the graph.
* <b>`master`</b>: `String` representation of the TensorFlow master to use.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.
* <b>`checkpoint_dir`</b>: A string.  Optional path to a directory where to restore
    variables.

<h3 id="close"><code>close()</code></h3>



<h3 id="raw_session"><code>raw_session()</code></h3>

Returns underlying `TensorFlow.Session` object.

<h3 id="run"><code>run(fetches, feed_dict=None, options=None, run_metadata=None)</code></h3>

Run ops in the monitored session.

This method is completely compatible with the `tf.Session.run()` method.

#### Args:

* <b>`fetches`</b>: Same as `tf.Session.run()`.
* <b>`feed_dict`</b>: Same as `tf.Session.run()`.
* <b>`options`</b>: Same as `tf.Session.run()`.
* <b>`run_metadata`</b>: Same as `tf.Session.run()`.


#### Returns:

  Same as `tf.Session.run()`.

<h3 id="should_stop"><code>should_stop()</code></h3>







Defined in [`tensorflow/python/training/monitored_session.py`](https://www.tensorflow.org/code/tensorflow/python/training/monitored_session.py).

