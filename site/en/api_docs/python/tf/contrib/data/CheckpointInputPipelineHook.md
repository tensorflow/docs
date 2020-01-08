page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.CheckpointInputPipelineHook

## Class `CheckpointInputPipelineHook`

Inherits From: [`SessionRunHook`](../../../tf/train/SessionRunHook)



Defined in [`tensorflow/contrib/data/python/ops/iterator_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/data/python/ops/iterator_ops.py).

Checkpoints input pipeline state every N steps or seconds.

This hook saves the state of the iterators in the `Graph` so that when
training is resumed the input pipeline continues from where it left off.
This could potentially avoid overfitting in certain pipelines where the
number of training steps per eval are small compared to the dataset
size or if the training pipeline is pre-empted.

Differences from `CheckpointSaverHook`:
1. Saves only the input pipelines in the "iterators" collection and not the
   global variables or other saveable objects.
2. Does not write the `GraphDef` and `MetaGraphDef` to the summary.

Example of checkpointing the training pipeline:

```python
est = tf.estimator.Estimator(model_fn)
while True:
  est.train(
      train_input_fn,
      hooks=[tf.contrib.data.CheckpointInputPipelineHook(est)],
      steps=train_steps_per_eval)
  # Note: We do not pass the hook here.
  metrics = est.evaluate(eval_input_fn)
  if should_stop_the_training(metrics):
    break
```

This hook should be used if the input pipeline state needs to be saved
separate from the model checkpoint. Doing so may be useful for a few reasons:
1. The input pipeline checkpoint may be large, if there are large shuffle
   or prefetch buffers for instance, and may bloat the checkpoint size.
2. If the input pipeline is shared between training and validation, restoring
   the checkpoint during validation may override the validation input
   pipeline.

For saving the input pipeline checkpoint alongside the model weights use
<a href="../../../tf/contrib/data/make_saveable_from_iterator"><code>tf.contrib.data.make_saveable_from_iterator</code></a> directly to create a
`SaveableObject` and add to the `SAVEABLE_OBJECTS` collection. Note, however,
that you will need to be careful not to restore the training iterator during
eval. You can do that by not adding the iterator to the SAVEABLE_OBJECTS
collector when building the eval graph.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(estimator)
```

Initializes a `CheckpointInputPipelineHook`.

#### Args:

* <b>`estimator`</b>: Estimator.


#### Raises:

* <b>`ValueError`</b>: One of `save_steps` or `save_secs` should be set.
* <b>`ValueError`</b>: At most one of saver or scaffold should be set.



## Methods

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





