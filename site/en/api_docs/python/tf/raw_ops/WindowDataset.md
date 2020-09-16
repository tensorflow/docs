description: Combines (nests of) input elements into a dataset of (nests of) windows.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.WindowDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.WindowDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Combines (nests of) input elements into a dataset of (nests of) windows.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.WindowDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.WindowDataset(
    input_dataset, size, shift, stride, drop_remainder, output_types, output_shapes,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

A "window" is a finite dataset of flat elements of size `size` (or possibly
fewer if there are not enough input elements to fill the window and
`drop_remainder` evaluates to false).

The `shift` argument determines the number of input elements by which
the window moves on each iteration.  The first element in the `k`th window
will be element

```
1 + (k-1) * shift
```

of the input dataset. In particular, the first element of the first window
will always be the first element of the input dataset.  

If the `stride` parameter is greater than 1, then each window will skip
`(stride - 1)` input elements between each element that appears in the
window. Output windows will still contain `size` elements regardless of
the value of `stride`.

The `stride` argument determines the stride of the input elements, and the
`shift` argument determines the shift of the window.

For example, letting `{...}` to represent a Dataset:

- `tf.data.Dataset.range(7).window(2)` produces
  `{{0, 1}, {2, 3}, {4, 5}, {6}}`
- `tf.data.Dataset.range(7).window(3, 2, 1, True)` produces
  `{{0, 1, 2}, {2, 3, 4}, {4, 5, 6}}`
- `tf.data.Dataset.range(7).window(3, 1, 2, True)` produces
  `{{0, 2, 4}, {1, 3, 5}, {2, 4, 6}}`

Note that when the `window` transformation is applied to a dataset of
nested elements, it produces a dataset of nested windows.

#### For example:



- `tf.data.Dataset.from_tensor_slices((range(4), range(4))).window(2)`
  produces `{({0, 1}, {0, 1}), ({2, 3}, {2, 3})}`
- `tf.data.Dataset.from_tensor_slices({"a": range(4)}).window(2)`
  produces `{{"a": {0, 1}}, {"a": {2, 3}}}`

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor` of type `int64`.
An integer scalar, representing the number of elements
of the input dataset to combine into a window. Must be positive.
</td>
</tr><tr>
<td>
`shift`
</td>
<td>
A `Tensor` of type `int64`.
An integer scalar, representing the number of input elements
by which the window moves in each iteration.  Defaults to `size`.
Must be positive.
</td>
</tr><tr>
<td>
`stride`
</td>
<td>
A `Tensor` of type `int64`.
An integer scalar, representing the stride of the input elements
in the sliding window. Must be positive. The default value of 1 means
"retain every input element".
</td>
</tr><tr>
<td>
`drop_remainder`
</td>
<td>
A `Tensor` of type `bool`.
A Boolean scalar, representing whether the last window should be
dropped if its size is smaller than `window_size`.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

