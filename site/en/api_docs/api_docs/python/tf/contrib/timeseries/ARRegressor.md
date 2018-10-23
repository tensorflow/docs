

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.timeseries.ARRegressor

## Class `ARRegressor`





Defined in [`tensorflow/contrib/timeseries/python/timeseries/estimators.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/timeseries/python/timeseries/estimators.py).

An Estimator for an (optionally non-linear) autoregressive model.

ARRegressor is a window-based model, inputting fixed windows of length
`input_window_size` and outputting fixed windows of length
`output_window_size`. These two parameters must add up to the window_size
passed to the `Chunker` used to create an `input_fn` for training or
evaluation. `RandomWindowInputFn` is suggested for both training and
evaluation, although it may be seeded for deterministic evaluation.

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
    input_window_size,
    output_window_size,
    num_features,
    num_time_buckets=10,
    loss=ar_model.ARModel.NORMAL_LIKELIHOOD_LOSS,
    hidden_layer_sizes=None,
    anomaly_prior_probability=None,
    anomaly_distribution=None,
    optimizer=None,
    model_dir=None,
    config=None
)
```

Initialize the Estimator.

#### Args:

* <b>`periodicities`</b>: periodicities of the input data, in the same units as the
    time feature. Note this can be a single value or a list of values for
    multiple periodicities.
* <b>`input_window_size`</b>: Number of past time steps of data to look at when doing
    the regression.
* <b>`output_window_size`</b>: Number of future time steps to predict. Note that
    setting it to > 1 empirically seems to give a better fit.
* <b>`num_features`</b>: The dimensionality of the time series (one for univariate,
      more than one for multivariate).
* <b>`num_time_buckets`</b>: Number of buckets into which to divide (time %
    periodicity) for generating time based features.
* <b>`loss`</b>: Loss function to use for training. Currently supported values are
    SQUARED_LOSS and NORMAL_LIKELIHOOD_LOSS. Note that for
    NORMAL_LIKELIHOOD_LOSS, we train the covariance term as well. For
    SQUARED_LOSS, the evaluation loss is reported based on un-scaled
    observations and predictions, while the training loss is computed on
    normalized data.
* <b>`hidden_layer_sizes`</b>: list of sizes of hidden layers.
* <b>`anomaly_prior_probability`</b>: If specified, constructs a mixture model under
    which anomalies (modeled with `anomaly_distribution`) have this prior
    probability. See `AnomalyMixtureARModel`.
* <b>`anomaly_distribution`</b>: May not be specified unless
    anomaly_prior_probability is specified and is not None. Controls the
    distribution of anomalies under the mixture model. Currently either
    `ar_model.AnomalyMixtureARModel.GAUSSIAN_ANOMALY` or
    `ar_model.AnomalyMixtureARModel.CAUCHY_ANOMALY`. See
    `AnomalyMixtureARModel`. Defaults to `GAUSSIAN_ANOMALY`.
* <b>`optimizer`</b>: The optimization algorithm to use when training, inheriting
      from tf.train.Optimizer. Defaults to Adagrad with step size 0.1.
* <b>`model_dir`</b>: See `Estimator`.
* <b>`config`</b>: See `Estimator`.

#### Raises:

* <b>`ValueError`</b>: For invalid combinations of arguments.

<h3 id="build_raw_serving_input_receiver_fn"><code>build_raw_serving_input_receiver_fn</code></h3>

``` python
build_raw_serving_input_receiver_fn(
    exogenous_features=None,
    default_batch_size=None,
    default_series_length=None
)
```

Build an input_receiver_fn for export_savedmodel which accepts arrays.

#### Args:

* <b>`exogenous_features`</b>: A dictionary mapping feature keys to exogenous
    features (either Numpy arrays or Tensors). Used to determine the shapes
    of placeholders for these features.
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

* <b>`input_fn`</b>: Input function returning a tuple of:
      features - Dictionary of string feature name to `Tensor` or
        `SparseTensor`.
      labels - `Tensor` or dictionary of `Tensor` with labels.
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
    checkpoint_path=None
)
```

Exports inference graph as a SavedModel into given dir.

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

Extra assets may be written into the SavedModel via the extra_assets
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

#### Args:

* <b>`export_dir_base`</b>: A string containing a directory in which to create
    timestamped subdirectories containing exported SavedModels.
* <b>`serving_input_receiver_fn`</b>: A function that takes no argument and
    returns a `ServingInputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported SavedModel, or `None` if no extra assets are needed.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
    the most recent checkpoint found within the model directory is chosen.


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
    checkpoint_path=None
)
```

Yields predictions for given features.

#### Args:

* <b>`input_fn`</b>: Input function returning features which is a dictionary of
    string feature name to `Tensor` or `SparseTensor`. If it returns a
    tuple, first item is extracted as features. Prediction continues until
    `input_fn` raises an end-of-input exception (`OutOfRangeError` or
    `StopIteration`).
* <b>`predict_keys`</b>: list of `str`, name of the keys to predict. It is used if
    the `EstimatorSpec.predictions` is a `dict`. If `predict_keys` is used
    then rest of the predictions will be filtered from the dictionary. If
    `None`, returns all.
* <b>`hooks`</b>: List of `SessionRunHook` subclass instances. Used for callbacks
    inside the prediction call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to predict. If `None`, the
    latest checkpoint in `model_dir` is used.


#### Yields:

Evaluated values of `predictions` tensors.


#### Raises:

* <b>`ValueError`</b>: Could not find a trained model in model_dir.
* <b>`ValueError`</b>: if batch length of predictions are not same.
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

* <b>`input_fn`</b>: Input function returning a tuple of:
      features - `Tensor` or dictionary of string feature name to `Tensor`.
      labels - `Tensor` or dictionary of `Tensor` with labels.
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



