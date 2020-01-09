page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.bucketized_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/feature_column/feature_column_v2.py#L1340-L1422">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Represents discretized dense input.

### Aliases:

* `tf.compat.v1.feature_column.bucketized_column`
* `tf.compat.v2.feature_column.bucketized_column`


``` python
tf.feature_column.bucketized_column(
    source_column,
    boundaries
)
```



### Used in the tutorials:

* [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)



Buckets include the left boundary, and exclude the right boundary. Namely,
`boundaries=[0., 1., 2.]` generates buckets `(-inf, 0.)`, `[0., 1.)`,
`[1., 2.)`, and `[2., +inf)`.

For example, if the inputs are

```python
boundaries = [0, 10, 100]
input tensor = [[-5, 10000]
                [150,   10]
                [5,    100]]
```

then the output will be

```python
output = [[0, 3]
          [3, 2]
          [1, 3]]
```

#### Example:



```python
price = numeric_column('price')
bucketized_price = bucketized_column(price, boundaries=[...])
columns = [bucketized_price, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)

# or
columns = [bucketized_price, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)
```

`bucketized_column` can also be crossed with another categorical column using
`crossed_column`:

```python
price = numeric_column('price')
# bucketized_column converts numerical feature to a categorical one.
bucketized_price = bucketized_column(price, boundaries=[...])
# 'keywords' is a string feature.
price_x_keywords = crossed_column([bucketized_price, 'keywords'], 50K)
columns = [price_x_keywords, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)
```

#### Args:


* <b>`source_column`</b>: A one-dimensional dense column which is generated with
  `numeric_column`.
* <b>`boundaries`</b>: A sorted list or tuple of floats specifying the boundaries.


#### Returns:

A `BucketizedColumn`.



#### Raises:


* <b>`ValueError`</b>: If `source_column` is not a numeric column, or if it is not
  one-dimensional.
* <b>`ValueError`</b>: If `boundaries` is not a sorted list or tuple.
