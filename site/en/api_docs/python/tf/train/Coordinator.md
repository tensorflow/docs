page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.Coordinator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/train/Coordinator">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L34-L407">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Coordinator`

A coordinator for threads.



### Aliases:

* Class <a href="/api_docs/python/tf/train/Coordinator"><code>tf.compat.v1.train.Coordinator</code></a>
* Class <a href="/api_docs/python/tf/train/Coordinator"><code>tf.compat.v2.train.Coordinator</code></a>


<!-- Placeholder for "Used in" -->

This class implements a simple mechanism to coordinate the termination of a
set of threads.

#### Usage:

```python
# Create a coordinator.
coord = Coordinator()
# Start a number of threads, passing the coordinator to each of them.
...start thread 1...(coord, ...)
...start thread N...(coord, ...)
# Wait for all the threads to terminate.
coord.join(threads)
```

Any of the threads can call `coord.request_stop()` to ask for all the threads
to stop.  To cooperate with the requests, each thread must check for
`coord.should_stop()` on a regular basis.  `coord.should_stop()` returns
`True` as soon as `coord.request_stop()` has been called.

A typical thread running with a coordinator will do something like:

```python
while not coord.should_stop():
  ...do some work...
```

#### Exception handling:

A thread can report an exception to the coordinator as part of the
`request_stop()` call.  The exception will be re-raised from the
`coord.join()` call.

#### Thread code:



```python
try:
  while not coord.should_stop():
    ...do some work...
except Exception as e:
  coord.request_stop(e)
```

#### Main code:



```python
try:
  ...
  coord = Coordinator()
  # Start a number of threads, passing the coordinator to each of them.
  ...start thread 1...(coord, ...)
  ...start thread N...(coord, ...)
  # Wait for all the threads to terminate.
  coord.join(threads)
except Exception as e:
  ...exception that was passed to coord.request_stop()
```

To simplify the thread implementation, the Coordinator provides a
context handler `stop_on_exception()` that automatically requests a stop if
an exception is raised.  Using the context handler the thread code above
can be written as:

```python
with coord.stop_on_exception():
  while not coord.should_stop():
    ...do some work...
```

#### Grace period for stopping:

After a thread has called `coord.request_stop()` the other threads have a
fixed time to stop, this is called the 'stop grace period' and defaults to 2
minutes.  If any of the threads is still alive after the grace period expires
`coord.join()` raises a RuntimeError reporting the laggards.

```python
try:
  ...
  coord = Coordinator()
  # Start a number of threads, passing the coordinator to each of them.
  ...start thread 1...(coord, ...)
  ...start thread N...(coord, ...)
  # Wait for all the threads to terminate, give them 10s grace period
  coord.join(threads, stop_grace_period_secs=10)
except RuntimeError:
  ...one of the threads took more than 10s to stop after request_stop()
  ...was called.
except Exception:
  ...exception that was passed to coord.request_stop()
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L130-L159">View source</a>

``` python
__init__(clean_stop_exception_types=None)
```

Create a new Coordinator.


#### Args:


* <b>`clean_stop_exception_types`</b>: Optional tuple of Exception types that should
  cause a clean stop of the coordinator. If an exception of one of these
  types is reported to `request_stop(ex)` the coordinator will behave as
  if `request_stop(None)` was called.  Defaults to
  `(tf.errors.OutOfRangeError,)` which is used by input queues to signal
  the end of input. When feeding training data from a Python iterator it
  is common to add `StopIteration` to this list.



## Properties

<h3 id="joined"><code>joined</code></h3>






## Methods

<h3 id="clear_stop"><code>clear_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L246-L255">View source</a>

``` python
clear_stop()
```

Clears the stop flag.

After this is called, calls to `should_stop()` will return `False`.

<h3 id="join"><code>join</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L322-L397">View source</a>

``` python
join(
    threads=None,
    stop_grace_period_secs=120,
    ignore_live_threads=False
)
```

Wait for threads to terminate.

This call blocks until a set of threads have terminated.  The set of thread
is the union of the threads passed in the `threads` argument and the list
of threads that registered with the coordinator by calling
<a href="../../tf/train/Coordinator#register_thread"><code>Coordinator.register_thread()</code></a>.

After the threads stop, if an `exc_info` was passed to `request_stop`, that
exception is re-raised.

Grace period handling: When `request_stop()` is called, threads are given
'stop_grace_period_secs' seconds to terminate.  If any of them is still
alive after that period expires, a `RuntimeError` is raised.  Note that if
an `exc_info` was passed to `request_stop()` then it is raised instead of
that `RuntimeError`.

#### Args:


* <b>`threads`</b>: List of `threading.Threads`. The started threads to join in
  addition to the registered threads.
* <b>`stop_grace_period_secs`</b>: Number of seconds given to threads to stop after
  `request_stop()` has been called.
* <b>`ignore_live_threads`</b>: If `False`, raises an error if any of the threads are
  still alive after `stop_grace_period_secs`.


#### Raises:


* <b>`RuntimeError`</b>: If any thread is still alive after `request_stop()`
  is called and the grace period expires.

<h3 id="raise_requested_exception"><code>raise_requested_exception</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L403-L407">View source</a>

``` python
raise_requested_exception()
```

If an exception has been passed to `request_stop`, this raises it.


<h3 id="register_thread"><code>register_thread</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L313-L320">View source</a>

``` python
register_thread(thread)
```

Register a thread to join.


#### Args:


* <b>`thread`</b>: A Python thread to join.

<h3 id="request_stop"><code>request_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L187-L244">View source</a>

``` python
request_stop(ex=None)
```

Request that the threads stop.

After this is called, calls to `should_stop()` will return `True`.

Note: If an exception is being passed in, in must be in the context of
handling the exception (i.e. `try: ... except Exception as ex: ...`) and not
a newly created one.

#### Args:


* <b>`ex`</b>: Optional `Exception`, or Python `exc_info` tuple as returned by
  `sys.exc_info()`.  If this is the first call to `request_stop()` the
  corresponding exception is recorded and re-raised from `join()`.

<h3 id="should_stop"><code>should_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L257-L263">View source</a>

``` python
should_stop()
```

Check if stop was requested.


#### Returns:

True if a stop was requested.


<h3 id="stop_on_exception"><code>stop_on_exception</code></h3>

``` python
stop_on_exception(
    *args,
    **kwds
)
```

Context manager to request stop when an Exception is raised.

Code that uses a coordinator must catch exceptions and pass
them to the `request_stop()` method to stop the other threads
managed by the coordinator.

This context handler simplifies the exception handling.
Use it as follows:

```python
with coord.stop_on_exception():
  # Any exception raised in the body of the with
  # clause is reported to the coordinator before terminating
  # the execution of the body.
  ...body...
```

This is completely equivalent to the slightly longer code:

```python
try:
  ...body...
except:
  coord.request_stop(sys.exc_info())
```

#### Yields:

nothing.


<h3 id="wait_for_stop"><code>wait_for_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/coordinator.py#L301-L311">View source</a>

``` python
wait_for_stop(timeout=None)
```

Wait till the Coordinator is told to stop.


#### Args:


* <b>`timeout`</b>: Float.  Sleep for up to that many seconds waiting for
  should_stop() to become True.


#### Returns:

True if the Coordinator is told stop, False if the timeout expired.
