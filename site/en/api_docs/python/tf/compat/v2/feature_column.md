page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.feature_column

Public API for tf.feature_column namespace.

<!-- Placeholder for "Used in" -->


## Functions

[`bucketized_column(...)`](../../../tf/feature_column/bucketized_column): Represents discretized dense input.

[`categorical_column_with_hash_bucket(...)`](../../../tf/feature_column/categorical_column_with_hash_bucket): Represents sparse feature where ids are set by hashing.

[`categorical_column_with_identity(...)`](../../../tf/feature_column/categorical_column_with_identity): A `CategoricalColumn` that returns identity values.

[`categorical_column_with_vocabulary_file(...)`](../../../tf/compat/v2/feature_column/categorical_column_with_vocabulary_file): A `CategoricalColumn` with a vocabulary file.

[`categorical_column_with_vocabulary_list(...)`](../../../tf/feature_column/categorical_column_with_vocabulary_list): A `CategoricalColumn` with in-memory vocabulary.

[`crossed_column(...)`](../../../tf/feature_column/crossed_column): Returns a column for performing crosses of categorical features.

[`embedding_column(...)`](../../../tf/feature_column/embedding_column): `DenseColumn` that converts from sparse, categorical input.

[`indicator_column(...)`](../../../tf/feature_column/indicator_column): Represents multi-hot representation of given categorical column.

[`make_parse_example_spec(...)`](../../../tf/compat/v2/feature_column/make_parse_example_spec): Creates parsing spec dictionary from input feature_columns.

[`numeric_column(...)`](../../../tf/feature_column/numeric_column): Represents real valued or numerical features.

[`sequence_categorical_column_with_hash_bucket(...)`](../../../tf/feature_column/sequence_categorical_column_with_hash_bucket): A sequence of categorical terms where ids are set by hashing.

[`sequence_categorical_column_with_identity(...)`](../../../tf/feature_column/sequence_categorical_column_with_identity): Returns a feature column that represents sequences of integers.

[`sequence_categorical_column_with_vocabulary_file(...)`](../../../tf/feature_column/sequence_categorical_column_with_vocabulary_file): A sequence of categorical terms where ids use a vocabulary file.

[`sequence_categorical_column_with_vocabulary_list(...)`](../../../tf/feature_column/sequence_categorical_column_with_vocabulary_list): A sequence of categorical terms where ids use an in-memory list.

[`sequence_numeric_column(...)`](../../../tf/feature_column/sequence_numeric_column): Returns a feature column that represents sequences of numeric data.

[`shared_embeddings(...)`](../../../tf/compat/v2/feature_column/shared_embeddings): List of dense columns that convert from sparse, categorical input.

[`weighted_categorical_column(...)`](../../../tf/feature_column/weighted_categorical_column): Applies weight values to a `CategoricalColumn`.

