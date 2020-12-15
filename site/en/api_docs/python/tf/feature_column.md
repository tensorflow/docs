description: Public API for tf.feature_column namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.feature_column" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.feature_column

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.feature_column namespace.



## Functions

[`bucketized_column(...)`](../tf/feature_column/bucketized_column.md): Represents discretized dense input bucketed by `boundaries`.

[`categorical_column_with_hash_bucket(...)`](../tf/feature_column/categorical_column_with_hash_bucket.md): Represents sparse feature where ids are set by hashing.

[`categorical_column_with_identity(...)`](../tf/feature_column/categorical_column_with_identity.md): A `CategoricalColumn` that returns identity values.

[`categorical_column_with_vocabulary_file(...)`](../tf/feature_column/categorical_column_with_vocabulary_file.md): A `CategoricalColumn` with a vocabulary file.

[`categorical_column_with_vocabulary_list(...)`](../tf/feature_column/categorical_column_with_vocabulary_list.md): A `CategoricalColumn` with in-memory vocabulary.

[`crossed_column(...)`](../tf/feature_column/crossed_column.md): Returns a column for performing crosses of categorical features.

[`embedding_column(...)`](../tf/feature_column/embedding_column.md): `DenseColumn` that converts from sparse, categorical input.

[`indicator_column(...)`](../tf/feature_column/indicator_column.md): Represents multi-hot representation of given categorical column.

[`make_parse_example_spec(...)`](../tf/feature_column/make_parse_example_spec.md): Creates parsing spec dictionary from input feature_columns.

[`numeric_column(...)`](../tf/feature_column/numeric_column.md): Represents real valued or numerical features.

[`sequence_categorical_column_with_hash_bucket(...)`](../tf/feature_column/sequence_categorical_column_with_hash_bucket.md): A sequence of categorical terms where ids are set by hashing.

[`sequence_categorical_column_with_identity(...)`](../tf/feature_column/sequence_categorical_column_with_identity.md): Returns a feature column that represents sequences of integers.

[`sequence_categorical_column_with_vocabulary_file(...)`](../tf/feature_column/sequence_categorical_column_with_vocabulary_file.md): A sequence of categorical terms where ids use a vocabulary file.

[`sequence_categorical_column_with_vocabulary_list(...)`](../tf/feature_column/sequence_categorical_column_with_vocabulary_list.md): A sequence of categorical terms where ids use an in-memory list.

[`sequence_numeric_column(...)`](../tf/feature_column/sequence_numeric_column.md): Returns a feature column that represents sequences of numeric data.

[`shared_embeddings(...)`](../tf/feature_column/shared_embeddings.md): List of dense columns that convert from sparse, categorical input.

[`weighted_categorical_column(...)`](../tf/feature_column/weighted_categorical_column.md): Applies weight values to a `CategoricalColumn`.

