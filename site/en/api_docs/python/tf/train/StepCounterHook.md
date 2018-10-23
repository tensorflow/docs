


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.train.StepCounterHook

### `class tf.train.StepCounterHook`

See the guide: [Training > Training Hooks](../../../../api_guides/python/train#Training_Hooks)

Steps per second monitor.

## Methods

<h3 id="__init__"><code>__init__(every_n_steps=100, every_n_secs=None, output_dir=None, summary_writer=None)</code></h3>



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



<h3 id="end"><code>end(session)</code></h3>

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

#### Args:

* <b>`session`</b>: A TensorFlow Session that will be soon closed.





Defined in [`tensorflow/python/training/basic_session_run_hooks.py`](https://www.tensorflow.org/code/tensorflow/python/training/basic_session_run_hooks.py).

