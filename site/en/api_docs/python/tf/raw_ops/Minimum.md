description: Returns the min of x and y (i.e. x < y ? x : y) element-wise.

robots: noindex

# tf.raw_ops.Minimum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the min of x and y (i.e. x < y ? x : y) element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Minimum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Minimum(
    x, y, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Both inputs are number-type tensors (except complex).  `minimum` expects that
both tensors have the same `dtype`.

#### Examples:



```
>>> x = tf.constant([0., 0., 0., 0.])
>>> y = tf.constant([-5., -2., 0., 3.])
>>> tf.math.minimum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([-5., -2., 0., 0.], dtype=float32)>
```

Note that `minimum` supports broadcast semantics.

```
>>> x = tf.constant([-5., 0., 0., 0.])
>>> y = tf.constant([-3.])
>>> tf.math.minimum(x, y)
<tf.Tensor: shape=(4,), dtype=float32, numpy=array([-5., -3., -3., -3.], dtype=float32)>
```

If inputs are not tensors, they will be converted to tensors.  See
<a href="../../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>.

```
>>> x = tf.constant([-3.], dtype=tf.float32)
>>> tf.math.minimum([-5], x)
<tf.Tensor: shape=(1,), dtype=float32, numpy=array([-5.], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int16`, `int32`, `int64`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A `Tensor`. Must have the same type as `x`.
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
A `Tensor`. Has the same type as `x`.
</td>
</tr>

</table>

