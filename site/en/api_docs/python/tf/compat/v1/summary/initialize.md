description: Initializes summary writing for graph execution mode.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.initialize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.summary.initialize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/summary_ops_v2.py#L315-L354">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Initializes summary writing for graph execution mode.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.initialize(
    graph=None, session=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation is a no-op when executing eagerly.

This helper method provides a higher-level alternative to using
`tf.contrib.summary.summary_writer_initializer_op` and
`tf.contrib.summary.graph`.

Most users will also want to call <a href="../../../../tf/compat/v1/train/create_global_step.md"><code>tf.compat.v1.train.create_global_step</code></a>
which can happen before or after this function is called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
A <a href="../../../../tf/Graph.md"><code>tf.Graph</code></a> or <a href="../../../../tf/compat/v1/GraphDef.md"><code>tf.compat.v1.GraphDef</code></a> to output to the writer.
This function will not write the default graph by default. When
writing to an event log file, the associated step will be zero.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
So this method can call `tf.Session.run`. This defaults
to <a href="../../../../tf/compat/v1/get_default_session.md"><code>tf.compat.v1.get_default_session</code></a>.
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
If  the current thread has no default
`tf.contrib.summary.SummaryWriter`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If session wasn't passed and no default session.
</td>
</tr>
</table>

