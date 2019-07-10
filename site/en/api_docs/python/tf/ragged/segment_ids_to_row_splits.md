page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.segment_ids_to_row_splits

``` python
tf.ragged.segment_ids_to_row_splits(
    segment_ids,
    num_segments=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/ragged/segment_id_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/ragged/segment_id_ops.py).

Generates the RaggedTensor `row_splits` corresponding to a segmentation.

Returns an integer vector `splits`, where `splits[0] = 0` and
`splits[i] = splits[i-1] + count(segment_ids==i)`.  Example:

```python
>>> ragged.segment_ids_to_row_splits([0, 0, 0, 2, 2, 3, 4, 4, 4]).eval()
[ 0 3 3 5 6 9 ]
```

#### Args:

* <b>`segment_ids`</b>: A 1-D integer Tensor.
* <b>`num_segments`</b>: A scalar integer indicating the number of segments.  Defaults
    to `max(segment_ids) + 1` (or zero if `segment_ids` is empty).
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A sorted 1-D int64 Tensor, with `shape=[num_segments + 1]`.