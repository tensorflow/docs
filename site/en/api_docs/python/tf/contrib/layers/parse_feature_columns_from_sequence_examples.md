page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.parse_feature_columns_from_sequence_examples

Parses tf.SequenceExamples to extract tensors for given `FeatureColumn`s.

``` python
tf.contrib.layers.parse_feature_columns_from_sequence_examples(
    serialized,
    context_feature_columns,
    sequence_feature_columns,
    name=None,
    example_name=None
)
```



Defined in [`contrib/layers/python/layers/feature_column_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/feature_column_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`serialized`</b>: A scalar (0-D Tensor) of type string, a single serialized
  `SequenceExample` proto.
* <b>`context_feature_columns`</b>: An iterable containing the feature columns for
  context features. All items should be instances of classes derived from
  `_FeatureColumn`. Can be `None`.
* <b>`sequence_feature_columns`</b>: An iterable containing the feature columns for
  sequence features. All items should be instances of classes derived from
  `_FeatureColumn`. Can be `None`.
* <b>`name`</b>: A name for this operation (optional).
* <b>`example_name`</b>: A scalar (0-D Tensor) of type string (optional), the names of
  the serialized proto.


#### Returns:

A tuple consisting of (context_features, sequence_features)

*  context_features: a dict mapping `FeatureColumns` from
    `context_feature_columns` to their parsed `Tensors`/`SparseTensor`s.
*  sequence_features: a dict mapping `FeatureColumns` from
    `sequence_feature_columns` to their parsed `Tensors`/`SparseTensor`s.
