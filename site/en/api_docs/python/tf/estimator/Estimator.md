page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.Estimator

## Class `Estimator`





Defined in [`tensorflow/python/estimator/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/estimator/estimator.py).

See the guide: [Regression Examples](../../../../api_guides/python/regression_examples)

Estimator class to train and evaluate TensorFlow models.

The `Estimator` object wraps a model which is specified by a `model_fn`,
which, given inputs and a number of other parameters, returns the ops
necessary to perform training, evaluation, or predictions.

All outputs (checkpoints, event files, etc.) are written to `model_dir`, or a
subdirectory thereof. If `model_dir` is not set, a temporary directory is
used.

The `config` argument can be passed `RunConfig` object containing information
about the execution environment. It is passed on to the `model_fn`, if the
`model_fn` has a parameter named "config" (and input functions in the same
manner). If the `config` parameter is not passed, it is instantiated by the
`Estimator`. Not passing config means that defaults useful for local execution
are used. `Estimator` makes config available to the model (for instance, to
allow specialization based on the number of workers available), and also uses
some of its fields to control internals, especially regarding checkpointing.

The `params` argument contains hyperparameters. It is passed to the
`model_fn`, if the `model_fn` has a parameter named "params", and to the input
functions in the same manner. `Estimator` only passes params along, it does
not inspect it. The structure of `params` is therefore entirely up to the
developer.

None of `Estimator`'s methods can be overridden in subclasses (its
constructor enforces this). Subclasses should use `model_fn` to configure
the base class, and may add methods implementing specialized functionality.

@compatbility(eager)
Calling methods of `Estimator` will work while eager execution is enabled.
However, the `model_fn` and `input_fn` is not executed eagerly, `Estimator`
will switch to graph model before calling all user-provided functions (incl.
hooks), so their code has to be compatible with graph mode execution. Note
that `input_fn` code using <a href="../../tf/data"><code>tf.data</code></a> generally works in both graph and eager
modes.
@end_compatibility

## Properties

<h3 id="config"><code>config</code></h3>



<h3 id="model_dir"><code>model_dir</code></h3>



<h3 id="model_fn"><code>model_fn</code></h3>

Returns the model_fn which is bound to self.params.

#### Returns:

The model_fn with following signature:
  `def model_fn(features, labels, mode, config)`

<h3 id="params"><code>params</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    model_fn,
    model_dir=None,
    config=None,
    params=None,
    warm_start_from=None
)
```

Constructs an `Estimator` instance.

See <a href="../../../../guide/estimators">Estimators</a> for more information. To warm-start an `Estimator`:

```python
estimator = tf.estimator.DNNClassifier(
    feature_columns=[categorical_feature_a_emb, categorical_feature_b_emb],
    hidden_units=[1024, 512, 256],
    warm_start_from="/path/to/checkpoint/dir")
```

For more details on warm-start configuration, see
<a href="../../tf/estimator/WarmStartSettings">WarmStartSettings</a>.

#### Args:

* <b>`model_fn`</b>: Model function. Follows the signature:

    * Args:

      * `features`: This is the first item returned from the `input_fn`
             passed to `train`, `evaluate`, and `predict`. This should be a
             single `Tensor` or `dict` of same.
      * `labels`: This is the second item returned from the `input_fn`
             passed to `train`, `evaluate`, and `predict`. This should be a
             single `Tensor` or `dict` of same (for multi-head models). If
             mode is `ModeKeys.PREDICT`, `labels=None` will be passed. If
             the `model_fn`'s signature does not accept `mode`, the
             `model_fn` must still be able to handle `labels=None`.
      * `mode`: Optional. Specifies if this training, evaluation or
             prediction. See `ModeKeys`.
      * `params`: Optional `dict` of hyperparameters.  Will receive what
             is passed to Estimator in `params` parameter. This allows
             to configure Estimators from hyper parameter tuning.
      * `config`: Optional configuration object. Will receive what is passed
             to Estimator in `config` parameter, or the default `config`.
             Allows updating things in your `model_fn` based on
             configuration such as `num_ps_replicas`, or `model_dir`.

    * Returns:
      `EstimatorSpec`

* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
    also be used to load checkpoints from the directory into a estimator to
    continue training a previously saved model. If `PathLike` object, the
    path will be resolved. If `None`, the model_dir in `config` will be used
    if set. If both are set, they must be same. If both are `None`, a
    temporary directory will be used.
* <b>`config`</b>: Configuration object.
* <b>`params`</b>: `dict` of hyper parameters that will be passed into `model_fn`.
          Keys are names of parameters, values are basic python types.
* <b>`warm_start_from`</b>: Optional string filepath to a checkpoint or SavedModel to
                   warm-start from, or a <a href="../../tf/estimator/WarmStartSettings"><code>tf.estimator.WarmStartSettings</code></a>
                   object to fully configure warm-starting.  If the string
                   filepath is provided instead of a `WarmStartSettings`,
                   then all variables are warm-started, and it is assumed
                   that vocabularies and Tensor names are unchanged.


#### Raises:

* <b>`ValueError`</b>: parameters of `model_fn` don't match `params`.
* <b>`ValueError`</b>: if this is called via a subclass and if that class overrides
    a member of `Estimator`.

<h3 id="eval_dir"><code>eval_dir</code></h3>

``` python
eval_dir(name=None)
```

Shows directory name where evaluation metrics are dumped.

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

Evaluates the model given evaluation data input_fn.

For each step, calls `input_fn`, which returns one batch of data.
Evaluates until:
- `steps` batches are processed, or
- `input_fn` raises an end-of-input exception (`OutOfRangeError` or
`StopIteration`).

#### Args:

* <b>`input_fn`</b>: A function that constructs the input data for evaluation.
    See <a href="../../../../guide/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:

      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
        tuple (features, labels) with same constraints as below.
      * A tuple (features, labels): Where `features` is a `Tensor` or a
        dictionary of string feature name to `Tensor` and `labels` is a
        `Tensor` or a dictionary of string label name to `Tensor`. Both
        `features` and `labels` are consumed by `model_fn`. They should
        satisfy the expectation of `model_fn` from inputs.

* <b>`steps`</b>: Number of steps for which to evaluate model. If `None`, evaluates
    until `input_fn` raises an end-of-input exception.
* <b>`hooks`</b>: List of `SessionRunHook` subclass instances. Used for callbacks
    inside the evaluation call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to evaluate. If `None`, the
    latest checkpoint in `model_dir` is used.  If there are no checkpoints
    in `model_dir`, evaluation is run with newly initialized `Variables`
    instead of restored from checkpoint.
* <b>`name`</b>: Name of the evaluation if user needs to run multiple evaluations on
    different data sets, such as on training data vs test data. Metrics for
    different evaluations are saved in separate folders, and appear
    separately in tensorboard.


#### Returns:

A dict containing the evaluation metrics specified in `model_fn` keyed by
name, as well as an entry `global_step` which contains the value of the
global step for which this evaluation was performed.


#### Raises:

* <b>`ValueError`</b>: If `steps <= 0`.
* <b>`ValueError`</b>: If no model has been trained, namely `model_dir`, or the
    given `checkpoint_path` is empty.

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

Exports inference graph as a SavedModel into given dir.

For a detailed guide, see
<a href="../../../../guide/saved_model#using_savedmodel_with_estimators">Using SavedModel with Estimators</a>.

This method builds a new graph by first calling the
serving_input_receiver_fn to obtain feature `Tensor`s, and then calling
this `Estimator`'s model_fn to generate the model graph based on those
features. It restores the given checkpoint (or, lacking that, the most
recent checkpoint) into this graph in a fresh session.  Finally it creates
a timestamped export directory below the given export_dir_base, and writes
a `SavedModel` into it containing a single `MetaGraphDef` saved from this
session.

The exported `MetaGraphDef` will provide one `SignatureDef` for each
element of the export_outputs dict returned from the model_fn, named using
the same keys.  One of these keys is always
signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY, indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
`ExportOutput`s, and the inputs are always the input receivers provided by
the serving_input_receiver_fn.

Extra assets may be written into the SavedModel via the assets_extra
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

#### Args:

* <b>`export_dir_base`</b>: A string containing a directory in which to create
    timestamped subdirectories containing exported SavedModels.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and
    returns a `ServingInputReceiver` or `TensorServingInputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported SavedModel, or `None` if no extra assets are needed.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
    the most recent checkpoint found within the model directory is chosen.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
    removed from the NodeDefs. For a detailed guide, see
    [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).


#### Returns:

The string path to the exported directory.


#### Raises:

* <b>`ValueError`</b>: if no serving_input_receiver_fn is provided, no export_outputs
      are provided, or no checkpoint can be found.

<h3 id="get_variable_names"><code>get_variable_names</code></h3>

``` python
get_variable_names()
```

Returns list of all variable names in this model.

#### Returns:

List of names.


#### Raises:

* <b>`ValueError`</b>: If the Estimator has not produced a checkpoint yet.

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

* <b>`ValueError`</b>: If the Estimator has not produced a checkpoint yet.

<h3 id="latest_checkpoint"><code>latest_checkpoint</code></h3>

``` python
latest_checkpoint()
```

Finds the filename of latest saved checkpoint file in `model_dir`.

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

Yields predictions for given features.

#### Args:

* <b>`input_fn`</b>: A function that constructs the features. Prediction continues
    until `input_fn` raises an end-of-input exception (`OutOfRangeError` or
    `StopIteration`).
    See <a href="../../../../guide/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:

      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must have
        same constraints as below.
      * features: A `Tensor` or a dictionary of string feature name to
        `Tensor`. features are consumed by `model_fn`. They should satisfy
        the expectation of `model_fn` from inputs.
      * A tuple, in which case the first item is extracted as features.

* <b>`predict_keys`</b>: list of `str`, name of the keys to predict. It is used if
    the `EstimatorSpec.predictions` is a `dict`. If `predict_keys` is used
    then rest of the predictions will be filtered from the dictionary. If
    `None`, returns all.
* <b>`hooks`</b>: List of `SessionRunHook` subclass instances. Used for callbacks
    inside the prediction call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to predict. If `None`, the
    latest checkpoint in `model_dir` is used.  If there are no checkpoints
    in `model_dir`, prediction is run with newly initialized `Variables`
    instead of restored from checkpoint.
* <b>`yield_single_examples`</b>: If False, yield the whole batch as returned by the
    `model_fn` instead of decomposing the batch into individual elements.
    This is useful if `model_fn` returns some tensors whose first dimension
    is not equal to the batch size.


#### Yields:

Evaluated values of `predictions` tensors.


#### Raises:

* <b>`ValueError`</b>: Could not find a trained model in `model_dir`.
* <b>`ValueError`</b>: If batch length of predictions is not the same and
    `yield_single_examples` is True.
* <b>`ValueError`</b>: If there is a conflict between `predict_keys` and
    `predictions`. For example if `predict_keys` is not `None` but
    `EstimatorSpec.predictions` is not a `dict`.

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

Trains a model given training data input_fn.

#### Args:

* <b>`input_fn`</b>: A function that provides input data for training as minibatches.
    See <a href="../../../../guide/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:

      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
        tuple (features, labels) with same constraints as below.
      * A tuple (features, labels): Where `features` is a `Tensor` or a
        dictionary of string feature name to `Tensor` and `labels` is a
        `Tensor` or a dictionary of string label name to `Tensor`. Both
        `features` and `labels` are consumed by `model_fn`. They should
        satisfy the expectation of `model_fn` from inputs.

* <b>`hooks`</b>: List of `SessionRunHook` subclass instances. Used for callbacks
    inside the training loop.
* <b>`steps`</b>: Number of steps for which to train model. If `None`, train forever
    or train until input_fn generates the `OutOfRange` error or
    `StopIteration` exception. 'steps' works incrementally. If you call two
    times train(steps=10) then training occurs in total 20 steps. If
    `OutOfRange` or `StopIteration` occurs in the middle, training stops
    before 20 steps. If you don't want to have incremental behavior please
    set `max_steps` instead. If set, `max_steps` must be `None`.
* <b>`max_steps`</b>: Number of total steps for which to train model. If `None`,
    train forever or train until input_fn generates the `OutOfRange` error
    or `StopIteration` exception. If set, `steps` must be `None`. If
    `OutOfRange` or `StopIteration` occurs in the middle, training stops
    before `max_steps` steps.
    Two calls to `train(steps=100)` means 200 training
    iterations. On the other hand, two calls to `train(max_steps=100)` means
    that the second call will not do any iteration since first call did
    all 100 steps.
* <b>`saving_listeners`</b>: list of `CheckpointSaverListener` objects. Used for
    callbacks that run immediately before or after checkpoint savings.


#### Returns:

`self`, for chaining.


#### Raises:

* <b>`ValueError`</b>: If both `steps` and `max_steps` are not `None`.
* <b>`ValueError`</b>: If either `steps` or `max_steps` is <= 0.



