description: Adds two tensors, at least one of each is a SparseTensor. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_add" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_add

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/sparse_ops.py#L425-L486">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adds two tensors, at least one of each is a `SparseTensor`. (deprecated arguments)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.add`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_add(
    a, b, threshold=None, thresh=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(thresh)`. They will be removed in a future version.
Instructions for updating:
thresh is deprecated, use threshold instead

If one `SparseTensor` and one `Tensor` are passed in, returns a `Tensor`.  If
both arguments are `SparseTensor`s, this returns a `SparseTensor`.  The order
of arguments does not matter.  Use vanilla <a href="../../../tf/math/add.md"><code>tf.add()</code></a> for adding two dense
`Tensor`s.

The shapes of the two operands must match: broadcasting is not supported.

The indices of any input `SparseTensor` are assumed ordered in standard
lexicographic order.  If this is not the case, before this step run
`SparseReorder` to restore index ordering.

If both arguments are sparse, we perform "clipping" as follows.  By default,
if two values sum to zero at some index, the output `SparseTensor` would still
include that particular location in its index, storing a zero in the
corresponding value slot.  To override this, callers can specify `thresh`,
indicating that if the sum has a magnitude strictly smaller than `thresh`, its
corresponding value and index would then not be included.  In particular,
`thresh == 0.0` (default) means everything is kept and actual thresholding
happens only for a positive value.

For example, suppose the logical sum of two sparse operands is (densified):

    [       2]
    [.1     0]
    [ 6   -.2]

Then,

* `thresh == 0` (the default): all 5 index/value pairs will be returned.
* `thresh == 0.11`: only .1 and 0 will vanish, and the remaining three
    index/value pairs will be returned.
* `thresh == 0.21`: .1, 0, and -.2 will vanish.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
The first operand; `SparseTensor` or `Tensor`.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
The second operand; `SparseTensor` or `Tensor`. At least one operand
must be sparse.
</td>
</tr><tr>
<td>
`threshold`
</td>
<td>
An optional 0-D `Tensor` (defaults to `0`). The magnitude
threshold that determines if an output value/index pair takes space. Its
dtype should match that of the values if they are real; if the latter are
complex64/complex128, then the dtype should be float32/float64,
correspondingly.
</td>
</tr><tr>
<td>
`thresh`
</td>
<td>
Deprecated alias for `threshold`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` or a `Tensor`, representing the sum.
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
If both `a` and `b` are `Tensor`s.  Use <a href="../../../tf/math/add.md"><code>tf.add()</code></a> instead.
</td>
</tr>
</table>

