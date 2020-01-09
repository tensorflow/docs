page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.safe_embedding_lookup_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/embedding_ops.py#L621-L682">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Lookup embedding results, accounting for invalid IDs and empty features.

``` python
tf.compat.v2.nn.safe_embedding_lookup_sparse(
    embedding_weights,
    sparse_ids,
    sparse_weights=None,
    combiner='mean',
    default_id=None,
    max_norm=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The partitioned embedding in `embedding_weights` must all be the same shape
except for the first dimension. The first dimension is allowed to vary as the
vocabulary size is not necessarily a multiple of `P`.  `embedding_weights`
may be a `PartitionedVariable` as returned by using
<a href="../../../../tf/get_variable"><code>tf.compat.v1.get_variable()</code></a> with a
partitioner.

Invalid IDs (< 0) are pruned from input IDs and weights, as well as any IDs
with non-positive weight. For an entry with no features, the embedding vector
for `default_id` is returned, or the 0-vector if `default_id` is not supplied.

The ids and weights may be multi-dimensional. Embeddings are always aggregated
along the last dimension.

Note: when doing embedding lookup on `embedding_weights`, "div" partition
strategy will be used. Support for other partition strategy will be added
later.

#### Args:


* <b>`embedding_weights`</b>:  A list of `P` float `Tensor`s or values representing
  partitioned embedding `Tensor`s.  Alternatively, a `PartitionedVariable`
  created by partitioning along dimension 0.  The total unpartitioned shape
  should be `[e_0, e_1, ..., e_m]`, where `e_0` represents the vocab size
  and `e_1, ..., e_m` are the embedding dimensions.
* <b>`sparse_ids`</b>: `SparseTensor` of shape `[d_0, d_1, ..., d_n]` containing the
  ids. `d_0` is typically batch size.
* <b>`sparse_weights`</b>: `SparseTensor` of same shape as `sparse_ids`, containing
  float weights corresponding to `sparse_ids`, or `None` if all weights are
  be assumed to be 1.0.
* <b>`combiner`</b>: A string specifying how to combine embedding results for each
  entry. Currently "mean", "sqrtn" and "sum" are supported, with "mean" the
  default.
* <b>`default_id`</b>: The id to use for an entry with no features.
* <b>`max_norm`</b>: If not `None`, all embeddings are l2-normalized to max_norm before
  combining.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Dense `Tensor` of shape `[d_0, d_1, ..., d_{n-1}, e_1, ..., e_m]`.



#### Raises:


* <b>`ValueError`</b>: if `embedding_weights` is empty.
