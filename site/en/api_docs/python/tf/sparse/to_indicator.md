description: Converts a SparseTensor of ids into a dense bool indicator tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.to_indicator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.to_indicator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L1503-L1565">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a `SparseTensor` of ids into a dense bool indicator tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.to_indicator`, `tf.compat.v1.sparse_to_indicator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.to_indicator(
    sp_input, vocab_size, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The last dimension of `sp_input.indices` is discarded and replaced with
the values of `sp_input`.  If `sp_input.dense_shape = [D0, D1, ..., Dn, K]`,
then `output.shape = [D0, D1, ..., Dn, vocab_size]`, where

    output[d_0, d_1, ..., d_n, sp_input[d_0, d_1, ..., d_n, k]] = True

and False elsewhere in `output`.

For example, if `sp_input.dense_shape = [2, 3, 4]` with non-empty values:

    [0, 0, 0]: 0
    [0, 1, 0]: 10
    [1, 0, 3]: 103
    [1, 1, 1]: 150
    [1, 1, 2]: 149
    [1, 1, 3]: 150
    [1, 2, 1]: 121

and `vocab_size = 200`, then the output will be a `[2, 3, 200]` dense bool
tensor with False everywhere except at positions

    (0, 0, 0), (0, 1, 10), (1, 0, 103), (1, 1, 149), (1, 1, 150),
    (1, 2, 121).

Note that repeats are allowed in the input SparseTensor.
This op is useful for converting `SparseTensor`s into dense formats for
compatibility with ops that expect dense tensors.

The input `SparseTensor` must be in row-major order.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
A `SparseTensor` with `values` property of type `int32` or
`int64`.
</td>
</tr><tr>
<td>
`vocab_size`
</td>
<td>
A scalar int64 Tensor (or Python int) containing the new size
of the last dimension, `all(0 <= sp_input.values < vocab_size)`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dense bool indicator tensor representing the indices with specified value.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `sp_input` is not a `SparseTensor`.
</td>
</tr>
</table>

