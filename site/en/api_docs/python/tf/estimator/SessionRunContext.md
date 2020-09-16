description: Provides information about the session.run() call being made.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.SessionRunContext" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="request_stop"/>
</div>

# tf.estimator.SessionRunContext

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/session_run_hook.py#L215-L263">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Provides information about the `session.run()` call being made.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.SessionRunContext`, `tf.compat.v1.train.SessionRunContext`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.SessionRunContext(
    original_args, session
)
</code></pre>



<!-- Placeholder for "Used in" -->

Provides information about original request to `Session.Run()` function.
SessionRunHook objects can stop the loop by calling `request_stop()` of
`run_context`. In the future we may use this object to add more information
about run without changing the Hook API.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`original_args`
</td>
<td>
A `SessionRunArgs` object holding the original arguments of `run()`.

If user called `MonitoredSession.run(fetches=a, feed_dict=b)`, then this
field is equal to SessionRunArgs(a, b).
</td>
</tr><tr>
<td>
`session`
</td>
<td>
A TensorFlow session object which will execute the `run`.
</td>
</tr><tr>
<td>
`stop_requested`
</td>
<td>
Returns whether a stop is requested or not.

If true, `MonitoredSession` stops iterations.
Returns:
A `bool`
</td>
</tr>
</table>



## Methods

<h3 id="request_stop"><code>request_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/session_run_hook.py#L257-L263">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>request_stop()
</code></pre>

Sets stop requested field.

Hooks can use this function to request stop of iterations.
`MonitoredSession` checks whether this is called or not.



