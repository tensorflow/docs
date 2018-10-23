

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.SummaryAtEndHook

## Class `SummaryAtEndHook`

Inherits From: [`SessionRunHook`](../../../tf/train/SessionRunHook)



Defined in [`tensorflow/contrib/training/python/training/evaluation.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/training/python/training/evaluation.py).

A run hook that saves a summary with the results of evaluation.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    log_dir=None,
    summary_writer=None,
    summary_op=None,
    feed_dict=None
)
```

Constructs the Summary Hook.

#### Args:

* <b>`log_dir`</b>: The directory where the summary events are saved to.  Used only
    when `summary_writer` is not specified.
* <b>`summary_writer`</b>: A <a href="../../../tf/summary/FileWriter"><code>tf.summary.FileWriter</code></a> to write summary events with.
* <b>`summary_op`</b>: The summary op to run. If left as `None`, then all summaries
    in the tf.GraphKeys.SUMMARIES collection are used.
* <b>`feed_dict`</b>: An optional feed dictionary to use when evaluating the
    summaries.


#### Raises:

* <b>`ValueError`</b>: If both `log_dir` and `summary_writer` are `None`.

<h3 id="after_create_session"><code>after_create_session</code></h3>

``` python
after_create_session(
    session,
    coord
)
```



<h3 id="after_run"><code>after_run</code></h3>

``` python
after_run(
    run_context,
    run_values
)
```

Called after each call to run().

The `run_values` argument contains results of requested ops/tensors by
`before_run()`.

The `run_context` argument is the same one send to `before_run` call.
`run_context.request_stop()` can be called to stop the iteration.

If `session.run()` raises any exceptions then `after_run()` is not called.

#### Args:

* <b>`run_context`</b>: A `SessionRunContext` object.
* <b>`run_values`</b>: A SessionRunValues object.

<h3 id="before_run"><code>before_run</code></h3>

``` python
before_run(run_context)
```

Called before each call to run().

You can return from this call a `SessionRunArgs` object indicating ops or
tensors to add to the upcoming `run()` call.  These ops/tensors will be run
together with the ops/tensors originally passed to the original run() call.
The run args you return can also contain feeds to be added to the run()
call.

The `run_context` argument is a `SessionRunContext` that provides
information about the upcoming `run()` call: the originally requested
op/tensors, the TensorFlow Session.

At this point graph is finalized and you can not add ops.

#### Args:

* <b>`run_context`</b>: A `SessionRunContext` object.


#### Returns:

None or a `SessionRunArgs` object.

<h3 id="begin"><code>begin</code></h3>

``` python
begin()
```



<h3 id="end"><code>end</code></h3>

``` python
end(session)
```





