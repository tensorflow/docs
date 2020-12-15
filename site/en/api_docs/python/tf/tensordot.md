description: Tensor contraction of a and b along specified axes and outer product.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.tensordot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.tensordot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L4451-L4635">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tensor contraction of a and b along specified axes and outer product.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.linalg.tensordot`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.tensordot`, `tf.compat.v1.tensordot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.tensordot(
    a, b, axes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Tensordot (also known as tensor contraction) sums the product of elements
from `a` and `b` over the indices specified by `a_axes` and `b_axes`.
The lists `a_axes` and `b_axes` specify those pairs of axes along which to
contract the tensors. The axis `a_axes[i]` of `a` must have the same dimension
as axis `b_axes[i]` of `b` for all `i` in `range(0, len(a_axes))`. The lists
`a_axes` and `b_axes` must have identical length and consist of unique
integers that specify valid axes for each of the tensors. Additionally
outer product is supported by passing `axes=0`.

This operation corresponds to `numpy.tensordot(a, b, axes)`.

Example 1: When `a` and `b` are matrices (order 2), the case `axes = 1`
is equivalent to matrix multiplication.

Example 2: When `a` and `b` are matrices (order 2), the case
`axes = [[1], [0]]` is equivalent to matrix multiplication.

Example 3: When `a` and `b` are matrices (order 2), the case `axes=0` gives
the outer product, a tensor of order 4.

Example 4: Suppose that \\(a_{ijk}\\) and \\(b_{lmn}\\) represent two
tensors of order 3. Then, `contract(a, b, [[0], [2]])` is the order 4 tensor
\\(c_{jklm}\\) whose entry
corresponding to the indices \\((j,k,l,m)\\) is given by:

\\( c_{jklm} = \sum_i a_{ijk} b_{lmi} \\).

In general, `order(c) = order(a) + order(b) - 2*len(axes[0])`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
`Tensor` of type `float32` or `float64`.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
`Tensor` with the same type as `a`.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
Either a scalar `N`, or a list or an `int32` `Tensor` of shape [2, k].
If axes is a scalar, sum over the last N axes of a and the first N axes of
b in order. If axes is a list or `Tensor` the first and second row contain
the set of unique integers specifying axes along which the contraction is
computed, for `a` and `b`, respectively. The number of axes for `a` and
`b` must be equal. If `axes=0`, computes the outer product between `a` and
`b`.
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
A `Tensor` with the same type as `a`.
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
If the shapes of `a`, `b`, and `axes` are incompatible.
</td>
</tr><tr>
<td>
`IndexError`
</td>
<td>
If the values in axes exceed the rank of the corresponding
tensor.
</td>
</tr>
</table>

