description: A transformation that buckets elements in a Dataset by length.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.data.experimental.bucket_by_sequence_length" />
<meta itemprop="path" content="Stable" />
</div>

# tf.data.experimental.bucket_by_sequence_length

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/experimental/ops/grouping.py#L127-L244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A transformation that buckets elements in a `Dataset` by length.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.data.experimental.bucket_by_sequence_length`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.data.experimental.bucket_by_sequence_length(
    element_length_func, bucket_boundaries, bucket_batch_sizes, padded_shapes=None,
    padding_values=None, pad_to_bucket_boundary=(False), no_padding=(False),
    drop_remainder=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Elements of the `Dataset` are grouped together by length and then are padded
and batched.

This is useful for sequence tasks in which the elements have variable length.
Grouping together elements that have similar lengths reduces the total
fraction of padding in a batch which increases training step efficiency.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`element_length_func`
</td>
<td>
function from element in `Dataset` to <a href="../../../tf.md#int32"><code>tf.int32</code></a>,
determines the length of the element, which will determine the bucket it
goes into.
</td>
</tr><tr>
<td>
`bucket_boundaries`
</td>
<td>
`list<int>`, upper length boundaries of the buckets.
</td>
</tr><tr>
<td>
`bucket_batch_sizes`
</td>
<td>
`list<int>`, batch size per bucket. Length should be
`len(bucket_boundaries) + 1`.
</td>
</tr><tr>
<td>
`padded_shapes`
</td>
<td>
Nested structure of <a href="../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> to pass to
<a href="../../../tf/data/Dataset.md#padded_batch"><code>tf.data.Dataset.padded_batch</code></a>. If not provided, will use
`dataset.output_shapes`, which will result in variable length dimensions
being padded out to the maximum length in each batch.
</td>
</tr><tr>
<td>
`padding_values`
</td>
<td>
Values to pad with, passed to
<a href="../../../tf/data/Dataset.md#padded_batch"><code>tf.data.Dataset.padded_batch</code></a>. Defaults to padding with 0.
</td>
</tr><tr>
<td>
`pad_to_bucket_boundary`
</td>
<td>
bool, if `False`, will pad dimensions with unknown
size to maximum length in batch. If `True`, will pad dimensions with
unknown size to bucket boundary minus 1 (i.e., the maximum length in each
bucket), and caller must ensure that the source `Dataset` does not contain
any elements with length longer than `max(bucket_boundaries)`.
</td>
</tr><tr>
<td>
`no_padding`
</td>
<td>
`bool`, indicates whether to pad the batch features (features
need to be either of type <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> or of same shape).
</td>
</tr><tr>
<td>
`drop_remainder`
</td>
<td>
(Optional.) A <a href="../../../tf.md#bool"><code>tf.bool</code></a> scalar <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, representing
whether the last batch should be dropped in the case it has fewer than
`batch_size` elements; the default behavior is not to drop the smaller
batch.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset.md#apply"><code>tf.data.Dataset.apply</code></a>.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if `len(bucket_batch_sizes) != len(bucket_boundaries) + 1`.
</td>
</tr>
</table>

