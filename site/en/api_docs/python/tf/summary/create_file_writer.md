description: Creates a summary file writer for the given log directory.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.summary.create_file_writer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.summary.create_file_writer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/summary_ops_v2.py#L363-L422">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a summary file writer for the given log directory.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.summary.create_file_writer(
    logdir, max_queue=None, flush_millis=None, filename_suffix=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logdir`
</td>
<td>
a string specifying the directory in which to write an event file.
</td>
</tr><tr>
<td>
`max_queue`
</td>
<td>
the largest number of summaries to keep in a queue; will
flush once the queue gets bigger than this. Defaults to 10.
</td>
</tr><tr>
<td>
`flush_millis`
</td>
<td>
the largest interval between flushes. Defaults to 120,000.
</td>
</tr><tr>
<td>
`filename_suffix`
</td>
<td>
optional suffix for the event file name. Defaults to `.v2`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
a name for the op that creates the writer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A SummaryWriter object.
</td>
</tr>

</table>

