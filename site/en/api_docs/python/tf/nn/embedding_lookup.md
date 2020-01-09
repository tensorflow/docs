page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.embedding_lookup


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/embedding_ops.py#L320-L364">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Looks up `ids` in a list of embedding tensors.

### Aliases:

* `tf.compat.v2.nn.embedding_lookup`


``` python
tf.nn.embedding_lookup(
    params,
    ids,
    max_norm=None,
    name=None
)
```



### Used in the guide:

* [Masking and padding with Keras](https://www.tensorflow.org/guide/keras/masking_and_padding)



This function is used to perform parallel lookups on the list of
tensors in `params`.  It is a generalization of
<a href="../../tf/gather"><code>tf.gather</code></a>, where `params` is
interpreted as a partitioning of a large embedding tensor.  `params` may be
a `PartitionedVariable` as returned by using <a href="../../tf/compat/v1/get_variable"><code>tf.compat.v1.get_variable()</code></a>
with a
partitioner.

If `len(params) > 1`, each element `id` of `ids` is partitioned between
the elements of `params` according to the `partition_strategy`.
In all strategies, if the id space does not evenly divide the number of
partitions, each of the first `(max_id + 1) % len(params)` partitions will
be assigned one more id.

The `partition_strategy` is always `"div"` currently. This means that we
assign ids to partitions in a contiguous manner. For instance, 13 ids are
split across 5 partitions as:
`[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10], [11, 12]]`

The results of the lookup are concatenated into a dense
tensor. The returned tensor has shape `shape(ids) + shape(params)[1:]`.

#### Args:


* <b>`params`</b>: A single tensor representing the complete embedding tensor, or a
  list of P tensors all of same shape except for the first dimension,
  representing sharded embedding tensors.  Alternatively, a
  `PartitionedVariable`, created by partitioning along dimension 0. Each
  element must be appropriately sized for the 'div' `partition_strategy`.
* <b>`ids`</b>: A `Tensor` with type `int32` or `int64` containing the ids to be looked
  up in `params`.
* <b>`max_norm`</b>: If not `None`, each embedding is clipped if its l2-norm is larger
  than this value.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` with the same type as the tensors in `params`.



#### Raises:


* <b>`ValueError`</b>: If `params` is empty.
