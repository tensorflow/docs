

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.timeseries.StructuralEnsembleRegressor

## Class `StructuralEnsembleRegressor`





Defined in [`tensorflow/contrib/timeseries/python/timeseries/estimators.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/timeseries/python/timeseries/estimators.py).

An Estimator for structural time series models.

"Structural" refers to the fact that this model explicitly accounts for
structure in the data, such as periodicity and trends.

`StructuralEnsembleRegressor` is a state space model. It contains components
for modeling level, local linear trends, periodicity, and mean-reverting
transients via a moving average component. Multivariate series are fit with
full covariance matrices for observation and latent state transition noise,
each feature of the multivariate series having its own latent components.

Note that unlike `ARRegressor`, `StructuralEnsembleRegressor` is sequential,
and so accepts variable window sizes with the same model.

For training, `RandomWindowInputFn` is recommended as an `input_fn`. Model
state is managed through `ChainingStateManager`: since state space models are
inherently sequential, we save state from previous iterations to get
approximate/eventual consistency while achieving good performance through
batched computation.

For evaluation, either pass a significant chunk of the series in a single
window (e.g. set `window_size` to the whole series with
`WholeDatasetInputFn`), or use enough random evaluation iterations to cover
several passes through the whole dataset. Either method will ensure that stale
saved state has been flushed.

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
    periodicities,
    num_features,
    cycle_num_latent_values=11,
    moving_average_order=4,
    autoregressive_order=0,
    exogenous_feature_columns=None,
    exogenous_update_condition=None,
    dtype=tf.double,
    anomaly_prior_probability=None,
    optimizer=None,
    model_dir=None,
    config=None
)
```

Initialize the Estimator.

#### Args:

* <b>`periodicities`</b>: The expected periodicity of the data (for example 24 if
      feeding hourly data with a daily periodicity, or 60 * 24 if feeding
      minute-level data with daily periodicity). Either a scalar or a
      list. This parameter can be any real value, and does not control the
      size of the model. However, increasing this without increasing
      `num_values_per_cycle` will lead to smoother periodic behavior, as the
      same number of distinct values will be cycled through over a longer
      period of time.
* <b>`num_features`</b>: The dimensionality of the time series (one for univariate,
      more than one for multivariate).
* <b>`cycle_num_latent_values`</b>: Along with `moving_average_order` and
      `num_features`, controls the latent state size of the model. Square
      matrices of size `num_features * (moving_average_order +
      cycle_num_latent_values + 3)` are created and multiplied, so larger
      values may be slow. The trade-off is with resolution: cycling between
      a smaller number of latent values means that only smoother functions
      can be modeled.
* <b>`moving_average_order`</b>: Controls model size (along with
      `cycle_num_latent_values` and `autoregressive_order`) and the number
      of steps before transient deviations revert to the mean defined by the
      period and level/trend components.
* <b>`autoregressive_order`</b>: Each contribution from this component is a linear
      combination of this many previous contributions. Also helps to
      determine the model size. Learning autoregressive coefficients
      typically requires more steps and a smaller step size than other
      components.
* <b>`exogenous_feature_columns`</b>: A list of `tf.feature_column`s (for example
      `tf.feature_column.embedding_column`) corresponding to exogenous
      features which provide extra information to the model but are not part
      of the series to be predicted. Passed to
      `tf.feature_column.input_layer`.
* <b>`exogenous_update_condition`</b>: A function taking two Tensor arguments,
      `times` (shape [batch size]) and `features` (a dictionary mapping
      exogenous feature keys to Tensors with shapes [batch size, ...]), and
      returning a boolean Tensor with shape [batch size] indicating whether
      state should be updated using exogenous features for each part of the
      batch. Where it is False, no exogenous update is performed. If None
      (default), exogenous updates are always performed. Useful for avoiding
      "leaky" frequent exogenous updates when sparse updates are
      desired. Called only during graph construction. See the "known
      anomaly" example for example usage.
* <b>`dtype`</b>: The floating point data type to compute with. float32 may be
    faster, but can be problematic for larger models and longer time series.
* <b>`anomaly_prior_probability`</b>: If not None, the model attempts to
      automatically detect and ignore anomalies during training. This
      parameter then controls the prior probability of an anomaly. Values
      closer to 0 mean that points will be discarded less frequently. The
      default value (None) means that anomalies are not discarded, which may
      be slightly faster.
* <b>`optimizer`</b>: The optimization algorithm to use when training, inheriting
      from tf.train.Optimizer. Defaults to Adam with step size 0.02.
* <b>`model_dir`</b>: See `Estimator`.
* <b>`config`</b>: See `Estimator`.

<h3 id="build_raw_serving_input_receiver_fn"><code>build_raw_serving_input_receiver_fn</code></h3>

``` python
build_raw_serving_input_receiver_fn(
    default_batch_size=None,
    default_series_length=None
)
```

Build an input_receiver_fn for export_savedmodel which accepts arrays.

Automatically creates placeholders for exogenous `FeatureColumn`s passed to
the model.

#### Args:

* <b>`default_batch_size`</b>: If specified, must be a scalar integer. Sets the batch
    size in the static shape information of all feature Tensors, which means
    only this batch size will be accepted by the exported model. If None
    (default), static shape information for batch sizes is omitted.
* <b>`default_series_length`</b>: If specified, must be a scalar integer. Sets the
    series length in the static shape information of all feature Tensors,
    which means only this series length will be accepted by the exported
    model. If None (default), static shape information for series length is
    omitted.

#### Returns:

An input_receiver_fn which may be passed to the Estimator's
export_savedmodel.

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
    See <a href="../../../../../get_started/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:

      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
        tuple (features, labels) with same constraints as below.
      * A tuple (features, labels): Where features is a `Tensor` or a
        dictionary of string feature name to `Tensor` and labels is a
        `Tensor` or a dictionary of string label name to `Tensor`. Both
        features and labels are consumed by `model_fn`. They should satisfy
        the expectation of `model_fn` from inputs.

* <b>`steps`</b>: Number of steps for which to evaluate model. If `None`, evaluates
    until `input_fn` raises an end-of-input exception.
* <b>`hooks`</b>: List of `SessionRunHook` subclass instances. Used for callbacks
    inside the evaluation call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to evaluate. If `None`, the
    latest checkpoint in `model_dir` is used.
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
<a href="../../../../../programmers_guide/saved_model#using_savedmodel_with_estimators">Using SavedModel with Estimators</a>.

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
    See <a href="../../../../../get_started/premade_estimators#create_input_functions">Premade Estimators</a> for more
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
    latest checkpoint in `model_dir` is used.
* <b>`yield_single_examples`</b>: If False, yield the whole batch as returned by the
    model_fn instead of decomposing the batch into individual elements. This
    is useful if model_fn return some tensor with first dimension not
    equal to the batch size


#### Yields:

Evaluated values of `predictions` tensors.


#### Raises:

* <b>`ValueError`</b>: Could not find a trained model in model_dir.
* <b>`ValueError`</b>: if batch length of predictions are not same and
    yield_single_examples is True.
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
    See <a href="../../../../../get_started/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:

      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
        tuple (features, labels) with same constraints as below.
      * A tuple (features, labels): Where features is a `Tensor` or a
        dictionary of string feature name to `Tensor` and labels is a
        `Tensor` or a dictionary of string label name to `Tensor`. Both
        features and labels are consumed by `model_fn`. They should satisfy
        the expectation of `model_fn` from inputs.

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



