description: Joins the elements of inputs based on segment_ids.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.UnsortedSegmentJoin" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.UnsortedSegmentJoin

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Joins the elements of `inputs` based on `segment_ids`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UnsortedSegmentJoin`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UnsortedSegmentJoin(
    inputs, segment_ids, num_segments, separator='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the string join along segments of a tensor.
Given `segment_ids` with rank `N` and `data` with rank `N+M`:

    `output[i, k1...kM] = strings.join([data[j1...jN, k1...kM])`

where the join is over all [j1...jN] such that segment_ids[j1...jN] = i.
Strings are joined in row-major order.

#### For example:



```python
inputs = [['Y', 'q', 'c'], ['Y', '6', '6'], ['p', 'G', 'a']]
output_array = string_ops.unsorted_segment_join(inputs=inputs,
                                                segment_ids=[1, 0, 1],
                                                num_segments=2,
                                                separator=':'))
# output_array ==> [['Y', '6', '6'], ['Y:p', 'q:G', 'c:a']]


inputs = ['this', 'is', 'a', 'test']
output_array = string_ops.unsorted_segment_join(inputs=inputs,
                                                segment_ids=[0, 0, 0, 0],
                                                num_segments=1,
                                                separator=':'))
# output_array ==> ['this:is:a:test']
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A `Tensor` of type `string`. The input to be joined.
</td>
</tr><tr>
<td>
`segment_ids`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A tensor whose shape is a prefix of data.shape.  Negative segment ids are not
supported.
</td>
</tr><tr>
<td>
`num_segments`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A scalar.
</td>
</tr><tr>
<td>
`separator`
</td>
<td>
An optional `string`. Defaults to `""`.
The separator to use when joining.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

