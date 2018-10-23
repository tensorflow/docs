

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.SKCompat

### `class tf.contrib.learn.SKCompat`



Defined in [`tensorflow/contrib/learn/python/learn/estimators/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/learn/python/learn/estimators/estimator.py).

Scikit learn wrapper for TensorFlow Learn Estimator.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(estimator)
```



<h3 id="fit"><code>fit</code></h3>

``` python
fit(
    x,
    y,
    batch_size=128,
    steps=None,
    max_steps=None,
    monitors=None
)
```



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

<h3 id="predict"><code>predict</code></h3>

``` python
predict(
    x,
    batch_size=128,
    outputs=None
)
```



<h3 id="score"><code>score</code></h3>

``` python
score(
    x,
    y,
    batch_size=128,
    steps=None,
    metrics=None
)
```



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



