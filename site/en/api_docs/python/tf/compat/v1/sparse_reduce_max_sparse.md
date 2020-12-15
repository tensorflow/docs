description: Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_reduce_max_sparse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_reduce_max_sparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L1361-L1411">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the max of elements across dimensions of a SparseTensor. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.reduce_max_sparse`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_reduce_max_sparse(
    sp_input, axis=None, keepdims=None, reduction_axes=None, keep_dims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(keep_dims)`. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

This Op takes a SparseTensor and is the sparse counterpart to
<a href="../../../tf/math/reduce_max.md"><code>tf.reduce_max()</code></a>.  In contrast to SparseReduceSum, this Op returns a
SparseTensor.

Note: A gradient is not defined for this function, so it can't be used
in training models that need gradient descent.

Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
`keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
`reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
with length 1.

If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
with a single element is returned.  Additionally, the axes can be negative,
which are interpreted according to the indexing rules in Python.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
The SparseTensor to reduce. Should have numeric type.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The dimensions to reduce; list or scalar. If `None` (the
default), reduces all dimensions.
</td>
</tr><tr>
<td>
`keepdims`
</td>
<td>
If true, retain reduced dimensions with length 1.
</td>
</tr><tr>
<td>
`reduction_axes`
</td>
<td>
Deprecated name of axis.
</td>
</tr><tr>
<td>
`keep_dims`
</td>
<td>
Deprecated alias for `keepdims`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The reduced SparseTensor.
</td>
</tr>

</table>

