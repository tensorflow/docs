description: Concatenates tensors along one dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Concat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Concat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Concatenates tensors along one dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Concat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Concat(
    concat_dim, values, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
0-D.  The dimension along which to concatenate.  Must be in the
range [0, rank(values)).
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A list of at least 2 `Tensor` objects with the same type.
The `N` Tensors to concatenate. Their ranks and types must match,
and their sizes must match in all dimensions except `concat_dim`.
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

