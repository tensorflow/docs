

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.learn_runner.tune

### `tf.contrib.learn.learn_runner.tune`

``` python
tune(
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/framework/python/framework/experimental.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/framework/python/framework/experimental.py).

Tune an experiment with hyper-parameters. (experimental)

THIS FUNCTION IS EXPERIMENTAL. It may change or be removed at any time, and without warning.


It iterates trials by running the Experiment for each trial with the
corresponding hyper-parameters. For each trial, it retrieves the
hyper-parameters from `tuner`, creates an Experiment by calling experiment_fn,
and then reports the measure back to `tuner`.

Example:

```
  def _create_my_experiment(run_config, hparams):
    hidden_units = [hparams.unit_per_layer] * hparams.num_hidden_layers

    return tf.contrib.learn.Experiment(
        estimator=DNNClassifier(config=run_config, hidden_units=hidden_units),
        train_input_fn=my_train_input,
        eval_input_fn=my_eval_input)

  tuner = create_tuner(study_configuration, objective_key)

  learn_runner.tune(experiment_fn=_create_my_experiment, tuner)
```
#### Args:

* <b>`experiment_fn`</b>: A function that creates an `Experiment`. It should accept an
    argument `run_config` which should be used to create the `Estimator` (
    passed as `config` to its constructor), and an argument `hparams`, which
    should be used for hyper-parameters tuning. It must return an
    `Experiment`.
* <b>`tuner`</b>: A `Tuner` instance.