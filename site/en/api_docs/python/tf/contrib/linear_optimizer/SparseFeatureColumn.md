

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.linear_optimizer.SparseFeatureColumn

### `class tf.contrib.linear_optimizer.SparseFeatureColumn`



Defined in [`tensorflow/contrib/linear_optimizer/python/ops/sparse_feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/linear_optimizer/python/ops/sparse_feature_column.py).

Represents a sparse feature column.

Contains three tensors representing a sparse feature column, they are
example indices (int64), feature indices (int64), and feature values (float).
Feature weights are optional, and are treated as 1.0f if missing.

For example, consider a batch of 4 examples, which contains the following
features in a particular SparseFeatureColumn:
 Example 0: feature 5, value 1
 Example 1: feature 6, value 1 and feature 10, value 0.5
 Example 2: no features
 Example 3: two copies of feature 2, value 1

This SparseFeatureColumn will be represented as follows:
 <0, 5,  1>
 <1, 6,  1>
 <1, 10, 0.5>
 <3, 2,  1>
 <3, 2,  1>

For a batch of 2 examples below:
 Example 0: feature 5
 Example 1: feature 6

is represented by SparseFeatureColumn as:
 <0, 5,  1>
 <1, 6,  1>

```


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



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    example_indices,
    feature_indices,
    feature_values
)
```

Creates a `SparseFeatureColumn` representation.

#### Args:

* <b>`example_indices`</b>: A 1-D int64 tensor of shape `[N]`. Also, accepts
  python lists, or numpy arrays.
* <b>`feature_indices`</b>: A 1-D int64 tensor of shape `[N]`. Also, accepts
  python lists, or numpy arrays.
* <b>`feature_values`</b>: An optional 1-D tensor float tensor of shape `[N]`. Also,
  accepts python lists, or numpy arrays.


#### Returns:

  A `SparseFeatureColumn`



