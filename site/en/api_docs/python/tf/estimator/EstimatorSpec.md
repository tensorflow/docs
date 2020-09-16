description: Ops and objects returned from a model_fn and passed to an Estimator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.EstimatorSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="eval_metric_ops"/>
<meta itemprop="property" content="evaluation_hooks"/>
<meta itemprop="property" content="export_outputs"/>
<meta itemprop="property" content="loss"/>
<meta itemprop="property" content="mode"/>
<meta itemprop="property" content="prediction_hooks"/>
<meta itemprop="property" content="predictions"/>
<meta itemprop="property" content="scaffold"/>
<meta itemprop="property" content="train_op"/>
<meta itemprop="property" content="training_chief_hooks"/>
<meta itemprop="property" content="training_hooks"/>
</div>

# tf.estimator.EstimatorSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/model_fn.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Ops and objects returned from a `model_fn` and passed to an `Estimator`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.EstimatorSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.EstimatorSpec(
    mode, predictions=None, loss=None, train_op=None, eval_metric_ops=None,
    export_outputs=None, training_chief_hooks=None, training_hooks=None,
    scaffold=None, evaluation_hooks=None, prediction_hooks=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`EstimatorSpec` fully defines the model to be run by an `Estimator`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`mode`
</td>
<td>
A `ModeKeys`. Specifies if this is training, evaluation or
prediction.
</td>
</tr><tr>
<td>
`predictions`
</td>
<td>
Predictions `Tensor` or dict of `Tensor`.
</td>
</tr><tr>
<td>
`loss`
</td>
<td>
Training loss `Tensor`. Must be either scalar, or with shape `[1]`.
</td>
</tr><tr>
<td>
`train_op`
</td>
<td>
Op for the training step.
</td>
</tr><tr>
<td>
`eval_metric_ops`
</td>
<td>
Dict of metric results keyed by name.
The values of the dict can be one of the following: (1) instance of
`Metric` class. (2) Results of calling a metric function, namely a
`(metric_tensor, update_op)` tuple. `metric_tensor` should be
evaluated without any impact on state (typically is a pure computation
results based on variables.). For example, it should not trigger the
`update_op` or requires any input fetching.
</td>
</tr><tr>
<td>
`export_outputs`
</td>
<td>
Describes the output signatures to be exported to
`SavedModel` and used during serving.
A dict `{name: output}` where:
* name: An arbitrary name for this output.
* output: an `ExportOutput` object such as `ClassificationOutput`,
`RegressionOutput`, or `PredictOutput`. Single-headed models only need
to specify one entry in this dictionary. Multi-headed models should
specify one entry for each head, one of which must be named using
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`.
If no entry is provided, a default `PredictOutput` mapping to
`predictions` will be created.
</td>
</tr><tr>
<td>
`training_chief_hooks`
</td>
<td>
Iterable of `tf.train.SessionRunHook` objects to run
on the chief worker during training.
</td>
</tr><tr>
<td>
`training_hooks`
</td>
<td>
Iterable of `tf.train.SessionRunHook` objects to run on
all workers during training.
</td>
</tr><tr>
<td>
`scaffold`
</td>
<td>
A `tf.train.Scaffold` object that can be used to set
initialization, saver, and more to be used in training.
</td>
</tr><tr>
<td>
`evaluation_hooks`
</td>
<td>
Iterable of `tf.train.SessionRunHook` objects to run
during evaluation.
</td>
</tr><tr>
<td>
`prediction_hooks`
</td>
<td>
Iterable of `tf.train.SessionRunHook` objects to run
during predictions.
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
If validation fails.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If any of the arguments is not the expected type.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`mode`
</td>
<td>

</td>
</tr><tr>
<td>
`predictions`
</td>
<td>

</td>
</tr><tr>
<td>
`loss`
</td>
<td>

</td>
</tr><tr>
<td>
`train_op`
</td>
<td>

</td>
</tr><tr>
<td>
`eval_metric_ops`
</td>
<td>

</td>
</tr><tr>
<td>
`export_outputs`
</td>
<td>

</td>
</tr><tr>
<td>
`training_chief_hooks`
</td>
<td>

</td>
</tr><tr>
<td>
`training_hooks`
</td>
<td>

</td>
</tr><tr>
<td>
`scaffold`
</td>
<td>

</td>
</tr><tr>
<td>
`evaluation_hooks`
</td>
<td>

</td>
</tr><tr>
<td>
`prediction_hooks`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `eval_metric_ops` <a id="eval_metric_ops"></a>
* `evaluation_hooks` <a id="evaluation_hooks"></a>
* `export_outputs` <a id="export_outputs"></a>
* `loss` <a id="loss"></a>
* `mode` <a id="mode"></a>
* `prediction_hooks` <a id="prediction_hooks"></a>
* `predictions` <a id="predictions"></a>
* `scaffold` <a id="scaffold"></a>
* `train_op` <a id="train_op"></a>
* `training_chief_hooks` <a id="training_chief_hooks"></a>
* `training_hooks` <a id="training_hooks"></a>
