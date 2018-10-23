

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tfdbg.LocalCLIDebugHook

## Class `LocalCLIDebugHook`

Inherits From: [`SessionRunHook`](../tf/train/SessionRunHook), [`LocalCLIDebugWrapperSession`](../tfdbg/LocalCLIDebugWrapperSession)



Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/debug/wrappers/hooks.py).

See the guide: [TensorFlow Debugger > Session wrapper class and `SessionRunHook` implementations](../../../api_guides/python/tfdbg#Session_wrapper_class_and_SessionRunHook_implementations)

Command-line-interface debugger hook.

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
    ui_type='curses',
    dump_root=None,
    thread_name_filter=None
)
```

Create a local debugger command-line interface (CLI) hook.

#### Args:

* <b>`ui_type`</b>: (str) user-interface type.
* <b>`dump_root`</b>: (`str`) optional path to the dump root directory. Must be a
    directory that does not exist or an empty directory. If the directory
    does not exist, it will be created by the debugger core during debug
    `run()` calls and removed afterwards.
* <b>`thread_name_filter`</b>: Regular-expression white list for threads on which the
    wrapper session will be active. See doc of `BaseDebugWrapperSession` for
    more details.

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



<h3 id="add_tensor_filter"><code>add_tensor_filter</code></h3>

``` python
add_tensor_filter(
    filter_name,
    tensor_filter
)
```

Add a tensor filter.

See doc of `LocalCLIDebugWrapperSession.add_tensor_filter()` for details.
Override default behavior to accommodate the possibility of this method being
called prior to the initialization of the underlying
`LocalCLIDebugWrapperSession` object.

#### Args:

* <b>`filter_name`</b>: See doc of `LocalCLIDebugWrapperSession.add_tensor_filter()`
    for details.
* <b>`tensor_filter`</b>: See doc of
    `LocalCLIDebugWrapperSession.add_tensor_filter()` for details.

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

If `session.run()` raises exception other than OutOfRangeError or
StopIteration then `end()` is not called.
Note the difference between `end()` and `after_run()` behavior when
`session.run()` raises OutOfRangeError or StopIteration. In that case
`end()` is called but `after_run()` is not called.

#### Args:

* <b>`session`</b>: A TensorFlow Session that will be soon closed.

<h3 id="invoke_node_stepper"><code>invoke_node_stepper</code></h3>

``` python
invoke_node_stepper(
    node_stepper,
    restore_variable_values_on_exit=True
)
```

Overrides method in base class to implement interactive node stepper.

#### Args:

* <b>`node_stepper`</b>: (`stepper.NodeStepper`) The underlying NodeStepper API
    object.
* <b>`restore_variable_values_on_exit`</b>: (`bool`) Whether any variables whose
    values have been altered during this node-stepper invocation should be
    restored to their old values when this invocation ends.


#### Returns:

  The same return values as the `Session.run()` call on the same fetches as
    the NodeStepper.

<h3 id="list_devices"><code>list_devices</code></h3>

``` python
list_devices(
    *args,
    **kwargs
)
```



<h3 id="make_callable"><code>make_callable</code></h3>

``` python
make_callable(
    fetches,
    feed_list=None,
    accept_options=False
)
```



<h3 id="on_run_end"><code>on_run_end</code></h3>

``` python
on_run_end(request)
```

Overrides on-run-end callback.

Actions taken:
  1) Load the debug dump.
  2) Bring up the Analyzer CLI.

#### Args:

* <b>`request`</b>: An instance of OnSessionInitRequest.


#### Returns:

  An instance of OnSessionInitResponse.

<h3 id="on_run_start"><code>on_run_start</code></h3>

``` python
on_run_start(request)
```

Overrides on-run-start callback.

Invoke the CLI to let user choose what action to take:
  `run` / `invoke_stepper`.

#### Args:

* <b>`request`</b>: An instance of `OnRunStartRequest`.


#### Returns:

  An instance of `OnRunStartResponse`.

<h3 id="on_session_init"><code>on_session_init</code></h3>

``` python
on_session_init(request)
```

Overrides on-session-init callback.

#### Args:

* <b>`request`</b>: An instance of `OnSessionInitRequest`.


#### Returns:

  An instance of `OnSessionInitResponse`.

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

<h3 id="reset"><code>reset</code></h3>

``` python
reset(
    *args,
    **kwargs
)
```



<h3 id="run"><code>run</code></h3>

``` python
run(
    fetches,
    feed_dict=None,
    options=None,
    run_metadata=None,
    callable_runner=None,
    callable_runner_args=None
)
```

Wrapper around Session.run() that inserts tensor watch options.

#### Args:

* <b>`fetches`</b>: Same as the `fetches` arg to regular `Session.run()`.
* <b>`feed_dict`</b>: Same as the `feed_dict` arg to regular `Session.run()`.
* <b>`options`</b>: Same as the `options` arg to regular `Session.run()`.
* <b>`run_metadata`</b>: Same as the `run_metadata` arg to regular `Session.run()`.
* <b>`callable_runner`</b>: A `callable` returned by `Session.make_callable()`.
    If not `None`, `fetches` and `feed_dict` must both be `None`.
* <b>`callable_runner_args`</b>: An optional list of arguments to `callable_runner`.


#### Returns:

  Simply forwards the output of the wrapped `Session.run()` call.


#### Raises:

* <b>`ValueError`</b>: On invalid `OnRunStartAction` value. Or if `callable_runner`
    is not `None` and either or both of `fetches` and `feed_dict` is `None`.



