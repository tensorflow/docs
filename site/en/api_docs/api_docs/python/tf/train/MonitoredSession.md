

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.MonitoredSession

## Class `MonitoredSession`





Defined in [`tensorflow/python/training/monitored_session.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/training/monitored_session.py).

See the guides: [Threading and Queues > Queue usage overview](../../../../api_guides/python/threading_and_queues#Queue_usage_overview), [Training > Distributed execution](../../../../api_guides/python/train#Distributed_execution)

Session-like object that handles initialization, recovery and hooks.

Example usage:

```python
saver_hook = CheckpointSaverHook(...)
summary_hook = SummarySaverHook(...)
with MonitoredSession(session_creator=ChiefSessionCreator(...),
                      hooks=[saver_hook, summary_hook]) as sess:
  while not sess.should_stop():
    sess.run(train_op)
```

Initialization: At creation time the monitored session does following things
in given order:

* calls `hook.begin()` for each given hook
* finalizes the graph via `scaffold.finalize()`
* create session
* initializes the model via initialization ops provided by `Scaffold`
* restores variables if a checkpoint exists
* launches queue runners
* calls `hook.after_create_session()`

Run: When `run()` is called, the monitored session does following things:

* calls `hook.before_run()`
* calls TensorFlow `session.run()` with merged fetches and feed_dict
* calls `hook.after_run()`
* returns result of `session.run()` asked by user
* if `AbortedError` or `UnavailableError` occurs, it recovers or
  reinitializes the session before executing the run() call again


Exit: At the `close()`, the monitored session does following things in order:

* calls `hook.end()`
* closes the queue runners and the session
* suppresses `OutOfRange` error which indicates that all inputs have been
  processed if the monitored_session is used as a context

How to set `tf.Session` arguments:

* In most cases you can set session arguments as follows:

```python
MonitoredSession(
  session_creator=ChiefSessionCreator(master=..., config=...))
```

* In distributed setting for a non-chief worker, you can use following:

```python
MonitoredSession(
  session_creator=WorkerSessionCreator(master=..., config=...))
```

See `MonitoredTrainingSession` for an example usage based on chief or worker.

Note: This is not a `tf.Session`. For example, it cannot do following:

* it cannot be set as default session.
* it cannot be sent to saver.save.
* it cannot be sent to tf.train.start_queue_runners.

#### Args:

* <b>`session_creator`</b>: A factory object to create session. Typically a
    `ChiefSessionCreator` which is the default one.
* <b>`hooks`</b>: An iterable of `SessionRunHook' objects.


#### Returns:

A MonitoredSession object.

## Properties

<h3 id="graph"><code>graph</code></h3>

The graph that was launched in this session.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    session_creator=None,
    hooks=None,
    stop_grace_period_secs=120
)
```



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

<h3 id="should_stop"><code>should_stop</code></h3>

``` python
should_stop()
```





