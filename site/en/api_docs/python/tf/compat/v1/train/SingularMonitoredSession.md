description: Session-like object that handles initialization, restoring, and hooks.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.SingularMonitoredSession" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="StepContext"/>
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="raw_session"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="run_step_fn"/>
<meta itemprop="property" content="should_stop"/>
</div>

# tf.compat.v1.train.SingularMonitoredSession

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L1042-L1132">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Session-like object that handles initialization, restoring, and hooks.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.SingularMonitoredSession(
    hooks=None, scaffold=None, master='', config=None, checkpoint_dir=None,
    stop_grace_period_secs=120, checkpoint_filename_with_path=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Please note that this utility is not recommended for distributed settings.
For distributed settings, please use <a href="../../../../tf/compat/v1/train/MonitoredSession.md"><code>tf.compat.v1.train.MonitoredSession</code></a>.
The
differences between `MonitoredSession` and `SingularMonitoredSession` are:

* `MonitoredSession` handles `AbortedError` and `UnavailableError` for
  distributed settings, but `SingularMonitoredSession` does not.
* `MonitoredSession` can be created in `chief` or `worker` modes.
  `SingularMonitoredSession` is always created as `chief`.
* You can access the raw <a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> object used by
  `SingularMonitoredSession`, whereas in MonitoredSession the raw session is
  private. This can be used:
    - To `run` without hooks.
    - To save and restore.
* All other functionality is identical.

#### Example usage:


```python
saver_hook = CheckpointSaverHook(...)
summary_hook = SummarySaverHook(...)
with SingularMonitoredSession(hooks=[saver_hook, summary_hook]) as sess:
  while not sess.should_stop():
    sess.run(train_op)
```

Initialization: At creation time the hooked session does following things
in given order:

* calls `hook.begin()` for each given hook
* finalizes the graph via `scaffold.finalize()`
* create session
* initializes the model via initialization ops provided by `Scaffold`
* restores variables if a checkpoint exists
* launches queue runners

Run: When `run()` is called, the hooked session does following things:

* calls `hook.before_run()`
* calls TensorFlow `session.run()` with merged fetches and feed_dict
* calls `hook.after_run()`
* returns result of `session.run()` asked by user

Exit: At the `close()`, the hooked session does following things in order:

* calls `hook.end()`
* closes the queue runners and the session
* suppresses `OutOfRange` error which indicates that all inputs have been
  processed if the `SingularMonitoredSession` is used as a context.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`hooks`
</td>
<td>
An iterable of `SessionRunHook' objects.
</td>
</tr><tr>
<td>
`scaffold`
</td>
<td>
A `Scaffold` used for gathering or building supportive ops. If
not specified a default one is created. It's used to finalize the graph.
</td>
</tr><tr>
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
`ConfigProto` proto used to configure the session.
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
`stop_grace_period_secs`
</td>
<td>
Number of seconds given to threads to stop after
`close()` has been called.
</td>
</tr><tr>
<td>
`checkpoint_filename_with_path`
</td>
<td>
A string. Optional path to a checkpoint
file from which to restore variables.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
The graph that was launched in this session.
</td>
</tr>
</table>



## Child Classes
[`class StepContext`](../../../../tf/compat/v1/train/MonitoredSession/StepContext.md)

## Methods

<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L876-L877">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>




<h3 id="raw_session"><code>raw_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L1130-L1132">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>raw_session()
</code></pre>

Returns underlying `TensorFlow.Session` object.


<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L760-L778">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fetches, feed_dict=None, options=None, run_metadata=None
)
</code></pre>

Run ops in the monitored session.

This method is completely compatible with the `tf.Session.run()` method.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fetches`
</td>
<td>
Same as `tf.Session.run()`.
</td>
</tr><tr>
<td>
`feed_dict`
</td>
<td>
Same as `tf.Session.run()`.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Same as `tf.Session.run()`.
</td>
</tr><tr>
<td>
`run_metadata`
</td>
<td>
Same as `tf.Session.run()`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Same as `tf.Session.run()`.
</td>
</tr>

</table>



<h3 id="run_step_fn"><code>run_step_fn</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L780-L834">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run_step_fn(
    step_fn
)
</code></pre>

Run ops using a step function.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`step_fn`
</td>
<td>
A function or a method with a single argument of type
`StepContext`.  The function may use methods of the argument to perform
computations with access to a raw session.  The returned value of the
`step_fn` will be returned from `run_step_fn`, unless a stop is
requested.  In that case, the next `should_stop` call will return True.
Example usage:
```python
with tf.Graph().as_default():
c = tf.compat.v1.placeholder(dtypes.float32)
v = tf.add(c, 4.0)
w = tf.add(c, 0.5)
def step_fn(step_context):
a = step_context.session.run(fetches=v, feed_dict={c: 0.5})
if a <= 4.5:
step_context.request_stop()
return step_context.run_with_hooks(fetches=w,
feed_dict={c: 0.1})

with tf.MonitoredSession() as session:
while not session.should_stop():
a = session.run_step_fn(step_fn)
```
Hooks interact with the `run_with_hooks()` call inside the
`step_fn` as they do with a `MonitoredSession.run` call.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Returns the returned value of `step_fn`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`StopIteration`
</td>
<td>
if `step_fn` has called `request_stop()`.  It may be
caught by `with tf.MonitoredSession()` to close the session.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if `step_fn` doesn't have a single argument called
`step_context`. It may also optionally have `self` for cases when it
belongs to an object.
</td>
</tr>
</table>



<h3 id="should_stop"><code>should_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L873-L874">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>should_stop()
</code></pre>




<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L879-L880">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/monitored_session.py#L882-L887">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    exception_type, exception_value, traceback
)
</code></pre>






