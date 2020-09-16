description: Rolls the elements of a tensor along an axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Roll" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Roll

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Rolls the elements of a tensor along an axis.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Roll`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Roll(
    input, shift, axis, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The elements are shifted positively (towards larger indices) by the offset of
`shift` along the dimension of `axis`. Negative `shift` values will shift
elements in the opposite direction. Elements that roll passed the last position
will wrap around to the first and vice versa. Multiple shifts along multiple
axes may be specified.

#### For example:



```
# 't' is [0, 1, 2, 3, 4]
roll(t, shift=2, axis=0) ==> [3, 4, 0, 1, 2]

# shifting along multiple dimensions
# 't' is [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
roll(t, shift=[1, -2], axis=[0, 1]) ==> [[7, 8, 9, 5, 6], [2, 3, 4, 0, 1]]

# shifting along the same axis multiple times
# 't' is [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
roll(t, shift=[2, -3], axis=[1, 1]) ==> [[1, 2, 3, 4, 0], [6, 7, 8, 9, 5]]
```

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
`shift`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Dimension must be 0-D or 1-D. `shift[i]` specifies the number of places by which
elements are shifted positively (towards larger indices) along the dimension
specified by `axis[i]`. Negative shifts will roll the elements in the opposite
direction.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Dimension must be 0-D or 1-D. `axis[i]` specifies the dimension that the shift
`shift[i]` should occur. If the same axis is referenced more than once, the
total shift for that axis will be the sum of all the shifts that belong to that
axis.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

