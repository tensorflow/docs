page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.LocalCLIDebugHook

## Class `LocalCLIDebugHook`

Inherits From: [`SessionRunHook`](../tf/train/SessionRunHook)



Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/debug/wrappers/hooks.py).

Command-line-interface debugger hook.

Can be used as a hook for <a href="../tf/train/MonitoredSession"><code>tf.train.MonitoredSession</code></a>s and
<a href="../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>s. Provides a substitute for
<a href="../tfdbg/LocalCLIDebugWrapperSession"><code>tfdbg.LocalCLIDebugWrapperSession</code></a> in cases where the session is not directly
available.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    ui_type='curses',
    dump_root=None,
    thread_name_filter=None
)
```

Create a local debugger command-line interface (CLI) hook.

#### Args:

* <b>`ui_type`</b>: (`str`) requested user-interface type. Currently supported:
    (curses | readline).
* <b>`dump_root`</b>: (`str`) optional path to the dump root directory. Must be a
    directory that does not exist or an empty directory. If the directory
    does not exist, it will be created by the debugger core during debug
    `run()` calls and removed afterwards.
* <b>`thread_name_filter`</b>: Regular-expression white list for threads on which the
    wrapper session will be active. See doc of `BaseDebugWrapperSession` for
    more details.



## Methods

<h3 id="add_tensor_filter"><code>add_tensor_filter</code></h3>

``` python
add_tensor_filter(
    filter_name,
    tensor_filter
)
```

Add a tensor filter.

See doc of `LocalCLIDebugWrapperSession.add_tensor_filter()` for details.
Override default behavior to accommodate the possibility of this method
being
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

Called after each call to run().

The `run_values` argument contains results of requested ops/tensors by
`before_run()`.

The `run_context` argument is the same one send to `before_run` call.
`run_context.request_stop()` can be called to stop the iteration.

If `session.run()` raises any exceptions then `after_run()` is not called.

#### Args:

* <b>`run_context`</b>: A `SessionRunContext` object.
* <b>`run_values`</b>: A SessionRunValues object.

<h3 id="before_run"><code>before_run</code></h3>

``` python
before_run(run_context)
```

Called before each call to run().

You can return from this call a `SessionRunArgs` object indicating ops or
tensors to add to the upcoming `run()` call.  These ops/tensors will be run
together with the ops/tensors originally passed to the original run() call.
The run args you return can also contain feeds to be added to the run()
call.

The `run_context` argument is a `SessionRunContext` that provides
information about the upcoming `run()` call: the originally requested
op/tensors, the TensorFlow Session.

At this point graph is finalized and you can not add ops.

#### Args:

* <b>`run_context`</b>: A `SessionRunContext` object.


#### Returns:

None or a `SessionRunArgs` object.

<h3 id="begin"><code>begin</code></h3>

``` python
begin()
```

Called once before using the session.

When called, the default graph is the one that will be launched in the
session.  The hook can modify the graph by adding new operations to it.
After the `begin()` call the graph will be finalized and the other callbacks
can not modify the graph anymore. Second call of `begin()` on the same
graph, should not change the graph.

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



