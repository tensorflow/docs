description: A thread that runs code repeatedly, optionally on a timer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.LooperThread" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="getName"/>
<meta itemprop="property" content="isAlive"/>
<meta itemprop="property" content="isDaemon"/>
<meta itemprop="property" content="is_alive"/>
<meta itemprop="property" content="join"/>
<meta itemprop="property" content="loop"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="run_loop"/>
<meta itemprop="property" content="setDaemon"/>
<meta itemprop="property" content="setName"/>
<meta itemprop="property" content="start"/>
<meta itemprop="property" content="start_loop"/>
<meta itemprop="property" content="stop_loop"/>
</div>

# tf.compat.v1.train.LooperThread

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/coordinator.py#L412-L509">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A thread that runs code repeatedly, optionally on a timer.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.LooperThread(
    coord, timer_interval_secs, target=None, args=None, kwargs=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This thread class is intended to be used with a `Coordinator`.  It repeatedly
runs code specified either as `target` and `args` or by the `run_loop()`
method.

Before each run the thread checks if the coordinator has requested stop.  In
that case the looper thread terminates immediately.

If the code being run raises an exception, that exception is reported to the
coordinator and the thread terminates.  The coordinator will then request all
the other threads it coordinates to stop.

You typically pass looper threads to the supervisor `Join()` method.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`coord`
</td>
<td>
A Coordinator.
</td>
</tr><tr>
<td>
`timer_interval_secs`
</td>
<td>
Time boundaries at which to call Run(), or None
if it should be called back to back.
</td>
</tr><tr>
<td>
`target`
</td>
<td>
Optional callable object that will be executed in the thread.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional arguments to pass to `target` when calling it.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments to pass to `target` when calling it.
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
`daemon`
</td>
<td>
A boolean value indicating whether this thread is a daemon thread.

This must be set before start() is called, otherwise RuntimeError is
raised. Its initial value is inherited from the creating thread; the
main thread is not a daemon thread and therefore all threads created in
the main thread default to daemon = False.

The entire Python program exits when only daemon threads are left.
</td>
</tr><tr>
<td>
`ident`
</td>
<td>
Thread identifier of this thread or None if it has not been started.

This is a nonzero integer. See the get_ident() function. Thread
identifiers may be recycled when a thread exits and another thread is
created. The identifier is available even after the thread has exited.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A string used for identification purposes only.

It has no semantics. Multiple threads may be given the same name. The
initial name is set by the constructor.
</td>
</tr><tr>
<td>
`native_id`
</td>
<td>
Native integral thread ID of this thread, or None if it has not been started.

This is a non-negative integer. See the get_native_id() function.
This represents the Thread ID as reported by the kernel.
</td>
</tr>
</table>



## Methods

<h3 id="getName"><code>getName</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>getName()
</code></pre>




<h3 id="isAlive"><code>isAlive</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>isAlive()
</code></pre>

Return whether the thread is alive.

This method is deprecated, use is_alive() instead.

<h3 id="isDaemon"><code>isDaemon</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>isDaemon()
</code></pre>




<h3 id="is_alive"><code>is_alive</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_alive()
</code></pre>

Return whether the thread is alive.

This method returns True just before the run() method starts until just
after the run() method terminates. The module function enumerate()
returns a list of all alive threads.

<h3 id="join"><code>join</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>join(
    timeout=None
)
</code></pre>

Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is
called terminates -- either normally or through an unhandled exception
or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a
floating point number specifying a timeout for the operation in seconds
(or fractions thereof). As join() always returns None, you must call
is_alive() after join() to decide whether a timeout happened -- if the
thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will
block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current
thread as that would cause a deadlock. It is also an error to join() a
thread before it has been started and attempts to do so raises the same
exception.

<h3 id="loop"><code>loop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/coordinator.py#L459-L481">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>loop(
    coord, timer_interval_secs, target, args=None, kwargs=None
)
</code></pre>

Start a LooperThread that calls a function periodically.

If `timer_interval_secs` is None the thread calls `target(args)`
repeatedly.  Otherwise `target(args)` is called every `timer_interval_secs`
seconds.  The thread terminates when a stop of the coordinator is
requested.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`coord`
</td>
<td>
A Coordinator.
</td>
</tr><tr>
<td>
`timer_interval_secs`
</td>
<td>
Number. Time boundaries at which to call `target`.
</td>
</tr><tr>
<td>
`target`
</td>
<td>
A callable object.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional arguments to pass to `target` when calling it.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments to pass to `target` when calling it.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The started thread.
</td>
</tr>

</table>



<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/coordinator.py#L483-L496">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run()
</code></pre>

Method representing the thread's activity.

You may override this method in a subclass. The standard run() method
invokes the callable object passed to the object's constructor as the
target argument, if any, with sequential and keyword arguments taken
from the args and kwargs arguments, respectively.

<h3 id="run_loop"><code>run_loop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/coordinator.py#L506-L509">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run_loop()
</code></pre>

Called at 'timer_interval_secs' boundaries.


<h3 id="setDaemon"><code>setDaemon</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>setDaemon(
    daemonic
)
</code></pre>




<h3 id="setName"><code>setName</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>setName(
    name
)
</code></pre>




<h3 id="start"><code>start</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start()
</code></pre>

Start the thread's activity.

It must be called at most once per thread object. It arranges for the
object's run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the
same thread object.

<h3 id="start_loop"><code>start_loop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/coordinator.py#L498-L500">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start_loop()
</code></pre>

Called when the thread starts.


<h3 id="stop_loop"><code>stop_loop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/coordinator.py#L502-L504">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>stop_loop()
</code></pre>

Called when the thread stops.




