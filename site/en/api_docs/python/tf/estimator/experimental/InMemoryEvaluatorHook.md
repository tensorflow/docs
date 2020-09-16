description: Hook to run evaluation in training without a checkpoint.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental.InMemoryEvaluatorHook" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="after_create_session"/>
<meta itemprop="property" content="after_run"/>
<meta itemprop="property" content="before_run"/>
<meta itemprop="property" content="begin"/>
<meta itemprop="property" content="end"/>
</div>

# tf.estimator.experimental.InMemoryEvaluatorHook

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Hook to run evaluation in training without a checkpoint.

Inherits From: [`SessionRunHook`](../../../tf/estimator/SessionRunHook.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.experimental.InMemoryEvaluatorHook`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.experimental.InMemoryEvaluatorHook(
    estimator, input_fn, steps=None, hooks=None, name=None, every_n_iter=100
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```python
def train_input_fn():
  ...
  return train_dataset

def eval_input_fn():
  ...
  return eval_dataset

estimator = tf.estimator.DNNClassifier(...)

evaluator = tf.estimator.experimental.InMemoryEvaluatorHook(
    estimator, eval_input_fn)
estimator.train(train_input_fn, hooks=[evaluator])
```

Current limitations of this approach are:

* It doesn't support multi-node distributed mode.
* It doesn't support saveable objects other than variables (such as boosted
  tree support)
* It doesn't support custom saver logic (such as ExponentialMovingAverage
  support)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`estimator`
</td>
<td>
A <a href="../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> instance to call evaluate.
</td>
</tr><tr>
<td>
`input_fn`
</td>
<td>
Equivalent to the `input_fn` arg to `estimator.evaluate`. A
function that constructs the input data for evaluation. See [Creating
input functions](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The function should construct and return one of
the following:
* A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
tuple (features, labels) with same constraints as below.
* A tuple (features, labels): Where `features` is a `Tensor` or a
dictionary of string feature name to `Tensor` and `labels` is a
`Tensor` or a dictionary of string label name to `Tensor`. Both
`features` and `labels` are consumed by `model_fn`. They should
satisfy the expectation of `model_fn` from inputs.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Equivalent to the `steps` arg to `estimator.evaluate`.  Number of
steps for which to evaluate model. If `None`, evaluates until `input_fn`
raises an end-of-input exception.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
Equivalent to the `hooks` arg to `estimator.evaluate`. List of
`SessionRunHook` subclass instances. Used for callbacks inside the
evaluation call.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Equivalent to the `name` arg to `estimator.evaluate`. Name of the
evaluation if user needs to run multiple evaluations on different data
sets, such as on training data vs test data. Metrics for different
evaluations are saved in separate folders, and appear separately in
tensorboard.
</td>
</tr><tr>
<td>
`every_n_iter`
</td>
<td>
`int`, runs the evaluator once every N training iteration.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `every_n_iter` is non-positive or it's not a single machine
training
</td>
</tr>
</table>



## Methods

<h3 id="after_create_session"><code>after_create_session</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>after_create_session(
    session, coord
)
</code></pre>

Does first run which shows the eval metrics before training.


<h3 id="after_run"><code>after_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>after_run(
    run_context, run_values
)
</code></pre>

Runs evaluator.


<h3 id="before_run"><code>before_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/session_run_hook.py#L129-L150">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>before_run(
    run_context
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`run_context`
</td>
<td>
A `SessionRunContext` object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
None or a `SessionRunArgs` object.
</td>
</tr>

</table>



<h3 id="begin"><code>begin</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>begin()
</code></pre>

Build eval graph and restoring op.


<h3 id="end"><code>end</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>end(
    session
)
</code></pre>

Runs evaluator for final model.




