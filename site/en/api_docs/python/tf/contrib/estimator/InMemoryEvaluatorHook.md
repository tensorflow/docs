page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.InMemoryEvaluatorHook

## Class `InMemoryEvaluatorHook`

Inherits From: [`SessionRunHook`](../../../tf/train/SessionRunHook)



Defined in [`tensorflow/contrib/estimator/python/estimator/hooks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/estimator/python/estimator/hooks.py).

Hook to run evaluation in training without a checkpoint.

Example:

```python
def train_input_fn():
  ...
  return train_dataset

def eval_input_fn():
  ...
  return eval_dataset

estimator = tf.estimator.DNNClassifier(...)

evaluator = tf.contrib.estimator.InMemoryEvaluatorHook(
    estimator, eval_input_fn)
estimator.train(train_input_fn, hooks=[evaluator])
```

Current limitations of this approach are:
* It doesn't support multi-node distributed mode.
* It doesn't support saveable objects other than variables (such as boosted
  tree support)
* It doesn't support custom saver logic (such as ExponentialMovingAverage
  support)

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    estimator,
    input_fn,
    steps=None,
    hooks=None,
    name=None,
    every_n_iter=100
)
```

Initializes a `InMemoryEvaluatorHook`.

#### Args:

* <b>`estimator`</b>: A <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> instance to call evaluate.
* <b>`input_fn`</b>:  Equivalent to the `input_fn` arg to `estimator.evaluate`. A
    function that constructs the input data for evaluation.
    See <a href="../../../../../guide/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:

      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
        tuple (features, labels) with same constraints as below.
      * A tuple (features, labels): Where `features` is a `Tensor` or a
        dictionary of string feature name to `Tensor` and `labels` is a
        `Tensor` or a dictionary of string label name to `Tensor`. Both
        `features` and `labels` are consumed by `model_fn`. They should
        satisfy the expectation of `model_fn` from inputs.

* <b>`steps`</b>: Equivalent to the `steps` arg to `estimator.evaluate`.  Number of
    steps for which to evaluate model. If `None`, evaluates until `input_fn`
    raises an end-of-input exception.
* <b>`hooks`</b>: Equivalent to the `hooks` arg to `estimator.evaluate`. List of
    `SessionRunHook` subclass instances. Used for callbacks inside the
    evaluation call.
* <b>`name`</b>:  Equivalent to the `name` arg to `estimator.evaluate`. Name of the
    evaluation if user needs to run multiple evaluations on different data
    sets, such as on training data vs test data. Metrics for different
    evaluations are saved in separate folders, and appear separately in
    tensorboard.
* <b>`every_n_iter`</b>: `int`, runs the evaluator once every N training iteration.


#### Raises:

* <b>`ValueError`</b>: if `every_n_iter` is non-positive or it's not a single machine
    training

<h3 id="after_create_session"><code>after_create_session</code></h3>

``` python
after_create_session(
    session,
    coord
)
```

Does first run which shows the eval metrics before training.

<h3 id="after_run"><code>after_run</code></h3>

``` python
after_run(
    run_context,
    run_values
)
```

Runs evaluator.

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

Build eval graph and restoring op.

<h3 id="end"><code>end</code></h3>

``` python
end(session)
```

Runs evaluator for final model.



