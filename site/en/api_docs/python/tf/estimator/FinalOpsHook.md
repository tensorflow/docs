page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.FinalOpsHook


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L927-L967">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `FinalOpsHook`

A hook which evaluates `Tensors` at the end of a session.

Inherits From: [`SessionRunHook`](../../tf/estimator/SessionRunHook)

### Aliases:

* Class `tf.compat.v1.estimator.FinalOpsHook`
* Class `tf.compat.v1.train.FinalOpsHook`
* Class `tf.compat.v2.estimator.FinalOpsHook`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L930-L941">View source</a>

``` python
__init__(
    final_ops,
    final_ops_feed_dict=None
)
```

Initializes `FinalOpHook` with ops to run at the end of the session.


#### Args:


* <b>`final_ops`</b>: A single `Tensor`, a list of `Tensors` or a dictionary of names
  to `Tensors`.
* <b>`final_ops_feed_dict`</b>: A feed dictionary to use when running
  `final_ops_dict`.



## Properties

<h3 id="final_ops_values"><code>final_ops_values</code></h3>






## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/session_run_hook.py#L112-L127">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/session_run_hook.py#L152-L169">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/session_run_hook.py#L129-L150">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/session_run_hook.py#L101-L110">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L947-L967">View source</a>

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
