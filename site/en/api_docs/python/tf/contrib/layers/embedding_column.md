page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.embedding_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/feature_column.py#L1303-L1352">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates an `_EmbeddingColumn` for feeding sparse data into a DNN.

``` python
tf.contrib.layers.embedding_column(
    sparse_id_column,
    dimension,
    combiner='mean',
    initializer=None,
    ckpt_to_load_from=None,
    tensor_name_in_ckpt=None,
    max_norm=None,
    trainable=True
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sparse_id_column`</b>: A `_SparseColumn` which is created by for example
  `sparse_column_with_*` or crossed_column functions. Note that `combiner`
  defined in `sparse_id_column` is ignored.
* <b>`dimension`</b>: An integer specifying dimension of the embedding.
* <b>`combiner`</b>: A string specifying how to reduce if there are multiple entries in
  a single row. Currently "mean", "sqrtn" and "sum" are supported, with
  "mean" the default. "sqrtn" often achieves good accuracy, in particular
  with bag-of-words columns. Each of this can be thought as example level
  normalizations on the column:
    * "sum": do not normalize
    * "mean": do l1 normalization
    * "sqrtn": do l2 normalization
  For more information: `tf.embedding_lookup_sparse`.
* <b>`initializer`</b>: A variable initializer function to be used in embedding
  variable initialization. If not specified, defaults to
  <a href="../../../tf/initializers/truncated_normal"><code>tf.compat.v1.truncated_normal_initializer</code></a> with mean 0.0 and standard
  deviation 1/sqrt(sparse_id_column.length).
* <b>`ckpt_to_load_from`</b>: (Optional). String representing checkpoint name/pattern
  to restore the column weights. Required if `tensor_name_in_ckpt` is not
  None.
* <b>`tensor_name_in_ckpt`</b>: (Optional). Name of the `Tensor` in the provided
  checkpoint from which to restore the column weights. Required if
  `ckpt_to_load_from` is not None.
* <b>`max_norm`</b>: (Optional). If not None, embedding values are l2-normalized to the
  value of max_norm.
* <b>`trainable`</b>: (Optional). Should the embedding be trainable. Default is True


#### Returns:

An `_EmbeddingColumn`.
