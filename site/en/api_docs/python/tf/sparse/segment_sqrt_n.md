page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.segment_sqrt_n


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/sparse/segment_sqrt_n">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L3838-L3873">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the sum along sparse segments of a tensor divided by the sqrt(N).

### Aliases:

* <a href="/api_docs/python/tf/sparse/segment_sqrt_n"><code>tf.compat.v1.sparse.segment_sqrt_n</code></a>
* <a href="/api_docs/python/tf/sparse/segment_sqrt_n"><code>tf.compat.v1.sparse_segment_sqrt_n</code></a>
* <a href="/api_docs/python/tf/sparse/segment_sqrt_n"><code>tf.sparse_segment_sqrt_n</code></a>


``` python
tf.sparse.segment_sqrt_n(
    data,
    indices,
    segment_ids,
    name=None,
    num_segments=None
)
```



<!-- Placeholder for "Used in" -->

`N` is the size of the segment being reduced.

#### Args:


* <b>`data`</b>: A `Tensor` with data that will be assembled in the output.
* <b>`indices`</b>: A 1-D `Tensor` with indices into `data`. Has same rank as
  `segment_ids`.
* <b>`segment_ids`</b>: A 1-D `Tensor` with indices into the output `Tensor`. Values
  should be sorted and can be repeated.
* <b>`name`</b>: A name for the operation (optional).
* <b>`num_segments`</b>: An optional int32 scalar. Indicates the size of the output
  `Tensor`.


#### Returns:

A `tensor` of the shape as data, except for dimension 0 which
has size `k`, the number of segments specified via `num_segments` or
inferred for the last element in `segments_ids`.
