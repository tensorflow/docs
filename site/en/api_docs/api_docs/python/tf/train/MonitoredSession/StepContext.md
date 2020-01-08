

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.MonitoredSession.StepContext

## Class `StepContext`



### Aliases:

* Class `tf.train.MonitoredSession.StepContext`
* Class `tf.train.SingularMonitoredSession.StepContext`



Defined in [`tensorflow/python/training/monitored_session.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/monitored_session.py).

Control flow instrument for the `step_fn` from `run_step_fn()`.

Users of `step_fn` may perform `run()` calls without running hooks
by accessing the `session`.  A `run()` call with hooks may be performed
using `run_with_hooks()`.  Computation flow can be interrupted using
`request_stop()`.

## Properties

<h3 id="session"><code>session</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    session,
    run_with_hooks_fn
)
```

Initializes the `step_context` argument for a `step_fn` invocation.

#### Args:

* <b>`session`</b>: An instance of <a href="../../../tf/Session"><code>tf.Session</code></a>.
* <b>`run_with_hooks_fn`</b>: A function for running fetches and hooks.

<h3 id="request_stop"><code>request_stop</code></h3>

``` python
request_stop()
```

Exit the training loop by causing `should_stop()` to return `True`.

   Causes `step_fn` to exit by raising an exception.

#### Raises:

StopIteration

<h3 id="run_with_hooks"><code>run_with_hooks</code></h3>

``` python
run_with_hooks(
    *args,
    **kwargs
)
```

Same as `MonitoredSession.run`. Accepts the same arguments.



