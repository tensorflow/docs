description: Base class for queue implementations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.queue.QueueBase" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="dequeue"/>
<meta itemprop="property" content="dequeue_many"/>
<meta itemprop="property" content="dequeue_up_to"/>
<meta itemprop="property" content="enqueue"/>
<meta itemprop="property" content="enqueue_many"/>
<meta itemprop="property" content="from_list"/>
<meta itemprop="property" content="is_closed"/>
<meta itemprop="property" content="size"/>
</div>

# tf.queue.QueueBase

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L119-L611">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for queue implementations.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.QueueBase`, `tf.compat.v1.io.QueueBase`, `tf.compat.v1.queue.QueueBase`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.queue.QueueBase(
    dtypes, shapes, names, queue_ref
)
</code></pre>



<!-- Placeholder for "Used in" -->

A queue is a TensorFlow data structure that stores tensors across
multiple steps, and exposes operations that enqueue and dequeue
tensors.

Each queue element is a tuple of one or more tensors, where each
tuple component has a static dtype, and may have a static shape. The
queue implementations support versions of enqueue and dequeue that
handle single elements, versions that support enqueuing and
dequeuing a batch of elements at once.

See <a href="../../tf/queue/FIFOQueue.md"><code>tf.queue.FIFOQueue</code></a> and
<a href="../../tf/queue/RandomShuffleQueue.md"><code>tf.queue.RandomShuffleQueue</code></a> for concrete
implementations of this class, and instructions on how to create
them.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtypes`
</td>
<td>
A list of types.  The length of dtypes must equal the number
of tensors in each element.
</td>
</tr><tr>
<td>
`shapes`
</td>
<td>
Constraints on the shapes of tensors in an element:
A list of shape tuples or None. This list is the same length
as dtypes.  If the shape of any tensors in the element are constrained,
all must be; shapes can be None if the shapes should not be constrained.
</td>
</tr><tr>
<td>
`names`
</td>
<td>
Optional list of names.  If provided, the `enqueue()` and
`dequeue()` methods will use dictionaries with these names as keys.
Must be None or a list or tuple of the same length as `dtypes`.
</td>
</tr><tr>
<td>
`queue_ref`
</td>
<td>
The queue reference, i.e. the output of the queue op.
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
If one of the arguments is invalid.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtypes`
</td>
<td>
The list of dtypes for each component of a queue element.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the underlying queue.
</td>
</tr><tr>
<td>
`names`
</td>
<td>
The list of names for each component of a queue element.
</td>
</tr><tr>
<td>
`queue_ref`
</td>
<td>
The underlying queue reference.
</td>
</tr><tr>
<td>
`shapes`
</td>
<td>
The list of shapes for each component of a queue element.
</td>
</tr>
</table>



## Methods

<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L543-L576">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close(
    cancel_pending_enqueues=(False), name=None
)
</code></pre>

Closes this queue.

This operation signals that no more elements will be enqueued in
the given queue. Subsequent `enqueue` and `enqueue_many`
operations will fail. Subsequent `dequeue` and `dequeue_many`
operations will continue to succeed if sufficient elements remain
in the queue. Subsequently dequeue and dequeue_many operations
that would otherwise block waiting for more elements (if close
hadn't been called) will now fail immediately.

If `cancel_pending_enqueues` is `True`, all pending requests will also
be canceled.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`cancel_pending_enqueues`
</td>
<td>
(Optional.) A boolean, defaulting to
`False` (described above).
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The operation that closes the queue.
</td>
</tr>

</table>



<h3 id="dequeue"><code>dequeue</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L421-L457">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>dequeue(
    name=None
)
</code></pre>

Dequeues one element from this queue.

If the queue is empty when this operation executes, it will block
until there is an element to dequeue.

At runtime, this operation may raise an error if the queue is
`tf.QueueBase.close` before or during its execution. If the
queue is closed, the queue is empty, and there are no pending
enqueue operations that can fulfill this request,
<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> will be raised. If the session is
`tf.Session.close`,
<a href="../../tf/errors/CancelledError.md"><code>tf.errors.CancelledError</code></a> will be raised.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The tuple of tensors that was dequeued.
</td>
</tr>

</table>



<h3 id="dequeue_many"><code>dequeue_many</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L459-L500">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>dequeue_many(
    n, name=None
)
</code></pre>

Dequeues and concatenates `n` elements from this queue.

This operation concatenates queue-element component tensors along
the 0th dimension to make a single component tensor.  All of the
components in the dequeued tuple will have size `n` in the 0th dimension.

If the queue is closed and there are less than `n` elements left, then an
`OutOfRange` exception is raised.

At runtime, this operation may raise an error if the queue is
`tf.QueueBase.close` before or during its execution. If the
queue is closed, the queue contains fewer than `n` elements, and
there are no pending enqueue operations that can fulfill this
request, <a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> will be raised. If the
session is `tf.Session.close`,
<a href="../../tf/errors/CancelledError.md"><code>tf.errors.CancelledError</code></a> will be raised.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`n`
</td>
<td>
A scalar `Tensor` containing the number of elements to dequeue.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The list of concatenated tensors that was dequeued.
</td>
</tr>

</table>



<h3 id="dequeue_up_to"><code>dequeue_up_to</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L502-L541">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>dequeue_up_to(
    n, name=None
)
</code></pre>

Dequeues and concatenates `n` elements from this queue.

**Note** This operation is not supported by all queues.  If a queue does not
support DequeueUpTo, then a <a href="../../tf/errors/UnimplementedError.md"><code>tf.errors.UnimplementedError</code></a> is raised.

This operation concatenates queue-element component tensors along
the 0th dimension to make a single component tensor. If the queue
has not been closed, all of the components in the dequeued tuple
will have size `n` in the 0th dimension.

If the queue is closed and there are more than `0` but fewer than
`n` elements remaining, then instead of raising a
<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> like `tf.QueueBase.dequeue_many`,
less than `n` elements are returned immediately.  If the queue is
closed and there are `0` elements left in the queue, then a
<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> is raised just like in `dequeue_many`.
Otherwise the behavior is identical to `dequeue_many`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`n`
</td>
<td>
A scalar `Tensor` containing the number of elements to dequeue.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The tuple of concatenated tensors that was dequeued.
</td>
</tr>

</table>



<h3 id="enqueue"><code>enqueue</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L311-L348">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>enqueue(
    vals, name=None
)
</code></pre>

Enqueues one element to this queue.

If the queue is full when this operation executes, it will block
until the element has been enqueued.

At runtime, this operation may raise an error if the queue is
`tf.QueueBase.close` before or during its execution. If the
queue is closed before this operation runs,
<a href="../../tf/errors/CancelledError.md"><code>tf.errors.CancelledError</code></a> will be raised. If this operation is
blocked, and either (i) the queue is closed by a close operation
with `cancel_pending_enqueues=True`, or (ii) the session is
`tf.Session.close`,
<a href="../../tf/errors/CancelledError.md"><code>tf.errors.CancelledError</code></a> will be raised.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`vals`
</td>
<td>
A tensor, a list or tuple of tensors, or a dictionary containing
the values to enqueue.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The operation that enqueues a new tuple of tensors to the queue.
</td>
</tr>

</table>



<h3 id="enqueue_many"><code>enqueue_many</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L350-L396">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>enqueue_many(
    vals, name=None
)
</code></pre>

Enqueues zero or more elements to this queue.

This operation slices each component tensor along the 0th dimension to
make multiple queue elements. All of the tensors in `vals` must have the
same size in the 0th dimension.

If the queue is full when this operation executes, it will block
until all of the elements have been enqueued.

At runtime, this operation may raise an error if the queue is
`tf.QueueBase.close` before or during its execution. If the
queue is closed before this operation runs,
<a href="../../tf/errors/CancelledError.md"><code>tf.errors.CancelledError</code></a> will be raised. If this operation is
blocked, and either (i) the queue is closed by a close operation
with `cancel_pending_enqueues=True`, or (ii) the session is
`tf.Session.close`,
<a href="../../tf/errors/CancelledError.md"><code>tf.errors.CancelledError</code></a> will be raised.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`vals`
</td>
<td>
A tensor, a list or tuple of tensors, or a dictionary
from which the queue elements are taken.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The operation that enqueues a batch of tuples of tensors to the queue.
</td>
</tr>

</table>



<h3 id="from_list"><code>from_list</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L184-L223">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_list(
    index, queues
)
</code></pre>

Create a queue using the queue reference from `queues[index]`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`index`
</td>
<td>
An integer scalar tensor that determines the input that gets
selected.
</td>
</tr><tr>
<td>
`queues`
</td>
<td>
A list of `QueueBase` objects.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `QueueBase` object.
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
When `queues` is not a list of `QueueBase` objects,
or when the data types of `queues` are not all the same.
</td>
</tr>
</table>



<h3 id="is_closed"><code>is_closed</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L578-L595">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_closed(
    name=None
)
</code></pre>

Returns true if queue is closed.

This operation returns true if the queue is closed and false if the queue
is open.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
True if the queue is closed and false if the queue is open.
</td>
</tr>

</table>



<h3 id="size"><code>size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/data_flow_ops.py#L597-L611">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>size(
    name=None
)
</code></pre>

Compute the number of elements in this queue.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar tensor containing the number of elements in this queue.
</td>
</tr>

</table>





