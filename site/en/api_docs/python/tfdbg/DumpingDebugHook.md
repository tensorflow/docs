

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tfdbg.DumpingDebugHook

### `class tfdbg.DumpingDebugHook`



Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/debug/wrappers/hooks.py).

See the guide: [TensorFlow Debugger > Session wrapper class and `SessionRunHook` implementations](../../../api_guides/python/tfdbg#Session_wrapper_class_and_SessionRunHook_implementations)

A debugger hook that dumps debug data to filesystem.

Can be used as a monitor/hook for `tf.train.MonitoredSession`s and
`tf.contrib.learn`'s `Estimator`s and `Experiment`s.

## Properties

<h3 id="graph"><code>graph</code></h3>



<h3 id="graph_def"><code>graph_def</code></h3>



<h3 id="sess_str"><code>sess_str</code></h3>



<h3 id="session"><code>session</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    session_root,
    watch_fn=None,
    log_usage=True
)
```

Create a local debugger command-line interface (CLI) hook.

#### Args:

* <b>`session_root`</b>: See doc of
    `dumping_wrapper.DumpingDebugWrapperSession.__init__`.
* <b>`watch_fn`</b>: See doc of
    `dumping_wrapper.DumpingDebugWrapperSession.__init__`.
* <b>`log_usage`</b>: (bool) Whether usage is to be logged.

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    exec_type,
    exec_value,
    exec_tb
)
```



<h3 id="after_create_session"><code>after_create_session</code></h3>

``` python
after_create_session(
    session,
    coord
)
```

Called when new TensorFlow session is created.

This is called to signal the hooks that a new session has been created. This
has two essential differences with the situation in which `begin` is called:

* When this is called, the graph is finalized and ops can no longer be added
    to the graph.
* This method will also be called as a result of recovering a wrapped
    session, not only at the beginning of the overall session.

#### Args:

* <b>`session`</b>: A TensorFlow Session that has been created.
* <b>`coord`</b>: A Coordinator object which keeps track of all threads.

<h3 id="after_run"><code>after_run</code></h3>

``` python
after_run(
    run_context,
    run_values
)
```



<h3 id="as_default"><code>as_default</code></h3>

``` python
as_default()
```



<h3 id="before_run"><code>before_run</code></h3>

``` python
before_run(run_context)
```



<h3 id="begin"><code>begin</code></h3>

``` python
begin()
```



<h3 id="close"><code>close</code></h3>

``` python
close()
```



<h3 id="end"><code>end</code></h3>

``` python
end(session)
```

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

#### Args:

* <b>`session`</b>: A TensorFlow Session that will be soon closed.

<h3 id="invoke_node_stepper"><code>invoke_node_stepper</code></h3>

``` python
invoke_node_stepper(
    node_stepper,
    restore_variable_values_on_exit=True
)
```

See doc of BaseDebugWrapperSession.invoke_node_stepper.

<h3 id="on_run_end"><code>on_run_end</code></h3>

``` python
on_run_end(request)
```

See doc of BaseDebugWrapperSession.on_run_end.

<h3 id="on_run_start"><code>on_run_start</code></h3>

``` python
on_run_start(request)
```

See doc of BaseDebugWrapperSession.on_run_start.

<h3 id="on_session_init"><code>on_session_init</code></h3>

``` python
on_session_init(request)
```

See doc of BaseDebugWrapperSession.on_run_start.

<h3 id="partial_run"><code>partial_run</code></h3>

``` python
partial_run(
    handle,
    fetches,
    feed_dict=None
)
```



<h3 id="partial_run_setup"><code>partial_run_setup</code></h3>

``` python
partial_run_setup(
    fetches,
    feeds=None
)
```

Sets up the feeds and fetches for partial runs in the session.

<h3 id="prepare_run_debug_urls"><code>prepare_run_debug_urls</code></h3>

``` python
prepare_run_debug_urls(
    fetches,
    feed_dict
)
```

Implementation of abstrat method in superclass.

See doc of `NonInteractiveDebugWrapperSession.prepare_run_debug_urls()`
for details. This implentation creates a run-specific subdirectory under
self._session_root and stores information regarding run `fetches` and
`feed_dict.keys()` in the subdirectory.

#### Args:

* <b>`fetches`</b>: Same as the `fetches` argument to `Session.run()`
* <b>`feed_dict`</b>: Same as the `feed_dict` argument to `Session.run()`


#### Returns:

* <b>`debug_urls`</b>: (`str` or `list` of `str`) file:// debug URLs to be used in
    this `Session.run()` call.

<h3 id="run"><code>run</code></h3>

``` python
run(
    fetches,
    feed_dict=None,
    options=None,
    run_metadata=None
)
```

Wrapper around Session.run() that inserts tensor watch options.

#### Args:

* <b>`fetches`</b>: Same as the `fetches` arg to regular `Session.run()`.
* <b>`feed_dict`</b>: Same as the `feed_dict` arg to regular `Session.run()`.
* <b>`options`</b>: Same as the `options` arg to regular `Session.run()`.
* <b>`run_metadata`</b>: Same as the `run_metadata` arg to regular `Session.run()`.


#### Returns:

  Simply forwards the output of the wrapped `Session.run()` call.


#### Raises:

* <b>`ValueError`</b>: On invalid `OnRunStartAction` value.



