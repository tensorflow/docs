

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tfdbg.LocalCLIDebugHook

## Class `LocalCLIDebugHook`

Inherits From: [`SessionRunHook`](../tf/train/SessionRunHook)



Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/debug/wrappers/hooks.py).

See the guide: [TensorFlow Debugger > Session wrapper class and `SessionRunHook` implementations](../../../api_guides/python/tfdbg#Session_wrapper_class_and_SessionRunHook_implementations)

Command-line-interface debugger hook.

Can be used as a monitor/hook for <a href="../tf/train/MonitoredSession"><code>tf.train.MonitoredSession</code></a>s and
<a href="../tf/contrib/learn"><code>tf.contrib.learn</code></a>'s `Estimator`s and `Experiment`s.

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



<h3 id="before_run"><code>before_run</code></h3>

``` python
before_run(run_context)
```



<h3 id="begin"><code>begin</code></h3>

``` python
begin()
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



