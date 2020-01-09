page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.linear_optimizer.SparseFeatureColumn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/linear_optimizer/python/ops/sparse_feature_column.py#L32-L132">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `SparseFeatureColumn`

Represents a sparse feature column.



<!-- Placeholder for "Used in" -->

Contains three tensors representing a sparse feature column, they are
example indices (`int64`), feature indices (`int64`), and feature
values (`float`).
Feature weights are optional, and are treated as `1.0f` if missing.

For example, consider a batch of 4 examples, which contains the following
features in a particular `SparseFeatureColumn`:

* Example 0: feature 5, value 1
* Example 1: feature 6, value 1 and feature 10, value 0.5
* Example 2: no features
* Example 3: two copies of feature 2, value 1

This SparseFeatureColumn will be represented as follows:

```
 <0, 5,  1>
 <1, 6,  1>
 <1, 10, 0.5>
 <3, 2,  1>
 <3, 2,  1>
```

For a batch of 2 examples below:

* Example 0: feature 5
* Example 1: feature 6

is represented by `SparseFeatureColumn` as:

```
 <0, 5,  1>
 <1, 6,  1>

```


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/linear_optimizer/python/ops/sparse_feature_column.py#L77-L105">View source</a>

``` python
__init__(
    example_indices,
    feature_indices,
    feature_values
)
```

Creates a `SparseFeatureColumn` representation. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This class is deprecated. To UPDATE or USE linear optimizers, please check its latest version in core: tensorflow_estimator/python/estimator/canned/linear_optimizer/.

#### Args:


* <b>`example_indices`</b>: A 1-D int64 tensor of shape `[N]`. Also, accepts
python lists, or numpy arrays.
* <b>`feature_indices`</b>: A 1-D int64 tensor of shape `[N]`. Also, accepts
python lists, or numpy arrays.
* <b>`feature_values`</b>: An optional 1-D tensor float tensor of shape `[N]`. Also,
accepts python lists, or numpy arrays.


#### Returns:

A `SparseFeatureColumn`




## Properties

<h3 id="example_indices"><code>example_indices</code></h3>

The example indices represented as a dense tensor.


#### Returns:

A 1-D Tensor of int64 with shape `[N]`.


<h3 id="feature_indices"><code>feature_indices</code></h3>

The feature indices represented as a dense tensor.


#### Returns:

A 1-D Tensor of int64 with shape `[N]`.


<h3 id="feature_values"><code>feature_values</code></h3>

The feature values represented as a dense tensor.


#### Returns:

May return None, or a 1-D Tensor of float32 with shape `[N]`.
