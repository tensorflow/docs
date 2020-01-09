page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.estimator.experimental.KMeans


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/kmeans.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `KMeans`

An Estimator for K-Means clustering.

Inherits From: [`Estimator`](../../../../../tf/compat/v1/estimator/Estimator)

<!-- Placeholder for "Used in" -->


#### Example:


```
import numpy as np
import tensorflow as tf

num_points = 100
dimensions = 2
points = np.random.uniform(0, 1000, [num_points, dimensions])

def input_fn():
  return tf.train.limit_epochs(
      tf.convert_to_tensor(points, dtype=tf.float32), num_epochs=1)

num_clusters = 5
kmeans = tf.estimator.experimental.KMeans(
    num_clusters=num_clusters, use_mini_batch=False)

# train
num_iterations = 10
previous_centers = None
for _ in xrange(num_iterations):
  kmeans.train(input_fn)
  cluster_centers = kmeans.cluster_centers()
  if previous_centers is not None:
    print 'delta:', cluster_centers - previous_centers
  previous_centers = cluster_centers
  print 'score:', kmeans.score(input_fn)
print 'cluster centers:', cluster_centers

# map the input points to their clusters
cluster_indices = list(kmeans.predict_cluster_index(input_fn))
for i, point in enumerate(points):
  cluster_index = cluster_indices[i]
  center = cluster_centers[cluster_index]
  print 'point:', point, 'is in cluster', cluster_index, 'centered at', center
```

The `SavedModel` saved by the `export_saved_model` method does not include the
cluster centers. However, the cluster centers may be retrieved by the
latest checkpoint saved during training. Specifically,

```
kmeans.cluster_centers()
```
is equivalent to

```
tf.train.load_variable(
    kmeans.model_dir, KMeansClustering.CLUSTER_CENTERS_VAR_NAME)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/kmeans.py">View source</a>

``` python
__init__(
    num_clusters,
    model_dir=None,
    initial_clusters=RANDOM_INIT,
    distance_metric=SQUARED_EUCLIDEAN_DISTANCE,
    seed=None,
    use_mini_batch=True,
    mini_batch_steps_per_iteration=1,
    kmeans_plus_plus_num_retries=2,
    relative_tolerance=None,
    config=None,
    feature_columns=None
)
```

Creates an Estimator for running KMeans training and inference.

This Estimator implements the following variants of the K-means algorithm:

If `use_mini_batch` is False, it runs standard full batch K-means. Each
training step runs a single iteration of K-Means and must process the full
input at once. To run in this mode, the `input_fn` passed to `train` must
return the entire input dataset.

If `use_mini_batch` is True, it runs a generalization of the mini-batch
K-means algorithm. It runs multiple iterations, where each iteration is
composed of `mini_batch_steps_per_iteration` steps. Each training step
accumulates the contribution from one mini-batch into temporary storage.
Every `mini_batch_steps_per_iteration` steps, the cluster centers are
updated and the temporary storage cleared for the next iteration.
For example: the entire dataset contains 64k examples, where the batch size
is 64. User can choose mini_batch_steps_per_iteration = 100 to run 10% of
the entire data every iteration in order to update the cluster centers.
Note that:
  * If `mini_batch_steps_per_iteration=1`, the algorithm reduces to the
    standard K-means mini-batch algorithm.
  * If `mini_batch_steps_per_iteration = num_inputs / batch_size`, the
    algorithm becomes an asynchronous version of the full-batch algorithm.
    However, there is no guarantee by this implementation that each input
    is seen exactly once per iteration. Also, different updates are applied
    asynchronously without locking. So this asynchronous version may not
    behave exactly like a full-batch version.

#### Args:


* <b>`num_clusters`</b>: An integer tensor specifying the number of clusters. This
  argument is ignored if `initial_clusters` is a tensor or numpy array.
* <b>`model_dir`</b>: The directory to save the model results and log files.
* <b>`initial_clusters`</b>: Specifies how the initial cluster centers are chosen.
  One of the following: * a tensor or numpy array with the initial cluster
    centers. * a callable `f(inputs, k)` that selects and returns up to
    `k` centers from an input batch. `f` is free to return any number of
    centers from `0` to `k`. It will be invoked on successive input
    batches as necessary until all `num_clusters` centers are chosen.
  * `KMeansClustering.RANDOM_INIT`: Choose centers randomly from an input
    batch. If the batch size is less than `num_clusters` then the entire
    batch is chosen to be initial cluster centers and the remaining
    centers are chosen from successive input batches.
  * `KMeansClustering.KMEANS_PLUS_PLUS_INIT`: Use kmeans++ to choose
    centers from the first input batch. If the batch size is less than
    `num_clusters`, a TensorFlow runtime error occurs.
* <b>`distance_metric`</b>: The distance metric used for clustering. One of:
  * `KMeansClustering.SQUARED_EUCLIDEAN_DISTANCE`: Euclidean distance
    between vectors `u` and `v` is defined as \\(||u - v||_2\\) which is
    the square root of the sum of the absolute squares of the elements'
    difference.
  * `KMeansClustering.COSINE_DISTANCE`: Cosine distance between vectors
    `u` and `v` is defined as \\(1 - (u . v) / (||u||_2 ||v||_2)\\).
* <b>`seed`</b>: Python integer. Seed for PRNG used to initialize centers.
* <b>`use_mini_batch`</b>: A boolean specifying whether to use the mini-batch k-means
  algorithm. See explanation above.
* <b>`mini_batch_steps_per_iteration`</b>: The number of steps after which the
  updated cluster centers are synced back to a master copy. Used only if
  `use_mini_batch=True`. See explanation above.
* <b>`kmeans_plus_plus_num_retries`</b>: For each point that is sampled during
  kmeans++ initialization, this parameter specifies the number of
  additional points to draw from the current distribution before selecting
  the best. If a negative value is specified, a heuristic is used to
  sample `O(log(num_to_sample))` additional points. Used only if
  `initial_clusters=KMeansClustering.KMEANS_PLUS_PLUS_INIT`.
* <b>`relative_tolerance`</b>: A relative tolerance of change in the loss between
  iterations. Stops learning if the loss changes less than this amount.
  This may not work correctly if `use_mini_batch=True`.
* <b>`config`</b>: See <a href="../../../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a>.
* <b>`feature_columns`</b>: An optionable iterable containing all the feature columns
  used by the model. All items in the set should be feature column
  instances that can be passed to `tf.feature_column.input_layer`. If this
  is None, all features will be used.


#### Raises:


* <b>`ValueError`</b>: An invalid argument was passed to `initial_clusters` or
  `distance_metric`.



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

<h3 id="cluster_centers"><code>cluster_centers</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/kmeans.py">View source</a>

``` python
cluster_centers()
```

Returns the cluster centers.


<h3 id="eval_dir"><code>eval_dir</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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
- `input_fn` raises an end-of-input exception (<a href="../../../../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a>
or
`StopIteration`).

#### Args:


* <b>`input_fn`</b>: A function that constructs the input data for evaluation. See
  [Premade Estimators](
  https://tensorflow.org/guide/premade_estimators#create_input_functions)
  for more information. The
  function should construct and return one of the following:  * A
  <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be a tuple
  `(features, labels)` with same constraints as below. * A tuple
  `(features, labels)`: Where `features` is a <a href="../../../../../tf/Tensor"><code>tf.Tensor</code></a> or a dictionary
  of string feature name to `Tensor` and `labels` is a `Tensor` or a
  dictionary of string label name to `Tensor`. Both `features` and
  `labels` are consumed by `model_fn`. They should satisfy the expectation
  of `model_fn` from inputs.
* <b>`steps`</b>: Number of steps for which to evaluate model. If `None`, evaluates
  until `input_fn` raises an end-of-input exception.
* <b>`hooks`</b>: List of `tf.train.SessionRunHook` subclass instances. Used for
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

<h3 id="experimental_export_all_saved_models"><code>experimental_export_all_saved_models</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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
(order of preference: <a href="../../../../../tf/estimator/ModeKeys#TRAIN"><code>tf.estimator.ModeKeys.TRAIN</code></a>,
<a href="../../../../../tf/estimator/ModeKeys#EVAL"><code>tf.estimator.ModeKeys.EVAL</code></a>, then
<a href="../../../../../tf/estimator/ModeKeys#PREDICT"><code>tf.estimator.ModeKeys.PREDICT</code></a>), such that up to three
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
<a href="../../../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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
* <b>`input_receiver_fn_map`</b>: dict of <a href="../../../../../tf/estimator/ModeKeys"><code>tf.estimator.ModeKeys</code></a> to
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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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
<a href="../../../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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
  <a href="../../../../../tf/estimator/export/ServingInputReceiver"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../../../tf/estimator/export/TensorServingInputReceiver"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
  within the exported `SavedModel`, or `None` if no extra assets are
  needed.
* <b>`as_text`</b>: whether to write the `SavedModel` proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
  the most recent checkpoint found within the model directory is chosen.
* <b>`experimental_mode`</b>: <a href="../../../../../tf/estimator/ModeKeys"><code>tf.estimator.ModeKeys</code></a> value indicating with mode
  will be exported. Note that this feature is experimental.


#### Returns:

The string path to the exported directory.



#### Raises:


* <b>`ValueError`</b>: if no `serving_input_receiver_fn` is provided, no
`export_outputs` are provided, or no checkpoint can be found.

<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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
<a href="../../../../../tf/estimator/export/ExportOutput"><code>tf.estimator.export.ExportOutput</code></a>s, and the inputs are always the input
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
  <a href="../../../../../tf/estimator/export/ServingInputReceiver"><code>tf.estimator.export.ServingInputReceiver</code></a> or
  <a href="../../../../../tf/estimator/export/TensorServingInputReceiver"><code>tf.estimator.export.TensorServingInputReceiver</code></a>.
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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

``` python
get_variable_names()
```

Returns list of all variable names in this model.


#### Returns:

List of names.



#### Raises:


* <b>`ValueError`</b>: If the `Estimator` has not produced a checkpoint yet.

<h3 id="get_variable_value"><code>get_variable_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

``` python
latest_checkpoint()
```

Finds the filename of the latest saved checkpoint file in `model_dir`.


#### Returns:

The full path to the latest checkpoint or `None` if no checkpoint was
found.


<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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
  (<a href="../../../../../tf/errors/OutOfRangeError"><code>tf.errors.OutOfRangeError</code></a> or `StopIteration`).
  See [Premade Estimators](
  https://tensorflow.org/guide/premade_estimators#create_input_functions)
  for more information. The function should construct and return one of
  the following:

    * A <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must have
      same constraints as below.
    * features: A <a href="../../../../../tf/Tensor"><code>tf.Tensor</code></a> or a dictionary of string feature name to
      `Tensor`. features are consumed by `model_fn`. They should satisfy
      the expectation of `model_fn` from inputs.
    * A tuple, in which case the first item is extracted as features.

* <b>`predict_keys`</b>: list of `str`, name of the keys to predict. It is used if
  the <a href="../../../../../tf/estimator/EstimatorSpec#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is a `dict`. If
  `predict_keys` is used then rest of the predictions will be filtered
  from the dictionary. If `None`, returns all.
* <b>`hooks`</b>: List of `tf.train.SessionRunHook` subclass instances. Used for
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


* <b>`ValueError`</b>: If batch length of predictions is not the same and
  `yield_single_examples` is `True`.
* <b>`ValueError`</b>: If there is a conflict between `predict_keys` and
  `predictions`. For example if `predict_keys` is not `None` but
  <a href="../../../../../tf/estimator/EstimatorSpec#predictions"><code>tf.estimator.EstimatorSpec.predictions</code></a> is not a `dict`.

<h3 id="predict_cluster_index"><code>predict_cluster_index</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/kmeans.py">View source</a>

``` python
predict_cluster_index(input_fn)
```

Finds the index of the closest cluster center to each input point.


#### Args:


* <b>`input_fn`</b>: Input points. See <a href="../../../../../tf/estimator/Estimator#predict"><code>tf.estimator.Estimator.predict</code></a>.


#### Yields:

The index of the closest cluster center for each input point.


<h3 id="score"><code>score</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/kmeans.py">View source</a>

``` python
score(input_fn)
```

Returns the sum of squared distances to nearest clusters.

Note that this function is different from the corresponding one in sklearn
which returns the negative sum.

#### Args:


* <b>`input_fn`</b>: Input points. See <a href="../../../../../tf/estimator/Estimator#evaluate"><code>tf.estimator.Estimator.evaluate</code></a>. Only one
    batch is retrieved.


#### Returns:

The sum of the squared distance from each point in the first batch of
inputs to its nearest cluster center.


<h3 id="train"><code>train</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/estimator.py">View source</a>

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
  the following:
    * A <a href="../../../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object: Outputs of `Dataset` object must be
      a tuple `(features, labels)` with same constraints as below.
    * A tuple `(features, labels)`: Where `features` is a <a href="../../../../../tf/Tensor"><code>tf.Tensor</code></a> or
      a dictionary of string feature name to `Tensor` and `labels` is a
      `Tensor` or a dictionary of string label name to `Tensor`. Both
      `features` and `labels` are consumed by `model_fn`. They should
      satisfy the expectation of `model_fn` from inputs.
* <b>`hooks`</b>: List of `tf.train.SessionRunHook` subclass instances. Used for
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

<h3 id="transform"><code>transform</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/canned/kmeans.py">View source</a>

``` python
transform(input_fn)
```

Transforms each input point to its distances to all cluster centers.

Note that if `distance_metric=KMeansClustering.SQUARED_EUCLIDEAN_DISTANCE`,
this
function returns the squared Euclidean distance while the corresponding
sklearn function returns the Euclidean distance.

#### Args:


* <b>`input_fn`</b>: Input points. See <a href="../../../../../tf/estimator/Estimator#predict"><code>tf.estimator.Estimator.predict</code></a>.


#### Yields:

The distances from each input point to each cluster center.




## Class Members

* `ALL_DISTANCES = 'all_distances'` <a id="ALL_DISTANCES"></a>
* `CLUSTER_CENTERS_VAR_NAME = 'clusters'` <a id="CLUSTER_CENTERS_VAR_NAME"></a>
* `CLUSTER_INDEX = 'cluster_index'` <a id="CLUSTER_INDEX"></a>
* `COSINE_DISTANCE = 'cosine'` <a id="COSINE_DISTANCE"></a>
* `KMEANS_PLUS_PLUS_INIT = 'kmeans_plus_plus'` <a id="KMEANS_PLUS_PLUS_INIT"></a>
* `RANDOM_INIT = 'random'` <a id="RANDOM_INIT"></a>
* `SCORE = 'score'` <a id="SCORE"></a>
* `SQUARED_EUCLIDEAN_DISTANCE = 'squared_euclidean'` <a id="SQUARED_EUCLIDEAN_DISTANCE"></a>
