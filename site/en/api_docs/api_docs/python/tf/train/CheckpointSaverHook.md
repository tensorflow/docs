

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.train.CheckpointSaverHook

## Class `CheckpointSaverHook`

Inherits From: [`SessionRunHook`](../../tf/train/SessionRunHook)



Defined in [`tensorflow/python/training/basic_session_run_hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/training/basic_session_run_hooks.py).

See the guide: [Training > Training Hooks](../../../../api_guides/python/train#Training_Hooks)

Saves checkpoints every N steps or seconds.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    checkpoint_dir,
    save_secs=None,
    save_steps=None,
    saver=None,
    checkpoint_basename='model.ckpt',
    scaffold=None,
    listeners=None
)
```

Initializes a `CheckpointSaverHook`.

#### Args:

* <b>`checkpoint_dir`</b>: `str`, base directory for the checkpoint files.
* <b>`save_secs`</b>: `int`, save every N secs.
* <b>`save_steps`</b>: `int`, save every N steps.
* <b>`saver`</b>: `Saver` object, used for saving.
* <b>`checkpoint_basename`</b>: `str`, base name for the checkpoint files.
* <b>`scaffold`</b>: `Scaffold`, use to get saver object.
* <b>`listeners`</b>: List of `CheckpointSaverListener` subclass instances.
    Used for callbacks that run immediately before or after this hook saves
    the checkpoint.


#### Raises:

* <b>`ValueError`</b>: One of `save_steps` or `save_secs` should be set.
* <b>`ValueError`</b>: Exactly one of saver or scaffold should be set.

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





