page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.numeric_column

``` python
tf.feature_column.numeric_column(
    key,
    shape=(1,),
    default_value=None,
    dtype=tf.float32,
    normalizer_fn=None
)
```



Defined in [`tensorflow/python/feature_column/feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/feature_column/feature_column.py).

Represents real valued or numerical features.

Example:

```python
price = numeric_column('price')
columns = [price, ...]
features = tf.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)

# or
bucketized_price = bucketized_column(price, boundaries=[...])
columns = [bucketized_price, ...]
features = tf.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction = linear_model(features, columns)
```

#### Args:

* <b>`key`</b>: A unique string identifying the input feature. It is used as the
    column name and the dictionary key for feature parsing configs, feature
    `Tensor` objects, and feature columns.
* <b>`shape`</b>: An iterable of integers specifies the shape of the `Tensor`. An
    integer can be given which means a single dimension `Tensor` with given
    width. The `Tensor` representing the column will have the shape of
    [batch_size] + `shape`.
* <b>`default_value`</b>: A single value compatible with `dtype` or an iterable of
    values compatible with `dtype` which the column takes on during
    `tf.Example` parsing if data is missing. A default value of `None` will
    cause <a href="../../tf/parse_example"><code>tf.parse_example</code></a> to fail if an example does not contain this
    column. If a single value is provided, the same value will be applied as
    the default value for every item. If an iterable of values is provided,
    the shape of the `default_value` should be equal to the given `shape`.
* <b>`dtype`</b>: defines the type of values. Default value is <a href="../../tf/float32"><code>tf.float32</code></a>. Must be a
    non-quantized, real integer or floating point type.
* <b>`normalizer_fn`</b>: If not `None`, a function that can be used to normalize the
    value of the tensor after `default_value` is applied for parsing.
    Normalizer function takes the input `Tensor` as its argument, and returns
    the output `Tensor`. (e.g. lambda x: (x - 3.0) / 4.2). Please note that
    even though the most common use case of this function is normalization, it
    can be used for any kind of Tensorflow transformations.


#### Returns:

A `_NumericColumn`.


#### Raises:

* <b>`TypeError`</b>: if any dimension in shape is not an int
* <b>`ValueError`</b>: if any dimension in shape is not a positive integer
* <b>`TypeError`</b>: if `default_value` is an iterable but not compatible with `shape`
* <b>`TypeError`</b>: if `default_value` is not compatible with `dtype`.
* <b>`ValueError`</b>: if `dtype` is not convertible to <a href="../../tf/float32"><code>tf.float32</code></a>.