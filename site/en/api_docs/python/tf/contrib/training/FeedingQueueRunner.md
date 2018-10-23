

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.FeedingQueueRunner

## Class `FeedingQueueRunner`

Inherits From: [`QueueRunner`](../../../tf/train/QueueRunner)



Defined in [`tensorflow/python/estimator/inputs/queues/feeding_queue_runner.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/estimator/inputs/queues/feeding_queue_runner.py).

A queue runner that allows the feeding of values such as numpy arrays.

## Properties

<h3 id="cancel_op"><code>cancel_op</code></h3>



<h3 id="close_op"><code>close_op</code></h3>



<h3 id="enqueue_ops"><code>enqueue_ops</code></h3>



<h3 id="exceptions_raised"><code>exceptions_raised</code></h3>

Exceptions raised but not handled by the `QueueRunner` threads.

Exceptions raised in queue runner threads are handled in one of two ways
depending on whether or not a `Coordinator` was passed to
`create_threads()`:

* With a `Coordinator`, exceptions are reported to the coordinator and
  forgotten by the `QueueRunner`.
* Without a `Coordinator`, exceptions are captured by the `QueueRunner` and
  made available in this `exceptions_raised` property.

#### Returns:

A list of Python `Exception` objects.  The list is empty if no exception
was captured.  (No exceptions are captured when using a Coordinator.)

<h3 id="name"><code>name</code></h3>

The string name of the underlying Queue.

<h3 id="queue"><code>queue</code></h3>



<h3 id="queue_closed_exception_types"><code>queue_closed_exception_types</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    queue=None,
    enqueue_ops=None,
    close_op=None,
    cancel_op=None,
    feed_fns=None,
    queue_closed_exception_types=None
)
```

Initialize the queue runner.

For further documentation, see `queue_runner.py`. Note that
`FeedingQueueRunner` does not support construction from protobuffer nor
serialization to protobuffer.

#### Args:

* <b>`queue`</b>: A `Queue`.
* <b>`enqueue_ops`</b>: List of enqueue ops to run in threads later.
* <b>`close_op`</b>: Op to close the queue. Pending enqueue ops are preserved.
* <b>`cancel_op`</b>: Op to close the queue and cancel pending enqueue ops.
* <b>`feed_fns`</b>: a list of functions that return a dictionary mapping fed
    `Tensor`s to values. Must be the same length as `enqueue_ops`.
* <b>`queue_closed_exception_types`</b>: Optional tuple of Exception types that
    indicate that the queue has been closed when raised during an enqueue
    operation.  Defaults to
    `(tf.errors.OutOfRangeError, tf.errors.CancelledError)`.


#### Raises:

* <b>`ValueError`</b>: `feed_fns` is not `None` and has different length than
    `enqueue_ops`.

<h3 id="create_threads"><code>create_threads</code></h3>

``` python
create_threads(
    sess,
    coord=None,
    daemon=False,
    start=False
)
```

Create threads to run the enqueue ops for the given session.

This method requires a session in which the graph was launched.  It creates
a list of threads, optionally starting them.  There is one thread for each
op passed in `enqueue_ops`.

The `coord` argument is an optional coordinator, that the threads will use
to terminate together and report exceptions.  If a coordinator is given,
this method starts an additional thread to close the queue when the
coordinator requests a stop.

If previously created threads for the given session are still running, no
new threads will be created.

#### Args:

* <b>`sess`</b>: A `Session`.
* <b>`coord`</b>: Optional `Coordinator` object for reporting errors and checking
    stop conditions.
* <b>`daemon`</b>: Boolean.  If `True` make the threads daemon threads.
* <b>`start`</b>: Boolean.  If `True` starts the threads.  If `False` the
    caller must call the `start()` method of the returned threads.


#### Returns:

A list of threads.

<h3 id="from_proto"><code>from_proto</code></h3>

``` python
from_proto(
    queue_runner_def,
    import_scope=None
)
```

Returns a `QueueRunner` object created from `queue_runner_def`.

<h3 id="to_proto"><code>to_proto</code></h3>

``` python
to_proto()
```





