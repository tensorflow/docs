page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.DynamicRnnEstimator

## Class `DynamicRnnEstimator`

Dynamically unrolled RNN (deprecated).

Inherits From: [`Estimator`](../../../tf/contrib/learn/Estimator)



Defined in [`contrib/learn/python/learn/estimators/dynamic_rnn_estimator.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/estimators/dynamic_rnn_estimator.py).

<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.tensorflow.org/code/tensorflow/contrib/learn/README.md)
for general migration instructions.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    problem_type,
    prediction_type,
    sequence_feature_columns,
    context_feature_columns=None,
    num_classes=None,
    num_units=None,
    cell_type='basic_rnn',
    optimizer='SGD',
    learning_rate=0.1,
    predict_probabilities=False,
    momentum=None,
    gradient_clipping_norm=5.0,
    dropout_keep_probabilities=None,
    model_dir=None,
    feature_engineering_fn=None,
    config=None
)
```

Initializes a `DynamicRnnEstimator`.

The input function passed to this `Estimator` optionally contains keys
`RNNKeys.SEQUENCE_LENGTH_KEY`. The value corresponding to
`RNNKeys.SEQUENCE_LENGTH_KEY` must be vector of size `batch_size` where
entry `n` corresponds to the length of the `n`th sequence in the batch. The
sequence length feature is required for batches of varying sizes. It will be
used to calculate loss and evaluation metrics. If
`RNNKeys.SEQUENCE_LENGTH_KEY` is not included, all sequences are assumed to
have length equal to the size of dimension 1 of the input to the RNN.

In order to specify an initial state, the input function must include keys
`STATE_PREFIX_i` for all `0 <= i < n` where `n` is the number of nested
elements in `cell.state_size`. The input function must contain values for
all state components or none of them. If none are included, then the default
(zero) state is used as an initial state. See the documentation for
`dict_to_state_tuple` and `state_tuple_to_dict` for further details.
The input function can call rnn_common.construct_rnn_cell() to obtain the
same cell type that this class will select from arguments to __init__.

The `predict()` method of the `Estimator` returns a dictionary with keys
`STATE_PREFIX_i` for `0 <= i < n` where `n` is the number of nested elements
in `cell.state_size`, along with `PredictionKey.CLASSES` for problem type
`CLASSIFICATION` or `PredictionKey.SCORES` for problem type
`LINEAR_REGRESSION`.  The value keyed by
`PredictionKey.CLASSES` or `PredictionKey.SCORES` has shape
`[batch_size, padded_length]` in the multi-value case and shape
`[batch_size]` in the single-value case.  Here, `padded_length` is the
largest value in the `RNNKeys.SEQUENCE_LENGTH` `Tensor` passed as input.
Entry `[i, j]` is the prediction associated with sequence `i` and time step
`j`. If the problem type is `CLASSIFICATION` and `predict_probabilities` is
`True`, it will also include key`PredictionKey.PROBABILITIES`.

#### Args:


* <b>`problem_type`</b>: whether the `Estimator` is intended for a regression or
  classification problem. Value must be one of
  `ProblemType.CLASSIFICATION` or `ProblemType.LINEAR_REGRESSION`.
* <b>`prediction_type`</b>: whether the `Estimator` should return a value for each
  step in the sequence, or just a single value for the final time step.
  Must be one of `PredictionType.SINGLE_VALUE` or
  `PredictionType.MULTIPLE_VALUE`.
* <b>`sequence_feature_columns`</b>: An iterable containing all the feature columns
  describing sequence features. All items in the iterable should be
  instances of classes derived from `FeatureColumn`.
* <b>`context_feature_columns`</b>: An iterable containing all the feature columns
  describing context features, i.e., features that apply across all time
  steps. All items in the set should be instances of classes derived from
  `FeatureColumn`.
* <b>`num_classes`</b>: the number of classes for a classification problem. Only
  used when `problem_type=ProblemType.CLASSIFICATION`.
* <b>`num_units`</b>: A list of integers indicating the number of units in the
  `RNNCell`s in each layer.
* <b>`cell_type`</b>: A subclass of `RNNCell` or one of 'basic_rnn,' 'lstm' or 'gru'.
* <b>`optimizer`</b>: The type of optimizer to use. Either a subclass of
  `Optimizer`, an instance of an `Optimizer`, a callback that returns an
  optimizer, or a string. Strings must be one of 'Adagrad', 'Adam',
  'Ftrl', 'Momentum', 'RMSProp' or 'SGD. See `layers.optimize_loss` for
  more details.
* <b>`learning_rate`</b>: Learning rate. This argument has no effect if `optimizer`
  is an instance of an `Optimizer`.
* <b>`predict_probabilities`</b>: A boolean indicating whether to predict
  probabilities for all classes. Used only if `problem_type` is
  `ProblemType.CLASSIFICATION`
* <b>`momentum`</b>: Momentum value. Only used if `optimizer_type` is 'Momentum'.
* <b>`gradient_clipping_norm`</b>: Parameter used for gradient clipping. If `None`,
  then no clipping is performed.
* <b>`dropout_keep_probabilities`</b>: a list of dropout probabilities or `None`.
  If a list is given, it must have length `len(num_units) + 1`. If
  `None`, then no dropout is applied.
* <b>`model_dir`</b>: The directory in which to save and restore the model graph,
  parameters, etc.
* <b>`feature_engineering_fn`</b>: Takes features and labels which are the output of
  `input_fn` and returns features and labels which will be fed into
  `model_fn`. Please check `model_fn` for a definition of features and
  labels.
* <b>`config`</b>: A `RunConfig` instance.


#### Raises:


* <b>`ValueError`</b>: `problem_type` is not one of
  `ProblemType.LINEAR_REGRESSION` or `ProblemType.CLASSIFICATION`.
* <b>`ValueError`</b>: `problem_type` is `ProblemType.CLASSIFICATION` but
  `num_classes` is not specified.
* <b>`ValueError`</b>: `prediction_type` is not one of
  `PredictionType.MULTIPLE_VALUE` or `PredictionType.SINGLE_VALUE`.



## Properties

<h3 id="config"><code>config</code></h3>




<h3 id="model_dir"><code>model_dir</code></h3>




<h3 id="model_fn"><code>model_fn</code></h3>

Returns the model_fn which is bound to self.params.


#### Returns:

The model_fn with the following signature:
  `def model_fn(features, labels, mode, metrics)`




## Methods

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

Warning: SOME ARGUMENTS ARE DEPRECATED: `(batch_size, x, y)`. They will be removed after 2016-12-01.
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

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-25.
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

Warning: SOME ARGUMENTS ARE DEPRECATED: `(batch_size, x, y)`. They will be removed after 2016-12-01.
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


* <b>`params`</b>: mapping of string to any
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

Warning: SOME ARGUMENTS ARE DEPRECATED: `(batch_size, x, y)`. They will be removed after 2016-12-01.
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

Warning: SOME ARGUMENTS ARE DEPRECATED: `(as_iterable, batch_size, x)`. They will be removed after 2016-12-01.
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



