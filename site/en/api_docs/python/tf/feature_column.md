page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.feature_column



Defined in [`tensorflow/feature_column/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/feature_column/__init__.py).

Public API for tf.feature_column namespace.

## Functions

[`bucketized_column(...)`](../tf/feature_column/bucketized_column): Represents discretized dense input.

[`categorical_column_with_hash_bucket(...)`](../tf/feature_column/categorical_column_with_hash_bucket): Represents sparse feature where ids are set by hashing.

[`categorical_column_with_identity(...)`](../tf/feature_column/categorical_column_with_identity): A `_CategoricalColumn` that returns identity values.

[`categorical_column_with_vocabulary_file(...)`](../tf/feature_column/categorical_column_with_vocabulary_file): A `_CategoricalColumn` with a vocabulary file.

[`categorical_column_with_vocabulary_list(...)`](../tf/feature_column/categorical_column_with_vocabulary_list): A `_CategoricalColumn` with in-memory vocabulary.

[`crossed_column(...)`](../tf/feature_column/crossed_column): Returns a column for performing crosses of categorical features.

[`embedding_column(...)`](../tf/feature_column/embedding_column): `_DenseColumn` that converts from sparse, categorical input.

[`indicator_column(...)`](../tf/feature_column/indicator_column): Represents multi-hot representation of given categorical column.

[`input_layer(...)`](../tf/feature_column/input_layer): Returns a dense `Tensor` as input layer based on given `feature_columns`.

[`linear_model(...)`](../tf/feature_column/linear_model): Returns a linear prediction `Tensor` based on given `feature_columns`.

[`make_parse_example_spec(...)`](../tf/feature_column/make_parse_example_spec): Creates parsing spec dictionary from input feature_columns.

[`numeric_column(...)`](../tf/feature_column/numeric_column): Represents real valued or numerical features.

[`shared_embedding_columns(...)`](../tf/feature_column/shared_embedding_columns): List of dense columns that convert from sparse, categorical input.

[`weighted_categorical_column(...)`](../tf/feature_column/weighted_categorical_column): Applies weight values to a `_CategoricalColumn`.

