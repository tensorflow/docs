page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.tpu.TPUEstimator

## Class `TPUEstimator`

Estimator with TPU support.

Inherits From: [`Estimator`](../../../tf/estimator/Estimator)

### Aliases:

* Class `tf.compat.v1.estimator.tpu.TPUEstimator`
* Class `tf.contrib.tpu.TPUEstimator`
* Class `tf.estimator.tpu.TPUEstimator`



Defined in [`python/estimator/tpu/tpu_estimator.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_estimator.py).

<!-- Placeholder for "Used in" -->

TPUEstimator also supports training on CPU and GPU. You don't need to define
a separate <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>.

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

<a href="../../../tf/estimator/tpu/TPUEstimatorSpec#eval_metrics"><code>TPUEstimatorSpec.eval_metrics</code></a> is a tuple of `metric_fn` and `tensors`, where
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
dataset is not repeated forever, the <a href="../../../tf/data"><code>tf.data</code></a> API will raise an end-of-input
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

`export_saved_model` exports 2 metagraphs, one with <a href="../../../tf/saved_model#SERVING"><code>saved_model.SERVING</code></a>, and
another with <a href="../../../tf/saved_model#SERVING"><code>saved_model.SERVING</code></a> and <a href="../../../tf/saved_model#TPU"><code>saved_model.TPU</code></a> tags. At serving
time, these tags are used to select the appropriate metagraph to load.

Before running the graph on TPU, the TPU system needs to be initialized. If
TensorFlow Serving model-server is used, this is done automatically. If not,
please use `session.run(tpu.initialize_system())`.

There are two versions of the API: ExportSavedModelApiVersion.V1 and V2.

In V1, the exported CPU graph is `model_fn` as it is. The exported TPU graph
wraps <a href="../../../tf/tpu/rewrite"><code>tpu.rewrite()</code></a> and `TPUPartitionedCallOp` around `model_fn` so
`model_fn` is on TPU by default. To place ops on CPU,
<a href="../../../tf/tpu/outside_compilation"><code>tpu.outside_compilation(host_call, logits)</code></a> can be used.

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
`True`, users need to call <a href="../../../tf/tpu/rewrite"><code>tpu.rewrite()</code></a>, `TPUPartitionedCallOp` and/or
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

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    model_fn=None,
    model_dir=None,
    config=None,
    params=None,
    use_tpu=True,
    train_batch_size=None,
    eval_batch_size=None,
    predict_batch_size=None,
    batch_axis=None,
    eval_on_tpu=True,
    export_to_tpu=True,
    export_to_cpu=True,
    warm_start_from=None,
    experimental_export_device_assignment=False,
    embedding_config_spec=None,
    export_saved_model_api_version=ExportSavedModelApiVersion.V1
)
```

Constructs an `TPUEstimator` instance.


#### Args:


* <b>`model_fn`</b>: Model function as required by `Estimator` which returns
  EstimatorSpec or TPUEstimatorSpec. `training_hooks`, 'evaluation_hooks',
  and `prediction_hooks` must not capure any TPU Tensor inside the
  model_fn.
* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
  also be used to load checkpoints from the directory into a estimator to
  continue training a previously saved model. If `None`, the model_dir in
  `config` will be used if set. If both are set, they must be same. If
  both are `None`, a temporary directory will be used.
* <b>`config`</b>: An `tpu_config.RunConfig` configuration object. Cannot be `None`.
* <b>`params`</b>: An optional `dict` of hyper parameters that will be passed into
  `input_fn` and `model_fn`.  Keys are names of parameters, values are
  basic python types. There are reserved keys for `TPUEstimator`,
  including 'batch_size'.
* <b>`use_tpu`</b>: A bool indicating whether TPU support is enabled. Currently, -
  TPU training and evaluation respect this bit, but eval_on_tpu can
  override execution of eval. See below. - Predict still happens on CPU.
* <b>`train_batch_size`</b>: An int representing the global training batch size.
  TPUEstimator transforms this global batch size to a per-shard batch
  size, as params['batch_size'], when calling `input_fn` and `model_fn`.
  Cannot be `None` if `use_tpu` is `True`. Must be divisible by total
  number of replicas.
* <b>`eval_batch_size`</b>: An int representing evaluation batch size. Must be
  divisible by total number of replicas.
* <b>`predict_batch_size`</b>: An int representing the prediction batch size. Must be
  divisible by total number of replicas.
* <b>`batch_axis`</b>: A python tuple of int values describing how each tensor
  produced by the Estimator `input_fn` should be split across the TPU
  compute shards. For example, if your input_fn produced (images, labels)
  where the images tensor is in `HWCN` format, your shard dimensions would
  be [3, 0], where 3 corresponds to the `N` dimension of your images
  Tensor, and 0 corresponds to the dimension along which to split the
  labels to match up with the corresponding images. If None is supplied,
  and per_host_input_for_training is True, batches will be sharded based
  on the major dimension. If tpu_config.per_host_input_for_training is
  False or `PER_HOST_V2`, batch_axis is ignored.
* <b>`eval_on_tpu`</b>: If False, evaluation runs on CPU or GPU. In this case, the
  model_fn must return `EstimatorSpec` when called with `mode` as `EVAL`.
* <b>`export_to_tpu`</b>: If True, `export_saved_model()` exports a metagraph for
  serving on TPU. Note that unsupported export modes such as EVAL will be
  ignored. For those modes, only a CPU model will be exported.
  Currently, export_to_tpu only supports PREDICT.
* <b>`export_to_cpu`</b>: If True, `export_saved_model()` exports a metagraph for
  serving on CPU.
* <b>`warm_start_from`</b>: Optional string filepath to a checkpoint or SavedModel to
  warm-start from, or a <a href="../../../tf/estimator/WarmStartSettings"><code>tf.estimator.WarmStartSettings</code></a> object to fully
  configure warm-starting.  If the string filepath is provided instead of
  a `WarmStartSettings`, then all variables are warm-started, and it is
  assumed that vocabularies and Tensor names are unchanged.
* <b>`experimental_export_device_assignment`</b>: Whether to include the device
  assignment in the exported model. Doing so is useful in case of model
  parallel inference but will tie the exported model to the TPU topology
  used to export the model.
* <b>`embedding_config_spec`</b>: Optional EmbeddingConfigSpec instance
  to support using TPU embedding.
* <b>`export_saved_model_api_version`</b>: ExportSavedModelApiVersion, V1 or V2.
  With V1, `export_saved_model()` adds rewrite() and TPUPartitionedCallOp()
  for user; while in v2, user is expected to add rewrite(),
  TPUPartitionedCallOp() etc in their model_fn.
  A helper function `inference_on_tpu` is provided for V2.
  brn_tpu_estimator.py includes examples for both versions
  i.e. TPUEstimatorExportTest and TPUEstimatorExportV2Test.


#### Raises:


* <b>`ValueError`</b>: `params` has reserved keys already.



## Properties

<h3 id="config"><code>config</code></h3>




<h3 id="model_dir"><code>model_dir</code></h3>




<h3 id="model_fn"><code>model_fn</code></h3>

Returns the `model_fn` which is bound to `self.params`.


#### Returns:

The `model_fn` with following signature:
  `def model_fn(features, labels, mode, config)`


<h3 id="params"><code>params</code></h3>






## Methods

<h3 id="eval_dir"><code>eval_dir</code></h3>

``` python
eval_dir(name=None)
```

Shows the directory name where evaluation metrics are dumped.


#### Args:


* <b>`name`</b>: Name of the evaluation if user needs to run multiple evaluations on
  different data sets, such as on training data vs test data. Metrics for
  different evaluations are saved in separate folders, and appear
  separately in tensorboard.


#### Returns:

A string which is the path of directory contains evaluation metrics.


<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(
    input_fn,
    steps=None,
    hooks=None,
    checkpoint_path=None,
    name=None
)
```




<h3 id="experimental_export_all_saved_models"><code>experimental_export_all_saved_models</code></h3>

``` python
experimental_export_all_saved_models(
    export_dir_base,
    input_receiver_fn_map,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None
)
```

Exports a `SavedModel` with `tf.MetaGraphDefs` for each requested mode.

For each mode passed in via the `input_receiver_fn_map`,
this method builds a new graph by calling the `input_receiver_fn` to obtain
feature and label `Tensor`s. Next, this method calls the `Estimator`'s
`model_fn` in the passed mode to generate the model graph based on
those features and labels, and restores the given checkpoint
(or, lacking that, the most recent checkpoint) into the graph.
Only one of the modes is used for saving variables to the `SavedModel`
(order of preference: <a href="../../../tf/estimator/ModeKeys#TRAIN"><code>tf.estimator.ModeKeys.TRAIN</code></a>,
<a href="../../../tf/estimator/ModeKeys#EVAL"><code>tf.estimator.ModeKeys.EVAL</code></a>, then
<a href="../../../tf/estimator/ModeKeys#PREDICT"><code>tf.estimator.ModeKeys.PREDICT</code></a>), such that up to three
`tf.MetaGraphDefs` are saved with a single set of variables in a single
`SavedModel` directory.

For the variables and `tf.MetaGraphDefs`, a timestamped export directory
below
`export_dir_base`, and writes a `SavedModel` into it containing
the <a href="../../../tf/MetaGraphDef"><code>tf.MetaGraphDef</code></a> for the given mode and its associated signatures.

For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
for each element of the `export_outputs` dict returned from the `model_fn`,
named using the same keys.  One of these keys is always
<a href="../../../tf/saved_model/signature_constants#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`input_receiver_fn_map`</b>: dict of <a href="../../../tf/estimator/ModeKeys"><code>tf.estimator.ModeKeys</code></a> to
  `input_receiver_fn` mappings, where the `input_receiver_fn` is a
  function that takes no arguments and returns the appropriate subclass of
  `InputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if any `input_receiver_fn` is `None`, no `export_outputs`
  are provided, or no checkpoint can be found.

<h3 id="export_saved_model"><code>export_saved_model</code></h3>

``` python
export_saved_model(
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    experimental_mode=ModeKeys.PREDICT
)
```

Exports inference graph as a `SavedModel` into the given dir.

For a detailed guide, see
[Using SavedModel with Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single <a href="../../../tf/MetaGraphDef"><code>tf.MetaGraphDef</code></a> saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
<a href="../../../tf/saved_model/signature_constants#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and returns a
  <a href="../../../tf/estimator/export/ServingInputReceiver"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../tf/estimator/export/TensorServingInputReceiver"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.
* <b>`experimental_mode`</b>: <a href="../../../tf/estimator/ModeKeys"><code>tf.estimator.ModeKeys</code></a> value indicating with mode
  will be exported. Note that this feature is experimental.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.

<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>

``` python
export_savedmodel(
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    strip_default_attrs=False
)
```

Exports inference graph as a `SavedModel` into the given dir. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function has been renamed, use `export_saved_model` instead.

For a detailed guide, see
[Using SavedModel with Estimators](https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

This method builds a new graph by first calling the
`serving_input_receiver_fn` to obtain feature `Tensor`s, and then calling
this `Estimator`'s `model_fn` to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given `export_dir_base`, and writes
a `SavedModel` into it containing a single <a href="../../../tf/MetaGraphDef"><code>tf.MetaGraphDef</code></a> saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the `export_outputs` dict returned from the `model_fn`, named
using
the same keys.  One of these keys is always
<a href="../../../tf/saved_model/signature_constants#DEFAULT_SERVING_SIGNATURE_DEF_KEY"><code>tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY</code></a>,
indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
<a href="../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
receivers provided by
the `serving_input_receiver_fn`.

Extra assets may be written into the `SavedModel` via the `assets_extra`
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

#### Args:


* <b>`export_dir_base`</b>: A string containing a directory in which to create
  timestamped subdirectories containing exported `SavedModel`s.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and returns a
  <a href="../../../tf/estimator/export/ServingInputReceiver"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../tf/estimator/export/TensorServingInputReceiver"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
  removed from the `NodeDef`s. For a detailed guide, see [Stripping
  Default-Valued Attributes](
  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.

<h3 id="get_variable_names"><code>get_variable_names</code></h3>

``` python
get_variable_names()
```

Returns list of all variable names in this model.


#### Returns:

List of names.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="get_variable_value"><code>get_variable_value</code></h3>

``` python
get_variable_value(name)
```

Returns value of the variable given by name.


#### Args:


* <b>`name`</b>: string or a list of string, name of the tensor.


#### Returns:

Numpy array - value of the tensor.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

``` python
latest_checkpoint()
```

Finds the filename of the latest saved checkpoint file in `model_dir`.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was
found.


<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    input_fn,
    predict_keys=None,
    hooks=None,
    checkpoint_path=None,
    yield_single_examples=True
)
```




<h3 id="train"><code>train</code></h3>

``` python
train(
    input_fn,
    hooks=None,
    steps=None,
    max_steps=None,
    saving_listeners=None
)
```






