page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.BaseEstimator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L396-L1096">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `BaseEstimator`

Abstract BaseEstimator class to train and evaluate TensorFlow models.

Inherits From: [`Evaluable`](../../../tf/contrib/learn/Evaluable), [`Trainable`](../../../tf/contrib/learn/Trainable)

<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.tensorflow.org/code/tensorflow/contrib/learn/README.md)
for general migration instructions.

Users should not instantiate or subclass this class. Instead, use an
`Estimator`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L413-L466">View source</a>

``` python
__init__(
    model_dir=None,
    config=None
)
```

Initializes a BaseEstimator instance. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please replace uses of any Estimator from tf.contrib.learn with an Estimator from tf.estimator.*

#### Args:


* <b>`model_dir`</b>: Directory to save model parameters, graph and etc. This can
  also be used to load checkpoints from the directory into a estimator to
  continue training a previously saved model. If `None`, the model_dir in
  `config` will be used if set. If both are set, they must be same.
* <b>`config`</b>: A RunConfig instance.



## Properties

<h3 id="config"><code>config</code></h3>




<h3 id="model_dir"><code>model_dir</code></h3>

Returns a path in which the eval process will look for checkpoints.


<h3 id="model_fn"><code>model_fn</code></h3>

Returns the model_fn which is bound to self.params.


#### Returns:

The model_fn with the following signature:
  `def model_fn(features, labels, mode, metrics)`




## Methods

<h3 id="evaluate"><code>evaluate</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L580-L621">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L695-L754">View source</a>

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


<h3 id="fit"><code>fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L487-L526">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/_sklearn.py#L41-L67">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L683-L689">View source</a>

``` python
get_variable_names()
```

Returns list of all variable names in this model.


#### Returns:

List of names.


<h3 id="get_variable_value"><code>get_variable_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L672-L681">View source</a>

``` python
get_variable_value(name)
```

Returns value of the variable given by name.


#### Args:


* <b>`name`</b>: string, name of the tensor.


#### Returns:

Numpy array - value of the tensor.


<h3 id="partial_fit"><code>partial_fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L528-L578">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L623-L670">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/_sklearn.py#L69-L110">View source</a>

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
