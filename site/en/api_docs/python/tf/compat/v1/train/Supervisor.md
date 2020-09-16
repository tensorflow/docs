description: A training helper that checkpoints models and computes summaries.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.Supervisor" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="Loop"/>
<meta itemprop="property" content="PrepareSession"/>
<meta itemprop="property" content="RequestStop"/>
<meta itemprop="property" content="ShouldStop"/>
<meta itemprop="property" content="StartQueueRunners"/>
<meta itemprop="property" content="StartStandardServices"/>
<meta itemprop="property" content="Stop"/>
<meta itemprop="property" content="StopOnException"/>
<meta itemprop="property" content="SummaryComputed"/>
<meta itemprop="property" content="WaitForStop"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="loop"/>
<meta itemprop="property" content="managed_session"/>
<meta itemprop="property" content="prepare_or_wait_for_session"/>
<meta itemprop="property" content="request_stop"/>
<meta itemprop="property" content="should_stop"/>
<meta itemprop="property" content="start_queue_runners"/>
<meta itemprop="property" content="start_standard_services"/>
<meta itemprop="property" content="stop"/>
<meta itemprop="property" content="stop_on_exception"/>
<meta itemprop="property" content="summary_computed"/>
<meta itemprop="property" content="wait_for_stop"/>
<meta itemprop="property" content="USE_DEFAULT"/>
</div>

# tf.compat.v1.train.Supervisor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L44-L1023">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A training helper that checkpoints models and computes summaries.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.Supervisor(
    graph=None, ready_op=USE_DEFAULT, ready_for_local_init_op=USE_DEFAULT,
    is_chief=(True), init_op=USE_DEFAULT, init_feed_dict=None,
    local_init_op=USE_DEFAULT, logdir=None, summary_op=USE_DEFAULT,
    saver=USE_DEFAULT, global_step=USE_DEFAULT, save_summaries_secs=120,
    save_model_secs=600, recovery_wait_secs=30, stop_grace_secs=120,
    checkpoint_basename='model.ckpt', session_manager=None,
    summary_writer=USE_DEFAULT, init_fn=None, local_init_run_options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class is deprecated. Please use
<a href="../../../../tf/compat/v1/train/MonitoredTrainingSession.md"><code>tf.compat.v1.train.MonitoredTrainingSession</code></a> instead.

The Supervisor is a small wrapper around a `Coordinator`, a `Saver`,
and a `SessionManager` that takes care of common needs of TensorFlow
training programs.

#### Use for a single program

```python
with tf.Graph().as_default():
  ...add operations to the graph...
  # Create a Supervisor that will checkpoint the model in '/tmp/mydir'.
  sv = Supervisor(logdir='/tmp/mydir')
  # Get a TensorFlow session managed by the supervisor.
  with sv.managed_session(FLAGS.master) as sess:
    # Use the session to train the graph.
    while not sv.should_stop():
      sess.run(<my_train_op>)
```

Within the `with sv.managed_session()` block all variables in the graph have
been initialized.  In addition, a few services have been started to
checkpoint the model and add summaries to the event log.

If the program crashes and is restarted, the managed session automatically
reinitialize variables from the most recent checkpoint.

The supervisor is notified of any exception raised by one of the services.
After an exception is raised, `should_stop()` returns `True`.  In that case
the training loop should also stop.  This is why the training loop has to
check for `sv.should_stop()`.

Exceptions that indicate that the training inputs have been exhausted,
<a href="../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>, also cause `sv.should_stop()` to return `True`
but are not re-raised from the `with` block: they indicate a normal
termination.

#### Use for multiple replicas

To train with replicas you deploy the same program in a `Cluster`.
One of the tasks must be identified as the *chief*: the task that handles
initialization, checkpoints, summaries, and recovery.  The other tasks
depend on the *chief* for these services.

The only change you have to do to the single program code is to indicate
if the program is running as the *chief*.

```python
# Choose a task as the chief. This could be based on server_def.task_index,
# or job_def.name, or job_def.tasks. It's entirely up to the end user.
# But there can be only one *chief*.
is_chief = (server_def.task_index == 0)
server = tf.distribute.Server(server_def)

with tf.Graph().as_default():
  ...add operations to the graph...
  # Create a Supervisor that uses log directory on a shared file system.
  # Indicate if you are the 'chief'
  sv = Supervisor(logdir='/shared_directory/...', is_chief=is_chief)
  # Get a Session in a TensorFlow server on the cluster.
  with sv.managed_session(server.target) as sess:
    # Use the session to train the graph.
    while not sv.should_stop():
      sess.run(<my_train_op>)
```

In the *chief* task, the `Supervisor` works exactly as in the first example
above.  In the other tasks `sv.managed_session()` waits for the Model to have
been initialized before returning a session to the training code.  The
non-chief tasks depend on the chief task for initializing the model.

If one of the tasks crashes and restarts, `managed_session()`
checks if the Model is initialized.  If yes, it just creates a session and
returns it to the training code that proceeds normally.  If the model needs
to be initialized, the chief task takes care of reinitializing it; the other
tasks just wait for the model to have been initialized.

NOTE: This modified program still works fine as a single program.
The single program marks itself as the chief.

#### What `master` string to use

Whether you are running on your machine or in the cluster you can use the
following values for the --master flag:

* Specifying `''` requests an in-process session that does not use RPC.

* Specifying `'local'` requests a session that uses the RPC-based
  "Master interface" to run TensorFlow programs. See
  `tf.train.Server.create_local_server` for
  details.

* Specifying `'grpc://hostname:port'` requests a session that uses
  the RPC interface to a specific host, and also allows the in-process
  master to access remote tensorflow workers. Often, it is
  appropriate to pass `server.target` (for some <a href="../../../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a>
  named `server).

#### Advanced use

##### Launching additional services

`managed_session()` launches the Checkpoint and Summary services (threads).
If you need more services to run you can simply launch them in the block
controlled by `managed_session()`.

Example: Start a thread to print losses.  We want this thread to run
every 60 seconds, so we launch it with `sv.loop()`.

```python
...
sv = Supervisor(logdir='/tmp/mydir')
with sv.managed_session(FLAGS.master) as sess:
  sv.loop(60, print_loss, (sess, ))
  while not sv.should_stop():
    sess.run(my_train_op)
```

##### Launching fewer services

`managed_session()` launches the "summary" and "checkpoint" threads which use
either the optionally `summary_op` and `saver` passed to the constructor, or
default ones created automatically by the supervisor.  If you want to run
your own summary and checkpointing logic, disable these services by passing
`None` to the `summary_op` and `saver` parameters.

Example: Create summaries manually every 100 steps in the chief.

```python
# Create a Supervisor with no automatic summaries.
sv = Supervisor(logdir='/tmp/mydir', is_chief=is_chief, summary_op=None)
# As summary_op was None, managed_session() does not start the
# summary thread.
with sv.managed_session(FLAGS.master) as sess:
  for step in xrange(1000000):
    if sv.should_stop():
      break
    if is_chief and step % 100 == 0:
      # Create the summary every 100 chief steps.
      sv.summary_computed(sess, sess.run(my_summary_op))
    else:
      # Train normally
      sess.run(my_train_op)
```

##### Custom model initialization

`managed_session()` only supports initializing the model by running an
`init_op` or restoring from the latest checkpoint.  If you have special
initialization needs, see how to specify a `local_init_op` when creating the
supervisor.  You can also use the `SessionManager` directly to create a
session and check if it could be initialized automatically.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
A `Graph`.  The graph that the model will use.  Defaults to the
default `Graph`.  The supervisor may add operations to the graph before
creating a session, but the graph should not be modified by the caller
after passing it to the supervisor.
</td>
</tr><tr>
<td>
`ready_op`
</td>
<td>
1-D string `Tensor`.  This tensor is evaluated by supervisors in
`prepare_or_wait_for_session()` to check if the model is ready to use.
The model is considered ready if it returns an empty array.  Defaults to
the tensor returned from <a href="../../../../tf/compat/v1/report_uninitialized_variables.md"><code>tf.compat.v1.report_uninitialized_variables()</code></a>
If `None`, the model is not checked for readiness.
</td>
</tr><tr>
<td>
`ready_for_local_init_op`
</td>
<td>
1-D string `Tensor`.  This tensor is evaluated by
supervisors in `prepare_or_wait_for_session()` to check if the model is
ready to run the local_init_op. The model is considered ready if it
returns an empty array. Defaults to `None`. If `None`, the model is not
checked for readiness before running local_init_op.
</td>
</tr><tr>
<td>
`is_chief`
</td>
<td>
If True, create a chief supervisor in charge of initializing and
restoring the model.  If False, create a supervisor that relies on a
chief supervisor for inits and restore.
</td>
</tr><tr>
<td>
`init_op`
</td>
<td>
`Operation`.  Used by chief supervisors to initialize the model
when it can not be recovered.  Defaults to an `Operation` that
initializes all global variables.  If `None`, no initialization is done
automatically unless you pass a value for `init_fn`, see below.
</td>
</tr><tr>
<td>
`init_feed_dict`
</td>
<td>
A dictionary that maps `Tensor` objects to feed values.
This feed dictionary will be used when `init_op` is evaluated.
</td>
</tr><tr>
<td>
`local_init_op`
</td>
<td>
`Operation`. Used by all supervisors to run initializations
that should run for every new supervisor instance. By default these are
table initializers and initializers for local variables. If `None`, no
further per supervisor-instance initialization is done automatically.
</td>
</tr><tr>
<td>
`logdir`
</td>
<td>
A string.  Optional path to a directory where to checkpoint the
model and log events for the visualizer.  Used by chief supervisors. The
directory will be created if it does not exist.
</td>
</tr><tr>
<td>
`summary_op`
</td>
<td>
An `Operation` that returns a Summary for the event logs. Used
by chief supervisors if a `logdir` was specified.  Defaults to the
operation returned from summary.merge_all().  If `None`, summaries are
not computed automatically.
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
A Saver object.  Used by chief supervisors if a `logdir` was
specified.  Defaults to the saved returned by Saver(). If `None`, the
model is not saved automatically.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
An integer Tensor of size 1 that counts steps.  The value
from 'global_step' is used in summaries and checkpoint filenames.
Default to the op named 'global_step' in the graph if it exists, is of
rank 1, size 1, and of type tf.int32 or tf.int64.  If `None` the global
step is not recorded in summaries and checkpoint files.  Used by chief
supervisors if a `logdir` was specified.
</td>
</tr><tr>
<td>
`save_summaries_secs`
</td>
<td>
Number of seconds between the computation of
summaries for the event log.  Defaults to 120 seconds.  Pass 0 to
disable summaries.
</td>
</tr><tr>
<td>
`save_model_secs`
</td>
<td>
Number of seconds between the creation of model
checkpoints.  Defaults to 600 seconds.  Pass 0 to disable checkpoints.
</td>
</tr><tr>
<td>
`recovery_wait_secs`
</td>
<td>
Number of seconds between checks that the model is
ready.  Used by supervisors when waiting for a chief supervisor to
initialize or restore the model.  Defaults to 30 seconds.
</td>
</tr><tr>
<td>
`stop_grace_secs`
</td>
<td>
Grace period, in seconds, given to running threads to
stop when `stop()` is called.  Defaults to 120 seconds.
</td>
</tr><tr>
<td>
`checkpoint_basename`
</td>
<td>
The basename for checkpoint saving.
</td>
</tr><tr>
<td>
`session_manager`
</td>
<td>
`SessionManager`, which manages Session creation and
recovery. If it is `None`, a default `SessionManager` will be created
with the set of arguments passed in for backwards compatibility.
</td>
</tr><tr>
<td>
`summary_writer`
</td>
<td>
`SummaryWriter` to use or `USE_DEFAULT`.  Can be `None` to
indicate that no summaries should be written.
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
</tr><tr>
<td>
`local_init_run_options`
</td>
<td>
RunOptions to be passed as the SessionManager
local_init_run_options parameter.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If called with eager execution enabled.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`coord`
</td>
<td>
Return the Coordinator used by the Supervisor.

The Coordinator can be useful if you want to run multiple threads
during your training.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Return the global_step Tensor used by the supervisor.
</td>
</tr><tr>
<td>
`init_feed_dict`
</td>
<td>
Return the feed dictionary used when evaluating the `init_op`.
</td>
</tr><tr>
<td>
`init_op`
</td>
<td>
Return the Init Op used by the supervisor.
</td>
</tr><tr>
<td>
`is_chief`
</td>
<td>
Return True if this is a chief supervisor.
</td>
</tr><tr>
<td>
`ready_for_local_init_op`
</td>
<td>

</td>
</tr><tr>
<td>
`ready_op`
</td>
<td>
Return the Ready Op used by the supervisor.
</td>
</tr><tr>
<td>
`save_model_secs`
</td>
<td>
Return the delay between checkpoints.
</td>
</tr><tr>
<td>
`save_path`
</td>
<td>
Return the save path used by the supervisor.
</td>
</tr><tr>
<td>
`save_summaries_secs`
</td>
<td>
Return the delay between summary computations.
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
Return the Saver used by the supervisor.
</td>
</tr><tr>
<td>
`session_manager`
</td>
<td>
Return the SessionManager used by the Supervisor.
</td>
</tr><tr>
<td>
`summary_op`
</td>
<td>
Return the Summary Tensor used by the chief supervisor.
</td>
</tr><tr>
<td>
`summary_writer`
</td>
<td>
Return the SummaryWriter used by the chief supervisor.
</td>
</tr>
</table>



## Methods

<h3 id="Loop"><code>Loop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L782-L808">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>Loop(
    timer_interval_secs, target, args=None, kwargs=None
)
</code></pre>

Start a LooperThread that calls a function periodically.

If `timer_interval_secs` is None the thread calls `target(*args, **kwargs)`
repeatedly.  Otherwise it calls it every `timer_interval_secs`
seconds.  The thread terminates when a stop is requested.

The started thread is added to the list of threads managed by the supervisor
so it does not need to be passed to the `stop()` method.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`timer_interval_secs`
</td>
<td>
Number. Time boundaries at which to call `target`.
</td>
</tr><tr>
<td>
`target`
</td>
<td>
A callable object.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional arguments to pass to `target` when calling it.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments to pass to `target` when calling it.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The started thread.
</td>
</tr>

</table>



<h3 id="PrepareSession"><code>PrepareSession</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L690-L745">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>PrepareSession(
    master='', config=None, wait_for_checkpoint=(False), max_wait_secs=7200,
    start_standard_services=(True)
)
</code></pre>

Make sure the model is ready to be used.

Create a session on 'master', recovering or initializing the model as
needed, or wait for a session to be ready.  If running as the chief
and `start_standard_service` is set to True, also call the session
manager to start the standard services.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`master`
</td>
<td>
name of the TensorFlow master to use.  See the
<a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> constructor for how this is interpreted.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
Optional ConfigProto proto used to configure the session, which is
passed as-is to create the session.
</td>
</tr><tr>
<td>
`wait_for_checkpoint`
</td>
<td>
Whether we should wait for the availability of a
checkpoint before creating Session. Defaults to False.
</td>
</tr><tr>
<td>
`max_wait_secs`
</td>
<td>
Maximum time to wait for the session to become available.
</td>
</tr><tr>
<td>
`start_standard_services`
</td>
<td>
Whether to start the standard services and the
queue runners.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A Session object that can be used to drive the model.
</td>
</tr>

</table>



<h3 id="RequestStop"><code>RequestStop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L849-L859">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>RequestStop(
    ex=None
)
</code></pre>

Request that the coordinator stop the threads.

See `Coordinator.request_stop()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`ex`
</td>
<td>
Optional `Exception`, or Python `exc_info` tuple as returned by
`sys.exc_info()`.  If this is the first call to `request_stop()` the
corresponding exception is recorded and re-raised from `join()`.
</td>
</tr>
</table>



<h3 id="ShouldStop"><code>ShouldStop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L861-L869">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>ShouldStop()
</code></pre>

Check if the coordinator was told to stop.

See `Coordinator.should_stop()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
True if the coordinator was told to stop, False otherwise.
</td>
</tr>

</table>



<h3 id="StartQueueRunners"><code>StartQueueRunners</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L747-L780">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>StartQueueRunners(
    sess, queue_runners=None
)
</code></pre>

Start threads for `QueueRunners`.

Note that the queue runners collected in the graph key `QUEUE_RUNNERS`
are already started automatically when you create a session with the
supervisor, so unless you have non-collected queue runners to start
you do not need to call this explicitly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A `Session`.
</td>
</tr><tr>
<td>
`queue_runners`
</td>
<td>
A list of `QueueRunners`. If not specified, we'll use the
list of queue runners gathered in the graph under the key
`GraphKeys.QUEUE_RUNNERS`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The list of threads started for the `QueueRunners`.
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
If called with eager execution enabled.
</td>
</tr>
</table>




#### Eager Compatibility
Queues are not compatible with eager execution. To ingest data when eager
execution is enabled, use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API.



<h3 id="StartStandardServices"><code>StartStandardServices</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L638-L688">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>StartStandardServices(
    sess
)
</code></pre>

Start the standard services for 'sess'.

This starts services in the background.  The services started depend
on the parameters to the constructor and may include:

  - A Summary thread computing summaries every save_summaries_secs.
  - A Checkpoint thread saving the model every save_model_secs.
  - A StepCounter thread measure step time.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A Session.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of threads that are running the standard services.  You can use
the Supervisor's Coordinator to join these threads with:
sv.coord.Join(<list of threads>)
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
If called with a non-chief Supervisor.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If not `logdir` was passed to the constructor as the
services need a log directory.
</td>
</tr>
</table>



<h3 id="Stop"><code>Stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L810-L847">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>Stop(
    threads=None, close_summary_writer=(True), ignore_live_threads=(False)
)
</code></pre>

Stop the services and the coordinator.

This does not close the session.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`threads`
</td>
<td>
Optional list of threads to join with the coordinator.  If
`None`, defaults to the threads running the standard services, the
threads started for `QueueRunners`, and the threads started by the
`loop()` method.  To wait on additional threads, pass the list in this
parameter.
</td>
</tr><tr>
<td>
`close_summary_writer`
</td>
<td>
Whether to close the `summary_writer`.  Defaults to
`True` if the summary writer was created by the supervisor, `False`
otherwise.
</td>
</tr><tr>
<td>
`ignore_live_threads`
</td>
<td>
If `True` ignores threads that remain running after a
grace period when joining threads via the coordinator, instead of
raising a RuntimeError.
</td>
</tr>
</table>



<h3 id="StopOnException"><code>StopOnException</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L871-L879">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>StopOnException()
</code></pre>

Context handler to stop the supervisor when an exception is raised.

See `Coordinator.stop_on_exception()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context handler.
</td>
</tr>

</table>



<h3 id="SummaryComputed"><code>SummaryComputed</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L885-L902">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>SummaryComputed(
    sess, summary, global_step=None
)
</code></pre>

Indicate that a summary was computed.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A `Session` object.
</td>
</tr><tr>
<td>
`summary`
</td>
<td>
A Summary proto, or a string holding a serialized summary proto.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Int. global step this summary is associated with. If `None`,
it will try to fetch the current step.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if 'summary' is not a Summary proto or a string.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
if the Supervisor was created without a `logdir`.
</td>
</tr>
</table>



<h3 id="WaitForStop"><code>WaitForStop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L881-L883">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>WaitForStop()
</code></pre>

Block waiting for the coordinator to stop.


<h3 id="loop"><code>loop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L782-L808">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>loop(
    timer_interval_secs, target, args=None, kwargs=None
)
</code></pre>

Start a LooperThread that calls a function periodically.

If `timer_interval_secs` is None the thread calls `target(*args, **kwargs)`
repeatedly.  Otherwise it calls it every `timer_interval_secs`
seconds.  The thread terminates when a stop is requested.

The started thread is added to the list of threads managed by the supervisor
so it does not need to be passed to the `stop()` method.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`timer_interval_secs`
</td>
<td>
Number. Time boundaries at which to call `target`.
</td>
</tr><tr>
<td>
`target`
</td>
<td>
A callable object.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional arguments to pass to `target` when calling it.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments to pass to `target` when calling it.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The started thread.
</td>
</tr>

</table>



<h3 id="managed_session"><code>managed_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L935-L1023">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@contextlib.contextmanager</code>
<code>managed_session(
    master='', config=None, start_standard_services=(True),
    close_summary_writer=(True)
)
</code></pre>

Returns a context manager for a managed session.

This context manager creates and automatically recovers a session.  It
optionally starts the standard services that handle checkpoints and
summaries.  It monitors exceptions raised from the `with` block or from the
services and stops the supervisor as needed.

The context manager is typically used as follows:

```python
def train():
  sv = tf.compat.v1.train.Supervisor(...)
  with sv.managed_session(<master>) as sess:
    for step in xrange(..):
      if sv.should_stop():
        break
      sess.run(<my training op>)
      ...do other things needed at each training step...
```

An exception raised from the `with` block or one of the service threads is
raised again when the block exits.  This is done after stopping all threads
and closing the session.  For example, an `AbortedError` exception, raised
in case of preemption of one of the workers in a distributed model, is
raised again when the block exits.

If you want to retry the training loop in case of preemption you can do it
as follows:

```python
def main(...):
  while True
    try:
      train()
    except tf.errors.Aborted:
      pass
```

As a special case, exceptions used for control flow, such as
`OutOfRangeError` which reports that input queues are exhausted, are not
raised again from the `with` block: they indicate a clean termination of
the training loop and are considered normal termination.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`master`
</td>
<td>
name of the TensorFlow master to use.  See the
<a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> constructor for how this is interpreted.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
Optional `ConfigProto` proto used to configure the session. Passed
as-is to create the session.
</td>
</tr><tr>
<td>
`start_standard_services`
</td>
<td>
Whether to start the standard services, such as
checkpoint, summary and step counter.
</td>
</tr><tr>
<td>
`close_summary_writer`
</td>
<td>
Whether to close the summary writer when closing the
session.  Defaults to True.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager that yields a `Session` restored from the latest
checkpoint or initialized from scratch if not checkpoint exists.  The
session is closed when the `with` block exits.
</td>
</tr>

</table>



<h3 id="prepare_or_wait_for_session"><code>prepare_or_wait_for_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L690-L745">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>prepare_or_wait_for_session(
    master='', config=None, wait_for_checkpoint=(False), max_wait_secs=7200,
    start_standard_services=(True)
)
</code></pre>

Make sure the model is ready to be used.

Create a session on 'master', recovering or initializing the model as
needed, or wait for a session to be ready.  If running as the chief
and `start_standard_service` is set to True, also call the session
manager to start the standard services.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`master`
</td>
<td>
name of the TensorFlow master to use.  See the
<a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> constructor for how this is interpreted.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
Optional ConfigProto proto used to configure the session, which is
passed as-is to create the session.
</td>
</tr><tr>
<td>
`wait_for_checkpoint`
</td>
<td>
Whether we should wait for the availability of a
checkpoint before creating Session. Defaults to False.
</td>
</tr><tr>
<td>
`max_wait_secs`
</td>
<td>
Maximum time to wait for the session to become available.
</td>
</tr><tr>
<td>
`start_standard_services`
</td>
<td>
Whether to start the standard services and the
queue runners.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A Session object that can be used to drive the model.
</td>
</tr>

</table>



<h3 id="request_stop"><code>request_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L849-L859">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>request_stop(
    ex=None
)
</code></pre>

Request that the coordinator stop the threads.

See `Coordinator.request_stop()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`ex`
</td>
<td>
Optional `Exception`, or Python `exc_info` tuple as returned by
`sys.exc_info()`.  If this is the first call to `request_stop()` the
corresponding exception is recorded and re-raised from `join()`.
</td>
</tr>
</table>



<h3 id="should_stop"><code>should_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L861-L869">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>should_stop()
</code></pre>

Check if the coordinator was told to stop.

See `Coordinator.should_stop()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
True if the coordinator was told to stop, False otherwise.
</td>
</tr>

</table>



<h3 id="start_queue_runners"><code>start_queue_runners</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L747-L780">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start_queue_runners(
    sess, queue_runners=None
)
</code></pre>

Start threads for `QueueRunners`.

Note that the queue runners collected in the graph key `QUEUE_RUNNERS`
are already started automatically when you create a session with the
supervisor, so unless you have non-collected queue runners to start
you do not need to call this explicitly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A `Session`.
</td>
</tr><tr>
<td>
`queue_runners`
</td>
<td>
A list of `QueueRunners`. If not specified, we'll use the
list of queue runners gathered in the graph under the key
`GraphKeys.QUEUE_RUNNERS`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The list of threads started for the `QueueRunners`.
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
If called with eager execution enabled.
</td>
</tr>
</table>




#### Eager Compatibility
Queues are not compatible with eager execution. To ingest data when eager
execution is enabled, use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API.



<h3 id="start_standard_services"><code>start_standard_services</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L638-L688">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start_standard_services(
    sess
)
</code></pre>

Start the standard services for 'sess'.

This starts services in the background.  The services started depend
on the parameters to the constructor and may include:

  - A Summary thread computing summaries every save_summaries_secs.
  - A Checkpoint thread saving the model every save_model_secs.
  - A StepCounter thread measure step time.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A Session.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of threads that are running the standard services.  You can use
the Supervisor's Coordinator to join these threads with:
sv.coord.Join(<list of threads>)
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
If called with a non-chief Supervisor.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If not `logdir` was passed to the constructor as the
services need a log directory.
</td>
</tr>
</table>



<h3 id="stop"><code>stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L810-L847">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stop(
    threads=None, close_summary_writer=(True), ignore_live_threads=(False)
)
</code></pre>

Stop the services and the coordinator.

This does not close the session.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`threads`
</td>
<td>
Optional list of threads to join with the coordinator.  If
`None`, defaults to the threads running the standard services, the
threads started for `QueueRunners`, and the threads started by the
`loop()` method.  To wait on additional threads, pass the list in this
parameter.
</td>
</tr><tr>
<td>
`close_summary_writer`
</td>
<td>
Whether to close the `summary_writer`.  Defaults to
`True` if the summary writer was created by the supervisor, `False`
otherwise.
</td>
</tr><tr>
<td>
`ignore_live_threads`
</td>
<td>
If `True` ignores threads that remain running after a
grace period when joining threads via the coordinator, instead of
raising a RuntimeError.
</td>
</tr>
</table>



<h3 id="stop_on_exception"><code>stop_on_exception</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L871-L879">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stop_on_exception()
</code></pre>

Context handler to stop the supervisor when an exception is raised.

See `Coordinator.stop_on_exception()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context handler.
</td>
</tr>

</table>



<h3 id="summary_computed"><code>summary_computed</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L885-L902">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>summary_computed(
    sess, summary, global_step=None
)
</code></pre>

Indicate that a summary was computed.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A `Session` object.
</td>
</tr><tr>
<td>
`summary`
</td>
<td>
A Summary proto, or a string holding a serialized summary proto.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Int. global step this summary is associated with. If `None`,
it will try to fetch the current step.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if 'summary' is not a Summary proto or a string.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
if the Supervisor was created without a `logdir`.
</td>
</tr>
</table>



<h3 id="wait_for_stop"><code>wait_for_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/supervisor.py#L881-L883">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wait_for_stop()
</code></pre>

Block waiting for the coordinator to stop.




## Class Variables

* `USE_DEFAULT = 0` <a id="USE_DEFAULT"></a>
