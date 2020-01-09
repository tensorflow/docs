page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.MonitoredSession.StepContext


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L812-L847">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StepContext`

Control flow instrument for the `step_fn` from `run_step_fn()`.



### Aliases:

* Class `tf.compat.v1.train.SingularMonitoredSession.StepContext`


<!-- Placeholder for "Used in" -->

Users of `step_fn` may perform `run()` calls without running hooks
by accessing the `session`.  A `run()` call with hooks may be performed
using `run_with_hooks()`.  Computation flow can be interrupted using
`request_stop()`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L821-L829">View source</a>

``` python
__init__(
    session,
    run_with_hooks_fn
)
```

Initializes the `step_context` argument for a `step_fn` invocation.


#### Args:


* <b>`session`</b>: An instance of <a href="../../../../../tf/compat/v1/Session"><code>tf.compat.v1.Session</code></a>.
* <b>`run_with_hooks_fn`</b>: A function for running fetches and hooks.



## Properties

<h3 id="session"><code>session</code></h3>






## Methods

<h3 id="request_stop"><code>request_stop</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L839-L847">View source</a>

``` python
request_stop()
```

Exit the training loop by causing `should_stop()` to return `True`.

   Causes `step_fn` to exit by raising an exception.

#### Raises:

StopIteration


<h3 id="run_with_hooks"><code>run_with_hooks</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/monitored_session.py#L835-L837">View source</a>

``` python
run_with_hooks(
    *args,
    **kwargs
)
```

Same as `MonitoredSession.run`. Accepts the same arguments.
