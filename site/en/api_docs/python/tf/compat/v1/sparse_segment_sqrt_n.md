description: Computes the sum along sparse segments of a tensor divided by the sqrt(N).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_segment_sqrt_n" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_segment_sqrt_n

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/math_ops.py#L4106-L4141">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the sum along sparse segments of a tensor divided by the sqrt(N).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.segment_sqrt_n`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_segment_sqrt_n(
    data, indices, segment_ids, name=None, num_segments=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`N` is the size of the segment being reduced.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A `Tensor` with data that will be assembled in the output.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A 1-D `Tensor` with indices into `data`. Has same rank as
`segment_ids`.
</td>
</tr><tr>
<td>
`segment_ids`
</td>
<td>
A 1-D `Tensor` with indices into the output `Tensor`. Values
should be sorted and can be repeated.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`num_segments`
</td>
<td>
An optional int32 scalar. Indicates the size of the output
`Tensor`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `tensor` of the shape as data, except for dimension 0 which
has size `k`, the number of segments specified via `num_segments` or
inferred for the last element in `segments_ids`.
</td>
</tr>

</table>

