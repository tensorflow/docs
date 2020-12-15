description: Returns a tensor with a length 1 axis inserted at index axis. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.expand_dims" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.expand_dims

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L295-L365">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a tensor with a length 1 axis inserted at index `axis`. (deprecated arguments)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.expand_dims(
    input, axis=None, name=None, dim=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
Use the `axis` argument instead

Given a tensor `input`, this operation inserts a dimension of length 1 at the
dimension index `axis` of `input`'s shape. The dimension index follows Python
indexing rules: It's zero-based, a negative index it is counted backward
from the end.

This operation is useful to:

* Add an outer "batch" dimension to a single element.
* Align axes for broadcasting.
* To add an inner vector length axis to a tensor of scalars.

#### For example:



If you have a single image of shape `[height, width, channels]`:

```
>>> image = tf.zeros([10,10,3])
```

You can add an outer `batch` axis by passing `axis=0`:

```
>>> tf.expand_dims(image, axis=0).shape.as_list()
[1, 10, 10, 3]
```

The new axis location matches Python `list.insert(axis, 1)`:

```
>>> tf.expand_dims(image, axis=1).shape.as_list()
[10, 1, 10, 3]
```

Following standard Python indexing rules, a negative `axis` counts from the
end so `axis=-1` adds an inner most dimension:

```
>>> tf.expand_dims(image, -1).shape.as_list()
[10, 10, 3, 1]
```

This operation requires that `axis` is a valid index for `input.shape`,
following Python indexing rules:

```
-1-tf.rank(input) <= axis <= tf.rank(input)
```

This operation is related to:

* <a href="../../../tf/squeeze.md"><code>tf.squeeze</code></a>, which removes dimensions of size 1.
* <a href="../../../tf/reshape.md"><code>tf.reshape</code></a>, which provides more flexible reshaping capability.
* <a href="../../../tf/sparse/expand_dims.md"><code>tf.sparse.expand_dims</code></a>, which provides this functionality for
  <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
0-D (scalar). Specifies the dimension index at which to expand the
shape of `input`. Must be in the range `[-rank(input) - 1, rank(input)]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the output `Tensor` (optional).
</td>
</tr><tr>
<td>
`dim`
</td>
<td>
0-D (scalar). Equivalent to `axis`, to be deprecated.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` with the same data as `input`, but its shape has an additional
dimension of size 1 added.
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
if either both or neither of `dim` and `axis` are specified.
</td>
</tr>
</table>

