description: Ops and objects returned from a model_fn and passed to TPUEstimator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.tpu.TPUEstimatorSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="as_estimator_spec"/>
<meta itemprop="property" content="eval_metrics"/>
<meta itemprop="property" content="evaluation_hooks"/>
<meta itemprop="property" content="export_outputs"/>
<meta itemprop="property" content="host_call"/>
<meta itemprop="property" content="loss"/>
<meta itemprop="property" content="mode"/>
<meta itemprop="property" content="prediction_hooks"/>
<meta itemprop="property" content="predictions"/>
<meta itemprop="property" content="scaffold_fn"/>
<meta itemprop="property" content="train_op"/>
<meta itemprop="property" content="training_hooks"/>
</div>

# tf.compat.v1.estimator.tpu.TPUEstimatorSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Ops and objects returned from a `model_fn` and passed to `TPUEstimator`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.tpu.TPUEstimatorSpec(
    mode, predictions=None, loss=None, train_op=None, eval_metrics=None,
    export_outputs=None, scaffold_fn=None, host_call=None, training_hooks=None,
    evaluation_hooks=None, prediction_hooks=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See `EstimatorSpec` for `mode`, `predictions`, `loss`, `train_op`, and
`export_outputs`.

For evaluation, `eval_metrics `is a tuple of `metric_fn` and `tensors`, where
`metric_fn` runs on CPU to generate metrics and `tensors` represents the
`Tensor`s transferred from TPU system to CPU host and passed to `metric_fn`.
To be precise, TPU evaluation expects a slightly different signature from the
<a href="../../../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a>. While `EstimatorSpec.eval_metric_ops` expects a
dict, `TPUEstimatorSpec.eval_metrics` is a tuple of `metric_fn` and `tensors`.
The `tensors` could be a list of `Tensor`s or dict of names to `Tensor`s. The
`tensors` usually specify the model logits, which are transferred back from
TPU system to CPU host. All tensors must have be batch-major, i.e., the batch
size is the first dimension. Once all tensors are available at CPU host from
all shards, they are concatenated (on CPU) and passed as positional arguments
to the `metric_fn` if `tensors` is list or keyword arguments if `tensors` is
a dict. `metric_fn` takes the `tensors` and returns a dict from metric string
name to the result of calling a metric function, namely a `(metric_tensor,
update_op)` tuple. See `TPUEstimator` for MNIST example how to specify the
`eval_metrics`.

`scaffold_fn` is a function running on CPU to generate the `Scaffold`. This
function should not capture any Tensors in `model_fn`.

`host_call` is a tuple of a `function` and a list or dictionary of `tensors`
to pass to that function and returns a list of Tensors. `host_call` currently
works for train() and evaluate(). The Tensors returned by the function is
executed on the CPU on every step, so there is communication overhead when
sending tensors from TPU to CPU. To reduce the overhead, try reducing the
size of the tensors. The `tensors` are concatenated along their major (batch)
dimension, and so must be >= rank 1. The `host_call` is useful for writing
summaries with `tf.contrib.summary.create_file_writer`.



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
`eval_metrics`
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
`scaffold_fn`
</td>
<td>

</td>
</tr><tr>
<td>
`host_call`
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



## Methods

<h3 id="as_estimator_spec"><code>as_estimator_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_estimator_spec()
</code></pre>

Creates an equivalent `EstimatorSpec` used by CPU train/eval.




## Class Variables

* `eval_metrics` <a id="eval_metrics"></a>
* `evaluation_hooks` <a id="evaluation_hooks"></a>
* `export_outputs` <a id="export_outputs"></a>
* `host_call` <a id="host_call"></a>
* `loss` <a id="loss"></a>
* `mode` <a id="mode"></a>
* `prediction_hooks` <a id="prediction_hooks"></a>
* `predictions` <a id="predictions"></a>
* `scaffold_fn` <a id="scaffold_fn"></a>
* `train_op` <a id="train_op"></a>
* `training_hooks` <a id="training_hooks"></a>
