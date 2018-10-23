


<!-- DO NOT EDIT! Automatically generated file. -->
# tfdbg.LocalCLIDebugHook

### `class tfdbg.LocalCLIDebugHook`

See the guide: [TensorFlow Debugger > Session wrapper class and `SessionRunHook` implementations](../../../api_guides/python/tfdbg#Session_wrapper_class_and_SessionRunHook_implementations)

Command-line-interface debugger hook.

Can be used as a monitor/hook for `tf.train.MonitoredSession`s and
`tf.contrib.learn`'s `Estimator`s and `Experiment`s.

## Properties

<h3 id="graph"><code>graph</code></h3>



<h3 id="sess_str"><code>sess_str</code></h3>



<h3 id="session"><code>session</code></h3>





## Methods

<h3 id="__init__"><code>__init__(ui_type='curses')</code></h3>

Create a local debugger command-line interface (CLI) hook.

#### Args:

* <b>`ui_type`</b>: (str) user-interface type.

<h3 id="add_tensor_filter"><code>add_tensor_filter(filter_name, tensor_filter)</code></h3>

Add a tensor filter.

#### Args:

* <b>`filter_name`</b>: (`str`) name of the filter.
* <b>`tensor_filter`</b>: (`callable`) the filter callable. See the doc string of
    `DebugDumpDir.find()` for more details about its signature.

<h3 id="after_create_session"><code>after_create_session(session, coord)</code></h3>

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

<h3 id="after_run"><code>after_run(run_context, run_values)</code></h3>



<h3 id="before_run"><code>before_run(run_context)</code></h3>



<h3 id="begin"><code>begin()</code></h3>



<h3 id="close"><code>close()</code></h3>



<h3 id="end"><code>end(session)</code></h3>

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

#### Args:

* <b>`session`</b>: A TensorFlow Session that will be soon closed.

<h3 id="invoke_node_stepper"><code>invoke_node_stepper(node_stepper, restore_variable_values_on_exit=True)</code></h3>

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

<h3 id="on_run_end"><code>on_run_end(request)</code></h3>

Overrides on-run-end callback.

Actions taken:
  1) Load the debug dump.
  2) Bring up the Analyzer CLI.

#### Args:

* <b>`request`</b>: An instance of OnSessionInitRequest.


#### Returns:

  An instance of OnSessionInitResponse.

<h3 id="on_run_start"><code>on_run_start(request)</code></h3>

Overrides on-run-start callback.

Invoke the CLI to let user choose what action to take:
  `run` / `invoke_stepper`.

#### Args:

* <b>`request`</b>: An instance of `OnSessionInitRequest`.


#### Returns:

  An instance of `OnSessionInitResponse`.


#### Raises:

* <b>`RuntimeError`</b>: If user chooses to prematurely exit the debugger.

<h3 id="on_session_init"><code>on_session_init(request)</code></h3>

Overrides on-session-init callback.

#### Args:

* <b>`request`</b>: An instance of `OnSessionInitRequest`.


#### Returns:

  An instance of `OnSessionInitResponse`.

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





Defined in [`tensorflow/python/debug/wrappers/hooks.py`](https://www.tensorflow.org/code/tensorflow/python/debug/wrappers/hooks.py).

