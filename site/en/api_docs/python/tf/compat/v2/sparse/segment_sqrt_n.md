page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.sparse.segment_sqrt_n

Computes the sum along sparse segments of a tensor divided by the sqrt(N).

``` python
tf.compat.v2.sparse.segment_sqrt_n(
    data,
    indices,
    segment_ids,
    num_segments=None,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

`N` is the size of the segment being reduced.

#### Args:


* <b>`data`</b>: A `Tensor` with data that will be assembled in the output.
* <b>`indices`</b>: A 1-D `Tensor` with indices into `data`. Has same rank as
  `segment_ids`.
* <b>`segment_ids`</b>: A 1-D `Tensor` with indices into the output `Tensor`. Values
  should be sorted and can be repeated.
* <b>`num_segments`</b>: An optional int32 scalar. Indicates the size of the output
  `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `tensor` of the shape as data, except for dimension 0 which
has size `k`, the number of segments specified via `num_segments` or
inferred for the last element in `segments_ids`.
