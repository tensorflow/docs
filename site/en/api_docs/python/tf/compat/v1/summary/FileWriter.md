description: Writes Summary protocol buffers to event files.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.summary.FileWriter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_event"/>
<meta itemprop="property" content="add_graph"/>
<meta itemprop="property" content="add_meta_graph"/>
<meta itemprop="property" content="add_run_metadata"/>
<meta itemprop="property" content="add_session_log"/>
<meta itemprop="property" content="add_summary"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="flush"/>
<meta itemprop="property" content="get_logdir"/>
<meta itemprop="property" content="reopen"/>
</div>

# tf.compat.v1.summary.FileWriter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L283-L433">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Writes `Summary` protocol buffers to event files.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.summary.FileWriter(
    logdir, graph=None, max_queue=10, flush_secs=120, graph_def=None,
    filename_suffix=None, session=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `FileWriter` class provides a mechanism to create an event file in a
given directory and add summaries and events to it. The class updates the
file contents asynchronously. This allows a training program to call methods
to add data to the file directly from the training loop, without slowing down
training.

When constructed with a <a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> parameter, a `FileWriter`
instead forms a compatibility layer over new graph-based summaries
(`tf.contrib.summary`) to facilitate the use of new summary writing with
pre-existing code that expects a `FileWriter` instance.

This class is not thread-safe.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logdir`
</td>
<td>
A string. Directory where event file will be written.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
A `Graph` object, such as `sess.graph`.
</td>
</tr><tr>
<td>
`max_queue`
</td>
<td>
Integer. Size of the queue for pending events and summaries.
</td>
</tr><tr>
<td>
`flush_secs`
</td>
<td>
Number. How often, in seconds, to flush the
pending events and summaries to disk.
</td>
</tr><tr>
<td>
`graph_def`
</td>
<td>
DEPRECATED: Use the `graph` argument instead.
</td>
</tr><tr>
<td>
`filename_suffix`
</td>
<td>
A string. Every event file's name is suffixed with
`suffix`.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
A <a href="../../../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> object. See details above.
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



## Methods

<h3 id="add_event"><code>add_event</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L396-L403">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_event(
    event
)
</code></pre>

Adds an event to the event file.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`event`
</td>
<td>
An `Event` protocol buffer.
</td>
</tr>
</table>



<h3 id="add_graph"><code>add_graph</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L163-L214">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_graph(
    graph, global_step=None, graph_def=None
)
</code></pre>

Adds a `Graph` to the event file.

The graph described by the protocol buffer will be displayed by
TensorBoard. Most users pass a graph in the constructor instead.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`graph`
</td>
<td>
A `Graph` object, such as `sess.graph`.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Number. Optional global step counter to record with the
graph.
</td>
</tr><tr>
<td>
`graph_def`
</td>
<td>
DEPRECATED. Use the `graph` parameter instead.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both graph and graph_def are passed to the method.
</td>
</tr>
</table>



<h3 id="add_meta_graph"><code>add_meta_graph</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L229-L249">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_meta_graph(
    meta_graph_def, global_step=None
)
</code></pre>

Adds a `MetaGraphDef` to the event file.

The `MetaGraphDef` allows running the given graph via
`saver.import_meta_graph()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`meta_graph_def`
</td>
<td>
A `MetaGraphDef` object, often as returned by
`saver.export_meta_graph()`.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Number. Optional global step counter to record with the
graph.
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
If both `meta_graph_def` is not an instance of `MetaGraphDef`.
</td>
</tr>
</table>



<h3 id="add_run_metadata"><code>add_run_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L251-L273">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_run_metadata(
    run_metadata, tag, global_step=None
)
</code></pre>

Adds a metadata information for a single session.run() call.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`run_metadata`
</td>
<td>
A `RunMetadata` protobuf object.
</td>
</tr><tr>
<td>
`tag`
</td>
<td>
The tag name for this metadata.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Number. Optional global step counter to record with the
StepStats.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the provided tag was already used for this type of event.
</td>
</tr>
</table>



<h3 id="add_session_log"><code>add_session_log</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L144-L156">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_session_log(
    session_log, global_step=None
)
</code></pre>

Adds a `SessionLog` protocol buffer to the event file.

This method wraps the provided session in an `Event` protocol buffer
and adds it to the event file.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`session_log`
</td>
<td>
A `SessionLog` protocol buffer.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Number. Optional global step value to record with the
summary.
</td>
</tr>
</table>



<h3 id="add_summary"><code>add_summary</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L101-L142">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_summary(
    summary, global_step=None
)
</code></pre>

Adds a `Summary` protocol buffer to the event file.

This method wraps the provided summary in an `Event` protocol buffer
and adds it to the event file.

You can pass the result of evaluating any summary op, using
`tf.Session.run` or
<a href="../../../../tf/Tensor.md#eval"><code>tf.Tensor.eval</code></a>, to this
function. Alternatively, you can pass a <a href="../../../../tf/compat/v1/Summary.md"><code>tf.compat.v1.Summary</code></a> protocol
buffer that you populate with your own data. The latter is
commonly done to report evaluation results in event files.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`summary`
</td>
<td>
A `Summary` protocol buffer, optionally serialized as a string.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
Number. Optional global step value to record with the
summary.
</td>
</tr>
</table>



<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L416-L422">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>

Flushes the event file to disk and close the file.

Call this method when you do not need the summary writer anymore.

<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L405-L414">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flush()
</code></pre>

Flushes the event file to disk.

Call this method to make sure that all pending events have been written to
disk.

<h3 id="get_logdir"><code>get_logdir</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L382-L384">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_logdir()
</code></pre>

Returns the directory where event file will be written.


<h3 id="reopen"><code>reopen</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L424-L433">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reopen()
</code></pre>

Reopens the EventFileWriter.

Can be called after `close()` to add more events in the same directory.
The events will go into a new events file.

Does nothing if the EventFileWriter was not closed.

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L374-L376">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>

Make usable with "with" statement.


<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/summary/writer/writer.py#L378-L380">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    unused_type, unused_value, unused_traceback
)
</code></pre>

Make usable with "with" statement.




