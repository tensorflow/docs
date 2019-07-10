page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.feature_column.shared_embedding_columns

List of dense columns that convert from sparse, categorical input.

### Aliases:

* `tf.compat.v1.feature_column.shared_embedding_columns`
* `tf.feature_column.shared_embedding_columns`

``` python
tf.feature_column.shared_embedding_columns(
    categorical_columns,
    dimension,
    combiner='mean',
    initializer=None,
    shared_embedding_collection_name=None,
    ckpt_to_load_from=None,
    tensor_name_in_ckpt=None,
    max_norm=None,
    trainable=True
)
```



Defined in [`python/feature_column/feature_column_v2.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/feature_column/feature_column_v2.py).

<!-- Placeholder for "Used in" -->

This is similar to `embedding_column`, except that it produces a list of
embedding columns that share the same embedding weights.

Use this when your inputs are sparse and of the same type (e.g. watched and
impression video IDs that share the same vocabulary), and you want to convert
them to a dense representation (e.g., to feed to a DNN).

Inputs must be a list of categorical columns created by any of the
`categorical_column_*` function. They must all be of the same type and have
the same arguments except `key`. E.g. they can be
categorical_column_with_vocabulary_file with the same vocabulary_file. Some or
all columns could also be weighted_categorical_column.

Here is an example embedding of two features for a DNNClassifier model:

```python
watched_video_id = categorical_column_with_vocabulary_file(
    'watched_video_id', video_vocabulary_file, video_vocabulary_size)
impression_video_id = categorical_column_with_vocabulary_file(
    'impression_video_id', video_vocabulary_file, video_vocabulary_size)
columns = shared_embedding_columns(
    [watched_video_id, impression_video_id], dimension=10)

estimator = tf.estimator.DNNClassifier(feature_columns=columns, ...)

label_column = ...
def input_fn():
  features = tf.io.parse_example(
      ..., features=make_parse_example_spec(columns + [label_column]))
  labels = features.pop(label_column.name)
  return features, labels

estimator.train(input_fn=input_fn, steps=100)
```

Here is an example using `shared_embedding_columns` with model_fn:

```python
def model_fn(features, ...):
  watched_video_id = categorical_column_with_vocabulary_file(
      'watched_video_id', video_vocabulary_file, video_vocabulary_size)
  impression_video_id = categorical_column_with_vocabulary_file(
      'impression_video_id', video_vocabulary_file, video_vocabulary_size)
  columns = shared_embedding_columns(
      [watched_video_id, impression_video_id], dimension=10)
  dense_tensor = input_layer(features, columns)
  # Form DNN layers, calculate loss, and return EstimatorSpec.
  ...
```

#### Args:


* <b>`categorical_columns`</b>: List of categorical columns created by a
  `categorical_column_with_*` function. These columns produce the sparse IDs
  that are inputs to the embedding lookup. All columns must be of the same
  type and have the same arguments except `key`. E.g. they can be
  categorical_column_with_vocabulary_file with the same vocabulary_file.
  Some or all columns could also be weighted_categorical_column.
* <b>`dimension`</b>: An integer specifying dimension of the embedding, must be > 0.
* <b>`combiner`</b>: A string specifying how to reduce if there are multiple entries in
  a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with
  'mean' the default. 'sqrtn' often achieves good accuracy, in particular
  with bag-of-words columns. Each of this can be thought as example level
  normalizations on the column. For more information, see
  `tf.embedding_lookup_sparse`.
* <b>`initializer`</b>: A variable initializer function to be used in embedding
  variable initialization. If not specified, defaults to
  <a href="../../tf/initializers/truncated_normal"><code>tf.compat.v1.truncated_normal_initializer</code></a> with mean `0.0` and
  standard deviation `1/sqrt(dimension)`.
* <b>`shared_embedding_collection_name`</b>: Optional name of the collection where
  shared embedding weights are added. If not given, a reasonable name will
  be chosen based on the names of `categorical_columns`. This is also used
  in `variable_scope` when creating shared embedding weights.
* <b>`ckpt_to_load_from`</b>: String representing checkpoint name/pattern from which to
  restore column weights. Required if `tensor_name_in_ckpt` is not `None`.
* <b>`tensor_name_in_ckpt`</b>: Name of the `Tensor` in `ckpt_to_load_from` from which
  to restore the column weights. Required if `ckpt_to_load_from` is not
  `None`.
* <b>`max_norm`</b>: If not `None`, each embedding is clipped if its l2-norm is larger
  than this value, before combining.
* <b>`trainable`</b>: Whether or not the embedding is trainable. Default is True.


#### Returns:

A list of dense columns that converts from sparse input. The order of
results follows the ordering of `categorical_columns`.



#### Raises:


* <b>`ValueError`</b>: if `dimension` not > 0.
* <b>`ValueError`</b>: if any of the given `categorical_columns` is of different type
  or has different arguments than the others.
* <b>`ValueError`</b>: if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt`
  is specified.
* <b>`ValueError`</b>: if `initializer` is specified and is not callable.
* <b>`RuntimeError`</b>: if eager execution is enabled.