description: Return the elements, either from x or y, depending on the condition.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.where" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.where

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L4314-L4365">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Return the elements, either from `x` or `y`, depending on the `condition`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.where(
    condition, x=None, y=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If both `x` and `y` are None, then this operation returns the coordinates of
true elements of `condition`.  The coordinates are returned in a 2-D tensor
where the first dimension (rows) represents the number of true elements, and
the second dimension (columns) represents the coordinates of the true
elements. Keep in mind, the shape of the output tensor can vary depending on
how many true values there are in input. Indices are output in row-major
order.

If both non-None, `x` and `y` must have the same shape.
The `condition` tensor must be a scalar if `x` and `y` are scalar.
If `x` and `y` are tensors of higher rank, then `condition` must be either a
vector with size matching the first dimension of `x`, or must have the same
shape as `x`.

The `condition` tensor acts as a mask that chooses, based on the value at each
element, whether the corresponding element / row in the output should be taken
from `x` (if true) or `y` (if false).

If `condition` is a vector and `x` and `y` are higher rank matrices, then it
chooses which row (outer dimension) to copy from `x` and `y`. If `condition`
has the same shape as `x` and `y`, then it chooses which element to copy from
`x` and `y`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`condition`
</td>
<td>
A `Tensor` of type `bool`
</td>
</tr><tr>
<td>
`x`
</td>
<td>
A Tensor which may have the same shape as `condition`. If `condition` is
rank 1, `x` may have higher rank, but its first dimension must match the
size of `condition`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `tensor` with the same shape and type as `x`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name of the operation (optional)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same type and shape as `x`, `y` if they are non-None.
Otherwise, a `Tensor` with shape `(num_true, rank(condition))`.
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
When exactly one of `x` or `y` is non-None.
</td>
</tr>
</table>

