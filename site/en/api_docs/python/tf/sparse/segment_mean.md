page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.segment_mean


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L3811-L3846">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the mean along sparse segments of a tensor.

### Aliases:

* `tf.compat.v2.sparse.segment_mean`


``` python
tf.sparse.segment_mean(
    data,
    indices,
    segment_ids,
    num_segments=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Read [the section on
segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

Like <a href="../../tf/math/segment_mean"><code>tf.math.segment_mean</code></a>, but `segment_ids` can have rank less than
`data`'s first dimension, selecting a subset of dimension 0, specified by
`indices`.
`segment_ids` is allowed to have missing ids, in which case the output will
be zeros at those indices. In those cases `num_segments` is used to determine
the size of the output.

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
