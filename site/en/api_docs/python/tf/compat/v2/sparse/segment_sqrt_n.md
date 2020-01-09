page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.sparse.segment_sqrt_n


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L3876-L3907">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



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



<!-- Placeholder for "Used in" -->

Read [the section on
segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
for an explanation of segments.

Like <a href="../../../../tf/sparse/segment_mean"><code>tf.sparse.segment_mean</code></a>, but instead of dividing by the size of the
segment, `N`, divide by `sqrt(N)` instead.

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
