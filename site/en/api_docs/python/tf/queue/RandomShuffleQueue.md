page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.queue.RandomShuffleQueue

## Class `RandomShuffleQueue`

A queue implementation that dequeues elements in a random order.

Inherits From: [`QueueBase`](../../tf/queue/QueueBase)

### Aliases:

* Class `tf.RandomShuffleQueue`
* Class `tf.compat.v1.RandomShuffleQueue`
* Class `tf.compat.v1.io.RandomShuffleQueue`
* Class `tf.compat.v1.queue.RandomShuffleQueue`
* Class `tf.compat.v2.queue.RandomShuffleQueue`
* Class `tf.io.RandomShuffleQueue`
* Class `tf.queue.RandomShuffleQueue`



Defined in [`python/ops/data_flow_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/data_flow_ops.py).

<!-- Placeholder for "Used in" -->

See <a href="../../tf/queue/QueueBase"><code>tf.queue.QueueBase</code></a> for a description of the methods on
this class.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    capacity,
    min_after_dequeue,
    dtypes,
    shapes=None,
    names=None,
    seed=None,
    shared_name=None,
    name='random_shuffle_queue'
)
```

Create a queue that dequeues elements in a random order.

A `RandomShuffleQueue` has bounded capacity; supports multiple
concurrent producers and consumers; and provides exactly-once
delivery.

A `RandomShuffleQueue` holds a list of up to `capacity`
elements. Each element is a fixed-length tuple of tensors whose
dtypes are described by `dtypes`, and whose shapes are optionally
described by the `shapes` argument.

If the `shapes` argument is specified, each component of a queue
element must have the respective fixed shape. If it is
unspecified, different queue elements may have different shapes,
but the use of `dequeue_many` is disallowed.

The `min_after_dequeue` argument allows the caller to specify a
minimum number of elements that will remain in the queue after a
`dequeue` or `dequeue_many` operation completes, to ensure a
minimum level of mixing of elements. This invariant is maintained
by blocking those operations until sufficient elements have been
enqueued. The `min_after_dequeue` argument is ignored after the
queue has been closed.

#### Args:


* <b>`capacity`</b>: An integer. The upper bound on the number of elements
  that may be stored in this queue.
* <b>`min_after_dequeue`</b>: An integer (described above).
* <b>`dtypes`</b>:  A list of `DType` objects. The length of `dtypes` must equal
  the number of tensors in each queue element.
* <b>`shapes`</b>: (Optional.) A list of fully-defined `TensorShape` objects
  with the same length as `dtypes`, or `None`.
* <b>`names`</b>: (Optional.) A list of string naming the components in the queue
  with the same length as `dtypes`, or `None`.  If specified the dequeue
  methods return a dictionary with the names as keys.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`shared_name`</b>: (Optional.) If non-empty, this queue will be shared under
  the given name across multiple sessions.
* <b>`name`</b>: Optional name for the queue operation.



## Properties

<h3 id="dtypes"><code>dtypes</code></h3>

The list of dtypes for each component of a queue element.


<h3 id="name"><code>name</code></h3>

The name of the underlying queue.


<h3 id="names"><code>names</code></h3>

The list of names for each component of a queue element.


<h3 id="queue_ref"><code>queue_ref</code></h3>

The underlying queue reference.


<h3 id="shapes"><code>shapes</code></h3>

The list of shapes for each component of a queue element.




## Methods

<h3 id="close"><code>close</code></h3>

``` python
close(
    cancel_pending_enqueues=False,
    name=None
)
```

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

#### Args:


* <b>`cancel_pending_enqueues`</b>: (Optional.) A boolean, defaulting to
  `False` (described above).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The operation that closes the queue.


<h3 id="dequeue"><code>dequeue</code></h3>

``` python
dequeue(name=None)
```

Dequeues one element from this queue.

If the queue is empty when this operation executes, it will block
until there is an element to dequeue.

At runtime, this operation may raise an error if the queue is
<a href="../../tf/queue/QueueBase#close"><code>tf.QueueBase.close</code></a> before or during its execution. If the
queue is closed, the queue is empty, and there are no pending
enqueue operations that can fulfill this request,
<a href="../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a> will be raised. If the session is
<a href="../../tf/Session#close"><code>tf.Session.close</code></a>,
<a href="../../tf/errors/CancelledError"><code>tf.errors.CancelledError</code></a> will be raised.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The tuple of tensors that was dequeued.


<h3 id="dequeue_many"><code>dequeue_many</code></h3>

``` python
dequeue_many(
    n,
    name=None
)
```

Dequeues and concatenates `n` elements from this queue.

This operation concatenates queue-element component tensors along
the 0th dimension to make a single component tensor.  All of the
components in the dequeued tuple will have size `n` in the 0th dimension.

If the queue is closed and there are less than `n` elements left, then an
`OutOfRange` exception is raised.

At runtime, this operation may raise an error if the queue is
<a href="../../tf/queue/QueueBase#close"><code>tf.QueueBase.close</code></a> before or during its execution. If the
queue is closed, the queue contains fewer than `n` elements, and
there are no pending enqueue operations that can fulfill this
request, <a href="../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a> will be raised. If the
session is <a href="../../tf/Session#close"><code>tf.Session.close</code></a>,
<a href="../../tf/errors/CancelledError"><code>tf.errors.CancelledError</code></a> will be raised.

#### Args:


* <b>`n`</b>: A scalar `Tensor` containing the number of elements to dequeue.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The list of concatenated tensors that was dequeued.


<h3 id="dequeue_up_to"><code>dequeue_up_to</code></h3>

``` python
dequeue_up_to(
    n,
    name=None
)
```

Dequeues and concatenates `n` elements from this queue.

**Note** This operation is not supported by all queues.  If a queue does not
support DequeueUpTo, then a <a href="../../tf/errors/UnimplementedError"><code>tf.errors.UnimplementedError</code></a> is raised.

This operation concatenates queue-element component tensors along
the 0th dimension to make a single component tensor. If the queue
has not been closed, all of the components in the dequeued tuple
will have size `n` in the 0th dimension.

If the queue is closed and there are more than `0` but fewer than
`n` elements remaining, then instead of raising a
<a href="../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a> like <a href="../../tf/queue/QueueBase#dequeue_many"><code>tf.QueueBase.dequeue_many</code></a>,
less than `n` elements are returned immediately.  If the queue is
closed and there are `0` elements left in the queue, then a
<a href="../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a> is raised just like in `dequeue_many`.
Otherwise the behavior is identical to `dequeue_many`.

#### Args:


* <b>`n`</b>: A scalar `Tensor` containing the number of elements to dequeue.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The tuple of concatenated tensors that was dequeued.


<h3 id="enqueue"><code>enqueue</code></h3>

``` python
enqueue(
    vals,
    name=None
)
```

Enqueues one element to this queue.

If the queue is full when this operation executes, it will block
until the element has been enqueued.

At runtime, this operation may raise an error if the queue is
<a href="../../tf/queue/QueueBase#close"><code>tf.QueueBase.close</code></a> before or during its execution. If the
queue is closed before this operation runs,
<a href="../../tf/errors/CancelledError"><code>tf.errors.CancelledError</code></a> will be raised. If this operation is
blocked, and either (i) the queue is closed by a close operation
with `cancel_pending_enqueues=True`, or (ii) the session is
<a href="../../tf/Session#close"><code>tf.Session.close</code></a>,
<a href="../../tf/errors/CancelledError"><code>tf.errors.CancelledError</code></a> will be raised.

#### Args:


* <b>`vals`</b>: A tensor, a list or tuple of tensors, or a dictionary containing
  the values to enqueue.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The operation that enqueues a new tuple of tensors to the queue.


<h3 id="enqueue_many"><code>enqueue_many</code></h3>

``` python
enqueue_many(
    vals,
    name=None
)
```

Enqueues zero or more elements to this queue.

This operation slices each component tensor along the 0th dimension to
make multiple queue elements. All of the tensors in `vals` must have the
same size in the 0th dimension.

If the queue is full when this operation executes, it will block
until all of the elements have been enqueued.

At runtime, this operation may raise an error if the queue is
<a href="../../tf/queue/QueueBase#close"><code>tf.QueueBase.close</code></a> before or during its execution. If the
queue is closed before this operation runs,
<a href="../../tf/errors/CancelledError"><code>tf.errors.CancelledError</code></a> will be raised. If this operation is
blocked, and either (i) the queue is closed by a close operation
with `cancel_pending_enqueues=True`, or (ii) the session is
<a href="../../tf/Session#close"><code>tf.Session.close</code></a>,
<a href="../../tf/errors/CancelledError"><code>tf.errors.CancelledError</code></a> will be raised.

#### Args:


* <b>`vals`</b>: A tensor, a list or tuple of tensors, or a dictionary
  from which the queue elements are taken.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The operation that enqueues a batch of tuples of tensors to the queue.


<h3 id="from_list"><code>from_list</code></h3>

``` python
from_list(
    index,
    queues
)
```

Create a queue using the queue reference from `queues[index]`.


#### Args:


* <b>`index`</b>: An integer scalar tensor that determines the input that gets
  selected.
* <b>`queues`</b>: A list of `QueueBase` objects.


#### Returns:

A `QueueBase` object.



#### Raises:


* <b>`TypeError`</b>: When `queues` is not a list of `QueueBase` objects,
  or when the data types of `queues` are not all the same.

<h3 id="is_closed"><code>is_closed</code></h3>

``` python
is_closed(name=None)
```

Returns true if queue is closed.

This operation returns true if the queue is closed and false if the queue
is open.

#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

True if the queue is closed and false if the queue is open.


<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this queue.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar tensor containing the number of elements in this queue.




