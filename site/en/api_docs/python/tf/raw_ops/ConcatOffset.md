description: Computes offsets of concat inputs within its output.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ConcatOffset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ConcatOffset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes offsets of concat inputs within its output.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ConcatOffset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ConcatOffset(
    concat_dim, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### For example:



```
# 'x' is [2, 2, 7]
# 'y' is [2, 3, 7]
# 'z' is [2, 5, 7]
concat_offset(2, [x, y, z]) => [0, 0, 0], [0, 2, 0], [0, 5, 0]
```

This is typically used by gradient computations for a concat operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`concat_dim`
</td>
<td>
A `Tensor` of type `int32`.
The dimension along which to concatenate.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A list of at least 2 `Tensor` objects with type `int32`.
The `N` int32 vectors representing shape of tensors being concatenated.
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
A list with the same length as `shape` of `Tensor` objects with type `int32`.
</td>
</tr>

</table>

