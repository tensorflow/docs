

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.unsorted_segment_mean

``` python
tf.unsorted_segment_mean(
    data,
    segment_ids,
    num_segments,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/math_ops.py).

Computes the mean along segments of a tensor.

Read <a href="../../../api_guides/python/math_ops#segmentation">the section on segmentation</a> for an explanation
of segments.

This operator is similar to the unsorted segment sum operator found
[here](../../../api_docs/python/math_ops#UnsortedSegmentSum).
Instead of computing the sum over segments, it computes the mean of all
entries belonging to a segment such that:

\\(output_i = 1/N_i \sum data_j\\) where the sum is over `j` such
that `segment_ids[j] == i` with \\N_i\\ being the number of occurrences
of id \\i\\.

If there is no entry for a given segment ID `i`, it outputs 0.

segment_ids: A 1-D tensor whose rank is equal to the rank of `data`'s
first dimension.

output: Has same shape as data, except for dimension 0 which
has size `num_segments`.