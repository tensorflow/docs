page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.experimental.stop_if_no_decrease_hook


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/early_stopping.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates hook to stop if metric does not decrease within given max steps.

### Aliases:

* `tf.compat.v1.estimator.experimental.stop_if_no_decrease_hook`
* `tf.compat.v2.estimator.experimental.stop_if_no_decrease_hook`


``` python
tf.estimator.experimental.stop_if_no_decrease_hook(
    estimator,
    metric_name,
    max_steps_without_decrease,
    eval_dir=None,
    min_steps=0,
    run_every_secs=60,
    run_every_steps=None
)
```



<!-- Placeholder for "Used in" -->


#### Usage example:



```python
estimator = ...
# Hook to stop training if loss does not decrease in over 100000 steps.
hook = early_stopping.stop_if_no_decrease_hook(estimator, "loss", 100000)
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
* <b>`metric_name`</b>: `str`, metric to track. "loss", "accuracy", etc.
* <b>`max_steps_without_decrease`</b>: `int`, maximum number of training steps with no
  decrease in the given metric.
* <b>`eval_dir`</b>: If set, directory containing summary files with eval metrics. By
  default, `estimator.eval_dir()` will be used.
* <b>`min_steps`</b>: `int`, stop is never requested if global step is less than this
  value. Defaults to 0.
* <b>`run_every_secs`</b>: If specified, calls `should_stop_fn` at an interval of
  `run_every_secs` seconds. Defaults to 60 seconds. Either this or
  `run_every_steps` must be set.
* <b>`run_every_steps`</b>: If specified, calls `should_stop_fn` every
  `run_every_steps` steps. Either this or `run_every_secs` must be set.


#### Returns:

An early-stopping hook of type `SessionRunHook` that periodically checks
if the given metric shows no decrease over given maximum number of
training steps, and initiates early stopping if true.
