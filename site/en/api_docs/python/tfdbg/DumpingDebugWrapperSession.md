


<!-- DO NOT EDIT! Automatically generated file. -->
# tfdbg.DumpingDebugWrapperSession

### `class tfdbg.DumpingDebugWrapperSession`

See the guide: [TensorFlow Debugger > Session wrapper class and `SessionRunHook` implementations](../../../api_guides/python/tfdbg#Session_wrapper_class_and_SessionRunHook_implementations)

Debug Session wrapper that dumps debug data to filesystem.

## Properties

<h3 id="graph"><code>graph</code></h3>



<h3 id="sess_str"><code>sess_str</code></h3>



<h3 id="session"><code>session</code></h3>





## Methods

<h3 id="__init__"><code>__init__(sess, session_root, watch_fn=None, log_usage=True)</code></h3>

Constructor of DumpingDebugWrapperSession.

#### Args:

* <b>`sess`</b>: The TensorFlow `Session` object being wrapped.
* <b>`session_root`</b>: (`str`) Path to the session root directory. Must be a
    directory that does not exist or an empty directory. If the directory
    does not exist, it will be created by the debugger core during debug
    [`tf.Session.run`](../tf/Session#run)
    calls.
    As the `run()` calls occur, subdirectories will be added to
    `session_root`. The subdirectories' names has the following pattern:
      run_<epoch_time_stamp>_<uuid>
    E.g., run_1480734393835964_ad4c953a85444900ae79fc1b652fb324
* <b>`watch_fn`</b>: (`Callable`) A Callable that can be used to define per-run
    debug ops and watched tensors. See the doc of
    `NonInteractiveDebugWrapperSession.__init__()` for details.
* <b>`log_usage`</b>: (`bool`) whether the usage of this class is to be logged.


#### Raises:

   ValueError: If `session_root` is an existing and non-empty directory or
   if `session_root` is a file.

<h3 id="close"><code>close()</code></h3>



<h3 id="invoke_node_stepper"><code>invoke_node_stepper(node_stepper, restore_variable_values_on_exit=True)</code></h3>

See doc of BaseDebugWrapperSession.invoke_node_stepper.

<h3 id="on_run_end"><code>on_run_end(request)</code></h3>

See doc of BaseDebugWrapperSession.on_run_end.

<h3 id="on_run_start"><code>on_run_start(request)</code></h3>

See doc of BaseDebugWrapperSession.on_run_start.

<h3 id="on_session_init"><code>on_session_init(request)</code></h3>

See doc of BaseDebugWrapperSession.on_run_start.

<h3 id="partial_run"><code>partial_run(handle, fetches, feed_dict=None)</code></h3>



<h3 id="partial_run_setup"><code>partial_run_setup(fetches, feeds=None)</code></h3>

Sets up the feeds and fetches for partial runs in the session.

<h3 id="run"><code>run(fetches, feed_dict=None, options=None, run_metadata=None)</code></h3>

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





Defined in [`tensorflow/python/debug/wrappers/dumping_wrapper.py`](https://www.tensorflow.org/code/tensorflow/python/debug/wrappers/dumping_wrapper.py).

