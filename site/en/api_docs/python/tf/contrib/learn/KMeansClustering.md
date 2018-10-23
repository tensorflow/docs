


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.KMeansClustering

### `class tf.contrib.learn.KMeansClustering`

See the guide: [Learn (contrib) > Estimators](../../../../../api_guides/python/contrib.learn#Estimators)

An Estimator fo rK-Means clustering.

## Child Classes
[`class LossRelativeChangeHook`](../../../tf/contrib/learn/KMeansClustering/LossRelativeChangeHook)

## Properties

<h3 id="config"><code>config</code></h3>



<h3 id="model_dir"><code>model_dir</code></h3>





## Methods

<h3 id="__init__"><code>__init__(num_clusters, model_dir=None, initial_clusters=clustering_ops.RANDOM_INIT, distance_metric=clustering_ops.SQUARED_EUCLIDEAN_DISTANCE, random_seed=0, use_mini_batch=True, kmeans_plus_plus_num_retries=2, relative_tolerance=None, config=None)</code></h3>

Creates a model for running KMeans training and inference.

#### Args:

* <b>`num_clusters`</b>: number of clusters to train.
* <b>`model_dir`</b>: the directory to save the model results and log files.
* <b>`initial_clusters`</b>: specifies how to initialize the clusters for training.
    See clustering_ops.kmeans for the possible values.
* <b>`distance_metric`</b>: the distance metric used for clustering.
    See clustering_ops.kmeans for the possible values.
* <b>`random_seed`</b>: Python integer. Seed for PRNG used to initialize centers.
* <b>`use_mini_batch`</b>: If true, use the mini-batch k-means algorithm. Else assume
    full batch.
* <b>`kmeans_plus_plus_num_retries`</b>: For each point that is sampled during
    kmeans++ initialization, this parameter specifies the number of
    additional points to draw from the current distribution before selecting
    the best. If a negative value is specified, a heuristic is used to
    sample O(log(num_to_sample)) additional points.
* <b>`relative_tolerance`</b>: A relative tolerance of change in the loss between
    iterations.  Stops learning if the loss changes less than this amount.
    Note that this may not work correctly if use_mini_batch=True.
* <b>`config`</b>: See Estimator

<h3 id="clusters"><code>clusters()</code></h3>

Returns cluster centers.

<h3 id="evaluate"><code>evaluate(*args, **kwargs)</code></h3>

See `Evaluable`. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-12-01.
Instructions for updating:
Estimator is decoupled from Scikit Learn interface by moving into
separate class SKCompat. Arguments x, y and batch_size are only
available in the SKCompat class, Estimator will only accept input_fn.
Example conversion:
  est = Estimator(...) -> est = SKCompat(Estimator(...))

#### Raises:

* <b>`ValueError`</b>: If at least one of `x` or `y` is provided, and at least one of
      `input_fn` or `feed_fn` is provided.
      Or if `metrics` is not `None` or `dict`.

<h3 id="export"><code>export(*args, **kwargs)</code></h3>

Exports inference graph into given dir. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-09-23.
Instructions for updating:
The signature of the input_fn accepted by export is changing to be consistent with what's used by tf.Learn Estimator's train/evaluate. input_fn (and in most cases, input_feature_key) will become required args, and use_deprecated_input_fn will default to False and be removed altogether.

#### Args:

* <b>`export_dir`</b>: A string containing a directory to write the exported graph
    and checkpoints.
* <b>`input_fn`</b>: If `use_deprecated_input_fn` is true, then a function that given
    `Tensor` of `Example` strings, parses it into features that are then
    passed to the model. Otherwise, a function that takes no argument and
    returns a tuple of (features, labels), where features is a dict of
    string key to `Tensor` and labels is a `Tensor` that's currently not
    used (and so can be `None`).
* <b>`input_feature_key`</b>: Only used if `use_deprecated_input_fn` is false. String
    key into the features dict returned by `input_fn` that corresponds to a
    the raw `Example` strings `Tensor` that the exported model will take as
    input. Can only be `None` if you're using a custom `signature_fn` that
    does not use the first arg (examples).
* <b>`use_deprecated_input_fn`</b>: Determines the signature format of `input_fn`.
* <b>`signature_fn`</b>: Function that returns a default signature and a named
    signature map, given `Tensor` of `Example` strings, `dict` of `Tensor`s
    for features and `Tensor` or `dict` of `Tensor`s for predictions.
* <b>`prediction_key`</b>: The key for a tensor in the `predictions` dict (output
    from the `model_fn`) to use as the `predictions` input to the
    `signature_fn`. Optional. If `None`, predictions will pass to
    `signature_fn` without filtering.
* <b>`default_batch_size`</b>: Default batch size of the `Example` placeholder.
* <b>`exports_to_keep`</b>: Number of exports to keep.


#### Returns:

  The string path to the exported directory. NB: this functionality was
  added ca. 2016/09/25; clients that depend on the return value may need
  to handle the case where this function returns None because subclasses
  are not returning a value.

<h3 id="export_savedmodel"><code>export_savedmodel(*args, **kwargs)</code></h3>

Exports inference graph as a SavedModel into given dir. (experimental)

THIS FUNCTION IS EXPERIMENTAL. It may change or be removed at any time, and without warning.


#### Args:

* <b>`export_dir_base`</b>: A string containing a directory to write the exported
    graph and checkpoints.
* <b>`input_fn`</b>: A function that takes no argument and
    returns an `InputFnOps`.
* <b>`default_output_alternative_key`</b>: the name of the head to serve when none is
    specified.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported SavedModel.  Each key should give the destination
    path (including the filename) relative to the assets.extra directory.
    The corresponding value gives the full path of the source file to be
    copied.  For example, the simple case of copying a single file without
    renaming it is specified as
    `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`exports_to_keep`</b>: Number of exports to keep.


#### Returns:

  The string path to the exported directory.


#### Raises:

* <b>`ValueError`</b>: if an unrecognized export_type is requested.

<h3 id="fit"><code>fit(*args, **kwargs)</code></h3>

See `Trainable`. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-12-01.
Instructions for updating:
Estimator is decoupled from Scikit Learn interface by moving into
separate class SKCompat. Arguments x, y and batch_size are only
available in the SKCompat class, Estimator will only accept input_fn.
Example conversion:
  est = Estimator(...) -> est = SKCompat(Estimator(...))

#### Raises:

* <b>`ValueError`</b>: If `x` or `y` are not `None` while `input_fn` is not `None`.
* <b>`ValueError`</b>: If both `steps` and `max_steps` are not `None`.

<h3 id="get_params"><code>get_params(deep=True)</code></h3>

Get parameters for this estimator.

#### Args:

* <b>`deep`</b>: boolean, optional

    If `True`, will return the parameters for this estimator and
    contained subobjects that are estimators.


#### Returns:

  params : mapping of string to any
  Parameter names mapped to their values.

<h3 id="get_variable_names"><code>get_variable_names()</code></h3>

Returns list of all variable names in this model.

#### Returns:

  List of names.

<h3 id="get_variable_value"><code>get_variable_value(name)</code></h3>

Returns value of the variable given by name.

#### Args:

* <b>`name`</b>: string, name of the tensor.


#### Returns:

  Numpy array - value of the tensor.

<h3 id="partial_fit"><code>partial_fit(*args, **kwargs)</code></h3>

Incremental fit on a batch of samples. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-12-01.
Instructions for updating:
Estimator is decoupled from Scikit Learn interface by moving into
separate class SKCompat. Arguments x, y and batch_size are only
available in the SKCompat class, Estimator will only accept input_fn.
Example conversion:
  est = Estimator(...) -> est = SKCompat(Estimator(...))

This method is expected to be called several times consecutively
on different or the same chunks of the dataset. This either can
implement iterative training or out-of-core/online training.

This is especially useful when the whole dataset is too big to
fit in memory at the same time. Or when model is taking long time
to converge, and you want to split up training into subparts.

#### Args:

* <b>`x`</b>: Matrix of shape [n_samples, n_features...]. Can be iterator that
     returns arrays of features. The training input samples for fitting the
     model. If set, `input_fn` must be `None`.
* <b>`y`</b>: Vector or matrix [n_samples] or [n_samples, n_outputs]. Can be
     iterator that returns array of labels. The training label values
     (class labels in classification, real numbers in regression). If set,
     `input_fn` must be `None`.
* <b>`input_fn`</b>: Input function. If set, `x`, `y`, and `batch_size` must be
    `None`.
* <b>`steps`</b>: Number of steps for which to train model. If `None`, train forever.
* <b>`batch_size`</b>: minibatch size to use on the input, defaults to first
    dimension of `x`. Must be `None` if `input_fn` is provided.
* <b>`monitors`</b>: List of `BaseMonitor` subclass instances. Used for callbacks
    inside the training loop.


#### Returns:

  `self`, for chaining.


#### Raises:

* <b>`ValueError`</b>: If at least one of `x` and `y` is provided, and `input_fn` is
      provided.

<h3 id="predict"><code>predict(*args, **kwargs)</code></h3>

Returns predictions for given features. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-12-01.
Instructions for updating:
Estimator is decoupled from Scikit Learn interface by moving into
separate class SKCompat. Arguments x, y and batch_size are only
available in the SKCompat class, Estimator will only accept input_fn.
Example conversion:
  est = Estimator(...) -> est = SKCompat(Estimator(...))

#### Args:

* <b>`x`</b>: Matrix of shape [n_samples, n_features...]. Can be iterator that
     returns arrays of features. The training input samples for fitting the
     model. If set, `input_fn` must be `None`.
* <b>`input_fn`</b>: Input function. If set, `x` and 'batch_size' must be `None`.
* <b>`batch_size`</b>: Override default batch size. If set, 'input_fn' must be
    'None'.
* <b>`outputs`</b>: list of `str`, name of the output to predict.
    If `None`, returns all.
* <b>`as_iterable`</b>: If True, return an iterable which keeps yielding predictions
    for each example until inputs are exhausted. Note: The inputs must
    terminate if you want the iterable to terminate (e.g. be sure to pass
    num_epochs=1 if you are using something like read_batch_features).


#### Returns:

  A numpy array of predicted classes or regression values if the
  constructor's `model_fn` returns a `Tensor` for `predictions` or a `dict`
  of numpy arrays if `model_fn` returns a `dict`. Returns an iterable of
  predictions if as_iterable is True.


#### Raises:

* <b>`ValueError`</b>: If x and input_fn are both provided or both `None`.

<h3 id="predict_cluster_idx"><code>predict_cluster_idx(input_fn=None)</code></h3>

Yields predicted cluster indices.

<h3 id="score"><code>score(input_fn=None, steps=None)</code></h3>

Predict total sum of distances to nearest clusters.

Note that this function is different from the corresponding one in sklearn
which returns the negative of the sum of distances.

#### Args:

* <b>`input_fn`</b>: see predict.
* <b>`steps`</b>: see predict.


#### Returns:

  Total sum of distances to nearest clusters.

<h3 id="set_params"><code>set_params(**params)</code></h3>

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects
(such as pipelines). The former have parameters of the form
``<component>__<parameter>`` so that it's possible to update each
component of a nested object.

#### Args:

  **params: Parameters.


#### Returns:

  self


#### Raises:

* <b>`ValueError`</b>: If params contain invalid names.

<h3 id="transform"><code>transform(input_fn=None, as_iterable=False)</code></h3>

Transforms each element to distances to cluster centers.

Note that this function is different from the corresponding one in sklearn.
For SQUARED_EUCLIDEAN distance metric, sklearn transform returns the
EUCLIDEAN distance, while this function returns the SQUARED_EUCLIDEAN
distance.

#### Args:

* <b>`input_fn`</b>: see predict.
* <b>`as_iterable`</b>: see predict


#### Returns:

  Array with same number of rows as x, and num_clusters columns, containing
  distances to the cluster centers.



## Class Members

<h3 id="ALL_SCORES"><code>ALL_SCORES</code></h3>

<h3 id="CLUSTERS"><code>CLUSTERS</code></h3>

<h3 id="CLUSTER_IDX"><code>CLUSTER_IDX</code></h3>

<h3 id="LOSS_OP_NAME"><code>LOSS_OP_NAME</code></h3>

<h3 id="SCORES"><code>SCORES</code></h3>



Defined in [`tensorflow/contrib/learn/python/learn/estimators/kmeans.py`](https://www.tensorflow.org/code/tensorflow/contrib/learn/python/learn/estimators/kmeans.py).

