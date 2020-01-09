page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.ModelFnOps


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/model_fn.py#L70-L307">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ModelFnOps`

Ops returned from a model_fn.



<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.tensorflow.org/code/tensorflow/contrib/learn/README.md)
for general migration instructions.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/model_fn.py#L83-L210">View source</a>

``` python
@staticmethod
__new__(
    cls,
    mode,
    predictions=None,
    loss=None,
    train_op=None,
    eval_metric_ops=None,
    output_alternatives=None,
    training_chief_hooks=None,
    training_hooks=None,
    scaffold=None
)
```

Creates a validated `ModelFnOps` instance. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
When switching to tf.estimator.Estimator, use tf.estimator.EstimatorSpec. You can use the `estimator_spec` method to create an equivalent one.

For a multi-headed model, the predictions dict here will contain the outputs
of all of the heads.  However: at serving time, requests will be made
specifically for one or more heads, and the RPCs used for these requests may
differ by problem type (i.e., regression, classification, other).  The
purpose of the output_alternatives dict is to aid in exporting a SavedModel
from which such head-specific queries can be served.  These
output_alternatives will be combined with input_alternatives (see
`saved_model_export_utils`) to produce a set of `SignatureDef`s specifying
the valid requests that can be served from this model.

For a single-headed model, it is still adviseable to provide
output_alternatives with a single entry, because this is how the problem
type is communicated for export and serving.  If output_alternatives is not
given, the resulting SavedModel will support only one head of unspecified
type.

#### Args:


* <b>`mode`</b>: One of `ModeKeys`. Specifies if this training, evaluation or
  prediction.
* <b>`predictions`</b>: Predictions `Tensor` or dict of `Tensor`.
* <b>`loss`</b>: Training loss `Tensor`.
* <b>`train_op`</b>: Op for the training step.
* <b>`eval_metric_ops`</b>: Dict of metric results keyed by name. The values of the
  dict are the results of calling a metric function, such as `Tensor`.
* <b>`output_alternatives`</b>: a dict of
  `{submodel_name: (problem_type, {tensor_name: Tensor})}`, where
  `submodel_name` is a submodel identifier that should be consistent
  across the pipeline (here likely taken from the name of each `Head`,
  for models that use them), `problem_type` is a `ProblemType`,
  `tensor_name` is a symbolic name for an output Tensor possibly but not
  necessarily taken from `PredictionKey`, and `Tensor` is the
  corresponding output Tensor itself.
* <b>`training_chief_hooks`</b>: A list of `SessionRunHook` objects that will be
  run on the chief worker during training.
* <b>`training_hooks`</b>: A list of `SessionRunHook` objects that will be run on
  all workers during training.
* <b>`scaffold`</b>: A <a href="../../../tf/train/Scaffold"><code>tf.compat.v1.train.Scaffold</code></a> object that can be used to set
  initialization, saver, and more to be used in training.


#### Returns:

A validated `ModelFnOps` object.



#### Raises:


* <b>`ValueError`</b>: If validation fails.



## Properties

<h3 id="predictions"><code>predictions</code></h3>




<h3 id="loss"><code>loss</code></h3>




<h3 id="train_op"><code>train_op</code></h3>




<h3 id="eval_metric_ops"><code>eval_metric_ops</code></h3>




<h3 id="output_alternatives"><code>output_alternatives</code></h3>




<h3 id="training_chief_hooks"><code>training_chief_hooks</code></h3>




<h3 id="training_hooks"><code>training_hooks</code></h3>




<h3 id="scaffold"><code>scaffold</code></h3>




<h3 id="mode"><code>mode</code></h3>






## Methods

<h3 id="estimator_spec"><code>estimator_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/model_fn.py#L212-L307">View source</a>

``` python
estimator_spec(default_serving_output_alternative_key=None)
```

Creates an equivalent `EstimatorSpec`.


#### Args:


* <b>`default_serving_output_alternative_key`</b>: Required for multiple heads. If
  you have multiple entries in `output_alternatives` dict (comparable to
  multiple heads), `EstimatorSpec` requires a default head that will be
  used if a Servo request does not explicitly mention which head to infer
  on. Pass the key of the output alternative here that you want to
  designate as default. A separate ExportOutpout for this default head
  will be added to the export_outputs dict with the special key
  saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY, unless there is
  already an enry in output_alternatives with this special key.


#### Returns:

Instance of `EstimatorSpec` that is equivalent to this `ModelFnOps`



#### Raises:


* <b>`ValueError`</b>: If problem type is unknown.
