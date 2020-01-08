

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.GrpcDebugHook

## Class `GrpcDebugHook`

Inherits From: [`SessionRunHook`](../tf/train/SessionRunHook)



Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/debug/wrappers/hooks.py).

A hook that streams debugger-related events to any grpc_debug_server.

For example, the debugger data server is a grpc_debug_server. The debugger
data server writes debugger-related events it receives via GRPC to logdir.
This enables debugging features in Tensorboard such as health pills.

When the arguments of debug_utils.watch_graph changes, strongly consider
changing arguments here too so that features are available to tflearn users.

Can be used as a hook for <a href="../tf/train/MonitoredSession"><code>tf.train.MonitoredSession</code></a>s and
<a href="../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>s.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    grpc_debug_server_addresses,
    watch_fn=None,
    thread_name_filter=None,
    log_usage=True
)
```

Constructs a GrpcDebugHook.

#### Args:

* <b>`grpc_debug_server_addresses`</b>: (`list` of `str`) A list of the gRPC debug
    server addresses, in the format of <host:port>, with or without the
    "grpc://" prefix. For example: ["localhost:7000", "192.168.0.2:8000"]
* <b>`watch_fn`</b>: A function that allows for customizing which ops to watch at
    which specific steps. See doc of
    `dumping_wrapper.DumpingDebugWrapperSession.__init__` for details.
* <b>`thread_name_filter`</b>: Regular-expression white list for threads on which the
    wrapper session will be active. See doc of `BaseDebugWrapperSession` for
    more details.
* <b>`log_usage`</b>: (bool) Whether usage is to be logged.

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

Called right before a session is run.

#### Args:

* <b>`run_context`</b>: A session_run_hook.SessionRunContext. Encapsulates
    information on the run.


#### Returns:

A session_run_hook.SessionRunArgs object.

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



