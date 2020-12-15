description: Reorders a SparseTensor into the canonical, row-major ordering.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.reorder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.reorder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L787-L835">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reorders a `SparseTensor` into the canonical, row-major ordering.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.reorder`, `tf.compat.v1.sparse_reorder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.reorder(
    sp_input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that by convention, all sparse ops preserve the canonical ordering
along increasing dimension number. The only time ordering can be violated
is during manual manipulation of the indices and values to add entries.

Reordering does not affect the shape of the `SparseTensor`.

For example, if `sp_input` has shape `[4, 5]` and `indices` / `values`:

    [0, 3]: b
    [0, 1]: a
    [3, 1]: d
    [2, 0]: c

then the output will be a `SparseTensor` of shape `[4, 5]` and
`indices` / `values`:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

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
A `SparseTensor` with the same shape and non-empty values, but in
canonical ordering.
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

