page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.SummarySaverHook


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L769-L874">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SummarySaverHook`

Saves summaries every N steps.

Inherits From: [`SessionRunHook`](../../tf/estimator/SessionRunHook)

### Aliases:

* Class `tf.compat.v1.estimator.SummarySaverHook`
* Class `tf.compat.v1.train.SummarySaverHook`
* Class `tf.compat.v2.estimator.SummarySaverHook`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L772-L808">View source</a>

``` python
__init__(
    save_steps=None,
    save_secs=None,
    output_dir=None,
    summary_writer=None,
    scaffold=None,
    summary_op=None
)
```

Initializes a `SummarySaverHook`.


#### Args:


* <b>`save_steps`</b>: `int`, save summaries every N steps. Exactly one of
  `save_secs` and `save_steps` should be set.
* <b>`save_secs`</b>: `int`, save summaries every N seconds.
* <b>`output_dir`</b>: `string`, the directory to save the summaries to. Only used if
  no `summary_writer` is supplied.
* <b>`summary_writer`</b>: `SummaryWriter`. If `None` and an `output_dir` was passed,
  one will be created accordingly.
* <b>`scaffold`</b>: `Scaffold` to get summary_op if it's not provided.
* <b>`summary_op`</b>: `Tensor` of type `string` containing the serialized `Summary`
  protocol buffer or a list of `Tensor`. They are most likely an output by
  TF summary methods like <a href="../../tf/compat/v1/summary/scalar"><code>tf.compat.v1.summary.scalar</code></a> or
  <a href="../../tf/compat/v1/summary/merge_all"><code>tf.compat.v1.summary.merge_all</code></a>. It can be passed in as one tensor; if
  more than one, they must be passed in as a list.


#### Raises:


* <b>`ValueError`</b>: Exactly one of scaffold or summary_op should be set.



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L831-L851">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L820-L829">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L811-L818">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/basic_session_run_hooks.py#L853-L855">View source</a>

``` python
end(session=None)
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
