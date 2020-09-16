description: Creates a dataset that shuffles and repeats elements from input_dataset

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ShuffleAndRepeatDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ShuffleAndRepeatDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that shuffles and repeats elements from `input_dataset`

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ShuffleAndRepeatDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ShuffleAndRepeatDataset(
    input_dataset, buffer_size, seed, seed2, count, output_types, output_shapes,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

pseudorandomly.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`buffer_size`
</td>
<td>
A `Tensor` of type `int64`.
The number of output elements to buffer in an iterator over
this dataset. Compare with the `min_after_dequeue` attr when creating a
`RandomShuffleQueue`.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A `Tensor` of type `int64`.
A scalar seed for the random number generator. If either `seed` or
`seed2` is set to be non-zero, the random number generator is seeded
by the given seed.  Otherwise, a random seed is used.
</td>
</tr><tr>
<td>
`seed2`
</td>
<td>
A `Tensor` of type `int64`.
A second scalar seed to avoid seed collision.
</td>
</tr><tr>
<td>
`count`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of times the underlying dataset
should be repeated. The default is `-1`, which results in infinite repetition.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

