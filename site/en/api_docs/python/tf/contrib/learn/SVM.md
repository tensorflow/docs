

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.SVM

### `class tf.contrib.learn.SVM`



Defined in [`tensorflow/contrib/learn/python/learn/estimators/svm.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/learn/python/learn/estimators/svm.py).

Support Vector Machine (SVM) model for binary classification.

Currently, only linear SVMs are supported. For the underlying optimization
problem, the `SDCAOptimizer` is used. For performance and convergence tuning,
the num_loss_partitions parameter passed to `SDCAOptimizer` (see `__init__()`
method), should be set to (#concurrent train ops per worker) x (#workers). If
num_loss_partitions is larger or equal to this value, convergence is
guaranteed but becomes slower as num_loss_partitions increases. If it is set
to a smaller value, the optimizer is more aggressive in reducing the global
loss but convergence is not guaranteed. The recommended value in tf.learn
(where there is one process per worker) is the number of workers running the
train steps. It defaults to 1 (single machine).

Example:

```python
real_feature_column = real_valued_column(...)
sparse_feature_column = sparse_column_with_hash_bucket(...)

estimator = SVM(
    example_id_column='example_id',
    feature_columns=[real_feature_column, sparse_feature_column],
    l2_regularization=10.0)

# Input builders
def input_fn_train: # returns x, y
  ...
def input_fn_eval: # returns x, y
  ...

estimator.fit(input_fn=input_fn_train)
estimator.evaluate(input_fn=input_fn_eval)
estimator.predict(x=x)
```

Input of `fit` and `evaluate` should have following features, otherwise there
will be a `KeyError`:
  a feature with `key=example_id_column` whose value is a `Tensor` of dtype
  string.
  if `weight_column_name` is not `None`, a feature with
  `key=weight_column_name` whose value is a `Tensor`.
  for each `column` in `feature_columns`:
    - if `column` is a `SparseColumn`, a feature with `key=column.name`
      whose `value` is a `SparseTensor`.
    - if `column` is a `RealValuedColumn, a feature with `key=column.name`
      whose `value` is a `Tensor`.

## Properties

<h3 id="config"><code>config</code></h3>



<h3 id="model_dir"><code>model_dir</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    example_id_column,
    feature_columns,
    weight_column_name=None,
    model_dir=None,
    l1_regularization=0.0,
    l2_regularization=0.0,
    num_loss_partitions=1,
    kernels=None,
    config=None,
    feature_engineering_fn=None
)
```

Constructs an `SVM` estimator object.

#### Args:

* <b>`example_id_column`</b>: A string defining the feature column name representing
    example ids. Used to initialize the underlying optimizer.
* <b>`feature_columns`</b>: An iterable containing all the feature columns used by
    the model. All items in the set should be instances of classes derived
    from `FeatureColumn`.
* <b>`weight_column_name`</b>: A string defining feature column name representing
    weights. It is used to down weight or boost examples during training. It
    will be multiplied by the loss of the example.
* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
    also be used to load checkpoints from the directory into a estimator to
    continue training a previously saved model.
* <b>`l1_regularization`</b>: L1-regularization parameter. Refers to global L1
    regularization (across all examples).
* <b>`l2_regularization`</b>: L2-regularization parameter. Refers to global L2
    regularization (across all examples).
* <b>`num_loss_partitions`</b>: number of partitions of the (global) loss function
    optimized by the underlying optimizer (SDCAOptimizer).
* <b>`kernels`</b>: A list of kernels for the SVM. Currently, no kernels are
    supported. Reserved for future use for non-linear SVMs.
* <b>`config`</b>: RunConfig object to configure the runtime settings.
* <b>`feature_engineering_fn`</b>: Feature engineering function. Takes features and
                    labels which are the output of `input_fn` and
                    returns features and labels which will be fed
                    into the model.


#### Raises:

* <b>`ValueError`</b>: if kernels passed is not None.

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
    signature_fn=None,
    input_fn=None,
    default_batch_size=1,
    exports_to_keep=None
)
```

See BaseEstimator.export. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-25.
Instructions for updating:
Please use Estimator.export_savedmodel() instead.

<h3 id="export_savedmodel"><code>export_savedmodel</code></h3>

``` python
export_savedmodel(
    export_dir_base,
    serving_input_fn,
    default_output_alternative_key=None,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None
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


#### Returns:

  The string path to the exported directory.


#### Raises:

* <b>`ValueError`</b>: if an unrecognized export_type is requested.

<h3 id="export_with_defaults"><code>export_with_defaults</code></h3>

``` python
export_with_defaults(
    export_dir,
    signature_fn=None,
    input_fn=None,
    default_batch_size=1,
    exports_to_keep=None
)
```

Same as BaseEstimator.export, but uses some defaults. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2017-03-25.
Instructions for updating:
Please use Estimator.export_savedmodel() instead.

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

  params : mapping of string to any
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
    as_iterable=True
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


#### Returns:

  A numpy array of predicted classes or regression values if the
  constructor's `model_fn` returns a `Tensor` for `predictions` or a `dict`
  of numpy arrays if `model_fn` returns a `dict`. Returns an iterable of
  predictions if as_iterable is True.


#### Raises:

* <b>`ValueError`</b>: If x and input_fn are both provided or both `None`.

<h3 id="predict_classes"><code>predict_classes</code></h3>

``` python
predict_classes(
    x=None,
    input_fn=None,
    batch_size=None,
    as_iterable=True
)
```

Runs inference to determine the predicted class. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-09-15.
Instructions for updating:
The default behavior of predict() is changing. The default value for
as_iterable will change to True, and then the flag will be removed
altogether. The behavior of this flag is described below.

<h3 id="predict_proba"><code>predict_proba</code></h3>

``` python
predict_proba(
    x=None,
    input_fn=None,
    batch_size=None,
    outputs=None,
    as_iterable=True
)
```

Runs inference to determine the class probability predictions. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed after 2016-09-15.
Instructions for updating:
The default behavior of predict() is changing. The default value for
as_iterable will change to True, and then the flag will be removed
altogether. The behavior of this flag is described below.

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

  **params: Parameters.


#### Returns:

  self


#### Raises:

* <b>`ValueError`</b>: If params contain invalid names.



