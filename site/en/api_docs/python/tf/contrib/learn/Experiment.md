

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.Experiment

### `class tf.contrib.learn.Experiment`



Defined in [`tensorflow/contrib/learn/python/learn/experiment.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/learn/python/learn/experiment.py).

See the guide: [Learn (contrib) > Distributed training utilities](../../../../../api_guides/python/contrib.learn#Distributed_training_utilities)

Experiment is a class containing all information needed to train a model.

After an experiment is created (by passing an Estimator and inputs for
training and evaluation), an Experiment instance knows how to invoke training
and eval loops in a sensible fashion for distributed training.

## Properties

<h3 id="estimator"><code>estimator</code></h3>



<h3 id="eval_metrics"><code>eval_metrics</code></h3>



<h3 id="eval_steps"><code>eval_steps</code></h3>



<h3 id="train_steps"><code>train_steps</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    *args,
    **kwargs
)
```

Constructor for `Experiment`. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-10-23.
Instructions for updating:
local_eval_frequency is deprecated as local_run will be renamed to train_and_evaluate. Use min_eval_frequency and call train_and_evaluate instead. Note, however, that the default for min_eval_frequency is 1, meaning models will be evaluated every time a new checkpoint is available. In contrast, the default for local_eval_frequency is None, resulting in evaluation occurring only after training has completed. min_eval_frequency is ignored when calling the deprecated local_run.

Creates an Experiment instance. None of the functions passed to this
constructor are executed at construction time. They are stored and used
when a method is executed which requires it.

#### Args:

* <b>`estimator`</b>: Object implementing `Trainable` and `Evaluable`.
* <b>`train_input_fn`</b>: function, returns features and labels for training.
* <b>`eval_input_fn`</b>: function, returns features and labels for evaluation. If
    `eval_steps` is `None`, this should be configured only to produce for a
    finite number of batches (generally, 1 epoch over the evaluation data).
* <b>`eval_metrics`</b>: `dict` of string, metric function. If `None`, default set
    is used.
* <b>`train_steps`</b>: Perform this many steps of training. `None`, the default,
    means train forever.
* <b>`eval_steps`</b>: `evaluate` runs until input is exhausted (or another exception
    is raised), or for `eval_steps` steps, if specified.
* <b>`train_monitors`</b>: A list of monitors to pass to the `Estimator`'s `fit`
    function.
* <b>`eval_hooks`</b>: A list of `SessionRunHook` hooks to pass to the
    `Estimator`'s `evaluate` function.
* <b>`local_eval_frequency`</b>: Frequency of running eval in steps,
    when running locally. If `None`, runs evaluation only at the end of
    training.
* <b>`eval_delay_secs`</b>: Start evaluating after waiting for this many seconds.
* <b>`continuous_eval_throttle_secs`</b>: Do not re-evaluate unless the last
    evaluation was started at least this many seconds ago for
    continuous_eval().
* <b>`min_eval_frequency`</b>: (applies only to train_and_evaluate). the minimum
    number of steps between evaluations. Of course, evaluation does not
    occur if no new snapshot is available, hence, this is the minimum.
* <b>`delay_workers_by_global_step`</b>: if `True` delays training workers
    based on global step instead of time.
* <b>`export_strategies`</b>: A list of `ExportStrategy`s, or a single one, or None.


#### Raises:

* <b>`ValueError`</b>: if `estimator` does not implement `Evaluable` and `Trainable`,
    or if export_strategies has the wrong type.

<h3 id="continuous_eval"><code>continuous_eval</code></h3>

``` python
continuous_eval(
    delay_secs=None,
    throttle_delay_secs=None,
    evaluate_checkpoint_only_once=True,
    continuous_eval_predicate_fn=None
)
```



<h3 id="continuous_eval_on_train_data"><code>continuous_eval_on_train_data</code></h3>

``` python
continuous_eval_on_train_data(
    delay_secs=None,
    throttle_delay_secs=None,
    continuous_eval_predicate_fn=None
)
```



<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(delay_secs=None)
```

Evaluate on the evaluation data.

Runs evaluation on the evaluation data and returns the result. Runs for
`self._eval_steps` steps, or if it's `None`, then run until input is
exhausted or another exception is raised. Start the evaluation after
`delay_secs` seconds, or if it's `None`, defaults to using
`self._eval_delay_secs` seconds.

#### Args:

* <b>`delay_secs`</b>: Start evaluating after this many seconds. If `None`, defaults
    to using `self._eval_delays_secs`.


#### Returns:

  The result of the `evaluate` call to the `Estimator`.

<h3 id="extend_train_hooks"><code>extend_train_hooks</code></h3>

``` python
extend_train_hooks(additional_hooks)
```

Extends the hooks for training.

<h3 id="local_run"><code>local_run</code></h3>

``` python
local_run(
    *args,
    **kwargs
)
```

DEPRECATED FUNCTION

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-10-23.
Instructions for updating:
local_run will be renamed to train_and_evaluate and the new default behavior will be to run evaluation every time there is a new checkpoint.

<h3 id="reset_export_strategies"><code>reset_export_strategies</code></h3>

``` python
reset_export_strategies(new_export_strategies=None)
```

Resets the export strategies with the `new_export_strategies`.

#### Args:

* <b>`new_export_strategies`</b>: A new list of `ExportStrategy`s, or a single one,
    or None.


#### Returns:

  The old export strategies.

<h3 id="run_std_server"><code>run_std_server</code></h3>

``` python
run_std_server()
```

Starts a TensorFlow server and joins the serving thread.

Typically used for parameter servers.

#### Raises:

* <b>`ValueError`</b>: if not enough information is available in the estimator's
    config to create a server.

<h3 id="test"><code>test</code></h3>

``` python
test()
```

Tests training, evaluating and exporting the estimator for a single step.

#### Returns:

  The result of the `evaluate` call to the `Estimator`.

<h3 id="train"><code>train</code></h3>

``` python
train(delay_secs=None)
```

Fit the estimator using the training data.

Train the estimator for `self._train_steps` steps, after waiting for
`delay_secs` seconds. If `self._train_steps` is `None`, train forever.

#### Args:

* <b>`delay_secs`</b>: Start training after this many seconds.


#### Returns:

  The trained estimator.

<h3 id="train_and_evaluate"><code>train_and_evaluate</code></h3>

``` python
train_and_evaluate()
```

Interleaves training and evaluation.

The frequency of evaluation is controlled by the contructor arg
`min_eval_frequency`. When this parameter is None or 0, evaluation happens
only after training has completed. Note that evaluation cannot happen
more frequently than checkpoints are taken. If no new snapshots are
available when evaluation is supposed to occur, then evaluation doesn't
happen for another `min_eval_frequency` steps (assuming a checkpoint is
available at that point). Thus, settings `min_eval_frequency` to 1 means
that the model will be evaluated everytime there is a new checkpoint.

This is particular useful for a "Master" task in the cloud, whose
responsibility it is to take checkpoints, evaluate those checkpoints,
and write out summaries. Participating in training as the supervisor
allows such a task to accomplish the first and last items, while
performing evaluation allows for the second.

#### Returns:

  The result of the `evaluate` call to the `Estimator` as well as the
  export results using the specified `ExportStrategy`.



