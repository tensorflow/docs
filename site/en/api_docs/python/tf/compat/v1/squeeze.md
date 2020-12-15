description: Removes dimensions of size 1 from the shape of a tensor. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.squeeze" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.squeeze

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L4327-L4379">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Removes dimensions of size 1 from the shape of a tensor. (deprecated arguments)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.squeeze(
    input, axis=None, name=None, squeeze_dims=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(squeeze_dims)`. They will be removed in a future version.
Instructions for updating:
Use the `axis` argument instead

Given a tensor `input`, this operation returns a tensor of the same type with
all dimensions of size 1 removed. If you don't want to remove all size 1
dimensions, you can remove specific size 1 dimensions by specifying
`axis`.

#### For example:



```
>>> # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
>>> t = tf.ones([1, 2, 1, 3, 1, 1])
>>> print(tf.shape(tf.squeeze(t)).numpy())
[2 3]
```

Or, to remove specific size 1 dimensions:

```
>>> # 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
>>> t = tf.ones([1, 2, 1, 3, 1, 1])
>>> print(tf.shape(tf.squeeze(t, [2, 4])).numpy())
[1 2 3 1]
```

Note: if `input` is a <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>, then this operation takes `O(N)`
time, where `N` is the number of elements in the squeezed dimensions.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. The `input` to squeeze.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An optional list of `ints`. Defaults to `[]`. If specified, only
squeezes the dimensions listed. The dimension index starts at 0. It is an
error to squeeze a dimension that is not 1. Must be in the range
`[-rank(input), rank(input))`. Must be specified if `input` is a
`RaggedTensor`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`squeeze_dims`
</td>
<td>
Deprecated keyword argument that is now axis.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `input`.
Contains the same data as `input`, but has one or more dimensions of
size 1 removed.
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
When both `squeeze_dims` and `axis` are specified.
</td>
</tr>
</table>

