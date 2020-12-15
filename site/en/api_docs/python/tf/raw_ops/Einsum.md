description: Tensor contraction according to Einstein summation convention.

robots: noindex

# tf.raw_ops.Einsum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Tensor contraction according to Einstein summation convention.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Einsum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Einsum(
    inputs, equation, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Implements generalized Tensor contraction and reduction. Each input Tensor must
have a corresponding input subscript appearing in the comma-separated left-hand
side of the equation. The right-hand side of the equation consists of the
output subscript. The input subscripts and the output subscript should consist
of zero or more named axis labels and at most one ellipsis (`...`).

The named axis labels may be any single character other than those having
special meaning, namely `,.->`. The behavior of this Op is undefined if it
receives an ill-formatted equation; since the validation is done at
graph-building time, we omit format validation checks at runtime.

Note: This Op is *not* intended to be called by the user; instead users should
call <a href="../../tf/einsum.md"><code>tf.einsum</code></a> directly. It is a hidden Op used by <a href="../../tf/einsum.md"><code>tf.einsum</code></a>.

Operations are applied to the input(s) according to the following rules:

 (a) Generalized Diagonals: For input dimensions corresponding to axis labels
     appearing more than once in the same input subscript, we take the
     generalized (`k`-dimensional) diagonal.
     For example, in the equation `iii->i` with input shape `[3, 3, 3]`, the
     generalized diagonal would consist of `3` elements at indices `(0, 0, 0)`,
     `(1, 1, 1)` and `(2, 2, 2)` to create a Tensor of shape `[3]`.

 (b) Reduction: Axes corresponding to labels appearing only in one input
     subscript but not in the output subscript are summed over prior to Tensor
     contraction.
     For example, in the equation `ab,bc->b`, the axis labels `a` and `c` are
     the reduction axis labels.

 (c) Batch Dimensions: Axes corresponding to labels appearing in each of the
     input subscripts and also in the output subscript make up the batch
     dimensions in Tensor contraction. Unnamed axis labels corresponding to
     ellipsis (`...`) also correspond to batch dimensions.
     For example, for the equation denoting batch matrix multiplication,
     `bij,bjk->bik`, the axis label `b` corresponds to a batch dimension.

 (d) Contraction: In case of binary einsum, axes corresponding to labels
     appearing in two different inputs (and not in the output) are contracted
     against each other.
     Considering the batch matrix multiplication equation again
     (`bij,bjk->bik`), the contracted axis label is `j`.

 (e) Expand Diagonal: If the output subscripts contain repeated (explicit) axis
     labels, the opposite operation of (a) is applied. For example, in the
     equation `i->iii`, and input shape `[3]`, the output of shape `[3, 3, 3]`
     are all zeros, except for the (generalized) diagonal which is populated
     with values from the input.
     Note: This operation is not supported by `np.einsum` or <a href="../../tf/einsum.md"><code>tf.einsum</code></a>; it is
     provided to enable computing the symbolic gradient of <a href="../../tf/einsum.md"><code>tf.einsum</code></a>.

The output subscripts must contain only labels appearing in at least one of the
input subscripts. Furthermore, all dimensions mapping to the same axis label
must be equal.

Any of the input and output subscripts may contain at most a single ellipsis
(`...`). These ellipsis are mapped against dimensions not corresponding to any
named axis label. If two inputs contain ellipsis, then they are broadcasted
according to standard NumPy broadcasting
[rules](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

The broadcasted dimensions are placed in the corresponding location of the
ellipsis in the output subscript. If the broadcasted dimensions are non-empty
and the output subscripts do not contain ellipsis, then an InvalidArgument error
is raised.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type.
List of 1 or 2 Tensors.
</td>
</tr><tr>
<td>
`equation`
</td>
<td>
A `string`.
String describing the Einstein Summation operation; in the format of np.einsum.
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
A `Tensor`. Has the same type as `inputs`.
</td>
</tr>

</table>



#### Numpy Compatibility
Similar to [`numpy.einsum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html).

Comparison with `numpy.einsum`:

 * This Op only supports unary and binary forms of `numpy.einsum`.
 * This Op does not support implicit form. (i.e. equations without `->`).
 * This Op also supports repeated indices in the output subscript, which is not
   supported by `numpy.einsum`.

