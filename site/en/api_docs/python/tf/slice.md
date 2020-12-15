description: Extracts a slice from a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.slice" />
<meta itemprop="path" content="Stable" />
</div>

# tf.slice

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L1051-L1103">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Extracts a slice from a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.slice`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.slice(
    input_, begin, size, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/strided_slice.md"><code>tf.strided_slice</code></a>.

This operation extracts a slice of size `size` from a tensor `input_` starting
at the location specified by `begin`. The slice `size` is represented as a
tensor shape, where `size[i]` is the number of elements of the 'i'th dimension
of `input_` that you want to slice. The starting location (`begin`) for the
slice is represented as an offset in each dimension of `input_`. In other
words, `begin[i]` is the offset into the i'th dimension of `input_` that you
want to slice from.

Note that <a href="../tf/Tensor.md#__getitem__"><code>tf.Tensor.__getitem__</code></a> is typically a more pythonic way to
perform slices, as it allows you to write `foo[3:7, :-2]` instead of
`tf.slice(foo, [3, 0], [4, foo.get_shape()[1]-2])`.

`begin` is zero-based; `size` is one-based. If `size[i]` is -1,
all remaining elements in dimension i are included in the
slice. In other words, this is equivalent to setting:

`size[i] = input_.dim_size(i) - begin[i]`

This operation requires that:

`0 <= begin[i] <= begin[i] + size[i] <= Di  for i in [0, n]`

#### For example:



```python
t = tf.constant([[[1, 1, 1], [2, 2, 2]],
                 [[3, 3, 3], [4, 4, 4]],
                 [[5, 5, 5], [6, 6, 6]]])
tf.slice(t, [1, 0, 0], [1, 1, 3])  # [[[3, 3, 3]]]
tf.slice(t, [1, 0, 0], [1, 2, 3])  # [[[3, 3, 3],
                                   #   [4, 4, 4]]]
tf.slice(t, [1, 0, 0], [2, 1, 3])  # [[[3, 3, 3]],
                                   #  [[5, 5, 5]]]
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
`size`
</td>
<td>
An `int32` or `int64` `Tensor`.
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
A `Tensor` the same type as `input_`.
</td>
</tr>

</table>

