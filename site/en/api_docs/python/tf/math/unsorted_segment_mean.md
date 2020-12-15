description: Computes the mean along segments of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.unsorted_segment_mean" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.unsorted_segment_mean

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4054-L4097">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the mean along segments of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.unsorted_segment_mean`, `tf.compat.v1.unsorted_segment_mean`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.unsorted_segment_mean(
    data, segment_ids, num_segments, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Read [the section on
segmentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/math#about_segmentation)
for an explanation of segments.

This operator is similar to the <a href="../../tf/math/unsorted_segment_sum.md"><code>tf.math.unsorted_segment_sum</code></a> operator.
Instead of computing the sum over segments, it computes the mean of all
entries belonging to a segment such that:

\\(output_i = 1/N_i \sum_{j...} data[j...]\\) where the sum is over tuples
`j...` such that `segment_ids[j...] == i` with \\N_i\\ being the number of
occurrences of id \\i\\.

If there is no entry for a given segment ID `i`, it outputs 0.

If the given segment ID `i` is negative, the value is dropped and will not
be added to the sum of the segment.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A `Tensor` with floating point or complex dtype.
</td>
</tr><tr>
<td>
`segment_ids`
</td>
<td>
An integer tensor whose shape is a prefix of `data.shape`.
</td>
</tr><tr>
<td>
`num_segments`
</td>
<td>
An integer scalar `Tensor`.  The number of distinct segment
IDs.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`.  Has same shape as data, except for the first `segment_ids.rank`
dimensions, which are replaced with a single dimension which has size
`num_segments`.
</td>
</tr>

</table>

