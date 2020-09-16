description: Converts an array of flat indices into a tuple of coordinate arrays.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.UnravelIndex" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.UnravelIndex

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts an array of flat indices into a tuple of coordinate arrays.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.UnravelIndex`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.UnravelIndex(
    indices, dims, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Example:



```
y = tf.unravel_index(indices=[2, 5, 7], dims=[3, 3])
# 'dims' represent a hypothetical (3, 3) tensor of indices:
# [[0, 1, *2*],
#  [3, 4, *5*],
#  [6, *7*, 8]]
# For each entry from 'indices', this operation returns
# its coordinates (marked with '*'), such as
# 2 ==> (0, 2)
# 5 ==> (1, 2)
# 7 ==> (2, 1)
y ==> [[0, 1, 2], [2, 2, 1]]
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
An 0-D or 1-D `int` Tensor whose elements are indices into the
flattened version of an array of dimensions dims.
</td>
</tr><tr>
<td>
`dims`
</td>
<td>
A `Tensor`. Must have the same type as `indices`.
An 1-D `int` Tensor. The shape of the array to use for unraveling
indices.
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
A `Tensor`. Has the same type as `indices`.
</td>
</tr>

</table>



#### Numpy Compatibility
Equivalent to np.unravel_index

