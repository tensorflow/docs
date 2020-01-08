

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.TensorBoardDebugWrapperSession

## Class `TensorBoardDebugWrapperSession`

Inherits From: [`GrpcDebugWrapperSession`](../tfdbg/GrpcDebugWrapperSession)



Defined in [`tensorflow/python/debug/wrappers/grpc_wrapper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/debug/wrappers/grpc_wrapper.py).

A tfdbg Session wrapper that can be used with TensorBoard Debugger Plugin.

This wrapper is the same as `GrpcDebugWrapperSession`, except that it uses a
  predefined `watch_fn` that
  1) uses `DebugIdentity` debug ops with the `gated_grpc` attribute set to
      `True` to allow the interactive enabling and disabling of tensor
     breakpoints.
  2) watches all tensors in the graph.
This saves the need for the user to define a `watch_fn`.

## Properties

<h3 id="graph"><code>graph</code></h3>



<h3 id="graph_def"><code>graph_def</code></h3>



<h3 id="run_call_count"><code>run_call_count</code></h3>



<h3 id="sess_str"><code>sess_str</code></h3>



<h3 id="session"><code>session</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    sess,
    grpc_debug_server_addresses,
    thread_name_filter=None,
    send_traceback_and_source_code=True,
    log_usage=True
)
```

Constructor of TensorBoardDebugWrapperSession.

#### Args:

* <b>`sess`</b>: The <a href="../tf/Session"><code>tf.Session</code></a> instance to be wrapped.
* <b>`grpc_debug_server_addresses`</b>: gRPC address(es) of debug server(s), as a
    `str` or a `list` of `str`s. E.g., "localhost:2333",
    "grpc://localhost:2333", ["192.168.0.7:2333", "192.168.0.8:2333"].
* <b>`thread_name_filter`</b>: Optional filter for thread names.
* <b>`send_traceback_and_source_code`</b>: Whether traceback of graph elements and
    the source code are to be sent to the debug server(s).
* <b>`log_usage`</b>: Whether the usage of this class is to be logged (if
    applicable).

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



<h3 id="as_default"><code>as_default</code></h3>

``` python
as_default()
```



<h3 id="close"><code>close</code></h3>

``` python
close()
```



<h3 id="increment_run_call_count"><code>increment_run_call_count</code></h3>

``` python
increment_run_call_count()
```



<h3 id="invoke_node_stepper"><code>invoke_node_stepper</code></h3>

``` python
invoke_node_stepper(
    node_stepper,
    restore_variable_values_on_exit=True
)
```

See doc of BaseDebugWrapperSession.invoke_node_stepper.

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

Implementation of abstract method in superclass.

See doc of `NonInteractiveDebugWrapperSession.prepare_run_debug_urls()`
for details.

#### Args:

* <b>`fetches`</b>: Same as the `fetches` argument to `Session.run()`
* <b>`feed_dict`</b>: Same as the `feed_dict` argument to `Session.run()`


#### Returns:

* <b>`debug_urls`</b>: (`str` or `list` of `str`) file:// debug URLs to be used in
    this `Session.run()` call.

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
    callable_runner_args=None,
    callable_options=None
)
```



<h3 id="run_step_fn"><code>run_step_fn</code></h3>

``` python
run_step_fn(step_fn)
```



<h3 id="should_stop"><code>should_stop</code></h3>

``` python
should_stop()
```





