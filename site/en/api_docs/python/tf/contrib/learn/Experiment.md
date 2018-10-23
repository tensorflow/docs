

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.Experiment

## Class `Experiment`





Defined in [`tensorflow/contrib/learn/python/learn/experiment.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/learn/python/learn/experiment.py).

See the guide: [Learn (contrib) > Distributed training utilities](../../../../../api_guides/python/contrib.learn#Distributed_training_utilities)

Experiment is a class containing all information needed to train a model.

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/learn/README.md)
for general migration instructions.

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
    estimator,
    train_input_fn,
    eval_input_fn,
    eval_metrics=None,
    train_steps=None,
    eval_steps=100,
    train_monitors=None,
    eval_hooks=None,
    local_eval_frequency=None,
    eval_delay_secs=120,
    continuous_eval_throttle_secs=60,
    min_eval_frequency=None,
    delay_workers_by_global_step=False,
    export_strategies=None,
    train_steps_per_iteration=None,
    checkpoint_and_export=False,
    saving_listeners=None,
    check_interval_secs=5
)
```

Constructor for `Experiment`. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to tf.estimator.train_and_evaluate. You will also have to convert to a tf.estimator.Estimator.

Creates an Experiment instance. None of the functions passed to this
constructor are executed at construction time. They are stored and used
when a method is executed which requires it.

#### Args:

* <b>`estimator`</b>: Object implementing Estimator interface, which could be a
    combination of <a href="../../../tf/contrib/learn/Trainable"><code>tf.contrib.learn.Trainable</code></a> and
    <a href="../../../tf/contrib/learn/Evaluable"><code>tf.contrib.learn.Evaluable</code></a> (deprecated), or
    <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>.
* <b>`train_input_fn`</b>: function, returns features and labels for training.
* <b>`eval_input_fn`</b>: function, returns features and labels for evaluation. If
    `eval_steps` is `None`, this should be configured only to produce for a
    finite number of batches (generally, 1 epoch over the evaluation data).
* <b>`eval_metrics`</b>: `dict` of string, metric function. If `None`, default set
    is used. This should be `None` if the `estimator` is
    <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>. If metrics are provided they will be
    *appended* to the default set.
* <b>`train_steps`</b>: Perform this many steps of training. `None`, the default,
    means train forever.
* <b>`eval_steps`</b>: `evaluate` runs until input is exhausted (or another exception
    is raised), or for `eval_steps` steps, if specified.
* <b>`train_monitors`</b>: A list of monitors to pass to the `Estimator`'s `fit`
    function.
* <b>`eval_hooks`</b>: A list of `SessionRunHook` hooks to pass to the
    `Estimator`'s `evaluate` function.
* <b>`local_eval_frequency`</b>: (applies only to local_run) Frequency of running
    eval in steps. If `None`, runs evaluation only at the end of training.
* <b>`eval_delay_secs`</b>: Start evaluating after waiting for this many seconds.
* <b>`continuous_eval_throttle_secs`</b>: Do not re-evaluate unless the last
    evaluation was started at least this many seconds ago for
    continuous_eval().
* <b>`min_eval_frequency`</b>: (applies only to train_and_evaluate). the minimum
    number of steps between evaluations. Of course, evaluation does not
    occur if no new snapshot is available, hence, this is the minimum.
    If 0, the evaluation will only happen after training.
    If None, defaults to 1. To avoid checking for new checkpoints too
    frequent, the interval is further limited to be at least
    check_interval_secs between checks.
* <b>`delay_workers_by_global_step`</b>: if `True` delays training workers
    based on global step instead of time.
* <b>`export_strategies`</b>: Iterable of `ExportStrategy`s, or a single one, or
    `None`.
* <b>`train_steps_per_iteration`</b>: (applies only to continuous_train_and_eval).
    Perform this many (integer) number of train steps for each
    training-evaluation iteration. With a small value, the model will be
    evaluated more frequently with more checkpoints saved. If `None`, will
    use a default value (which is smaller than `train_steps` if provided).
* <b>`checkpoint_and_export`</b>: (applies only to train_and_evaluate). If `True`,
    performs intermediate model checkpoints and exports during the training
    process, rather than only once model training is complete. This
    parameter is experimental and may be changed or removed in the future.
    Setting this parameter leads to the following: the value of
    `min_eval_frequency` will be ignored, and the number of steps between
    evaluations and exports will instead be determined by the Estimator
    configuration parameters `save_checkpoints_secs` and
    `save_checkpoints_steps`. Also, this parameter leads to the creation of
    a default `CheckpointSaverHook` instead of a `ValidationMonitor`, so the
    provided `train_monitors` will need to be adjusted accordingly.
* <b>`saving_listeners`</b>: list of `CheckpointSaverListener` objects. Used by
    tf.estimator.Estimator for callbacks that run immediately before or
    after checkpoint savings.
* <b>`check_interval_secs`</b>:     Minimum time between subsequent checks for a new checkpoint. This
    mostly applies if both min_eval_frequency and the time spent per
    training step is low.

#### Raises:

* <b>`ValueError`</b>: if `estimator` does not implement Estimator interface,
    or if export_strategies has the wrong type.

<h3 id="continuous_eval"><code>continuous_eval</code></h3>

``` python
continuous_eval(
    delay_secs=None,
    throttle_delay_secs=None,
    evaluate_checkpoint_only_once=True,
    continuous_eval_predicate_fn=None,
    name='continuous'
)
```



<h3 id="continuous_eval_on_train_data"><code>continuous_eval_on_train_data</code></h3>

``` python
continuous_eval_on_train_data(
    delay_secs=None,
    throttle_delay_secs=None,
    continuous_eval_predicate_fn=None,
    name='continuous_on_train_data'
)
```



<h3 id="continuous_train_and_eval"><code>continuous_train_and_eval</code></h3>

``` python
continuous_train_and_eval(
    *args,
    **kwargs
)
```

Interleaves training and evaluation. (experimental)

THIS FUNCTION IS EXPERIMENTAL. It may change or be removed at any time, and without warning.

The frequency of evaluation is controlled by the `train_steps_per_iteration`
(via constructor). The model will be first trained for
`train_steps_per_iteration`, and then be evaluated in turns.

This method is intended for single machine usage.

This differs from `train_and_evaluate` as follows:

  1. The procedure will have train and evaluation in turns. The model
  will be trained for a number of steps (usually smaller than `train_steps`
  if provided) and then be evaluated.  `train_and_evaluate` will train the
  model for `train_steps` (no small training iterations).

  2. Due to the different approach this schedule takes, it leads to two
  differences in resource control. First, the resources (e.g., memory) used
  by training will be released before evaluation (`train_and_evaluate` takes
  double resources). Second, more checkpoints will be saved as a checkpoint
  is generated at the end of each training iteration.

  3. As the estimator.train starts from scratch (new graph, new states for
  input, etc) at each iteration, it is recommended to have the
  `train_steps_per_iteration` larger. It is also recommended to shuffle your
  input.

#### Args:

* <b>`continuous_eval_predicate_fn`</b>: A predicate function determining whether to
    continue eval after each iteration. A `predicate_fn` has one of the
    following signatures:
      * (eval_results) -> boolean
      * (eval_results, checkpoint_path) -> boolean
    Where `eval_results` is the dictionary of metric evaluations and
    checkpoint_path is the path to the checkpoint containing the parameters
    on which that evaluation was based.
    At the beginning of evaluation, the passed `eval_results` and
    `checkpoint_path` will be None so it's expected that the predicate
    function handles that gracefully.
    When `predicate_fn` is not specified, continuous eval will run in an
    infinite loop (if `train_steps` is None). or exit once global step
    reaches `train_steps`.


#### Returns:

A tuple of the result of the `evaluate` call to the `Estimator` and the
export results using the specified `ExportStrategy`.


#### Raises:

* <b>`ValueError`</b>: if `continuous_eval_predicate_fn` is neither None nor
    callable.

<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(
    delay_secs=None,
    name=None
)
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
* <b>`name`</b>: Gives the name to the evauation for the case multiple evaluation is
    run for the same experiment.


#### Returns:

The result of the `evaluate` call to the `Estimator`.

<h3 id="extend_train_hooks"><code>extend_train_hooks</code></h3>

``` python
extend_train_hooks(additional_hooks)
```

Extends the hooks for training.

<h3 id="local_run"><code>local_run</code></h3>

``` python
local_run()
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

The frequency of evaluation is controlled by the constructor arg
`min_eval_frequency`. When this parameter is 0, evaluation happens
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



