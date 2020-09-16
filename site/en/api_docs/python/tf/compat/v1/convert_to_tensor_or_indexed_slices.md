description: Converts the given object to a Tensor or an IndexedSlices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.convert_to_tensor_or_indexed_slices" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.convert_to_tensor_or_indexed_slices

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/indexed_slices.py#L258-L280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts the given object to a `Tensor` or an `IndexedSlices`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.convert_to_tensor_or_indexed_slices(
    value, dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If `value` is an `IndexedSlices` or `SparseTensor` it is returned
unmodified. Otherwise, it is converted to a `Tensor` using
`convert_to_tensor()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
An `IndexedSlices`, `SparseTensor`, or an object that can be consumed
by `convert_to_tensor()`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional.) The required `DType` of the returned `Tensor` or
`IndexedSlices`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional.) A name to use if a new `Tensor` is created.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`, `IndexedSlices`, or `SparseTensor` based on `value`.
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
If `dtype` does not match the element type of `value`.
</td>
</tr>
</table>

