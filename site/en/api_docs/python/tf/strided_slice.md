description: Extracts a strided slice of a tensor (generalized Python array indexing).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strided_slice" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strided_slice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L1107-L1247">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Extracts a strided slice of a tensor (generalized Python array indexing).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.strided_slice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strided_slice(
    input_, begin, end, strides=None, begin_mask=0, end_mask=0, ellipsis_mask=0,
    new_axis_mask=0, shrink_axis_mask=0, var=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/slice.md"><code>tf.slice</code></a>.

**Instead of calling this op directly most users will want to use the
NumPy-style slicing syntax (e.g. `tensor[..., 3:4:-1, tf.newaxis, 3]`), which
is supported via <a href="../tf/Tensor.md#__getitem__"><code>tf.Tensor.__getitem__</code></a> and <a href="../tf/Variable.md#__getitem__"><code>tf.Variable.__getitem__</code></a>.**
The interface of this op is a low-level encoding of the slicing syntax.

Roughly speaking, this op extracts a slice of size `(end-begin)/stride`
from the given `input_` tensor. Starting at the location specified by `begin`
the slice continues by adding `stride` to the index until all dimensions are
not less than `end`.
Note that a stride can be negative, which causes a reverse slice.

Given a Python slice `input[spec0, spec1, ..., specn]`,
this function will be called as follows.

`begin`, `end`, and `strides` will be vectors of length n.
n in general is not equal to the rank of the `input_` tensor.

In each mask field (`begin_mask`, `end_mask`, `ellipsis_mask`,
`new_axis_mask`, `shrink_axis_mask`) the ith bit will correspond to
the ith spec.

If the ith bit of `begin_mask` is set, `begin[i]` is ignored and
the fullest possible range in that dimension is used instead.
`end_mask` works analogously, except with the end range.

`foo[5:,:,:3]` on a 7x8x9 tensor is equivalent to `foo[5:7,0:8,0:3]`.
`foo[::-1]` reverses a tensor with shape 8.

If the ith bit of `ellipsis_mask` is set, as many unspecified dimensions
as needed will be inserted between other dimensions. Only one
non-zero bit is allowed in `ellipsis_mask`.

For example `foo[3:5,...,4:5]` on a shape 10x3x3x10 tensor is
equivalent to `foo[3:5,:,:,4:5]` and
`foo[3:5,...]` is equivalent to `foo[3:5,:,:,:]`.

If the ith bit of `new_axis_mask` is set, then `begin`,
`end`, and `stride` are ignored and a new length 1 dimension is
added at this point in the output tensor.

For example,
`foo[:4, tf.newaxis, :2]` would produce a shape `(4, 1, 2)` tensor.

If the ith bit of `shrink_axis_mask` is set, it implies that the ith
specification shrinks the dimensionality by 1, taking on the value at index
`begin[i]`. `end[i]` and `strides[i]` are ignored in this case. For example in
Python one might do `foo[:, 3, :]` which would result in `shrink_axis_mask`
equal to 2.


NOTE: `begin` and `end` are zero-indexed.
`strides` entries must be non-zero.


```python
t = tf.constant([[[1, 1, 1], [2, 2, 2]],
                 [[3, 3, 3], [4, 4, 4]],
                 [[5, 5, 5], [6, 6, 6]]])
tf.strided_slice(t, [1, 0, 0], [2, 1, 3], [1, 1, 1])  # [[[3, 3, 3]]]
tf.strided_slice(t, [1, 0, 0], [2, 2, 3], [1, 1, 1])  # [[[3, 3, 3],
                                                      #   [4, 4, 4]]]
tf.strided_slice(t, [1, -1, 0], [2, -3, 3], [1, -1, 1])  # [[[4, 4, 4],
                                                         #   [3, 3, 3]]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`begin`
</td>
<td>
An `int32` or `int64` `Tensor`.
</td>
</tr><tr>
<td>
`end`
</td>
<td>
An `int32` or `int64` `Tensor`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
An `int32` or `int64` `Tensor`.
</td>
</tr><tr>
<td>
`begin_mask`
</td>
<td>
An `int32` mask.
</td>
</tr><tr>
<td>
`end_mask`
</td>
<td>
An `int32` mask.
</td>
</tr><tr>
<td>
`ellipsis_mask`
</td>
<td>
An `int32` mask.
</td>
</tr><tr>
<td>
`new_axis_mask`
</td>
<td>
An `int32` mask.
</td>
</tr><tr>
<td>
`shrink_axis_mask`
</td>
<td>
An `int32` mask.
</td>
</tr><tr>
<td>
`var`
</td>
<td>
The variable corresponding to `input_` or None
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
A `Tensor` the same type as `input`.
</td>
</tr>

</table>

