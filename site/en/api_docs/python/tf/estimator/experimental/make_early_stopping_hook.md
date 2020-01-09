page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.experimental.make_early_stopping_hook


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/early_stopping.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates early-stopping hook.

### Aliases:

* `tf.compat.v1.estimator.experimental.make_early_stopping_hook`
* `tf.compat.v2.estimator.experimental.make_early_stopping_hook`


``` python
tf.estimator.experimental.make_early_stopping_hook(
    estimator,
    should_stop_fn,
    run_every_secs=60,
    run_every_steps=None
)
```



<!-- Placeholder for "Used in" -->

Returns a `SessionRunHook` that stops training when `should_stop_fn` returns
`True`.

#### Usage example:



```python
estimator = ...
hook = early_stopping.make_early_stopping_hook(
    estimator, should_stop_fn=make_stop_fn(...))
train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
tf.estimator.train_and_evaluate(estimator, train_spec, ...)
```

Caveat: Current implementation supports early-stopping both training and
evaluation in local mode. In distributed mode, training can be stopped but
evaluation (where it's a separate job) will indefinitely wait for new model
checkpoints to evaluate, so you will need other means to detect and stop it.
Early-stopping evaluation in distributed mode requires changes in
`train_and_evaluate` API and will be addressed in a future revision.

#### Args:


* <b>`estimator`</b>: A <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> instance.
* <b>`should_stop_fn`</b>: `callable`, function that takes no arguments and returns a
  `bool`. If the function returns `True`, stopping will be initiated by the
  chief.
* <b>`run_every_secs`</b>: If specified, calls `should_stop_fn` at an interval of
  `run_every_secs` seconds. Defaults to 60 seconds. Either this or
  `run_every_steps` must be set.
* <b>`run_every_steps`</b>: If specified, calls `should_stop_fn` every
  `run_every_steps` steps. Either this or `run_every_secs` must be set.


#### Returns:

A `SessionRunHook` that periodically executes `should_stop_fn` and initiates
early stopping if the function returns `True`.



#### Raises:


* <b>`TypeError`</b>: If `estimator` is not of type <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>.
* <b>`ValueError`</b>: If both `run_every_secs` and `run_every_steps` are set.
