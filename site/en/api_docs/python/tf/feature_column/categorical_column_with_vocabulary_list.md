

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.feature_column.categorical_column_with_vocabulary_list

### `tf.feature_column.categorical_column_with_vocabulary_list`

``` python
categorical_column_with_vocabulary_list(
    key,
    vocabulary_list,
    dtype=None,
    default_value=-1
)
```



Defined in [`tensorflow/python/feature_column/feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/feature_column/feature_column.py).

A `_CategoricalColumn` with in-memory vocabulary.

Logic for feature f is:
id = vocabulary_list.index_of(f) if f in vocabulary_list else default_value

Use this when your inputs are in string or integer format, and you have an
in-memory vocabulary mapping each value to an integer ID. By default,
out-of-vocabulary values are ignored. Use `default_value` to specify how to
include out-of-vocabulary values.

For input dictionary `features`, `features[key]` is either `Tensor` or
`SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
and `''` for string. Note that these values are independent of the
`default_value` argument.

In the following examples, each input in `vocabulary_list` is assigned an ID
0-4 corresponding to its index (e.g., input 'B' produces output 2). All other
inputs are assigned `default_value` 0.

Linear model:

```python
colors = categorical_column_with_vocabulary_list(
    key='colors', vocabulary_list=('X', 'R', 'G', 'B', 'Y'), default_value=0)
columns = [colors, ...]
features = tf.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction, _, _ = linear_model(features, columns)
```

Embedding for a DNN model:

```python
columns = [embedding_column(colors, 3),...]
features = tf.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)
```

#### Args:

* <b>`key`</b>: A unique string identifying the input feature. It is used as the
    column name and the dictionary key for feature parsing configs, feature
    `Tensor` objects, and feature columns.
* <b>`vocabulary_list`</b>: An ordered iterable defining the vocabulary. Each feature
    is mapped to the index of its value (if present) in `vocabulary_list`.
    Must be castable to `dtype`.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.
    If `None`, it will be inferred from `vocabulary_list`.
* <b>`default_value`</b>: The value to use for values not in `vocabulary_list`.


#### Returns:

  A `_CategoricalColumn` with in-memory vocabulary.


#### Raises:

* <b>`ValueError`</b>: if `vocabulary_list` is empty, or contains duplicate keys.
* <b>`ValueError`</b>: if `dtype` is not integer or string.