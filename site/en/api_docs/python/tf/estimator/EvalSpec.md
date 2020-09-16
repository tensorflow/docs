description: Configuration for the "eval" part for the train_and_evaluate call.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.EvalSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="exporters"/>
<meta itemprop="property" content="hooks"/>
<meta itemprop="property" content="input_fn"/>
<meta itemprop="property" content="name"/>
<meta itemprop="property" content="start_delay_secs"/>
<meta itemprop="property" content="steps"/>
<meta itemprop="property" content="throttle_secs"/>
</div>

# tf.estimator.EvalSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/training.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for the "eval" part for the `train_and_evaluate` call.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.EvalSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.EvalSpec(
    input_fn, steps=100, name=None, hooks=None, exporters=None,
    start_delay_secs=120, throttle_secs=600
)
</code></pre>



<!-- Placeholder for "Used in" -->

`EvalSpec` combines details of evaluation of the trained model as well as its
export. Evaluation consists of computing metrics to judge the performance of
the trained model.  Export writes out the trained model on to external
storage.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that constructs the input data for evaluation. See
[Premade Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The function should construct and return one of
the following:
* A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
tuple (features, labels) with same constraints as below.
* A tuple (features, labels): Where features is a `Tensor` or a
dictionary of string feature name to `Tensor` and labels is a
`Tensor` or a dictionary of string label name to `Tensor`.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Int. Positive number of steps for which to evaluate model. If
`None`, evaluates until `input_fn` raises an end-of-input exception. See
<a href="../../tf/compat/v1/estimator/Estimator.md#evaluate"><code>Estimator.evaluate</code></a> for details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String. Name of the evaluation if user needs to run multiple
evaluations on different data sets. Metrics for different evaluations
are saved in separate folders, and appear separately in tensorboard.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
Iterable of `tf.train.SessionRunHook` objects to run during
evaluation.
</td>
</tr><tr>
<td>
`exporters`
</td>
<td>
Iterable of `Exporter`s, or a single one, or `None`.
`exporters` will be invoked after each evaluation.
</td>
</tr><tr>
<td>
`start_delay_secs`
</td>
<td>
Int. Start evaluating after waiting for this many
seconds.
</td>
</tr><tr>
<td>
`throttle_secs`
</td>
<td>
Int. Do not re-evaluate unless the last evaluation was
started at least this many seconds ago. Of course, evaluation does not
occur if no new checkpoints are available, hence, this is the minimum.
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
If any of the input arguments is invalid.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If any of the arguments is not of the expected type.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`input_fn`
</td>
<td>

</td>
</tr><tr>
<td>
`steps`
</td>
<td>

</td>
</tr><tr>
<td>
`name`
</td>
<td>

</td>
</tr><tr>
<td>
`hooks`
</td>
<td>

</td>
</tr><tr>
<td>
`exporters`
</td>
<td>

</td>
</tr><tr>
<td>
`start_delay_secs`
</td>
<td>

</td>
</tr><tr>
<td>
`throttle_secs`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `exporters` <a id="exporters"></a>
* `hooks` <a id="hooks"></a>
* `input_fn` <a id="input_fn"></a>
* `name` <a id="name"></a>
* `start_delay_secs` <a id="start_delay_secs"></a>
* `steps` <a id="steps"></a>
* `throttle_secs` <a id="throttle_secs"></a>
