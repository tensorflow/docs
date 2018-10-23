

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.feature_column.indicator_column

``` python
tf.feature_column.indicator_column(categorical_column)
```



Defined in [`tensorflow/python/feature_column/feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/feature_column/feature_column.py).

Represents multi-hot representation of given categorical column.

Used to wrap any `categorical_column_*` (e.g., to feed to DNN). Use
`embedding_column` if the inputs are sparse.

```python
name = indicator_column(categorical_column_with_vocabulary_list(
    'name', ['bob', 'george', 'wanda'])
columns = [name, ...]
features = tf.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)

dense_tensor == [[1, 0, 0]]  # If "name" bytes_list is ["bob"]
dense_tensor == [[1, 0, 1]]  # If "name" bytes_list is ["bob", "wanda"]
dense_tensor == [[2, 0, 0]]  # If "name" bytes_list is ["bob", "bob"]
```

#### Args:

* <b>`categorical_column`</b>: A `_CategoricalColumn` which is created by
    `categorical_column_with_*` or `crossed_column` functions.


#### Returns:

An `_IndicatorColumn`.