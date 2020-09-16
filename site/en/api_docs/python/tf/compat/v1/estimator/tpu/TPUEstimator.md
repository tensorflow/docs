description: Estimator with TPU support.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.tpu.TPUEstimator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="eval_dir"/>
<meta itemprop="property" content="evaluate"/>
<meta itemprop="property" content="experimental_export_all_saved_models"/>
<meta itemprop="property" content="export_saved_model"/>
<meta itemprop="property" content="export_savedmodel"/>
<meta itemprop="property" content="get_variable_names"/>
<meta itemprop="property" content="get_variable_value"/>
<meta itemprop="property" content="latest_checkpoint"/>
<meta itemprop="property" content="predict"/>
<meta itemprop="property" content="train"/>
</div>

# tf.compat.v1.estimator.tpu.TPUEstimator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Estimator with TPU support.

Inherits From: [`Estimator`](../../../../../tf/compat/v1/estimator/Estimator.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.tpu.TPUEstimator(
    model_fn=None, model_dir=None, config=None, params=None, use_tpu=(True),
    train_batch_size=None, eval_batch_size=None, predict_batch_size=None,
    batch_axis=None, eval_on_tpu=(True), export_to_tpu=(True), export_to_cpu=(True),
    warm_start_from=None, embedding_config_spec=None,
    export_saved_model_api_version=ExportSavedModelApiVersion.V1
)
</code></pre>



<!-- Placeholder for "Used in" -->

TPUEstimator also supports training on CPU and GPU. You don't need to define
a separate <a href="../../../../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a>.

TPUEstimator handles many of the details of running on TPU devices, such as
replicating inputs and models for each core, and returning to host
periodically to run hooks.

TPUEstimator transforms a global batch size in params to a per-shard batch
size when calling the `input_fn` and `model_fn`. Users should specify
global batch size in constructor, and then get the batch size for each shard
in `input_fn` and `model_fn` by `params['batch_size']`.

- For training, `model_fn` gets per-core batch size; `input_fn` may get
  per-core or per-host batch size depending on `per_host_input_for_training`
  in `TPUConfig` (See docstring for TPUConfig for details).

- For evaluation and prediction, `model_fn` gets per-core batch size and
  `input_fn` get per-host batch size.

Evaluation
==========

`model_fn` should return `TPUEstimatorSpec`, which expects the `eval_metrics`
for TPU evaluation. If eval_on_tpu is False, the evaluation will execute on
CPU or GPU; in this case the following discussion on TPU evaluation does not
apply.

`TPUEstimatorSpec.eval_metrics` is a tuple of `metric_fn` and `tensors`, where
`tensors` could be a list of any nested structure of `Tensor`s (See
`TPUEstimatorSpec` for details).  `metric_fn` takes the `tensors` and returns
a dict from metric string name to the result of calling a metric function,
namely a `(metric_tensor, update_op)` tuple.

One can set `use_tpu` to `False` for testing. All training, evaluation, and
predict will be executed on CPU. `input_fn` and `model_fn` will receive
`train_batch_size` or `eval_batch_size` unmodified as `params['batch_size']`.

#### Current limitations:


--------------------

1. TPU evaluation only works on a single host (one TPU worker) except
   BROADCAST mode.

2. `input_fn` for evaluation should **NOT** raise an end-of-input exception
   (`OutOfRangeError` or `StopIteration`). And all evaluation steps and all
   batches should have the same size.

Example (MNIST):
----------------

```
# The metric Fn which runs on CPU.
def metric_fn(labels, logits):
  predictions = tf.argmax(logits, 1)
  return {
    'accuracy': tf.compat.v1.metrics.precision(
        labels=labels, predictions=predictions),
  }

# Your model Fn which runs on TPU (eval_metrics is list in this example)
def model_fn(features, labels, mode, config, params):
  ...
  logits = ...

  if mode = tf.estimator.ModeKeys.EVAL:
    return tpu_estimator.TPUEstimatorSpec(
        mode=mode,
        loss=loss,
        eval_metrics=(metric_fn, [labels, logits]))

# or specify the eval_metrics tensors as dict.
def model_fn(features, labels, mode, config, params):
  ...
  final_layer_output = ...

  if mode = tf.estimator.ModeKeys.EVAL:
    return tpu_estimator.TPUEstimatorSpec(
        mode=mode,
        loss=loss,
        eval_metrics=(metric_fn, {
            'labels': labels,
            'logits': final_layer_output,
        }))
```

Prediction
==========

Prediction on TPU is an experimental feature to support large batch inference.
It is not designed for latency-critical system. In addition, due to some
usability issues, for prediction with small dataset, CPU `.predict`, i.e.,
creating a new `TPUEstimator` instance with `use_tpu=False`, might be more
convenient.

Note: In contrast to TPU training/evaluation, the `input_fn` for prediction
*should* raise an end-of-input exception (`OutOfRangeError` or
`StopIteration`), which serves as the stopping signal to `TPUEstimator`. To be
precise, the ops created by `input_fn` produce one batch of the data.
The `predict()` API processes one batch at a time. When reaching the end of
the data source, an end-of-input exception should be raised by one of these
operations. The user usually does not need to do this manually. As long as the
dataset is not repeated forever, the <a href="../../../../../tf/data.md"><code>tf.data</code></a> API will raise an end-of-input
exception automatically after the last batch has been produced.

Note: Estimator.predict returns a Python generator. Please consume all the
data from the generator so that TPUEstimator can shutdown the TPU system
properly for user.

#### Current limitations:


--------------------
1. TPU prediction only works on a single host (one TPU worker).

2. `input_fn` must return a `Dataset` instance rather than `features`. In
fact, .train() and .evaluate() also support Dataset as return value.

Example (MNIST):
----------------
```
height = 32
width = 32
total_examples = 100

def predict_input_fn(params):
  batch_size = params['batch_size']

  images = tf.random.uniform(
      [total_examples, height, width, 3], minval=-1, maxval=1)

  dataset = tf.data.Dataset.from_tensor_slices(images)
  dataset = dataset.map(lambda images: {'image': images})

  dataset = dataset.batch(batch_size)
  return dataset

def model_fn(features, labels, params, mode):
   # Generate predictions, called 'output', from features['image']

  if mode == tf.estimator.ModeKeys.PREDICT:
    return tf.contrib.tpu.TPUEstimatorSpec(
        mode=mode,
        predictions={
            'predictions': output,
            'is_padding': features['is_padding']
        })

tpu_est = TPUEstimator(
    model_fn=model_fn,
    ...,
    predict_batch_size=16)

# Fully consume the generator so that TPUEstimator can shutdown the TPU
# system.
for item in tpu_est.predict(input_fn=input_fn):
  # Filter out item if the `is_padding` is 1.
  # Process the 'predictions'
```

Exporting
=========

`export_saved_model` exports 2 metagraphs, one with `saved_model.SERVING`, and
another with `saved_model.SERVING` and `saved_model.TPU` tags. At serving
time, these tags are used to select the appropriate metagraph to load.

Before running the graph on TPU, the TPU system needs to be initialized. If
TensorFlow Serving model-server is used, this is done automatically. If not,
please use `session.run(tpu.initialize_system())`.

There are two versions of the API: ExportSavedModelApiVersion.V1 and V2.

In V1, the exported CPU graph is `model_fn` as it is. The exported TPU graph
wraps `tpu.rewrite()` and `TPUPartitionedCallOp` around `model_fn` so
`model_fn` is on TPU by default. To place ops on CPU,
`tpu.outside_compilation(host_call, logits)` can be used.

#### Example:


----------------

```
def model_fn(features, labels, mode, config, params):
  ...
  logits = ...
  export_outputs = {
    'logits': export_output_lib.PredictOutput(
      {'logits': logits})
  }

  def host_call(logits):
    class_ids = math_ops.argmax(logits)
    classes = string_ops.as_string(class_ids)
    export_outputs['classes'] =
      export_output_lib.ClassificationOutput(classes=classes)

  tpu.outside_compilation(host_call, logits)

  ...
```

In V2, `export_saved_model()` sets up `params['use_tpu']` flag to let the user
know if the code is exporting to TPU (or not). When `params['use_tpu']` is
`True`, users need to call `tpu.rewrite()`, `TPUPartitionedCallOp` and/or
`batch_function()`. Alternatively use `inference_on_tpu()` which is a
convenience wrapper of the three.

```
  def model_fn(features, labels, mode, config, params):
    ...
    # This could be some pre-processing on CPU like calls to input layer with
    # embedding columns.
    x2 = features['x'] * 2

    def computation(input_tensor):
      return layers.dense(
          input_tensor, 1, kernel_initializer=init_ops.zeros_initializer())

    inputs = [x2]
    if params['use_tpu']:
      predictions = array_ops.identity(
          tpu_estimator.inference_on_tpu(computation, inputs,
          num_batch_threads=1, max_batch_size=2, batch_timeout_micros=100),
          name='predictions')
    else:
      predictions = array_ops.identity(
          computation(*inputs), name='predictions')
    key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
    export_outputs = {
        key: export_lib.PredictOutput({'prediction': predictions})
    }
    ...
```

TIP: V2 is recommended as it is more flexible (eg: batching, etc).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`model_fn`
</td>
<td>
Model function as required by `Estimator` which returns
EstimatorSpec or TPUEstimatorSpec. `training_hooks`, 'evaluation_hooks',
and `prediction_hooks` must not capure any TPU Tensor inside the
model_fn.
</td>
</tr><tr>
<td>
`model_dir`
</td>
<td>
Directory to save model parameters, graph and etc. This can
also be used to load checkpoints from the directory into a estimator to
continue training a previously saved model. If `None`, the model_dir in
`config` will be used if set. If both are set, they must be same. If
both are `None`, a temporary directory will be used.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
An `tpu_config.RunConfig` configuration object. Cannot be `None`.
</td>
</tr><tr>
<td>
`params`
</td>
<td>
An optional `dict` of hyper parameters that will be passed into
`input_fn` and `model_fn`.  Keys are names of parameters, values are
basic python types. There are reserved keys for `TPUEstimator`,
including 'batch_size'.
</td>
</tr><tr>
<td>
`use_tpu`
</td>
<td>
A bool indicating whether TPU support is enabled. Currently, -
TPU training and evaluation respect this bit, but eval_on_tpu can
override execution of eval. See below.
</td>
</tr><tr>
<td>
`train_batch_size`
</td>
<td>
An int representing the global training batch size.
TPUEstimator transforms this global batch size to a per-shard batch
size, as params['batch_size'], when calling `input_fn` and `model_fn`.
Cannot be `None` if `use_tpu` is `True`. Must be divisible by total
number of replicas.
</td>
</tr><tr>
<td>
`eval_batch_size`
</td>
<td>
An int representing evaluation batch size. Must be
divisible by total number of replicas.
</td>
</tr><tr>
<td>
`predict_batch_size`
</td>
<td>
An int representing the prediction batch size. Must be
divisible by total number of replicas.
</td>
</tr><tr>
<td>
`batch_axis`
</td>
<td>
A python tuple of int values describing how each tensor
produced by the Estimator `input_fn` should be split across the TPU
compute shards. For example, if your input_fn produced (images, labels)
where the images tensor is in `HWCN` format, your shard dimensions would
be [3, 0], where 3 corresponds to the `N` dimension of your images
Tensor, and 0 corresponds to the dimension along which to split the
labels to match up with the corresponding images. If None is supplied,
and per_host_input_for_training is True, batches will be sharded based
on the major dimension. If tpu_config.per_host_input_for_training is
False or `PER_HOST_V2`, batch_axis is ignored.
</td>
</tr><tr>
<td>
`eval_on_tpu`
</td>
<td>
If False, evaluation runs on CPU or GPU. In this case, the
model_fn must return `EstimatorSpec` when called with `mode` as `EVAL`.
</td>
</tr><tr>
<td>
`export_to_tpu`
</td>
<td>
If True, `export_saved_model()` exports a metagraph for
serving on TPU. Note that unsupported export modes such as EVAL will be
ignored. For those modes, only a CPU model will be exported. Currently,
export_to_tpu only supports PREDICT.
</td>
</tr><tr>
<td>
`export_to_cpu`
</td>
<td>
If True, `export_saved_model()` exports a metagraph for
serving on CPU.
</td>
</tr><tr>
<td>
`warm_start_from`
</td>
<td>
Optional string filepath to a checkpoint or SavedModel to
warm-start from, or a <a href="../../../../../tf/estimator/WarmStartSettings.md"><code>tf.estimator.WarmStartSettings</code></a> object to fully
configure warm-starting.  If the string filepath is provided instead of
a `WarmStartSettings`, then all variables are warm-started, and it is
assumed that vocabularies and Tensor names are unchanged.
</td>
</tr><tr>
<td>
`embedding_config_spec`
</td>
<td>
Optional EmbeddingConfigSpec instance to support
using TPU embedding.
</td>
</tr><tr>
<td>
`export_saved_model_api_version`
</td>
<td>
ExportSavedModelApiVersion, V1 or V2. With
V1, `export_saved_model()` adds rewrite() and TPUPartitionedCallOp() for
user; while in v2, user is expected to add rewrite(),
TPUPartitionedCallOp() etc in their model_fn. A helper function
`inference_on_tpu` is provided for V2. brn_tpu_estimator.py includes
examples for both versions i.e. TPUEstimatorExportTest and
TPUEstimatorExportV2Test.
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
`params` has reserved keys already.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`config`
</td>
<td>

</td>
</tr><tr>
<td>
`model_dir`
</td>
<td>

</td>
</tr><tr>
<td>
`model_fn`
</td>
<td>
Returns the `model_fn` which is bound to `self.params`.
</td>
</tr><tr>
<td>
`params`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="eval_dir"><code>eval_dir</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>eval_dir(
    name=None
)
</code></pre>

Shows the directory name where evaluation metrics are dumped.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
Name of the evaluation if user needs to run multiple evaluations on
different data sets, such as on training data vs test data. Metrics for
different evaluations are saved in separate folders, and appear
separately in tensorboard.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A string which is the path of directory contains evaluation metrics.
</td>
</tr>

</table>



<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>evaluate(
    input_fn, steps=None, hooks=None, checkpoint_path=None, name=None
)
</code></pre>

Evaluates the model given evaluation data `input_fn`.

For each step, calls `input_fn`, which returns one batch of data.
Evaluates until:
- `steps` batches are processed, or
- `input_fn` raises an end-of-input exception (<a href="../../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>
or
`StopIteration`).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that constructs the input data for evaluation. See
[Premade Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The
function should construct and return one of the following:  * A
<a href="../../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a tuple
`(features, labels)` with same constraints as below. * A tuple
`(features, labels)`: Where `features` is a <a href="../../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or a dictionary
of string feature name to `Tensor` and `labels` is a `Tensor` or a
dictionary of string label name to `Tensor`. Both `features` and
`labels` are consumed by `model_fn`. They should satisfy the
expectation of `model_fn` from inputs.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Number of steps for which to evaluate model. If `None`, evaluates
until `input_fn` raises an end-of-input exception.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
List of `tf.train.SessionRunHook` subclass instances. Used for
callbacks inside the evaluation call.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
Path of a specific checkpoint to evaluate. If `None`, the
latest checkpoint in `model_dir` is used.  If there are no checkpoints
in `model_dir`, evaluation is run with newly initialized `Variables`
instead of ones restored from checkpoint.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name of the evaluation if user needs to run multiple evaluations on
different data sets, such as on training data vs test data. Metrics for
different evaluations are saved in separate folders, and appear
separately in tensorboard.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dict containing the evaluation metrics specified in `model_fn` keyed by
name, as well as an entry `global_step` which contains the value of the
global step for which this evaluation was performed. For canned
estimators, the dict contains the `loss` (mean loss per mini-batch) and
the `average_loss` (mean loss per sample). Canned classifiers also return
the `accuracy`. Canned regressors also return the `label/mean` and the
`prediction/mean`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If `steps <= 0`.
</td>
</tr>
</table>



<h3 id="experimental_export_all_saved_models"><code>experimental_export_all_saved_models</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_export_all_saved_models(
    export_dir_base, input_receiver_fn_map, assets_extra=None, as_text=(False),
    checkpoint_path=None
)
</code></pre>

Exports a `SavedModel` with `tf.MetaGraphDefs` for each requested mode.

For each mode passed in via the `input_receiver_fn_map`,
this method builds a new graph by calling the `input_receiver_fn` to obtain
feature and label `Tensor`s. Next, this method calls the `Estimator`'s
`model_fn` in the passed mode to generate the model graph based on
those features and labels, and restores the given checkpoint
(or, lacking that, the most recent checkpoint) into the graph.
Only one of the modes is used for saving variables to the `SavedModel`
(order of preference: <a href="../../../../../tf/estimator/ModeKeys.md#TRAIN"><code>tf.estimator.ModeKeys.TRAIN</code></a>,
<a href="../../../../../tf/estimator/ModeKeys.md#EVAL"><code>tf.estimator.ModeKeys.EVAL</code></a>, then
<a href="../../../../../tf/estimator/ModeKeys.md#PREDICT"><code>tf.estimator.ModeKeys.PREDICT</code></a>), such that up to three
`tf.MetaGraphDefs` are saved with a single set of variables in a single
`SavedModel` directory.

For the variables and `tf.MetaGraphDefs`, a timestamped export directory
below
`export_dir_base`, and writes a `SavedModel` into it containing
the `tf.MetaGraphDef` for the given mode and its associated signatures.

For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
for each element of the `export_outputs` dict returned from the `model_fn`,
named using the same keys.  One of these keys is always
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

For training and evaluation, the `train_op` is stored in an extra
collection,
and loss, metrics, and predictions are included in a `SignatureDef` for the
mode in question.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_dir_base`
</td>
<td>
A string containing a directory in which to create
timestamped subdirectories containing exported `SavedModel`s.
</td>
</tr><tr>
<td>
`input_receiver_fn_map`
</td>
<td>
dict of <a href="../../../../../tf/estimator/ModeKeys.md"><code>tf.estimator.ModeKeys</code></a> to
`input_receiver_fn` mappings, where the `input_receiver_fn` is a
function that takes no arguments and returns the appropriate subclass of
`InputReceiver`.
</td>
</tr><tr>
<td>
`assets_extra`
</td>
<td>
A dict specifying how to populate the assets.extra directory
within the exported `SavedModel`, or `None` if no extra assets are
needed.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
whether to write the `SavedModel` proto in text format.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.  If `None` (the default),
the most recent checkpoint found within the model directory is chosen.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to the exported directory as a bytes object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if any `input_receiver_fn` is `None`, no `export_outputs`
are provided, or no checkpoint can be found.
</td>
</tr>
</table>



<h3 id="export_saved_model"><code>export_saved_model</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>export_saved_model(
    export_dir_base, serving_input_receiver_fn, assets_extra=None, as_text=(False),
    checkpoint_path=None, experimental_mode=ModeKeys.PREDICT
)
</code></pre>

Exports inference graph as a `SavedModel` into the given dir.

For a detailed guide, see
[Using SavedModel with
Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single `tf.MetaGraphDef` saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

The experimental_mode parameter can be used to export a single
train/eval/predict graph as a `SavedModel`.
See `experimental_export_all_saved_models` for full docs.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_dir_base`
</td>
<td>
A string containing a directory in which to create
timestamped subdirectories containing exported `SavedModel`s.
</td>
</tr><tr>
<td>
`serving_input_receiver_fn`
</td>
<td>
A function that takes no argument and returns a
<a href="../../../../../tf/estimator/export/ServingInputReceiver.md"><code>tf.estimator.export.ServingInputReceiver</code></a> or
<a href="../../../../../tf/estimator/export/TensorServingInputReceiver.md"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
</td>
</tr><tr>
<td>
`assets_extra`
</td>
<td>
A dict specifying how to populate the assets.extra directory
within the exported `SavedModel`, or `None` if no extra assets are
needed.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
whether to write the `SavedModel` proto in text format.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.  If `None` (the default),
the most recent checkpoint found within the model directory is chosen.
</td>
</tr><tr>
<td>
`experimental_mode`
</td>
<td>
<a href="../../../../../tf/estimator/ModeKeys.md"><code>tf.estimator.ModeKeys</code></a> value indicating with mode will
be exported. Note that this feature is experimental.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to the exported directory as a bytes object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.
</td>
</tr>
</table>



<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>export_savedmodel(
    export_dir_base, serving_input_receiver_fn, assets_extra=None, as_text=(False),
    checkpoint_path=None, strip_default_attrs=(False)
)
</code></pre>

Exports inference graph as a `SavedModel` into the given dir. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function has been renamed, use `export_saved_model` instead.

For a detailed guide, see
[Using SavedModel with
Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single `tf.MetaGraphDef` saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../../../tf/estimator/export/ExportOutput.md"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_dir_base`
</td>
<td>
A string containing a directory in which to create
timestamped subdirectories containing exported `SavedModel`s.
</td>
</tr><tr>
<td>
`serving_input_receiver_fn`
</td>
<td>
A function that takes no argument and returns a
<a href="../../../../../tf/estimator/export/ServingInputReceiver.md"><code>tf.estimator.export.ServingInputReceiver</code></a> or
<a href="../../../../../tf/estimator/export/TensorServingInputReceiver.md"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
</td>
</tr><tr>
<td>
`assets_extra`
</td>
<td>
A dict specifying how to populate the assets.extra directory
within the exported `SavedModel`, or `None` if no extra assets are
needed.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
whether to write the `SavedModel` proto in text format.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.  If `None` (the default),
the most recent checkpoint found within the model directory is chosen.
</td>
</tr><tr>
<td>
`strip_default_attrs`
</td>
<td>
Boolean. If `True`, default-valued attributes will be
removed from the `NodeDef`s. For a detailed guide, see [Stripping
Default-Valued Attributes](
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to the exported directory as a bytes object.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.
</td>
</tr>
</table>



<h3 id="get_variable_names"><code>get_variable_names</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_variable_names()
</code></pre>

Returns list of all variable names in this model.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
List of names.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the `Estimator` has not produced a checkpoint yet.
</td>
</tr>
</table>



<h3 id="get_variable_value"><code>get_variable_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_variable_value(
    name
)
</code></pre>

Returns value of the variable given by name.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
string or a list of string, name of the tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Numpy array - value of the tensor.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the `Estimator` has not produced a checkpoint yet.
</td>
</tr>
</table>



<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>latest_checkpoint()
</code></pre>

Finds the filename of the latest saved checkpoint file in `model_dir`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The full path to the latest checkpoint or `None` if no checkpoint was
found.
</td>
</tr>

</table>



<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>predict(
    input_fn, predict_keys=None, hooks=None, checkpoint_path=None,
    yield_single_examples=(True)
)
</code></pre>

Yields predictions for given features.

Please note that interleaving two predict outputs does not work. See:
[issue/20506](
https://github.com/tensorflow/tensorflow/issues/20506#issuecomment-422208517)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that constructs the features. Prediction continues
until `input_fn` raises an end-of-input exception
(<a href="../../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> or `StopIteration`). See [Premade
Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The function should construct and return one of
the following:
* <a href="../../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object -- Outputs of `Dataset` object must have
same constraints as below.
* features -- A <a href="../../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or a dictionary of string feature name to
`Tensor`. features are consumed by `model_fn`. They should satisfy
the expectation of `model_fn` from inputs. * A tuple, in which case
the first item is extracted as features.
</td>
</tr><tr>
<td>
`predict_keys`
</td>
<td>
list of `str`, name of the keys to predict. It is used if
the <a href="../../../../../tf/estimator/EstimatorSpec.md#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is a `dict`. If
`predict_keys` is used then rest of the predictions will be filtered
from the dictionary. If `None`, returns all.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
List of `tf.train.SessionRunHook` subclass instances. Used for
callbacks inside the prediction call.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
Path of a specific checkpoint to predict. If `None`, the
latest checkpoint in `model_dir` is used.  If there are no checkpoints
in `model_dir`, prediction is run with newly initialized `Variables`
instead of ones restored from checkpoint.
</td>
</tr><tr>
<td>
`yield_single_examples`
</td>
<td>
If `False`, yields the whole batch as returned by
the `model_fn` instead of decomposing the batch into individual
elements. This is useful if `model_fn` returns some tensors whose first
dimension is not equal to the batch size.
</td>
</tr>
</table>



#### Yields:

Evaluated values of `predictions` tensors.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If batch length of predictions is not the same and
`yield_single_examples` is `True`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If there is a conflict between `predict_keys` and
`predictions`. For example if `predict_keys` is not `None` but
<a href="../../../../../tf/estimator/EstimatorSpec.md#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is not a `dict`.
</td>
</tr>
</table>



<h3 id="train"><code>train</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>train(
    input_fn, hooks=None, steps=None, max_steps=None, saving_listeners=None
)
</code></pre>

Trains a model given training data `input_fn`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function that provides input data for training as minibatches.
See [Premade Estimators](
https://tensorflow.org/guide/premade_estimators#create_input_functions)
for more information. The function should construct and return one of
the following:
* A <a href="../../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a
tuple `(features, labels)` with same constraints as below.
* A tuple `(features, labels)`: Where `features` is a <a href="../../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or a
dictionary of string feature name to `Tensor` and `labels` is a
`Tensor` or a dictionary of string label name to `Tensor`. Both
`features` and `labels` are consumed by `model_fn`. They should
satisfy the expectation of `model_fn` from inputs.
</td>
</tr><tr>
<td>
`hooks`
</td>
<td>
List of `tf.train.SessionRunHook` subclass instances. Used for
callbacks inside the training loop.
</td>
</tr><tr>
<td>
`steps`
</td>
<td>
Number of steps for which to train the model. If `None`, train
forever or train until `input_fn` generates the `tf.errors.OutOfRange`
error or `StopIteration` exception. `steps` works incrementally. If you
call two times `train(steps=10)` then training occurs in total 20 steps.
If `OutOfRange` or `StopIteration` occurs in the middle, training stops
before 20 steps. If you don't want to have incremental behavior please
set `max_steps` instead. If set, `max_steps` must be `None`.
</td>
</tr><tr>
<td>
`max_steps`
</td>
<td>
Number of total steps for which to train model. If `None`,
train forever or train until `input_fn` generates the
`tf.errors.OutOfRange` error or `StopIteration` exception. If set,
`steps` must be `None`. If `OutOfRange` or `StopIteration` occurs in the
middle, training stops before `max_steps` steps. Two calls to
`train(steps=100)` means 200 training iterations. On the other hand, two
calls to `train(max_steps=100)` means that the second call will not do
any iteration since first call did all 100 steps.
</td>
</tr><tr>
<td>
`saving_listeners`
</td>
<td>
list of `CheckpointSaverListener` objects. Used for
callbacks that run immediately before or after checkpoint savings.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
`self`, for chaining.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If both `steps` and `max_steps` are not `None`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If either `steps` or `max_steps <= 0`.
</td>
</tr>
</table>





