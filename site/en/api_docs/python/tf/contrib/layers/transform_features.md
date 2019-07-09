

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.transform_features

``` python
tf.contrib.layers.transform_features(
    features,
    feature_columns
)
```



Defined in [`tensorflow/contrib/layers/python/layers/feature_column_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/layers/python/layers/feature_column_ops.py).

Returns transformed features based on features columns passed in.

Example:

```python
columns_to_tensor = transform_features(features=features,
                                       feature_columns=feature_columns)

# Where my_features are:
# Define features and transformations
sparse_feature_a = sparse_column_with_keys(
    column_name="sparse_feature_a", keys=["AB", "CD", ...])

embedding_feature_a = embedding_column(
    sparse_id_column=sparse_feature_a, dimension=3, combiner="sum")

sparse_feature_b = sparse_column_with_hash_bucket(
    column_name="sparse_feature_b", hash_bucket_size=1000)

embedding_feature_b = embedding_column(
    sparse_id_column=sparse_feature_b, dimension=16, combiner="sum")

crossed_feature_a_x_b = crossed_column(
    columns=[sparse_feature_a, sparse_feature_b], hash_bucket_size=10000)

real_feature = real_valued_column("real_feature")
real_feature_buckets = bucketized_column(
    source_column=real_feature, boundaries=[...])

feature_columns = [embedding_feature_b,
                   real_feature_buckets,
                   embedding_feature_a]
```

#### Args:

* <b>`features`</b>: A dictionary of features.
* <b>`feature_columns`</b>: An iterable containing all the feature columns. All items
    should be instances of classes derived from _FeatureColumn.


#### Returns:

A `dict` mapping FeatureColumn to `Tensor` and `SparseTensor` values.