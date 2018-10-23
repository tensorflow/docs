

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.SingularMonitoredSession

## Class `SingularMonitoredSession`





Defined in [`tensorflow/python/training/monitored_session.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/training/monitored_session.py).

See the guide: [Training > Distributed execution](../../../../api_guides/python/train#Distributed_execution)

Session-like object that handles initialization, restoring, and hooks.

Please note that this utility is not recommended for distributed settings.
For distributed settings, please use `tf.train.MonitoredSession`. The
differences between `MonitoredSession` and `SingularMonitoredSession` are:

* `MonitoredSession` handles `AbortedError` and `UnavailableError` for
  distributed settings, but `SingularMonitoredSession` does not.
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
summary_hook = SummarySaverHook(...)
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
* suppresses `OutOfRange` error which indicates that all inputs have been
  processed if the `SingularMonitoredSession` is used as a context.

## Child Classes
[`class StepContext`](../../tf/train/MonitoredSession/StepContext)

## Properties

<h3 id="graph"><code>graph</code></h3>

The graph that was launched in this session.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    hooks=None,
    scaffold=None,
    master='',
    config=None,
    checkpoint_dir=None,
    stop_grace_period_secs=120,
    checkpoint_filename_with_path=None
)
```

Creates a SingularMonitoredSession.

#### Args:

* <b>`hooks`</b>: An iterable of `SessionRunHook' objects.
* <b>`scaffold`</b>: A `Scaffold` used for gathering or building supportive ops. If
    not specified a default one is created. It's used to finalize the graph.
* <b>`master`</b>: `String` representation of the TensorFlow master to use.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.
* <b>`checkpoint_dir`</b>: A string.  Optional path to a directory where to restore
    variables.
* <b>`stop_grace_period_secs`</b>: Number of seconds given to threads to stop after
    `close()` has been called.
* <b>`checkpoint_filename_with_path`</b>: A string. Optional path to a checkpoint
    file from which to restore variables.

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    exception_type,
    exception_value,
    traceback
)
```



<h3 id="close"><code>close</code></h3>

``` python
close()
```



<h3 id="raw_session"><code>raw_session</code></h3>

``` python
raw_session()
```

Returns underlying `TensorFlow.Session` object.

<h3 id="run"><code>run</code></h3>

``` python
run(
    fetches,
    feed_dict=None,
    options=None,
    run_metadata=None
)
```

Run ops in the monitored session.

This method is completely compatible with the `tf.Session.run()` method.

#### Args:

* <b>`fetches`</b>: Same as `tf.Session.run()`.
* <b>`feed_dict`</b>: Same as `tf.Session.run()`.
* <b>`options`</b>: Same as `tf.Session.run()`.
* <b>`run_metadata`</b>: Same as `tf.Session.run()`.


#### Returns:

Same as `tf.Session.run()`.

<h3 id="run_step_fn"><code>run_step_fn</code></h3>

``` python
run_step_fn(step_fn)
```

Run ops using a step function.

#### Args:

* <b>`step_fn`</b>: A function or a method with a single argument of type
    `StepContext`.  The function may use methods of the argument to
    perform computations with access to a raw session.

    The returned value of the `step_fn` will be returned from `run_step_fn`,
    unless a stop is requested.  In that case, the next `should_stop` call
    will return True.

    Example usage:

    ```python
       with tf.Graph().as_default():
         c = tf.placeholder(dtypes.float32)
         v = tf.add(c, 4.0)
         w = tf.add(c, 0.5)

         def step_fn(step_context):
           a = step_context.session.run(fetches=v, feed_dict={c: 0.5})
           if a <= 4.5:
             step_context.request_stop()
           return step_context.run_with_hooks(fetches=w, feed_dict={c: 0.1})

         with tf.MonitoredSession() as session:
           while not session.should_stop():
             a = session.run_step_fn(step_fn)
    ```

    Hooks interact with the `run_with_hooks()` call inside the `step_fn`
    as they do with a `MonitoredSession.run` call.


#### Returns:

Returns the returned value of `step_fn`.


#### Raises:

* <b>`StopIteration`</b>: if `step_fn` has called `request_stop()`.  It may be
    caught by `with tf.MonitoredSession()` to close the session.
* <b>`ValueError`</b>: if `step_fn` doesn't have a single argument called
    `step_context`. It may also optionally have `self` for cases when it
    belongs to an object.

<h3 id="should_stop"><code>should_stop</code></h3>

``` python
should_stop()
```





