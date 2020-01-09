page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.unsorted_segment_sqrt_n


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L3573-L3619">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the sum along segments of a tensor divided by the sqrt(N).

### Aliases:

* `tf.compat.v1.math.unsorted_segment_sqrt_n`
* `tf.compat.v1.unsorted_segment_sqrt_n`
* `tf.compat.v2.math.unsorted_segment_sqrt_n`


``` python
tf.math.unsorted_segment_sqrt_n(
    data,
    segment_ids,
    num_segments,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Read [the section on
segmentation](https://tensorflow.org/api_docs/python/tf/math#Segmentation)
for an explanation of segments.

This operator is similar to the unsorted segment sum operator found
[here](../../../api_docs/python/math_ops#UnsortedSegmentSum).
Additionally to computing the sum over segments, it divides the results by
sqrt(N).

\\(output_i = 1/sqrt(N_i) \sum_{j...} data[j...]\\) where the sum is over
tuples `j...` such that `segment_ids[j...] == i` with \\N_i\\ being the
number of occurrences of id \\i\\.

If there is no entry for a given segment ID `i`, it outputs 0.

Note that this op only supports floating point and complex dtypes,
due to tf.sqrt only supporting these types.

If the given segment ID `i` is negative, the value is dropped and will not
be added to the sum of the segment.

#### Args:


* <b>`data`</b>: A `Tensor` with floating point or complex dtype.
* <b>`segment_ids`</b>: An integer tensor whose shape is a prefix of `data.shape`.
* <b>`num_segments`</b>: An integer scalar `Tensor`.  The number of distinct segment
  IDs.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

 A `Tensor`.  Has same shape as data, except for the first `segment_ids.rank`
 dimensions, which are replaced with a single dimension which has size
`num_segments`.
