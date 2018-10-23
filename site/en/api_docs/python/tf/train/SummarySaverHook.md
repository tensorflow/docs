

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.SummarySaverHook

## Class `SummarySaverHook`

Inherits From: [`SessionRunHook`](../../tf/train/SessionRunHook)



Defined in [`tensorflow/python/training/basic_session_run_hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/training/basic_session_run_hooks.py).

See the guide: [Training > Training Hooks](../../../../api_guides/python/train#Training_Hooks)

Saves summaries every N steps.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    save_steps=None,
    save_secs=None,
    output_dir=None,
    summary_writer=None,
    scaffold=None,
    summary_op=None
)
```

Initializes a `SummarySaverHook`.

#### Args:

* <b>`save_steps`</b>: `int`, save summaries every N steps. Exactly one of
      `save_secs` and `save_steps` should be set.
* <b>`save_secs`</b>: `int`, save summaries every N seconds.
* <b>`output_dir`</b>: `string`, the directory to save the summaries to. Only used
      if no `summary_writer` is supplied.
* <b>`summary_writer`</b>: `SummaryWriter`. If `None` and an `output_dir` was passed,
      one will be created accordingly.
* <b>`scaffold`</b>: `Scaffold` to get summary_op if it's not provided.
* <b>`summary_op`</b>: `Tensor` of type `string` containing the serialized `Summary`
      protocol buffer or a list of `Tensor`. They are most likely an output
      by TF summary methods like `tf.summary.scalar` or
      `tf.summary.merge_all`. It can be passed in as one tensor; if more
      than one, they must be passed in as a list.


#### Raises:

* <b>`ValueError`</b>: Exactly one of scaffold or summary_op should be set.

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
end(session=None)
```





