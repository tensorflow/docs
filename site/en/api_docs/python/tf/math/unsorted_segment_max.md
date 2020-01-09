page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.unsorted_segment_max


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes the maximum along segments of a tensor.

### Aliases:

* `tf.compat.v1.math.unsorted_segment_max`
* `tf.compat.v1.unsorted_segment_max`
* `tf.compat.v2.math.unsorted_segment_max`


``` python
tf.math.unsorted_segment_max(
    data,
    segment_ids,
    num_segments,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Read
[the section on segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

This operator is similar to the unsorted segment sum operator found
[(here)](../../../api_docs/python/math_ops#UnsortedSegmentSum).
Instead of computing the sum over segments, it computes the maximum such that:

\\(output_i = \max_{j...} data[j...]\\) where max is over tuples `j...` such
that `segment_ids[j...] == i`.

If the maximum is empty for a given segment ID `i`, it outputs the smallest
possible value for the specific numeric type,
`output[i] = numeric_limits<T>::lowest()`.

If the given segment ID `i` is negative, then the corresponding value is
dropped, and will not be included in the result.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src="https://www.tensorflow.org/images/UnsortedSegmentMax.png" alt>
</div>

#### For example:



``` python
c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])
tf.unsorted_segment_max(c, tf.constant([0, 1, 0]), num_segments=2)
# ==> [[ 4,  3, 3, 4],
#       [5,  6, 7, 8]]
```

#### Args:


* <b>`data`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`segment_ids`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  A tensor whose shape is a prefix of `data.shape`.
* <b>`num_segments`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `data`.
