

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.SessionRunContext

## Class `SessionRunContext`





Defined in [`tensorflow/python/training/session_run_hook.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/session_run_hook.py).

See the guide: [Training > Training Hooks](../../../../api_guides/python/train#Training_Hooks)

Provides information about the `session.run()` call being made.

Provides information about original request to `Session.Run()` function.
SessionRunHook objects can stop the loop by calling `request_stop()` of
`run_context`. In the future we may use this object to add more information
about run without changing the Hook API.

## Properties

<h3 id="original_args"><code>original_args</code></h3>

A `SessionRunArgs` object holding the original arguments of `run()`.

If user called `MonitoredSession.run(fetches=a, feed_dict=b)`, then this
field is equal to SessionRunArgs(a, b).

#### Returns:

A `SessionRunArgs` object

<h3 id="session"><code>session</code></h3>

A TensorFlow session object which will execute the `run`.

<h3 id="stop_requested"><code>stop_requested</code></h3>

Returns whether a stop is requested or not.

If true, `MonitoredSession` stops iterations.
#### Returns:

A `bool`



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    original_args,
    session
)
```

Initializes SessionRunContext.

<h3 id="request_stop"><code>request_stop</code></h3>

``` python
request_stop()
```

Sets stop requested field.

Hooks can use this function to request stop of iterations.
`MonitoredSession` checks whether this is called or not.



