description: Training helper that restores from checkpoint and creates session.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.SessionManager" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="prepare_session"/>
<meta itemprop="property" content="recover_session"/>
<meta itemprop="property" content="wait_for_session"/>
</div>

# tf.compat.v1.train.SessionManager

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/session_manager.py#L51-L512">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Training helper that restores from checkpoint and creates session.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.SessionManager(
    local_init_op=None, ready_op=None, ready_for_local_init_op=None, graph=None,
    recovery_wait_secs=30, local_init_run_options=None, local_init_feed_dict=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class is a small wrapper that takes care of session creation and
checkpoint recovery. It also provides functions that to facilitate
coordination among multiple training threads or processes.

* Checkpointing trained variables as the training progresses.
* Initializing variables on startup, restoring them from the most recent
  checkpoint after a crash, or wait for checkpoints to become available.

### Usage:

```python
with tf.Graph().as_default():
   ...add operations to the graph...
  # Create a SessionManager that will checkpoint the model in '/tmp/mydir'.
  sm = SessionManager()
  sess = sm.prepare_session(master, init_op, saver, checkpoint_dir)
  # Use the session to train the graph.
  while True:
    sess.run(<my_train_op>)
```

`prepare_session()` initializes or restores a model. It requires `init_op`
and `saver` as an argument.

A second process could wait for the model to be ready by doing the following:

```python
with tf.Graph().as_default():
   ...add operations to the graph...
  # Create a SessionManager that will wait for the model to become ready.
  sm = SessionManager()
  sess = sm.wait_for_session(master)
  # Use the session to train the graph.
  while True:
    sess.run(<my_train_op>)
```

`wait_for_session()` waits for a model to be initialized by other processes.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`local_init_op`
</td>
<td>
An `Operation` run immediately after session creation.
Usually used to initialize tables and local variables.
</td>
</tr><tr>
<td>
`ready_op`
</td>
<td>
An `Operation` to check if the model is initialized.
</td>
</tr><tr>
<td>
`ready_for_local_init_op`
</td>
<td>
An `Operation` to check if the model is ready
to run local_init_op.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
The `Graph` that the model will use.
</td>
</tr><tr>
<td>
`recovery_wait_secs`
</td>
<td>
Seconds between checks for the model to be ready.
</td>
</tr><tr>
<td>
`local_init_run_options`
</td>
<td>
RunOptions to be passed to session.run when
executing the local_init_op.
</td>
</tr><tr>
<td>
`local_init_feed_dict`
</td>
<td>
Optional session feed dictionary to use when running
the local_init_op.
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
If ready_for_local_init_op is not None but local_init_op is
None
</td>
</tr>
</table>



## Methods

<h3 id="prepare_session"><code>prepare_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/session_manager.py#L229-L319">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>prepare_session(
    master, init_op=None, saver=None, checkpoint_dir=None,
    checkpoint_filename_with_path=None, wait_for_checkpoint=(False),
    max_wait_secs=7200, config=None, init_feed_dict=None, init_fn=None
)
</code></pre>

Creates a `Session`. Makes sure the model is ready to be used.

Creates a `Session` on 'master'. If a `saver` object is passed in, and
`checkpoint_dir` points to a directory containing valid checkpoint
files, then it will try to recover the model from checkpoint. If
no checkpoint files are available, and `wait_for_checkpoint` is
`True`, then the process would check every `recovery_wait_secs`,
up to `max_wait_secs`, for recovery to succeed.

If the model cannot be recovered successfully then it is initialized by
running the `init_op` and calling `init_fn` if they are provided.
The `local_init_op` is also run after init_op and init_fn, regardless of
whether the model was recovered successfully, but only if
`ready_for_local_init_op` passes.

If the model is recovered from a checkpoint it is assumed that all
global variables have been initialized, in particular neither `init_op`
nor `init_fn` will be executed.

It is an error if the model cannot be recovered and no `init_op`
or `init_fn` or `local_init_op` are passed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`master`
</td>
<td>
`String` representation of the TensorFlow master to use.
</td>
</tr><tr>
<td>
`init_op`
</td>
<td>
Optional `Operation` used to initialize the model.
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
A `Saver` object used to restore a model.
</td>
</tr><tr>
<td>
`checkpoint_dir`
</td>
<td>
Path to the checkpoint files. The latest checkpoint in the
dir will be used to restore.
</td>
</tr><tr>
<td>
`checkpoint_filename_with_path`
</td>
<td>
Full file name path to the checkpoint file.
</td>
</tr><tr>
<td>
`wait_for_checkpoint`
</td>
<td>
Whether to wait for checkpoint to become available.
</td>
</tr><tr>
<td>
`max_wait_secs`
</td>
<td>
Maximum time to wait for checkpoints to become available.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
Optional `ConfigProto` proto used to configure the session.
</td>
</tr><tr>
<td>
`init_feed_dict`
</td>
<td>
Optional dictionary that maps `Tensor` objects to feed
values.  This feed dictionary is passed to the session `run()` call when
running the init op.
</td>
</tr><tr>
<td>
`init_fn`
</td>
<td>
Optional callable used to initialize the model. Called after the
optional `init_op` is called.  The callable must accept one argument,
the session being initialized.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Session` object that can be used to drive the model.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If the model cannot be initialized or recovered.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If both checkpoint_dir and checkpoint_filename_with_path are
set.
</td>
</tr>
</table>



<h3 id="recover_session"><code>recover_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/session_manager.py#L321-L383">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recover_session(
    master, saver=None, checkpoint_dir=None, checkpoint_filename_with_path=None,
    wait_for_checkpoint=(False), max_wait_secs=7200, config=None
)
</code></pre>

Creates a `Session`, recovering if possible.

Creates a new session on 'master'.  If the session is not initialized
and can be recovered from a checkpoint, recover it.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`master`
</td>
<td>
`String` representation of the TensorFlow master to use.
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
A `Saver` object used to restore a model.
</td>
</tr><tr>
<td>
`checkpoint_dir`
</td>
<td>
Path to the checkpoint files. The latest checkpoint in the
dir will be used to restore.
</td>
</tr><tr>
<td>
`checkpoint_filename_with_path`
</td>
<td>
Full file name path to the checkpoint file.
</td>
</tr><tr>
<td>
`wait_for_checkpoint`
</td>
<td>
Whether to wait for checkpoint to become available.
</td>
</tr><tr>
<td>
`max_wait_secs`
</td>
<td>
Maximum time to wait for checkpoints to become available.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
Optional `ConfigProto` proto used to configure the session.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A pair (sess, initialized) where 'initialized' is `True` if
the session could be recovered and initialized, `False` otherwise.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both checkpoint_dir and checkpoint_filename_with_path are
set.
</td>
</tr>
</table>



<h3 id="wait_for_session"><code>wait_for_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/session_manager.py#L385-L442">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wait_for_session(
    master, config=None, max_wait_secs=float('Inf')
)
</code></pre>

Creates a new `Session` and waits for model to be ready.

Creates a new `Session` on 'master'.  Waits for the model to be
initialized or recovered from a checkpoint.  It's expected that
another thread or process will make the model ready, and that this
is intended to be used by threads/processes that participate in a
distributed training configuration where a different thread/process
is responsible for initializing or recovering the model being trained.

NB: The amount of time this method waits for the session is bounded
by max_wait_secs. By default, this function will wait indefinitely.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`master`
</td>
<td>
`String` representation of the TensorFlow master to use.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
Optional ConfigProto proto used to configure the session.
</td>
</tr><tr>
<td>
`max_wait_secs`
</td>
<td>
Maximum time to wait for the session to become available.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Session`. May be None if the operation exceeds the timeout
specified by config.operation_timeout_in_ms.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.DeadlineExceededError`
</td>
<td>
if the session is not available after
max_wait_secs.
</td>
</tr>
</table>





