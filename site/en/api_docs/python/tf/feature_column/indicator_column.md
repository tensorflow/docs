page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.indicator_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/feature_column/indicator_column">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/feature_column/feature_column_v2.py#L1870-L1902">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Represents multi-hot representation of given categorical column.

### Aliases:

* <a href="/api_docs/python/tf/feature_column/indicator_column"><code>tf.compat.v1.feature_column.indicator_column</code></a>
* <a href="/api_docs/python/tf/feature_column/indicator_column"><code>tf.compat.v2.feature_column.indicator_column</code></a>


``` python
tf.feature_column.indicator_column(categorical_column)
```



<!-- Placeholder for "Used in" -->

- For DNN model, `indicator_column` can be used to wrap any
  `categorical_column_*` (e.g., to feed to DNN). Consider to Use
  `embedding_column` if the number of buckets/unique(values) are large.

- For Wide (aka linear) model, `indicator_column` is the internal
  representation for categorical column when passing categorical column
  directly (as any element in feature_columns) to `linear_model`. See
  `linear_model` for details.

```python
name = indicator_column(categorical_column_with_vocabulary_list(
    'name', ['bob', 'george', 'wanda'])
columns = [name, ...]
features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = input_layer(features, columns)

dense_tensor == [[1, 0, 0]]  # If "name" bytes_list is ["bob"]
dense_tensor == [[1, 0, 1]]  # If "name" bytes_list is ["bob", "wanda"]
dense_tensor == [[2, 0, 0]]  # If "name" bytes_list is ["bob", "bob"]
```

#### Args:


* <b>`categorical_column`</b>: A `CategoricalColumn` which is created by
  `categorical_column_with_*` or `crossed_column` functions.


#### Returns:

An `IndicatorColumn`.
