description: Stops and exports the active trace as a Summary and/or profile file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.trace_export" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.trace_export

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/summary_ops_v2.py#L1302-L1355">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stops and exports the active trace as a Summary and/or profile file.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.trace_export(
    name, step=None, profiler_outdir=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Stops the trace and exports all metadata collected during the trace to the
default SummaryWriter, if one has been set.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the summary to be written.
</td>
</tr><tr>
<td>
`step`
</td>
<td>
Explicit `int64`-castable monotonic step value for this summary. If
omitted, this defaults to <a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a>, which must
not be None.
</td>
</tr><tr>
<td>
`profiler_outdir`
</td>
<td>
Output directory for profiler. This is only used when the
profiler was enabled when the trace was started. In that case, if there is
a logdir-based default SummaryWriter, this defaults to the same directory,
but otherwise the argument must be passed.
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
if a default writer exists, but no step was provided and
<a href="../../tf/summary/experimental/get_step.md"><code>tf.summary.experimental.get_step()</code></a> is None.
</td>
</tr>
</table>

