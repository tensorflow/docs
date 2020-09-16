description: Starts a trace to record computation graphs and profiling information.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.trace_on" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.trace_on

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L1163-L1205">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Starts a trace to record computation graphs and profiling information.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.trace_on(
    graph=(True), profiler=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Must be invoked in eager mode.

When enabled, TensorFlow runtime will collection information that can later be
exported and consumed by TensorBoard. The trace is activated across the entire
TensorFlow runtime and affects all threads of execution.

To stop the trace and export the collected information, use
<a href="../../tf/summary/trace_export.md"><code>tf.summary.trace_export</code></a>. To stop the trace without exporting, use
<a href="../../tf/summary/trace_off.md"><code>tf.summary.trace_off</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
If True, enables collection of executed graphs. It includes ones from
tf.function invocation and ones from the legacy graph mode. The default
is True.
</td>
</tr><tr>
<td>
`profiler`
</td>
<td>
If True, enables the advanced profiler. Enabling profiler
implicitly enables the graph collection. The profiler may incur a high
memory overhead. The default is False.
</td>
</tr>
</table>

