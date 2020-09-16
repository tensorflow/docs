description: Creates hook to stop if the given metric is lower than the threshold.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental.stop_if_lower_hook" />
<meta itemprop="path" content="Stable" />
</div>

# tf.estimator.experimental.stop_if_lower_hook

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/early_stopping.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates hook to stop if the given metric is lower than the threshold.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.experimental.stop_if_lower_hook`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.experimental.stop_if_lower_hook(
    estimator, metric_name, threshold, eval_dir=None, min_steps=0,
    run_every_secs=60, run_every_steps=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage example:



```python
estimator = ...
# Hook to stop training if loss becomes lower than 100.
hook = early_stopping.stop_if_lower_hook(estimator, "loss", 100)
train_spec = tf.estimator.TrainSpec(..., hooks=[hook])
tf.estimator.train_and_evaluate(estimator, train_spec, ...)
```

Caveat: Current implementation supports early-stopping both training and
evaluation in local mode. In distributed mode, training can be stopped but
evaluation (where it's a separate job) will indefinitely wait for new model
checkpoints to evaluate, so you will need other means to detect and stop it.
Early-stopping evaluation in distributed mode requires changes in
`train_and_evaluate` API and will be addressed in a future revision.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`estimator`
</td>
<td>
A <a href="../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> instance.
</td>
</tr><tr>
<td>
`metric_name`
</td>
<td>
`str`, metric to track. "loss", "accuracy", etc.
</td>
</tr><tr>
<td>
`threshold`
</td>
<td>
Numeric threshold for the given metric.
</td>
</tr><tr>
<td>
`eval_dir`
</td>
<td>
If set, directory containing summary files with eval metrics. By
default, `estimator.eval_dir()` will be used.
</td>
</tr><tr>
<td>
`min_steps`
</td>
<td>
`int`, stop is never requested if global step is less than this
value. Defaults to 0.
</td>
</tr><tr>
<td>
`run_every_secs`
</td>
<td>
If specified, calls `should_stop_fn` at an interval of
`run_every_secs` seconds. Defaults to 60 seconds. Either this or
`run_every_steps` must be set.
</td>
</tr><tr>
<td>
`run_every_steps`
</td>
<td>
If specified, calls `should_stop_fn` every
`run_every_steps` steps. Either this or `run_every_secs` must be set.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An early-stopping hook of type `SessionRunHook` that periodically checks
if the given metric is lower than specified threshold and initiates
early stopping if true.
</td>
</tr>

</table>

