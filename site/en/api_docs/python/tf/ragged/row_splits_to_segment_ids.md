page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.row_splits_to_segment_ids

Generates the segmentation corresponding to a RaggedTensor `row_splits`.

### Aliases:

* `tf.compat.v1.ragged.row_splits_to_segment_ids`
* `tf.compat.v2.ragged.row_splits_to_segment_ids`
* `tf.ragged.row_splits_to_segment_ids`

``` python
tf.ragged.row_splits_to_segment_ids(
    splits,
    name=None,
    out_type=None
)
```



Defined in [`python/ops/ragged/segment_id_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ragged/segment_id_ops.py).

<!-- Placeholder for "Used in" -->

Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if
`splits[j] <= i < splits[j+1]`.  Example:

```python
>>> ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]).eval()
[ 0 0 0 2 2 3 4 4 4 ]
```

#### Args:


* <b>`splits`</b>: A sorted 1-D integer Tensor.  `splits[0]` must be zero.
* <b>`name`</b>: A name prefix for the returned tensor (optional).
* <b>`out_type`</b>: The dtype for the return value.  Defaults to `splits.dtype`,
  or <a href="../../tf#int64"><code>tf.int64</code></a> if `splits` does not have a dtype.


#### Returns:

A sorted 1-D integer Tensor, with `shape=[splits[-1]]`



#### Raises:


* <b>`ValueError`</b>: If `splits` is invalid.