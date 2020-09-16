description: Holds a list of enqueue operations for a queue, each to be run in a thread.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.QueueRunner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_threads"/>
<meta itemprop="property" content="from_proto"/>
<meta itemprop="property" content="to_proto"/>
</div>

# tf.compat.v1.train.QueueRunner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/queue_runner_impl.py#L38-L391">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Holds a list of enqueue operations for a queue, each to be run in a thread.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.queue_runner.QueueRunner`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.QueueRunner(
    queue=None, enqueue_ops=None, close_op=None, cancel_op=None,
    queue_closed_exception_types=None, queue_runner_def=None, import_scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Queues are a convenient TensorFlow mechanism to compute tensors
asynchronously using multiple threads. For example in the canonical 'Input
Reader' setup one set of threads generates filenames in a queue; a second set
of threads read records from the files, processes them, and enqueues tensors
on a second queue; a third set of threads dequeues these input records to
construct batches and runs them through training operations.

There are several delicate issues when running multiple threads that way:
closing the queues in sequence as the input is exhausted, correctly catching
and reporting exceptions, etc.

The `QueueRunner`, combined with the `Coordinator`, helps handle these issues.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`queue`
</td>
<td>
A `Queue`.
</td>
</tr><tr>
<td>
`enqueue_ops`
</td>
<td>
List of enqueue ops to run in threads later.
</td>
</tr><tr>
<td>
`close_op`
</td>
<td>
Op to close the queue. Pending enqueue ops are preserved.
</td>
</tr><tr>
<td>
`cancel_op`
</td>
<td>
Op to close the queue and cancel pending enqueue ops.
</td>
</tr><tr>
<td>
`queue_closed_exception_types`
</td>
<td>
Optional tuple of Exception types that
indicate that the queue has been closed when raised during an enqueue
operation.  Defaults to `(tf.errors.OutOfRangeError,)`.  Another common
case includes `(tf.errors.OutOfRangeError, tf.errors.CancelledError)`,
when some of the enqueue ops may dequeue from other Queues.
</td>
</tr><tr>
<td>
`queue_runner_def`
</td>
<td>
Optional `QueueRunnerDef` protocol buffer. If specified,
recreates the QueueRunner from its contents. `queue_runner_def` and the
other arguments are mutually exclusive.
</td>
</tr><tr>
<td>
`import_scope`
</td>
<td>
Optional `string`. Name scope to add. Only used when
initializing from protocol buffer.
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
If both `queue_runner_def` and `queue` are both specified.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `queue` or `enqueue_ops` are not provided when not
restoring from `queue_runner_def`.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If eager execution is enabled.
</td>
</tr>
</table>



#### Eager Compatibility
QueueRunners are not compatible with eager execution. Instead, please
use <a href="../../../../tf/data.md"><code>tf.data</code></a> to get data into your model.





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`cancel_op`
</td>
<td>

</td>
</tr><tr>
<td>
`close_op`
</td>
<td>

</td>
</tr><tr>
<td>
`enqueue_ops`
</td>
<td>

</td>
</tr><tr>
<td>
`exceptions_raised`
</td>
<td>
Exceptions raised but not handled by the `QueueRunner` threads.

Exceptions raised in queue runner threads are handled in one of two ways
depending on whether or not a `Coordinator` was passed to
`create_threads()`:

* With a `Coordinator`, exceptions are reported to the coordinator and
forgotten by the `QueueRunner`.
* Without a `Coordinator`, exceptions are captured by the `QueueRunner` and
made available in this `exceptions_raised` property.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The string name of the underlying Queue.
</td>
</tr><tr>
<td>
`queue`
</td>
<td>

</td>
</tr><tr>
<td>
`queue_closed_exception_types`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="create_threads"><code>create_threads</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/queue_runner_impl.py#L301-L356">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_threads(
    sess, coord=None, daemon=(False), start=(False)
)
</code></pre>

Create threads to run the enqueue ops for the given session.

This method requires a session in which the graph was launched.  It creates
a list of threads, optionally starting them.  There is one thread for each
op passed in `enqueue_ops`.

The `coord` argument is an optional coordinator that the threads will use
to terminate together and report exceptions.  If a coordinator is given,
this method starts an additional thread to close the queue when the
coordinator requests a stop.

If previously created threads for the given session are still running, no
new threads will be created.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A `Session`.
</td>
</tr><tr>
<td>
`coord`
</td>
<td>
Optional `Coordinator` object for reporting errors and checking
stop conditions.
</td>
</tr><tr>
<td>
`daemon`
</td>
<td>
Boolean.  If `True` make the threads daemon threads.
</td>
</tr><tr>
<td>
`start`
</td>
<td>
Boolean.  If `True` starts the threads.  If `False` the
caller must call the `start()` method of the returned threads.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of threads.
</td>
</tr>

</table>



<h3 id="from_proto"><code>from_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/queue_runner_impl.py#L387-L391">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_proto(
    queue_runner_def, import_scope=None
)
</code></pre>

Returns a `QueueRunner` object created from `queue_runner_def`.


<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/queue_runner_impl.py#L358-L385">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto(
    export_scope=None
)
</code></pre>

Converts this `QueueRunner` to a `QueueRunnerDef` protocol buffer.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_scope`
</td>
<td>
Optional `string`. Name scope to remove.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `QueueRunnerDef` protocol buffer, or `None` if the `Variable` is not in
the specified name scope.
</td>
</tr>

</table>





