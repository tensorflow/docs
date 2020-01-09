page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.wrappers.scikit_learn.KerasClassifier


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L191-L310">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `KerasClassifier`

Implementation of the scikit-learn classifier API for Keras.



### Aliases:

* Class `tf.compat.v1.keras.wrappers.scikit_learn.KerasClassifier`
* Class `tf.compat.v2.keras.wrappers.scikit_learn.KerasClassifier`


<!-- Placeholder for "Used in" -->
  

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L74-L77">View source</a>

``` python
__init__(
    build_fn=None,
    **sk_params
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="check_params"><code>check_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L79-L106">View source</a>

``` python
check_params(params)
```

Checks for user typos in `params`.


#### Arguments:


* <b>`params`</b>: dictionary; the parameters to be checked


#### Raises:


* <b>`ValueError`</b>: if any member of `params` is not a valid argument.

<h3 id="filter_sk_params"><code>filter_sk_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L170-L187">View source</a>

``` python
filter_sk_params(
    fn,
    override=None
)
```

Filters `sk_params` and returns those in `fn`'s arguments.


#### Arguments:


* <b>`fn`</b>: arbitrary function
* <b>`override`</b>: dictionary, values to override `sk_params`


#### Returns:


* <b>`res`</b>: dictionary containing variables
    in both `sk_params` and `fn`'s arguments.

<h3 id="fit"><code>fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L195-L223">View source</a>

``` python
fit(
    x,
    y,
    **kwargs
)
```

Constructs a new model with `build_fn` & fit the model to `(x, y)`.


#### Arguments:


* <b>`x`</b>: array-like, shape `(n_samples, n_features)`
    Training samples where `n_samples` is the number of samples
    and `n_features` is the number of features.
* <b>`y`</b>: array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
    True labels for `x`.
* <b>`**kwargs`</b>: dictionary arguments
    Legal arguments are the arguments of <a href="../../../../tf/keras/Model#fit"><code>Sequential.fit</code></a>


#### Returns:


* <b>`history`</b>: object
    details about the training history at each epoch.


#### Raises:


* <b>`ValueError`</b>: In case of invalid shape for `y` argument.

<h3 id="get_params"><code>get_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L108-L119">View source</a>

``` python
get_params(**params)
```

Gets parameters for this estimator.


#### Arguments:


* <b>`**params`</b>: ignored (exists for API compatibility).


#### Returns:

Dictionary of parameter names mapped to their values.


<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L225-L242">View source</a>

``` python
predict(
    x,
    **kwargs
)
```

Returns the class predictions for the given test data.


#### Arguments:


* <b>`x`</b>: array-like, shape `(n_samples, n_features)`
    Test samples where `n_samples` is the number of samples
    and `n_features` is the number of features.
* <b>`**kwargs`</b>: dictionary arguments
    Legal arguments are the arguments
    of <a href="../../../../tf/keras/Sequential#predict_classes"><code>Sequential.predict_classes</code></a>.


#### Returns:


* <b>`preds`</b>: array-like, shape `(n_samples,)`
    Class predictions.

<h3 id="predict_proba"><code>predict_proba</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L244-L270">View source</a>

``` python
predict_proba(
    x,
    **kwargs
)
```

Returns class probability estimates for the given test data.


#### Arguments:


* <b>`x`</b>: array-like, shape `(n_samples, n_features)`
    Test samples where `n_samples` is the number of samples
    and `n_features` is the number of features.
* <b>`**kwargs`</b>: dictionary arguments
    Legal arguments are the arguments
    of <a href="../../../../tf/keras/Sequential#predict_classes"><code>Sequential.predict_classes</code></a>.


#### Returns:


* <b>`proba`</b>: array-like, shape `(n_samples, n_outputs)`
    Class probability estimates.
    In the case of binary classification,
    to match the scikit-learn API,
    will return an array of shape `(n_samples, 2)`
    (instead of `(n_sample, 1)` as in Keras).

<h3 id="score"><code>score</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L272-L310">View source</a>

``` python
score(
    x,
    y,
    **kwargs
)
```

Returns the mean accuracy on the given test data and labels.


#### Arguments:


* <b>`x`</b>: array-like, shape `(n_samples, n_features)`
    Test samples where `n_samples` is the number of samples
    and `n_features` is the number of features.
* <b>`y`</b>: array-like, shape `(n_samples,)` or `(n_samples, n_outputs)`
    True labels for `x`.
* <b>`**kwargs`</b>: dictionary arguments
    Legal arguments are the arguments of <a href="../../../../tf/keras/Model#evaluate"><code>Sequential.evaluate</code></a>.


#### Returns:


* <b>`score`</b>: float
    Mean accuracy of predictions on `x` wrt. `y`.


#### Raises:


* <b>`ValueError`</b>: If the underlying model isn't configured to
    compute accuracy. You should pass `metrics=["accuracy"]` to
    the `.compile()` method of the model.

<h3 id="set_params"><code>set_params</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/wrappers/scikit_learn.py#L121-L132">View source</a>

``` python
set_params(**params)
```

Sets the parameters of this estimator.


#### Arguments:


* <b>`**params`</b>: Dictionary of parameter names mapped to their values.


#### Returns:

self
