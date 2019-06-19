page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.TensorBoardDebugHook

## Class `TensorBoardDebugHook`

Inherits From: [`GrpcDebugHook`](../tfdbg/GrpcDebugHook)



Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/debug/wrappers/hooks.py).

A tfdbg hook that can be used with TensorBoard Debugger Plugin.

This hook is the same as `GrpcDebugHook`, except that it uses a predefined
  `watch_fn` that
  1) uses `DebugIdentity` debug ops with the `gated_grpc` attribute set to
      `True`, to allow the interactive enabling and disabling of tensor
     breakpoints.
  2) watches all tensors in the graph.
This saves the need for the user to define a `watch_fn`.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    grpc_debug_server_addresses,
    thread_name_filter=None,
    send_traceback_and_source_code=True,
    log_usage=True
)
```

Constructor of TensorBoardDebugHook.

#### Args:

* <b>`grpc_debug_server_addresses`</b>: gRPC address(es) of debug server(s), as a
    `str` or a `list` of `str`s. E.g., "localhost:2333",
    "grpc://localhost:2333", ["192.168.0.7:2333", "192.168.0.8:2333"].
* <b>`thread_name_filter`</b>: Optional filter for thread names.
* <b>`send_traceback_and_source_code`</b>: Whether traceback of graph elements and
    the source code are to be sent to the debug server(s).
* <b>`log_usage`</b>: Whether the usage of this class is to be logged (if
    applicable).

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



