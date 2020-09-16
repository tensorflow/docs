description: Checkpoints input pipeline state every N steps or seconds.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.CheckpointInputPipelineHook" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="after_create_session"/>
<meta itemprop="property" content="after_run"/>
<meta itemprop="property" content="before_run"/>
<meta itemprop="property" content="begin"/>
<meta itemprop="property" content="end"/>
</div>

# tf.data.experimental.CheckpointInputPipelineHook

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/iterator_ops.py#L102-L290">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Checkpoints input pipeline state every N steps or seconds.

Inherits From: [`SessionRunHook`](../../../tf/estimator/SessionRunHook.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.CheckpointInputPipelineHook`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.CheckpointInputPipelineHook(
    estimator, external_state_policy='fail'
)
</code></pre>



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
<a href="../../../tf/data/experimental/make_saveable_from_iterator.md"><code>tf.data.experimental.make_saveable_from_iterator</code></a> directly to create a
`SaveableObject` and add to the `SAVEABLE_OBJECTS` collection. Note, however,
that you will need to be careful not to restore the training iterator during
eval. You can do that by not adding the iterator to the SAVEABLE_OBJECTS
collector when building the eval graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`estimator`
</td>
<td>
Estimator.
</td>
</tr><tr>
<td>
`external_state_policy`
</td>
<td>
A string that identifies how to handle input
pipelines that depend on external state. Possible values are
'ignore': The external state is silently ignored.
'warn': The external state is ignored, logging a warning.
'fail': The operation fails upon encountering external state.
By default we set it to 'fail'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
One of `save_steps` or `save_secs` should be set.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
At most one of saver or scaffold should be set.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `external_state_policy` is not one of 'warn', 'ignore' or
'fail'.
</td>
</tr>
</table>



## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/iterator_ops.py#L240-L243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>after_create_session(
    session, coord
)
</code></pre>

Called when new TensorFlow session is created.

This is called to signal the hooks that a new session has been created. This
has two essential differences with the situation in which `begin` is called:

* When this is called, the graph is finalized and ops can no longer be added
    to the graph.
* This method will also be called as a result of recovering a wrapped
    session, not only at the beginning of the overall session.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`session`
</td>
<td>
A TensorFlow Session that has been created.
</td>
</tr><tr>
<td>
`coord`
</td>
<td>
A Coordinator object which keeps track of all threads.
</td>
</tr>
</table>



<h3 id="after_run"><code>after_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/iterator_ops.py#L286-L287">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>after_run(
    run_context, run_values
)
</code></pre>

Called after each call to run().

The `run_values` argument contains results of requested ops/tensors by
`before_run()`.

The `run_context` argument is the same one send to `before_run` call.
`run_context.request_stop()` can be called to stop the iteration.

If `session.run()` raises any exceptions then `after_run()` is not called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`run_context`
</td>
<td>
A `SessionRunContext` object.
</td>
</tr><tr>
<td>
`run_values`
</td>
<td>
A SessionRunValues object.
</td>
</tr>
</table>



<h3 id="before_run"><code>before_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/iterator_ops.py#L280-L284">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>before_run(
    run_context
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`run_context`
</td>
<td>
A `SessionRunContext` object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
None or a `SessionRunArgs` object.
</td>
</tr>

</table>



<h3 id="begin"><code>begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/iterator_ops.py#L223-L238">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin()
</code></pre>

Called once before using the session.

When called, the default graph is the one that will be launched in the
session.  The hook can modify the graph by adding new operations to it.
After the `begin()` call the graph will be finalized and the other callbacks
can not modify the graph anymore. Second call of `begin()` on the same
graph, should not change the graph.

<h3 id="end"><code>end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/iterator_ops.py#L289-L290">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end(
    session
)
</code></pre>

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

If `session.run()` raises exception other than OutOfRangeError or
StopIteration then `end()` is not called.
Note the difference between `end()` and `after_run()` behavior when
`session.run()` raises OutOfRangeError or StopIteration. In that case
`end()` is called but `after_run()` is not called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`session`
</td>
<td>
A TensorFlow Session that will be soon closed.
</td>
</tr>
</table>





