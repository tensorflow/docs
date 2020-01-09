page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.SavedModelEstimator

## Class `SavedModelEstimator`





Defined in [`tensorflow/contrib/estimator/python/estimator/saved_model_estimator.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/estimator/python/estimator/saved_model_estimator.py).

Create an Estimator from a SavedModel.

Only SavedModels exported with
`tf.contrib.estimator.export_all_saved_models()` or
`tf.estimator.Estimator.export_savedmodel()` are supported for this class.

Example with `tf.estimator.DNNClassifier`:

**Step 1: Create and train DNNClassifier.**

```python
feature1 = tf.feature_column.embedding_column(
    tf.feature_column.categorical_column_with_vocabulary_list(
        key='feature1', vocabulary_list=('green', 'yellow')), dimension=1)
feature2 = tf.feature_column.numeric_column(key='feature2', default_value=0.0)

classifier = tf.estimator.DNNClassifier(
    hidden_units=[4,2], feature_columns=[feature1, feature2])

def input_fn():
  features = {'feature1': tf.constant(['green', 'green', 'yellow']),
              'feature2': tf.constant([3.5, 4.2, 6.1])}
  label = tf.constant([1., 0., 0.])
  return tf.data.Dataset.from_tensors((features, label)).repeat()

classifier.train(input_fn=input_fn, steps=10)
```

**Step 2: Export classifier.**
First, build functions that specify the expected inputs.

```python
# During train and evaluation, both the features and labels should be defined.
supervised_input_receiver_fn = (
    tf.contrib.estimator.build_raw_supervised_input_receiver_fn(
        {'feature1': tf.placeholder(dtype=tf.string, shape=[None]),
         'feature2': tf.placeholder(dtype=tf.float32, shape=[None])},
        tf.placeholder(dtype=tf.float32, shape=[None])))

# During predict mode, expect to receive a `tf.Example` proto, so a parsing
# function is used.
serving_input_receiver_fn = (
    tf.estimator.export.build_parsing_serving_input_receiver_fn(
        tf.feature_column.make_parse_example_spec([feature1, feature2])))
```

Next, export the model as a SavedModel. A timestamped directory will be
created (for example `/tmp/export_all/1234567890`).

```python
# Option 1: Save all modes (train, eval, predict)
export_dir = tf.contrib.estimator.export_all_saved_models(
    classifier, '/tmp/export_all',
    {tf.estimator.ModeKeys.TRAIN: supervised_input_receiver_fn,
     tf.estimator.ModeKeys.EVAL: supervised_input_receiver_fn,
     tf.estimator.ModeKeys.PREDICT: serving_input_receiver_fn})

# Option 2: Only export predict mode
export_dir = classifier.export_savedmodel(
    '/tmp/export_predict', serving_input_receiver_fn)
```

**Step 3: Create a SavedModelEstimator from the exported SavedModel.**

```python
est = tf.contrib.estimator.SavedModelEstimator(export_dir)

# If all modes were exported, you can immediately evaluate and predict, or
# continue training. Otherwise only predict is available.
eval_results = est.evaluate(input_fn=input_fn, steps=1)
print(eval_results)

est.train(input_fn=input_fn, steps=20)

def predict_input_fn():
  example = tf.train.Example()
  example.features.feature['feature1'].bytes_list.value.extend(['yellow'])
  example.features.feature['feature2'].float_list.value.extend([1.])
  return {'inputs':tf.constant([example.SerializeToString()])}

predictions = est.predict(predict_input_fn)
print(next(predictions))
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    saved_model_dir,
    model_dir=None
)
```

Initialize a SavedModelEstimator.

The SavedModelEstimator loads its model function and variable values from
the graphs defined in the SavedModel. There is no option to pass in
`RunConfig` or `params` arguments, because the model function graph is
defined statically in the SavedModel.

#### Args:

* <b>`saved_model_dir`</b>: Directory containing SavedModel protobuf and subfolders.
* <b>`model_dir`</b>: Directory to save new checkpoints during training.


#### Raises:

* <b>`NotImplementedError`</b>: If a DistributionStrategy is defined in the config.
    Unless the SavedModelEstimator is subclassed, this shouldn't happen.



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

Evaluates the model given evaluation data `input_fn`.

For each step, calls `input_fn`, which returns one batch of data.
Evaluates until:
- `steps` batches are processed, or
- `input_fn` raises an end-of-input exception (<a href="../../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a>
or
`StopIteration`).

#### Args:

* <b>`input_fn`</b>: A function that constructs the input data for evaluation. See
    [Premade Estimators](
    https://tensorflow.org/guide/premade_estimators#create_input_functions)
    for more information. The
    function should construct and return one of the following:  * A
    <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a tuple
    `(features, labels)` with same constraints as below. * A tuple
    `(features, labels)`: Where `features` is a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> or a dictionary
    of string feature name to `Tensor` and `labels` is a `Tensor` or a
    dictionary of string label name to `Tensor`. Both `features` and
    `labels` are consumed by `model_fn`. They should satisfy the expectation
    of `model_fn` from inputs.
* <b>`steps`</b>: Number of steps for which to evaluate model. If `None`, evaluates
    until `input_fn` raises an end-of-input exception.
* <b>`hooks`</b>: List of <a href="../../../tf/train/SessionRunHook"><code>tf.train.SessionRunHook</code></a> subclass instances. Used for
    callbacks inside the evaluation call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to evaluate. If `None`, the
    latest checkpoint in `model_dir` is used.  If there are no checkpoints
    in `model_dir`, evaluation is run with newly initialized `Variables`
    instead of ones restored from checkpoint.
* <b>`name`</b>: Name of the evaluation if user needs to run multiple evaluations on
    different data sets, such as on training data vs test data. Metrics for
    different evaluations are saved in separate folders, and appear
    separately in tensorboard.


#### Returns:

A dict containing the evaluation metrics specified in `model_fn` keyed by
name, as well as an entry `global_step` which contains the value of the
global step for which this evaluation was performed. For canned
estimators, the dict contains the `loss` (mean loss per mini-batch) and
the `average_loss` (mean loss per sample). Canned classifiers also return
the `accuracy`. Canned regressors also return the `label/mean` and the
`prediction/mean`.


#### Raises:

* <b>`ValueError`</b>: If `steps <= 0`.
* <b>`ValueError`</b>: If no model has been trained, namely `model_dir`, or the
    given `checkpoint_path` is empty.

<h3 id="export_saved_model"><code>export_saved_model</code></h3>

``` python
export_saved_model(
    export_dir_base,
    serving_input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None
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
`tf.estimator.export.ExportOutput`s, and the inputs are always the input
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
    `tf.estimator.export.ServingInputReceiver` or
    `tf.estimator.export.TensorServingInputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported `SavedModel`, or `None` if no extra assets are
    needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
    the most recent checkpoint found within the model directory is chosen.


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

Exports inference graph as a `SavedModel` into the given dir.

Note that `export_to_savedmodel` will be renamed to `export_saved_model`
in TensorFlow 2.0. At that time, `export_to_savedmodel` without the
additional underscore will be available only through tf.compat.v1.

Please see `tf.estimator.Estimator.export_saved_model` for more information.

There is one additional arg versus the new method:
  strip_default_attrs: This parameter is going away in TF 2.0, and
    the new behavior will automatically strip all default attributes.
    Boolean. If `True`, default-valued attributes will be
    removed from the `NodeDef`s. For a detailed guide, see [Stripping
    Default-Valued Attributes](
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).

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

Yields predictions for given features.

Please note that interleaving two predict outputs does not work. See:
[issue/20506](
https://github.com/tensorflow/tensorflow/issues/20506#issuecomment-422208517)

#### Args:

* <b>`input_fn`</b>: A function that constructs the features. Prediction continues
    until `input_fn` raises an end-of-input exception
    (<a href="../../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a> or `StopIteration`).
    See [Premade Estimators](
    https://tensorflow.org/guide/premade_estimators#create_input_functions)
    for more information. The function should construct and return one of
    the following:

      * A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must have
        same constraints as below.
      * features: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> or a dictionary of string feature name to
        `Tensor`. features are consumed by `model_fn`. They should satisfy
        the expectation of `model_fn` from inputs.
      * A tuple, in which case the first item is extracted as features.

* <b>`predict_keys`</b>: list of `str`, name of the keys to predict. It is used if
    the `tf.estimator.EstimatorSpec.predictions` is a `dict`. If
    `predict_keys` is used then rest of the predictions will be filtered
    from the dictionary. If `None`, returns all.
* <b>`hooks`</b>: List of <a href="../../../tf/train/SessionRunHook"><code>tf.train.SessionRunHook</code></a> subclass instances. Used for
    callbacks inside the prediction call.
* <b>`checkpoint_path`</b>: Path of a specific checkpoint to predict. If `None`, the
    latest checkpoint in `model_dir` is used.  If there are no checkpoints
    in `model_dir`, prediction is run with newly initialized `Variables`
    instead of ones restored from checkpoint.
* <b>`yield_single_examples`</b>: If `False`, yields the whole batch as returned by
    the `model_fn` instead of decomposing the batch into individual
    elements. This is useful if `model_fn` returns some tensors whose first
    dimension is not equal to the batch size.


#### Yields:

Evaluated values of `predictions` tensors.


#### Raises:

* <b>`ValueError`</b>: Could not find a trained model in `model_dir`.
* <b>`ValueError`</b>: If batch length of predictions is not the same and
    `yield_single_examples` is `True`.
* <b>`ValueError`</b>: If there is a conflict between `predict_keys` and
    `predictions`. For example if `predict_keys` is not `None` but
    `tf.estimator.EstimatorSpec.predictions` is not a `dict`.

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

Trains a model given training data `input_fn`.

#### Args:

* <b>`input_fn`</b>: A function that provides input data for training as minibatches.
    See [Premade Estimators](
    https://tensorflow.org/guide/premade_estimators#create_input_functions)
    for more information. The function should construct and return one of
    the following:  * A
    <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a tuple
    `(features, labels)` with same constraints as below. * A tuple
    `(features, labels)`: Where `features` is a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> or a dictionary
    of string feature name to `Tensor` and `labels` is a `Tensor` or a
    dictionary of string label name to `Tensor`. Both `features` and
    `labels` are consumed by `model_fn`. They should satisfy the expectation
    of `model_fn` from inputs.
* <b>`hooks`</b>: List of <a href="../../../tf/train/SessionRunHook"><code>tf.train.SessionRunHook</code></a> subclass instances. Used for
    callbacks inside the training loop.
* <b>`steps`</b>: Number of steps for which to train the model. If `None`, train
    forever or train until `input_fn` generates the `tf.errors.OutOfRange`
    error or `StopIteration` exception. `steps` works incrementally. If you
    call two times `train(steps=10)` then training occurs in total 20 steps.
    If `OutOfRange` or `StopIteration` occurs in the middle, training stops
    before 20 steps. If you don't want to have incremental behavior please
    set `max_steps` instead. If set, `max_steps` must be `None`.
* <b>`max_steps`</b>: Number of total steps for which to train model. If `None`,
    train forever or train until `input_fn` generates the
    `tf.errors.OutOfRange` error or `StopIteration` exception. If set,
    `steps` must be `None`. If `OutOfRange` or `StopIteration` occurs in the
    middle, training stops before `max_steps` steps. Two calls to
    `train(steps=100)` means 200 training iterations. On the other hand, two
    calls to `train(max_steps=100)` means that the second call will not do
    any iteration since first call did all 100 steps.
* <b>`saving_listeners`</b>: list of `CheckpointSaverListener` objects. Used for
    callbacks that run immediately before or after checkpoint savings.


#### Returns:

`self`, for chaining.


#### Raises:

* <b>`ValueError`</b>: If both `steps` and `max_steps` are not `None`.
* <b>`ValueError`</b>: If either `steps` or `max_steps <= 0`.



