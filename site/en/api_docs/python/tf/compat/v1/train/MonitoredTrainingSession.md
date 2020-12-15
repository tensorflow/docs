description: Creates a MonitoredSession for training.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.MonitoredTrainingSession" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.MonitoredTrainingSession

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L433-L604">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a `MonitoredSession` for training.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.MonitoredTrainingSession(
    master='', is_chief=(True), checkpoint_dir=None, scaffold=None, hooks=None,
    chief_only_hooks=None, save_checkpoint_secs=USE_DEFAULT,
    save_summaries_steps=USE_DEFAULT, save_summaries_secs=USE_DEFAULT, config=None,
    stop_grace_period_secs=120, log_step_count_steps=100, max_wait_secs=7200,
    save_checkpoint_steps=USE_DEFAULT, summary_dir=None, save_graph_def=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

For a chief, this utility sets proper session initializer/restorer. It also
creates hooks related to checkpoint and summary saving. For workers, this
utility sets proper session creator which waits for the chief to
initialize/restore. Please check <a href="../../../../tf/compat/v1/train/MonitoredSession.md"><code>tf.compat.v1.train.MonitoredSession</code></a> for
more
information.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`master`
</td>
<td>
`String` the TensorFlow master to use.
</td>
</tr><tr>
<td>
`is_chief`
</td>
<td>
If `True`, it will take care of initialization and recovery the
underlying TensorFlow session. If `False`, it will wait on a chief to
initialize or recover the TensorFlow session.
</td>
</tr><tr>
<td>
`checkpoint_dir`
</td>
<td>
A string.  Optional path to a directory where to restore
variables.
</td>
</tr><tr>
<td>
`scaffold`
</td>
<td>
A `Scaffold` used for gathering or building supportive ops. If not
specified, a default one is created. It's used to finalize the graph.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
Optional list of `SessionRunHook` objects.
</td>
</tr><tr>
<td>
`chief_only_hooks`
</td>
<td>
list of `SessionRunHook` objects. Activate these hooks if
`is_chief==True`, ignore otherwise.
</td>
</tr><tr>
<td>
`save_checkpoint_secs`
</td>
<td>
The frequency, in seconds, that a checkpoint is saved
using a default checkpoint saver. If both `save_checkpoint_steps` and
`save_checkpoint_secs` are set to `None`, then the default checkpoint
saver isn't used. If both are provided, then only `save_checkpoint_secs`
is used. Default 600.
</td>
</tr><tr>
<td>
`save_summaries_steps`
</td>
<td>
The frequency, in number of global steps, that the
summaries are written to disk using a default summary saver. If both
`save_summaries_steps` and `save_summaries_secs` are set to `None`, then
the default summary saver isn't used. Default 100.
</td>
</tr><tr>
<td>
`save_summaries_secs`
</td>
<td>
The frequency, in secs, that the summaries are written
to disk using a default summary saver.  If both `save_summaries_steps` and
`save_summaries_secs` are set to `None`, then the default summary saver
isn't used. Default not enabled.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
an instance of <a href="../../../../tf/compat/v1/ConfigProto.md"><code>tf.compat.v1.ConfigProto</code></a> proto used to configure
the session. It's the `config` argument of constructor of
<a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a>.
</td>
</tr><tr>
<td>
`stop_grace_period_secs`
</td>
<td>
Number of seconds given to threads to stop after
`close()` has been called.
</td>
</tr><tr>
<td>
`log_step_count_steps`
</td>
<td>
The frequency, in number of global steps, that the
global step/sec is logged.
</td>
</tr><tr>
<td>
`max_wait_secs`
</td>
<td>
Maximum time workers should wait for the session to become
available. This should be kept relatively short to help detect incorrect
code, but sometimes may need to be increased if the chief takes a while to
start up.
</td>
</tr><tr>
<td>
`save_checkpoint_steps`
</td>
<td>
The frequency, in number of global steps, that a
checkpoint is saved using a default checkpoint saver. If both
`save_checkpoint_steps` and `save_checkpoint_secs` are set to `None`, then
the default checkpoint saver isn't used. If both are provided, then only
`save_checkpoint_secs` is used. Default not enabled.
</td>
</tr><tr>
<td>
`summary_dir`
</td>
<td>
A string.  Optional path to a directory where to save
summaries. If None, checkpoint_dir is used instead.
</td>
</tr><tr>
<td>
`save_graph_def`
</td>
<td>
Whether to save the GraphDef and MetaGraphDef to
`checkpoint_dir`. The GraphDef is saved after the session is created as
`graph.pbtxt`. MetaGraphDefs are saved out for every checkpoint as
`model.ckpt-*.meta`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `MonitoredSession` object.
</td>
</tr>

</table>

