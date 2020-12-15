description: Returns a tensor with an length 1 axis inserted at index axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.expand_dims" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.expand_dims

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/sparse_ops.py#L130-L233">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a tensor with an length 1 axis inserted at index `axis`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.expand_dims`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.expand_dims(
    sp_input, axis=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation inserts a dimension of length 1 at the
dimension index `axis` of `input`'s shape. The dimension index follows python
indexing rules: It's zero-based, a negative index it is counted backward
from the end.

This operation is useful to:

* Add an outer "batch" dimension to a single element.
* Align axes for broadcasting.
* To add an inner vector length axis to a tensor of scalars.

#### For example:



If you have a sparse tensor with shape `[height, width, depth]`:

```
>>> sp = tf.sparse.SparseTensor(indices=[[3,4,1]], values=[7,],
...                             dense_shape=[10,10,3])
```

You can add an outer `batch` axis by passing `axis=0`:

```
>>> tf.sparse.expand_dims(sp, axis=0).shape.as_list()
[1, 10, 10, 3]
```

The new axis location matches Python `list.insert(axis, 1)`:

```
>>> tf.sparse.expand_dims(sp, axis=1).shape.as_list()
[10, 1, 10, 3]
```

Following standard python indexing rules, a negative `axis` counts from the
end so `axis=-1` adds an inner most dimension:

```
>>> tf.sparse.expand_dims(sp, axis=-1).shape.as_list()
[10, 10, 3, 1]
```

Note: Unlike <a href="../../tf/expand_dims.md"><code>tf.expand_dims</code></a> this function includes a default value for the
`axis`: `-1`. So if `axis is not specified, an inner dimension is added.

```
>>> sp.shape.as_list()
[10, 10, 3]
>>> tf.sparse.expand_dims(sp).shape.as_list()
[10, 10, 3, 1]
```

This operation requires that `axis` is a valid index for `input.shape`,
following python indexing rules:

```
-1-tf.rank(input) <= axis <= tf.rank(input)
```

This operation is related to:

* <a href="../../tf/expand_dims.md"><code>tf.expand_dims</code></a>, which provides this functionality for dense tensors.
* <a href="../../tf/squeeze.md"><code>tf.squeeze</code></a>, which removes dimensions of size 1, from dense tensors.
* <a href="../../tf/sparse/reshape.md"><code>tf.sparse.reshape</code></a>, which provides more flexible reshaping capability.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
A `SparseTensor`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
0-D (scalar). Specifies the dimension index at which to expand the
shape of `input`. Must be in the range `[-rank(sp_input) - 1,
rank(sp_input)]`. Defaults to `-1`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
The name of the output `SparseTensor`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` with the same data as `sp_input`, but its shape has an
additional dimension of size 1 added.
</td>
</tr>

</table>

