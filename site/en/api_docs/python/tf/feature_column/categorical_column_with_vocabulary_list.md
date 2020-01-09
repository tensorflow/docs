page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.categorical_column_with_vocabulary_list


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/feature_column/feature_column_v2.py#L1695-L1809">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A `CategoricalColumn` with in-memory vocabulary.

### Aliases:

* `tf.compat.v1.feature_column.categorical_column_with_vocabulary_list`
* `tf.compat.v2.feature_column.categorical_column_with_vocabulary_list`


``` python
tf.feature_column.categorical_column_with_vocabulary_list(
    key,
    vocabulary_list,
    dtype=None,
    default_value=-1,
    num_oov_buckets=0
)
```



### Used in the guide:

* [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)

### Used in the tutorials:

* [Boosted trees using Estimators](https://www.tensorflow.org/tutorials/estimator/boosted_trees)
* [Build a linear model with Estimators](https://www.tensorflow.org/tutorials/estimator/linear)
* [Classify structured data with feature columns](https://www.tensorflow.org/tutorials/structured_data/feature_columns)
* [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)



Use this when your inputs are in string or integer format, and you have an
in-memory vocabulary mapping each value to an integer ID. By default,
out-of-vocabulary values are ignored. Use either (but not both) of
`num_oov_buckets` and `default_value` to specify how to include
out-of-vocabulary values.

For input dictionary `features`, `features[key]` is either `Tensor` or
`SparseTensor`. If `Tensor`, missing values can be represented by `-1` for int
and `''` for string, which will be dropped by this feature column.

Example with `num_oov_buckets`:
In the following example, each input in `vocabulary_list` is assigned an ID
0-3 corresponding to its index (e.g., input 'B' produces output 2). All other
inputs are hashed and assigned an ID 4-5.

```python
colors = categorical_column_with_vocabulary_list(
    key='colors', vocabulary_list=('R', 'G', 'B', 'Y'),
    num_oov_buckets=2)
columns = [colors, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction, _, _ = linear_model(features, columns)
```

Example with `default_value`:
In the following example, each input in `vocabulary_list` is assigned an ID
0-4 corresponding to its index (e.g., input 'B' produces output 3). All other
inputs are assigned `default_value` 0.


```python
colors = categorical_column_with_vocabulary_list(
    key='colors', vocabulary_list=('X', 'R', 'G', 'B', 'Y'), default_value=0)
columns = [colors, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
linear_prediction, _, _ = linear_model(features, columns)
```

And to make an embedding with either:

```python
columns = [embedding_column(colors, 3),...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)
```

#### Args:


* <b>`key`</b>: A unique string identifying the input feature. It is used as the column
  name and the dictionary key for feature parsing configs, feature `Tensor`
  objects, and feature columns.
* <b>`vocabulary_list`</b>: An ordered iterable defining the vocabulary. Each feature
  is mapped to the index of its value (if present) in `vocabulary_list`.
  Must be castable to `dtype`.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported. If
  `None`, it will be inferred from `vocabulary_list`.
* <b>`default_value`</b>: The integer ID value to return for out-of-vocabulary feature
  values, defaults to `-1`. This can not be specified with a positive
  `num_oov_buckets`.
* <b>`num_oov_buckets`</b>: Non-negative integer, the number of out-of-vocabulary
  buckets. All out-of-vocabulary inputs will be assigned IDs in the range
  `[len(vocabulary_list), len(vocabulary_list)+num_oov_buckets)` based on a
  hash of the input value. A positive `num_oov_buckets` can not be specified
  with `default_value`.


#### Returns:

A `CategoricalColumn` with in-memory vocabulary.



#### Raises:


* <b>`ValueError`</b>: if `vocabulary_list` is empty, or contains duplicate keys.
* <b>`ValueError`</b>: `num_oov_buckets` is a negative integer.
* <b>`ValueError`</b>: `num_oov_buckets` and `default_value` are both specified.
* <b>`ValueError`</b>: if `dtype` is not integer or string.
