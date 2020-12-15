description: Creates early-stopping hook.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental.make_early_stopping_hook" />
<meta itemprop="path" content="Stable" />
</div>

# tf.estimator.experimental.make_early_stopping_hook

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/early_stopping.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates early-stopping hook.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.experimental.make_early_stopping_hook`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.experimental.make_early_stopping_hook(
    estimator, should_stop_fn, run_every_secs=60, run_every_steps=None
)
</code></pre>



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
`should_stop_fn`
</td>
<td>
`callable`, function that takes no arguments and returns a
`bool`. If the function returns `True`, stopping will be initiated by the
chief.
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
A `SessionRunHook` that periodically executes `should_stop_fn` and initiates
early stopping if the function returns `True`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `estimator` is not of type <a href="../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a>.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If both `run_every_secs` and `run_every_steps` are set.
</td>
</tr>
</table>

