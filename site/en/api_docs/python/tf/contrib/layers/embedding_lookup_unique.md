page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.embedding_lookup_unique

Version of embedding_lookup that avoids duplicate lookups.

``` python
tf.contrib.layers.embedding_lookup_unique(
    params,
    ids,
    partition_strategy='mod',
    name=None
)
```



Defined in [`contrib/layers/python/layers/embedding_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/embedding_ops.py).

<!-- Placeholder for "Used in" -->

This can save communication in the case of repeated ids.
Same interface as embedding_lookup. Except it supports multi-dimensional `ids`
which allows to not reshape input/output to fit gather.

#### Args:


* <b>`params`</b>: A list of tensors with the same shape and type, or a
  `PartitionedVariable`. Shape `[index, d1, d2, ...]`.
* <b>`ids`</b>: A one-dimensional `Tensor` with type `int32` or `int64` containing the
  ids to be looked up in `params`. Shape `[ids1, ids2, ...]`.
* <b>`partition_strategy`</b>: A string specifying the partitioning strategy, relevant
  if `len(params) > 1`. Currently `"div"` and `"mod"` are supported. Default
  is `"mod"`.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A `Tensor` with the same type as the tensors in `params` and dimension of
`[ids1, ids2, d1, d2, ...]`.



#### Raises:


* <b>`ValueError`</b>: If `params` is empty.