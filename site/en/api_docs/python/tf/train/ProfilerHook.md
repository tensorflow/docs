

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.ProfilerHook

## Class `ProfilerHook`

Inherits From: [`SessionRunHook`](../../tf/train/SessionRunHook)



Defined in [`tensorflow/python/training/basic_session_run_hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/training/basic_session_run_hooks.py).

Captures CPU/GPU profiling information every N steps or seconds.

This produces files called "timeline-<step>.json", which are in Chrome
Trace format.

For more information see:
https://github.com/catapult-project/catapult/blob/master/tracing/README.md

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    save_steps=None,
    save_secs=None,
    output_dir='',
    show_dataflow=True,
    show_memory=False
)
```

Initializes a hook that takes periodic profiling snapshots.

`options.run_metadata` argument of `tf.Session.Run` is used to collect
metadata about execution. This hook sets the metadata and dumps it in Chrome
Trace format.


#### Args:

* <b>`save_steps`</b>: `int`, save profile traces every N steps. Exactly one of
      `save_secs` and `save_steps` should be set.
* <b>`save_secs`</b>: `int` or `float`, save profile traces every N seconds.
* <b>`output_dir`</b>: `string`, the directory to save the profile traces to.
      Defaults to the current directory.
* <b>`show_dataflow`</b>: `bool`, if True, add flow events to the trace connecting
      producers and consumers of tensors.
* <b>`show_memory`</b>: `bool`, if True, add object snapshot events to the trace
      showing the sizes and lifetimes of tensors.

<h3 id="after_create_session"><code>after_create_session</code></h3>

``` python
after_create_session(
    session,
    coord
)
```

Called when new TensorFlow session is created.

This is called to signal the hooks that a new session has been created. This
has two essential differences with the situation in which `begin` is called:

* When this is called, the graph is finalized and ops can no longer be added
    to the graph.
* This method will also be called as a result of recovering a wrapped
    session, not only at the beginning of the overall session.

#### Args:

* <b>`session`</b>: A TensorFlow Session that has been created.
* <b>`coord`</b>: A Coordinator object which keeps track of all threads.

<h3 id="after_run"><code>after_run</code></h3>

``` python
after_run(
    run_context,
    run_values
)
```



<h3 id="before_run"><code>before_run</code></h3>

``` python
before_run(run_context)
```



<h3 id="begin"><code>begin</code></h3>

``` python
begin()
```



<h3 id="end"><code>end</code></h3>

``` python
end(session)
```

Called at the end of session.

The `session` argument can be used in case the hook wants to run final ops,
such as saving a last checkpoint.

If `session.run()` raises exception other than OutOfRangeError or
StopIteration then `end()` is not called.
Note the difference between `end()` and `after_run()` behavior when
`session.run()` raises OutOfRangeError or StopIteration. In that case
`end()` is called but `after_run()` is not called.

#### Args:

* <b>`session`</b>: A TensorFlow Session that will be soon closed.



