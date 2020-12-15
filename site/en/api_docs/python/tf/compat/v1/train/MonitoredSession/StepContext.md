description: Control flow instrument for the step_fn from run_step_fn().

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.MonitoredSession.StepContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="request_stop"/>
<meta itemprop="property" content="run_with_hooks"/>
</div>

# tf.compat.v1.train.MonitoredSession.StepContext

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/monitored_session.py#L836-L871">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Control flow instrument for the `step_fn` from `run_step_fn()`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.SingularMonitoredSession.StepContext`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.MonitoredSession.StepContext(
    session, run_with_hooks_fn
)
</code></pre>



<!-- Placeholder for "Used in" -->

Users of `step_fn` may perform `run()` calls without running hooks
by accessing the `session`.  A `run()` call with hooks may be performed
using `run_with_hooks()`.  Computation flow can be interrupted using
`request_stop()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`session`
</td>
<td>
An instance of <a href="../../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a>.
</td>
</tr><tr>
<td>
`run_with_hooks_fn`
</td>
<td>
A function for running fetches and hooks.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`session`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="request_stop"><code>request_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/monitored_session.py#L863-L871">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>request_stop()
</code></pre>

Exit the training loop by causing `should_stop()` to return `True`.

   Causes `step_fn` to exit by raising an exception.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
StopIteration
</td>
</tr>

</table>



<h3 id="run_with_hooks"><code>run_with_hooks</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/monitored_session.py#L859-L861">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run_with_hooks(
    *args, **kwargs
)
</code></pre>

Same as `MonitoredSession.run`. Accepts the same arguments.




