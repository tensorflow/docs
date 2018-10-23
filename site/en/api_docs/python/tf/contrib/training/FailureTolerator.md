

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.FailureTolerator

### `class tf.contrib.training.FailureTolerator`



Defined in [`tensorflow/contrib/training/python/training/failure_tolerator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/training/python/training/failure_tolerator.py).

Helper for tolerating certain exceptions.

When encountering a handled exception inside tolerator.forgive(), it
is suppressed (but logged). A subsequent call to tolerator.forgive()
will sleep for a period of time before continuing, with exponential
backoff on multiple exceptions. (The delay avoids retrying too
quickly -- a subsequent attempt will often only succeed after a
transient failure has resolved itself.)

If more than `limit` exceptions have been encountered,
the error will not be suppressed.

Exceptions occurring more than `forgive_after_seconds` ago
(excluding time spent waiting between retries) are forgiven and no
longer count towards the limit.

An example loop using FailureTolerator to retry until a successful
`session.run(...)` would look like:

```
failure_tolerator = FailureTolerator()
while True:
  with failure_tolerator.forgive():
    session = make_session_somehow()
    while not should_stop():
      session.run(...)
    break  # session.run was successful
```

By using FailureTolerator, failures are logged, there are delays
between retries, and there's a ceiling on the maximum number of
retries available. (In the case of persistent errors, the task won't
just loop forever!)

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    limit=5,
    init_delay=5.0,
    backoff_factor=2.0,
    forgive_after_seconds=6000,
    handled_exceptions=None
)
```

Creates a FailureTolerator.

The result will pause for `init_delay *
(backoff_factor^(failure_count-1))` when re-entering `forgive()`
after a failure.

#### Args:

* <b>`limit`</b>: The maximum number of suppressed, unforgiven, failures.
* <b>`init_delay`</b>: How long to pause once the first failure is
    encountered. Defaults to five seconds.
* <b>`backoff_factor`</b>: Each subsequent failure grows the pause by this factor.
* <b>`forgive_after_seconds`</b>: Failures older than this are forgiven.
* <b>`handled_exceptions`</b>: The exceptions to forgive. Defaults to
      `(errors.AbortedError,)`.

<h3 id="forgive"><code>forgive</code></h3>

``` python
forgive(
    *args,
    **kwds
)
```





