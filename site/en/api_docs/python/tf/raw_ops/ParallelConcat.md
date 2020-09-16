description: Concatenates a list of N tensors along the first dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ParallelConcat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ParallelConcat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Concatenates a list of `N` tensors along the first dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParallelConcat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParallelConcat(
    values, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input tensors are all required to have size 1 in the first dimension.

#### For example:



```
# 'x' is [[1, 4]]
# 'y' is [[2, 5]]
# 'z' is [[3, 6]]
parallel_concat([x, y, z]) => [[1, 4], [2, 5], [3, 6]]  # Pack along first dim.
```

The difference between concat and parallel_concat is that concat requires all
of the inputs be computed before the operation will begin but doesn't require
that the input shapes be known during graph construction.  Parallel concat
will copy pieces of the input into the output as they become available, in
some situations this can provide a performance benefit.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type.
Tensors to be concatenated. All must have size 1 in the first dimension
and same shape.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`.
the final shape of the result; should be equal to the shapes of any input
but with the number of input values in the first dimension.
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
A `Tensor`. Has the same type as `values`.
</td>
</tr>

</table>

