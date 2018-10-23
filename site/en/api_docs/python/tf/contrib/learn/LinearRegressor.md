


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.LinearRegressor

### `class tf.contrib.learn.LinearRegressor`

See the guide: [Learn (contrib) > Estimators](../../../../../api_guides/python/contrib.learn#Estimators)

Linear regressor model.

Train a linear regression model to predict label value given observation of
feature values.

Example:

```python
sparse_column_a = sparse_column_with_hash_bucket(...)
sparse_column_b = sparse_column_with_hash_bucket(...)

sparse_feature_a_x_sparse_feature_b = crossed_column(...)

estimator = LinearRegressor(
    feature_columns=[sparse_column_a, sparse_feature_a_x_sparse_feature_b])

# Input builders
def input_fn_train: # returns x, y
  ...
def input_fn_eval: # returns x, y
  ...
estimator.fit(input_fn=input_fn_train)
estimator.evaluate(input_fn=input_fn_eval)
estimator.predict(x=x)
```

Input of `fit` and `evaluate` should have following features,
  otherwise there will be a KeyError:

* if `weight_column_name` is not `None`:
  key=weight_column_name, value=a `Tensor`
* for column in `feature_columns`:
  - if isinstance(column, `SparseColumn`):
      key=column.name, value=a `SparseTensor`
  - if isinstance(column, `WeightedSparseColumn`):
      {key=id column name, value=a `SparseTensor`,
       key=weight column name, value=a `SparseTensor`}
  - if isinstance(column, `RealValuedColumn`):
      key=column.name, value=a `Tensor`

## Properties

<h3 id="bias_"><code>bias_</code></h3>

DEPRECATED FUNCTION

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-10-30.
Instructions for updating:
This method will be removed after the deprecation date. To inspect variables, use get_variable_names() and get_variable_value().

<h3 id="config"><code>config</code></h3>



<h3 id="model_dir"><code>model_dir</code></h3>



<h3 id="weights_"><code>weights_</code></h3>

DEPRECATED FUNCTION

THIS FUNCTION IS DEPRECATED. It will be removed after 2016-10-30.
Instructions for updating:
This method will be removed after the deprecation date. To inspect variables, use get_variable_names() and get_variable_value().



## Methods

<h3 id="__init__"><code>__init__(feature_columns, model_dir=None, weight_column_name=None, optimizer=None, gradient_clip_norm=None, enable_centered_bias=False, label_dimension=1, _joint_weights=False, config=None, feature_engineering_fn=None)</code></h3>

Construct a `LinearRegressor` estimator object.

#### Args:

* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
    the model. All items in the set should be instances of classes derived
    from `FeatureColumn`.
* <b>`model_dir`</b>: Directory to save model parameters, graph, etc. This can
    also be used to load checkpoints from the directory into a estimator
    to continue training a previously saved model.
* <b>`weight_column_name`</b>: A string defining feature column name representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`optimizer`</b>: An instance of `tf.Optimizer` used to train the model. If
    `None`, will use an Ftrl optimizer.
* <b>`gradient_clip_norm`</b>: A `float` > 0. If provided, gradients are clipped
    to their global norm with this clipping ratio. See
    `tf.clip_by_global_norm` for more details.
* <b>`enable_centered_bias`</b>: A bool. If True, estimator will learn a centered
    bias variable for each class. Rest of the model structure learns the
    residual after centered bias.
* <b>`label_dimension`</b>: Dimension of the label for multilabels. Defaults to 1.
* <b>`_joint_weights`</b>: If True use a single (possibly partitioned) variable to
    store the weights. It's faster, but requires all feature columns are
    sparse and have the 'sum' combiner. Incompatible with SDCAOptimizer.
* <b>`config`</b>: `RunConfig` object to configure the runtime settings.
* <b>`feature_engineering_fn`</b>: Feature engineering function. Takes features and
                    labels which are the output of `input_fn` and
                    returns features and labels which will be fed
                    into the model.


#### Returns:

  A `LinearRegressor` estimator.

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

<h3 id="export"><code>export(export_dir, input_fn=None, input_feature_key=None, use_deprecated_input_fn=True, signature_fn=None, default_batch_size=1, exports_to_keep=None)</code></h3>

See BaseEstimator.export.

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

Runs inference to determine the predicted scores. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-09-15.
Instructions for updating:
The default behavior of predict() is changing. The default value for
as_iterable will change to True, and then the flag will be removed
altogether. The behavior of this flag is described below.

<h3 id="predict_scores"><code>predict_scores(*args, **kwargs)</code></h3>

Runs inference to determine the predicted scores. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-09-15.
Instructions for updating:
The default behavior of predict() is changing. The default value for
as_iterable will change to True, and then the flag will be removed
altogether. The behavior of this flag is described below.

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





Defined in [`tensorflow/contrib/learn/python/learn/estimators/linear.py`](https://www.tensorflow.org/code/tensorflow/contrib/learn/python/learn/estimators/linear.py).

