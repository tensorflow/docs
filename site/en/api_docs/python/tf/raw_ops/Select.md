description: Selects elements from x or y, depending on condition.

robots: noindex

# tf.raw_ops.Select

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Selects elements from `x` or `y`, depending on `condition`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Select`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Select(
    condition, x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `x`, and `y` tensors must all have the same shape, and the
output will also have that shape.

The `condition` tensor must be a scalar if `x` and `y` are scalars.
If `x` and `y` are vectors or higher rank, then `condition` must be either a
scalar, a vector with size matching the first dimension of `x`, or must have
the same shape as `x`.

The `condition` tensor acts as a mask that chooses, based on the value at each
element, whether the corresponding element / row in the output should be
taken from `x` (if true) or `y` (if false).

If `condition` is a vector and `x` and `y` are higher rank matrices, then
it chooses which row (outer dimension) to copy from `x` and `y`.
If `condition` has the same shape as `x` and `y`, then it chooses which
element to copy from `x` and `y`.

#### For example:



```python
# 'condition' tensor is [[True,  False]
#                        [False, True]]
# 't' is [[1, 2],
#         [3, 4]]
# 'e' is [[5, 6],
#         [7, 8]]
select(condition, t, e)  # => [[1, 6], [7, 4]]


# 'condition' tensor is [True, False]
# 't' is [[1, 2],
#         [3, 4]]
# 'e' is [[5, 6],
#         [7, 8]]
select(condition, t, e) ==> [[1, 2],
                             [7, 8]]

```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`condition`
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`x`
</td>
<td>
A `Tensor` which may have the same shape as `condition`.
If `condition` is rank 1, `x` may have higher rank,
but its first dimension must match the size of `condition`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor` with the same type and shape as `x`.
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
A `Tensor`. Has the same type as `t`.
</td>
</tr>

</table>

