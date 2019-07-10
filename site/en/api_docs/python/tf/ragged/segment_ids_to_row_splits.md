page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.segment_ids_to_row_splits

Generates the RaggedTensor `row_splits` corresponding to a segmentation.

### Aliases:

* `tf.compat.v1.ragged.segment_ids_to_row_splits`
* `tf.compat.v2.ragged.segment_ids_to_row_splits`
* `tf.ragged.segment_ids_to_row_splits`

``` python
tf.ragged.segment_ids_to_row_splits(
    segment_ids,
    num_segments=None,
    out_type=None,
    name=None
)
```



Defined in [`python/ops/ragged/segment_id_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ragged/segment_id_ops.py).

<!-- Placeholder for "Used in" -->

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
* <b>`out_type`</b>: The dtype for the return value.  Defaults to `segment_ids.dtype`,
  or <a href="../../tf#int64"><code>tf.int64</code></a> if `segment_ids` does not have a dtype.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A sorted 1-D integer Tensor, with `shape=[num_segments + 1]`.
