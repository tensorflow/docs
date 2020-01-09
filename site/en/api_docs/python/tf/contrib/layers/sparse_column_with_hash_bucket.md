page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.sparse_column_with_hash_bucket


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/feature_column.py#L596-L638">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a _SparseColumn with hashed bucket configuration.

``` python
tf.contrib.layers.sparse_column_with_hash_bucket(
    column_name,
    hash_bucket_size,
    combiner='sum',
    dtype=tf.dtypes.string,
    hash_keys=None
)
```



<!-- Placeholder for "Used in" -->

Use this when your sparse features are in string or integer format, but you
don't have a vocab file that maps each value to an integer ID.
output_id = Hash(input_feature_string) % bucket_size

When hash_keys is set, multiple integer IDs would be created with each key
pair in the `hash_keys`. This is useful to reduce the collision of hashed ids.

#### Args:


* <b>`column_name`</b>: A string defining sparse column name.
* <b>`hash_bucket_size`</b>: An int that is > 1. The number of buckets.
* <b>`combiner`</b>: A string specifying how to reduce if the sparse column is
  multivalent. Currently "mean", "sqrtn" and "sum" are supported, with "sum"
  the default. "sqrtn" often achieves good accuracy, in particular with
  bag-of-words columns.
    * "sum": do not normalize features in the column
    * "mean": do l1 normalization on features in the column
    * "sqrtn": do l2 normalization on features in the column
  For more information: `tf.embedding_lookup_sparse`.
* <b>`dtype`</b>: The type of features. Only string and integer types are supported.
* <b>`hash_keys`</b>: The hash keys to use. It is a list of lists of two uint64s. If
  None, simple and fast hashing algorithm is used. Otherwise, multiple
  strong hash ids would be produced with each two uint64s in this argument.


#### Returns:

A _SparseColumn with hashed bucket configuration



#### Raises:


* <b>`ValueError`</b>: hash_bucket_size is not greater than 2.
* <b>`ValueError`</b>: dtype is neither string nor integer.
