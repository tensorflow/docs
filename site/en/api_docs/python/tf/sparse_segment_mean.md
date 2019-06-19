page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse_segment_mean

``` python
tf.sparse_segment_mean(
    data,
    indices,
    segment_ids,
    name=None,
    num_segments=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Segmentation](../../../api_guides/python/math_ops#Segmentation)

Computes the mean along sparse segments of a tensor.

Read <a href="../../../api_guides/python/math_ops#Segmentation">the section on segmentation</a> for an explanation
of segments.

Like `SegmentMean`, but `segment_ids` can have rank less than `data`'s first
dimension, selecting a subset of dimension 0, specified by `indices`.
`segment_ids` is allowed to have missing ids, in which case the output will
be zeros at those indices. In those cases `num_segments` is used to determine
the size of the output.

#### Args:

* <b>`data`</b>: A `Tensor` with data that will be assembled in the output.
* <b>`indices`</b>: A 1-D `Tensor` with indices into `data`. Has same rank as
    `segment_ids`.
* <b>`segment_ids`</b>: A 1-D `Tensor` with indices into the output `Tensor`.
    Values should be sorted and can be repeated.
* <b>`name`</b>: A name for the operation (optional).
* <b>`num_segments`</b>: An optional int32 scalar. Indicates the size of the output
    `Tensor`.


#### Returns:

A `tensor` of the shape as data, except for dimension 0 which
has size `k`, the number of segments specified via `num_segments` or
inferred for the last element in `segments_ids`.