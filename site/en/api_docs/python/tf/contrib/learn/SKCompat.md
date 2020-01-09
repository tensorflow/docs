page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.SKCompat


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L1495-L1573">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SKCompat`

Scikit learn wrapper for TensorFlow Learn Estimator.



<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED. See
[contrib/learn/README.md](https://www.tensorflow.org/code/tensorflow/contrib/learn/README.md)
for general migration instructions.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L1503-L1505">View source</a>

``` python
__init__(estimator)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please switch to the Estimator interface.



## Methods

<h3 id="fit"><code>fit</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L1507-L1528">View source</a>

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

<h3 id="predict"><code>predict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L1552-L1573">View source</a>

``` python
predict(
    x,
    batch_size=128,
    outputs=None
)
```




<h3 id="score"><code>score</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L1530-L1550">View source</a>

``` python
score(
    x,
    y,
    batch_size=128,
    steps=None,
    metrics=None,
    name=None
)
```




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
