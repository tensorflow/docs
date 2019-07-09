page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.row_splits_to_segment_ids

``` python
tf.ragged.row_splits_to_segment_ids(
    splits,
    name=None
)
```



Defined in [`tensorflow/python/ops/ragged/segment_id_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/ragged/segment_id_ops.py).

Generates the segmentation corresponding to a RaggedTensor `row_splits`.

Returns an integer vector `segment_ids`, where `segment_ids[i] == j` if
`splits[j] <= i < splits[j+1]`.  Example:

```python
>>> ragged.row_splits_to_segment_ids([0, 3, 3, 5, 6, 9]).eval()
[ 0 0 0 2 2 3 4 4 4 ]
```

#### Args:

* <b>`splits`</b>: A sorted 1-D int64 Tensor.  `splits[0]` must be zero.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A sorted 1-D int64 Tensor, with `shape=[splits[-1]]`


#### Raises:

* <b>`ValueError`</b>: If `splits` is invalid.