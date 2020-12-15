description: Reshapes a SparseTensor to represent values in a new dense shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.reshape" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.reshape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L838-L941">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reshapes a `SparseTensor` to represent values in a new dense shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.reshape`, `tf.compat.v1.sparse_reshape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.reshape(
    sp_input, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation has the same semantics as `reshape` on the represented dense
tensor.  The indices of non-empty values in `sp_input` are recomputed based
on the new dense shape, and a new `SparseTensor` is returned containing the
new indices and new shape.  The order of non-empty values in `sp_input` is
unchanged.

If one component of `shape` is the special value -1, the size of that
dimension is computed so that the total dense size remains constant.  At
most one component of `shape` can be -1.  The number of dense elements
implied by `shape` must be the same as the number of dense elements
originally represented by `sp_input`.

For example, if `sp_input` has shape `[2, 3, 6]` and `indices` / `values`:

    [0, 0, 0]: a
    [0, 0, 1]: b
    [0, 1, 0]: c
    [1, 0, 0]: d
    [1, 2, 3]: e

and `shape` is `[9, -1]`, then the output will be a `SparseTensor` of
shape `[9, 4]` and `indices` / `values`:

    [0, 0]: a
    [0, 1]: b
    [1, 2]: c
    [4, 2]: d
    [8, 1]: e

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
The input `SparseTensor`.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A 1-D (vector) int64 `Tensor` specifying the new dense shape of the
represented `SparseTensor`.
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
A `SparseTensor` with the same non-empty values but with indices calculated
by the new dense shape.
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
</tr><tr>
<td>
`ValueError`
</td>
<td>
If argument `shape` requests a `SparseTensor` with a different
number of elements than `sp_input`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `shape` has more than one inferred (== -1) dimension.
</td>
</tr>
</table>

