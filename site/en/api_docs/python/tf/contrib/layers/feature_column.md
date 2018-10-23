

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.layers.feature_column



Defined in [`tensorflow/contrib/layers/python/layers/feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/layers/python/layers/feature_column.py).

This API defines FeatureColumn abstraction.

FeatureColumns provide a high level abstraction for ingesting and representing
features in `Estimator` models.

FeatureColumns are the primary way of encoding features for pre-canned
`Estimator` models.

When using FeatureColumns with `Estimator` models, the type of feature column
you should choose depends on (1) the feature type and (2) the model type.

(1) Feature type:

 * Continuous features can be represented by `real_valued_column`.
 * Categorical features can be represented by any `sparse_column_with_*`
 column (`sparse_column_with_keys`, `sparse_column_with_vocabulary_file`,
 `sparse_column_with_hash_bucket`, `sparse_column_with_integerized_feature`).

(2) Model type:

 * Deep neural network models (`DNNClassifier`, `DNNRegressor`).

   Continuous features can be directly fed into deep neural network models.

     age_column = real_valued_column("age")

   To feed sparse features into DNN models, wrap the column with
   `embedding_column` or `one_hot_column`. `one_hot_column` will create a dense
   boolean tensor with an entry for each possible value, and thus the
   computation cost is linear in the number of possible values versus the number
   of values that occur in the sparse tensor. Thus using a "one_hot_column" is
   only recommended for features with only a few possible values. For features
   with many possible values or for very sparse features, `embedding_column` is
   recommended.

     embedded_dept_column = embedding_column(
       sparse_column_with_keys("department", ["math", "philosphy", ...]),
       dimension=10)

* Wide (aka linear) models (`LinearClassifier`, `LinearRegressor`).

   Sparse features can be fed directly into linear models. When doing so
   an embedding_lookups are used to efficiently perform the sparse matrix
   multiplication.

     dept_column = sparse_column_with_keys("department",
       ["math", "philosophy", "english"])

   It is recommended that continuous features be bucketized before being
   fed into linear models.

     bucketized_age_column = bucketized_column(
      source_column=age_column,
      boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])

   Sparse features can be crossed (also known as conjuncted or combined) in
   order to form non-linearities, and then fed into linear models.

    cross_dept_age_column = crossed_column(
      columns=[department_column, bucketized_age_column],
      hash_bucket_size=1000)

Example of building an `Estimator` model using FeatureColumns:

  # Define features and transformations
  deep_feature_columns = [age_column, embedded_dept_column]
  wide_feature_columns = [dept_column, bucketized_age_column,
      cross_dept_age_column]

  # Build deep model
  estimator = DNNClassifier(
      feature_columns=deep_feature_columns,
      hidden_units=[500, 250, 50])
  estimator.train(...)

  # Or build a wide model
  estimator = LinearClassifier(
      feature_columns=wide_feature_columns)
  estimator.train(...)

  # Or build a wide and deep model!
  estimator = DNNLinearCombinedClassifier(
      linear_feature_columns=wide_feature_columns,
      dnn_feature_columns=deep_feature_columns,
      dnn_hidden_units=[500, 250, 50])
  estimator.train(...)


FeatureColumns can also be transformed into a generic input layer for
custom models using `input_from_feature_columns` within
`feature_column_ops.py`.

Example of building a non-`Estimator` model using FeatureColumns:

  # Building model via layers

  deep_feature_columns = [age_column, embedded_dept_column]
  columns_to_tensor = parse_feature_columns_from_examples(
      serialized=my_data,
      feature_columns=deep_feature_columns)
  first_layer = input_from_feature_columns(
      columns_to_tensors=columns_to_tensor,
      feature_columns=deep_feature_columns)
  second_layer = fully_connected(first_layer, ...)

See feature_column_ops_test for more examples.

