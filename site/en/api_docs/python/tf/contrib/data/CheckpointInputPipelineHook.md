page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.CheckpointInputPipelineHook


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/data/python/ops/iterator_ops.py#L64-L112">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CheckpointInputPipelineHook`

Checkpoints input pipeline state every N steps or seconds.

Inherits From: [`CheckpointInputPipelineHook`](../../../tf/data/experimental/CheckpointInputPipelineHook)

<!-- Placeholder for "Used in" -->

This hook saves the state of the iterators in the `Graph` so that when
training is resumed the input pipeline continues from where it left off.
This could potentially avoid overfitting in certain pipelines where the
number of training steps per eval are small compared to the dataset
size or if the training pipeline is pre-empted.

Differences from `CheckpointSaverHook`:
1. Saves only the input pipelines in the "iterators" collection and not the
   global variables or other saveable objects.
2. Does not write the `GraphDef` and `MetaGraphDef` to the summary.

Example of checkpointing the training pipeline:

```python
est = tf.estimator.Estimator(model_fn)
while True:
  est.train(
      train_input_fn,
      hooks=[tf.data.experimental.CheckpointInputPipelineHook(est)],
      steps=train_steps_per_eval)
  # Note: We do not pass the hook here.
  metrics = est.evaluate(eval_input_fn)
  if should_stop_the_training(metrics):
    break
```

This hook should be used if the input pipeline state needs to be saved
separate from the model checkpoint. Doing so may be useful for a few reasons:
1. The input pipeline checkpoint may be large, if there are large shuffle
   or prefetch buffers for instance, and may bloat the checkpoint size.
2. If the input pipeline is shared between training and validation, restoring
   the checkpoint during validation may override the validation input
   pipeline.

For saving the input pipeline checkpoint alongside the model weights use
<a href="../../../tf/data/experimental/make_saveable_from_iterator"><code>tf.data.experimental.make_saveable_from_iterator</code></a> directly to create a
`SaveableObject` and add to the `SAVEABLE_OBJECTS` collection. Note, however,
that you will need to be careful not to restore the training iterator during
eval. You can do that by not adding the iterator to the SAVEABLE_OBJECTS
collector when building the eval graph.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/data/python/ops/iterator_ops.py#L109-L112">View source</a>

``` python
__init__(estimator)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/CheckpointInputPipelineHook"><code>tf.data.experimental.CheckpointInputPipelineHook(...)</code></a>.



## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/session_run_hook.py#L112-L127">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/iterator_ops.py#L240-L241">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/iterator_ops.py#L234-L238">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/iterator_ops.py#L186-L197">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/iterator_ops.py#L243-L244">View source</a>

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
