


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.KMeansClustering.LossRelativeChangeHook

### `class tf.contrib.learn.KMeansClustering.LossRelativeChangeHook`

Stops when the change in loss goes below a tolerance.

## Methods

<h3 id="__init__"><code>__init__(tolerance)</code></h3>

Initializes LossRelativeChangeHook.

#### Args:

* <b>`tolerance`</b>: A relative tolerance of change between iterations.

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





Defined in [`tensorflow/contrib/learn/python/learn/estimators/kmeans.py`](https://www.tensorflow.org/code/tensorflow/contrib/learn/python/learn/estimators/kmeans.py).

