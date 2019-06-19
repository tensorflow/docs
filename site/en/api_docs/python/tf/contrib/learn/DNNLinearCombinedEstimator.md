

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.DNNLinearCombinedEstimator

## Class `DNNLinearCombinedEstimator`

Inherits From: [`Estimator`](../../../tf/contrib/learn/Estimator)



Defined in [`tensorflow/contrib/learn/python/learn/estimators/dnn_linear_combined.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/learn/python/learn/estimators/dnn_linear_combined.py).

An estimator for TensorFlow Linear and DNN joined training models.

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/learn/README.md)
for general migration instructions.

Note: New users must set `fix_global_step_increment_bug=True` when creating an
estimator.

Input of `fit`, `train`, and `evaluate` should have following features,
  otherwise there will be a `KeyError`:
    if `weight_column_name` is not `None`, a feature with
      `key=weight_column_name` whose value is a `Tensor`.
    for each `column` in `dnn_feature_columns` + `linear_feature_columns`:
    - if `column` is a `SparseColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `WeightedSparseColumn`, two features: the first with
      `key` the id column name, the second with `key` the weight column
      name. Both features' `value` must be a `SparseTensor`.
    - if `column` is a `RealValuedColumn, a feature with `key=column.name`
      whose `value` is a `Tensor`.

## Properties

<h3 id="config"><code>config</code></h3>



<h3 id="model_dir"><code>model_dir</code></h3>



<h3 id="model_fn"><code>model_fn</code></h3>

Returns the model_fn which is bound to self.params.

#### Returns:

The model_fn with the following signature:
  `def model_fn(features, labels, mode, metrics)`



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    head,
    model_dir=None,
    linear_feature_columns=None,
    linear_optimizer=None,
    _joint_linear_weights=False,
    dnn_feature_columns=None,
    dnn_optimizer=None,
    dnn_hidden_units=None,
    dnn_activation_fn=None,
    dnn_dropout=None,
    gradient_clip_norm=None,
    config=None,
    feature_engineering_fn=None,
    embedding_lr_multipliers=None,
    fix_global_step_increment_bug=False,
    input_layer_partitioner=None
)
```

Initializes a DNNLinearCombinedEstimator instance. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2017-04-15.
Instructions for updating:
Please set fix_global_step_increment_bug=True and update training steps in your pipeline. See pydoc for details.

Note: New users must set `fix_global_step_increment_bug=True` when creating
an estimator.

#### Args:

* <b>`head`</b>: A _Head object.
* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
    also be used to load checkpoints from the directory into a estimator
    to continue training a previously saved model.
* <b>`linear_feature_columns`</b>: An iterable containing all the feature columns
    used by linear part of the model. All items in the set should be
    instances of classes derived from `FeatureColumn`.
* <b>`linear_optimizer`</b>: An instance of `tf.Optimizer` used to apply gradients to
    the linear part of the model. If `None`, will use a FTRL optimizer.
* <b>`_joint_linear_weights`</b>: If True will use a single (possibly partitioned)
    variable to store all weights for the linear model. More efficient if
    there are many columns, however requires all columns are sparse and
    have the 'sum' combiner.
* <b>`dnn_feature_columns`</b>: An iterable containing all the feature columns used
    by deep part of the model. All items in the set should be instances of
    classes derived from `FeatureColumn`.
* <b>`dnn_optimizer`</b>: An instance of `tf.Optimizer` used to apply gradients to
    the deep part of the model. If `None`, will use an Adagrad optimizer.
* <b>`dnn_hidden_units`</b>: List of hidden units per layer. All layers are fully
    connected.
* <b>`dnn_activation_fn`</b>: Activation function applied to each layer. If `None`,
    will use <a href="../../../tf/nn/relu"><code>tf.nn.relu</code></a>.
* <b>`dnn_dropout`</b>: When not None, the probability we will drop out
    a given coordinate.
* <b>`gradient_clip_norm`</b>: A float > 0. If provided, gradients are clipped
    to their global norm with this clipping ratio. See
    tf.clip_by_global_norm for more details.
* <b>`config`</b>: RunConfig object to configure the runtime settings.
* <b>`feature_engineering_fn`</b>: Feature engineering function. Takes features and
    labels which are the output of `input_fn` and returns features and
    labels which will be fed into the model.
* <b>`embedding_lr_multipliers`</b>: Optional. A dictionary from `EmbeddingColumn` to
    a `float` multiplier. Multiplier will be used to multiply with
    learning rate for the embedding variables.
* <b>`fix_global_step_increment_bug`</b>: If `False`, the estimator needs two fit
    steps to optimize both linear and dnn parts. If `True`, this bug is
    fixed. New users must set this to `True`, but the default value is
    `False` for backwards compatibility.
* <b>`input_layer_partitioner`</b>: Optional. Partitioner for input layer.


#### Raises:

* <b>`ValueError`</b>: If both linear_feature_columns and dnn_features_columns are
    empty at the same time.

<h3 id="evaluate"><code>evaluate</code></h3>

``` python
evaluate(
    x=None,
    y=None,
    input_fn=None,
    feed_fn=None,
    batch_size=None,
    steps=None,
    metrics=None,
    name=None,
    checkpoint_path=None,
    hooks=None,
    log_progress=True
)
```

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

<h3 id="export"><code>export</code></h3>

``` python
export(
    export_dir,
    input_fn=export._default_input_fn,
    input_feature_key=None,
    use_deprecated_input_fn=True,
    signature_fn=None,
    prediction_key=None,
    default_batch_size=1,
    exports_to_keep=None,
    checkpoint_path=None
)
```

Exports inference graph into given dir. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-25.
Instructions for updating:
Please use Estimator.export_savedmodel() instead.

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
* <b>`checkpoint_path`</b>: the checkpoint path of the model to be exported. If it is
      `None` (which is default), will use the latest checkpoint in
      export_dir.


#### Returns:

The string path to the exported directory. NB: this functionality was
added ca. 2016/09/25; clients that depend on the return value may need
to handle the case where this function returns None because subclasses
are not returning a value.

<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>

``` python
export_savedmodel(
    export_dir_base,
    serving_input_fn,
    default_output_alternative_key=None,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    graph_rewrite_specs=(GraphRewriteSpec((tag_constants.SERVING,), ()),),
    strip_default_attrs=False
)
```

Exports inference graph as a SavedModel into given dir.

#### Args:

* <b>`export_dir_base`</b>: A string containing a directory to write the exported
    graph and checkpoints.
* <b>`serving_input_fn`</b>: A function that takes no argument and
    returns an `InputFnOps`.
* <b>`default_output_alternative_key`</b>: the name of the head to serve when none is
    specified.  Not needed for single-headed models.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported SavedModel.  Each key should give the destination
    path (including the filename) relative to the assets.extra directory.
    The corresponding value gives the full path of the source file to be
    copied.  For example, the simple case of copying a single file without
    renaming it is specified as
    `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If None (the default),
    the most recent checkpoint found within the model directory is chosen.
* <b>`graph_rewrite_specs`</b>: an iterable of `GraphRewriteSpec`.  Each element will
    produce a separate MetaGraphDef within the exported SavedModel, tagged
    and rewritten as specified.  Defaults to a single entry using the
    default serving tag ("serve") and no rewriting.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
    removed from the NodeDefs. For a detailed guide, see
    [Stripping Default-Valued
      Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).


#### Returns:

The string path to the exported directory.


#### Raises:

* <b>`ValueError`</b>: if an unrecognized export_type is requested.

<h3 id="fit"><code>fit</code></h3>

``` python
fit(
    x=None,
    y=None,
    input_fn=None,
    steps=None,
    batch_size=None,
    monitors=None,
    max_steps=None
)
```

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

<h3 id="get_params"><code>get_params</code></h3>

``` python
get_params(deep=True)
```

Get parameters for this estimator.

#### Args:

* <b>`deep`</b>: boolean, optional

    If `True`, will return the parameters for this estimator and
    contained subobjects that are estimators.


#### Returns:

* <b>`params `</b>: mapping of string to any
  Parameter names mapped to their values.

<h3 id="get_variable_names"><code>get_variable_names</code></h3>

``` python
get_variable_names()
```

Returns list of all variable names in this model.

#### Returns:

List of names.

<h3 id="get_variable_value"><code>get_variable_value</code></h3>

``` python
get_variable_value(name)
```

Returns value of the variable given by name.

#### Args:

* <b>`name`</b>: string, name of the tensor.


#### Returns:

Numpy array - value of the tensor.

<h3 id="partial_fit"><code>partial_fit</code></h3>

``` python
partial_fit(
    x=None,
    y=None,
    input_fn=None,
    steps=1,
    batch_size=None,
    monitors=None
)
```

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

<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    x=None,
    input_fn=None,
    batch_size=None,
    outputs=None,
    as_iterable=True,
    iterate_batches=False
)
```

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
* <b>`iterate_batches`</b>: If True, yield the whole batch at once instead of
    decomposing the batch into individual samples. Only relevant when
    as_iterable is True.


#### Returns:

A numpy array of predicted classes or regression values if the
constructor's `model_fn` returns a `Tensor` for `predictions` or a `dict`
of numpy arrays if `model_fn` returns a `dict`. Returns an iterable of
predictions if as_iterable is True.


#### Raises:

* <b>`ValueError`</b>: If x and input_fn are both provided or both `None`.

<h3 id="set_params"><code>set_params</code></h3>

``` python
set_params(**params)
```

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects
(such as pipelines). The former have parameters of the form
``<component>__<parameter>`` so that it's possible to update each
component of a nested object.

#### Args:

* <b>`**params`</b>: Parameters.


#### Returns:

self


#### Raises:

* <b>`ValueError`</b>: If params contain invalid names.



