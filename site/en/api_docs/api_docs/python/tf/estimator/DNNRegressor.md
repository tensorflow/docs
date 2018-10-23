

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.DNNRegressor

## Class `DNNRegressor`

Inherits From: [`Estimator`](../../tf/estimator/Estimator)



Defined in [`tensorflow/python/estimator/canned/dnn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/estimator/canned/dnn.py).

A regressor for TensorFlow DNN models.

Example:

```python
sparse_feature_a = sparse_column_with_hash_bucket(...)
sparse_feature_b = sparse_column_with_hash_bucket(...)

sparse_feature_a_emb = embedding_column(sparse_id_column=sparse_feature_a,
                                        ...)
sparse_feature_b_emb = embedding_column(sparse_id_column=sparse_feature_b,
                                        ...)

estimator = DNNRegressor(
    feature_columns=[sparse_feature_a_emb, sparse_feature_b_emb],
    hidden_units=[1024, 512, 256])

# Or estimator using the ProximalAdagradOptimizer optimizer with
# regularization.
estimator = DNNRegressor(
    feature_columns=[sparse_feature_a_emb, sparse_feature_b_emb],
    hidden_units=[1024, 512, 256],
    optimizer=tf.train.ProximalAdagradOptimizer(
      learning_rate=0.1,
      l1_regularization_strength=0.001
    ))

# Input builders
def input_fn_train: # returns x, y
  pass
estimator.train(input_fn=input_fn_train, steps=100)

def input_fn_eval: # returns x, y
  pass
metrics = estimator.evaluate(input_fn=input_fn_eval, steps=10)
def input_fn_predict: # returns x, None
  pass
predictions = estimator.predict(input_fn=input_fn_predict)
```

Input of `train` and `evaluate` should have following features,
otherwise there will be a `KeyError`:

* if `weight_column` is not `None`, a feature with
  `key=weight_column` whose value is a `Tensor`.
* for each `column` in `feature_columns`:
  - if `column` is a `_CategoricalColumn`, a feature with `key=column.name`
    whose `value` is a `SparseTensor`.
  - if `column` is a `_WeightedCategoricalColumn`, two features: the first
    with `key` the id column name, the second with `key` the weight column
    name. Both features' `value` must be a `SparseTensor`.
  - if `column` is a `_DenseColumn`, a feature with `key=column.name`
    whose `value` is a `Tensor`.

Loss is calculated by using mean squared error.

## Properties

<h3 id="config"><code>config</code></h3>



<h3 id="model_dir"><code>model_dir</code></h3>



<h3 id="params"><code>params</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    hidden_units,
    feature_columns,
    model_dir=None,
    label_dimension=1,
    weight_column=None,
    optimizer='Adagrad',
    activation_fn=tf.nn.relu,
    dropout=None,
    input_layer_partitioner=None,
    config=None
)
```

Initializes a `DNNRegressor` instance.

#### Args:

* <b>`hidden_units`</b>: Iterable of number hidden units per layer. All layers are
    fully connected. Ex. `[64, 32]` means first layer has 64 nodes and
    second one has 32.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
    the model. All items in the set should be instances of classes derived
    from `_FeatureColumn`.
* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
    also be used to load checkpoints from the directory into a estimator to
    continue training a previously saved model.
* <b>`label_dimension`</b>: Number of regression targets per example. This is the
    size of the last dimension of the labels and logits `Tensor` objects
    (typically, these have shape `[batch_size, label_dimension]`).
* <b>`weight_column`</b>: A string or a `_NumericColumn` created by
    `tf.feature_column.numeric_column` defining feature column representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example. If it is a string, it is
    used as a key to fetch weight tensor from the `features`. If it is a
    `_NumericColumn`, raw tensor is fetched by key `weight_column.key`,
    then weight_column.normalizer_fn is applied on it to get weight tensor.
* <b>`optimizer`</b>: An instance of `tf.Optimizer` used to train the model. Defaults
    to Adagrad optimizer.
* <b>`activation_fn`</b>: Activation function applied to each layer. If `None`, will
    use `tf.nn.relu`.
* <b>`dropout`</b>: When not `None`, the probability we will drop out a given
    coordinate.
* <b>`input_layer_partitioner`</b>: Optional. Partitioner for input layer. Defaults
    to `min_max_variable_partitioner` with `min_slice_size` 64 << 20.
* <b>`config`</b>: `RunConfig` object to configure the runtime settings.

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

<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    input_fn,
    predict_keys=None,
    hooks=None,
    checkpoint_path=None
)
```

Returns predictions for given features.

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
    max_steps=None
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
    or train until input_fn generates the `OutOfRange` or `StopIteration`
    error. 'steps' works incrementally. If you call two times
    train(steps=10) then training occurs in total 20 steps. If `OutOfRange`
    or `StopIteration` error occurs in the middle, training stops before 20
    steps. If you don't want to have incremental behavior please set
    `max_steps` instead. If set, `max_steps` must be `None`.
* <b>`max_steps`</b>: Number of total steps for which to train model. If `None`,
    train forever or train until input_fn generates the `OutOfRange` or
    `StopIteration` error. If set, `steps` must be `None`. If `OutOfRange`
    or `StopIteration` error occurs in the middle, training stops before
    `max_steps` steps.

    Two calls to `train(steps=100)` means 200 training
    iterations. On the other hand, two calls to `train(max_steps=100)` means
    that the second call will not do any iteration since first call did
    all 100 steps.


#### Returns:

  `self`, for chaining.


#### Raises:

* <b>`ValueError`</b>: If both `steps` and `max_steps` are not `None`.
* <b>`ValueError`</b>: If either `steps` or `max_steps` is <= 0.



