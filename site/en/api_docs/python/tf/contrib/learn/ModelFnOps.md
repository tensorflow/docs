

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.ModelFnOps

## Class `ModelFnOps`





Defined in [`tensorflow/contrib/learn/python/learn/estimators/model_fn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/learn/python/learn/estimators/model_fn.py).

See the guide: [Learn (contrib) > Estimators](../../../../../api_guides/python/contrib.learn#Estimators)

Ops returned from a model_fn.

## Properties

<h3 id="eval_metric_ops"><code>eval_metric_ops</code></h3>

Alias for field number 3

<h3 id="loss"><code>loss</code></h3>

Alias for field number 1

<h3 id="mode"><code>mode</code></h3>

Alias for field number 8

<h3 id="output_alternatives"><code>output_alternatives</code></h3>

Alias for field number 4

<h3 id="predictions"><code>predictions</code></h3>

Alias for field number 0

<h3 id="scaffold"><code>scaffold</code></h3>

Alias for field number 7

<h3 id="train_op"><code>train_op</code></h3>

Alias for field number 2

<h3 id="training_chief_hooks"><code>training_chief_hooks</code></h3>

Alias for field number 5

<h3 id="training_hooks"><code>training_hooks</code></h3>

Alias for field number 6



## Methods

<h3 id="__new__"><code>__new__</code></h3>

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

Creates a validated `ModelFnOps` instance.

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
* <b>`scaffold`</b>: A `tf.train.Scaffold` object that can be used to set
    initialization, saver, and more to be used in training.


#### Returns:

A validated `ModelFnOps` object.


#### Raises:

* <b>`ValueError`</b>: If validation fails.

<h3 id="estimator_spec"><code>estimator_spec</code></h3>

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
    wil be added to the export_outputs dict with the special key
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY, unless there is
    already an enry in output_alternatives with this special key.


#### Returns:

Instance of `EstimatorSpec` that is equivalent to this `ModelFnOps`


#### Raises:

* <b>`ValueError`</b>: If problem type is unknown.



