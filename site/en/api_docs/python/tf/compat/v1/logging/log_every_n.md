description: Log 'msg % args' at level 'level' once per 'n' times.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.logging.log_every_n" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.logging.log_every_n

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/platform/tf_logging.py#L230-L244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Log 'msg % args' at level 'level' once per 'n' times.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.logging.log_every_n(
    level, msg, n, *args
)
</code></pre>



<!-- Placeholder for "Used in" -->

Logs the 1st call, (N+1)st call, (2N+1)st call,  etc.
Not threadsafe.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`level`
</td>
<td>
The level at which to log.
</td>
</tr><tr>
<td>
`msg`
</td>
<td>
The message to be logged.
</td>
</tr><tr>
<td>
`n`
</td>
<td>
The number of times this should be called before it is logged.
</td>
</tr><tr>
<td>
`*args`
</td>
<td>
The args to be substituted into the msg.
</td>
</tr>
</table>

