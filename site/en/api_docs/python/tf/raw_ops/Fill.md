description: Creates a tensor filled with a scalar value.

robots: noindex

# tf.raw_ops.Fill

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a tensor filled with a scalar value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Fill`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Fill(
    dims, value, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation creates a tensor of shape `dims` and fills it with `value`.

#### For example:



```
# Output tensor has shape [2, 3].
fill([2, 3], 9) ==> [[9, 9, 9]
                     [9, 9, 9]]
```

<a href="../../tf/fill.md"><code>tf.fill</code></a> differs from <a href="../../tf/constant.md"><code>tf.constant</code></a> in a few ways:

*   <a href="../../tf/fill.md"><code>tf.fill</code></a> only supports scalar contents, whereas <a href="../../tf/constant.md"><code>tf.constant</code></a> supports
    Tensor values.
*   <a href="../../tf/fill.md"><code>tf.fill</code></a> creates an Op in the computation graph that constructs the actual
    Tensor value at runtime. This is in contrast to <a href="../../tf/constant.md"><code>tf.constant</code></a> which embeds
    the entire Tensor into the graph with a `Const` node.
*   Because <a href="../../tf/fill.md"><code>tf.fill</code></a> evaluates at graph runtime, it supports dynamic shapes
    based on other runtime Tensors, unlike <a href="../../tf/constant.md"><code>tf.constant</code></a>.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dims`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
1-D. Represents the shape of the output tensor.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A `Tensor`. 0-D (scalar). Value to fill the returned tensor.
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
A `Tensor`. Has the same type as `value`.
</td>
</tr>

</table>



#### Numpy Compatibility
Equivalent to np.full

