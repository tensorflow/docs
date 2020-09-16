description: Saves summaries every N steps.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.SummarySaverHook" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="after_create_session"/>
<meta itemprop="property" content="after_run"/>
<meta itemprop="property" content="before_run"/>
<meta itemprop="property" content="begin"/>
<meta itemprop="property" content="end"/>
</div>

# tf.estimator.SummarySaverHook

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/basic_session_run_hooks.py#L779-L884">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Saves summaries every N steps.

Inherits From: [`SessionRunHook`](../../tf/estimator/SessionRunHook.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.SummarySaverHook`, `tf.compat.v1.train.SummarySaverHook`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.SummarySaverHook(
    save_steps=None, save_secs=None, output_dir=None, summary_writer=None,
    scaffold=None, summary_op=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`save_steps`
</td>
<td>
`int`, save summaries every N steps. Exactly one of
`save_secs` and `save_steps` should be set.
</td>
</tr><tr>
<td>
`save_secs`
</td>
<td>
`int`, save summaries every N seconds.
</td>
</tr><tr>
<td>
`output_dir`
</td>
<td>
`string`, the directory to save the summaries to. Only used if
no `summary_writer` is supplied.
</td>
</tr><tr>
<td>
`summary_writer`
</td>
<td>
`SummaryWriter`. If `None` and an `output_dir` was passed,
one will be created accordingly.
</td>
</tr><tr>
<td>
`scaffold`
</td>
<td>
`Scaffold` to get summary_op if it's not provided.
</td>
</tr><tr>
<td>
`summary_op`
</td>
<td>
`Tensor` of type `string` containing the serialized `Summary`
protocol buffer or a list of `Tensor`. They are most likely an output by
TF summary methods like <a href="../../tf/compat/v1/summary/scalar.md"><code>tf.compat.v1.summary.scalar</code></a> or
<a href="../../tf/compat/v1/summary/merge_all.md"><code>tf.compat.v1.summary.merge_all</code></a>. It can be passed in as one tensor; if
more than one, they must be passed in as a list.
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
Exactly one of scaffold or summary_op should be set.
</td>
</tr>
</table>



## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/session_run_hook.py#L112-L127">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/basic_session_run_hooks.py#L841-L861">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/basic_session_run_hooks.py#L830-L839">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/basic_session_run_hooks.py#L821-L828">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/basic_session_run_hooks.py#L863-L865">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end(
    session=None
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





