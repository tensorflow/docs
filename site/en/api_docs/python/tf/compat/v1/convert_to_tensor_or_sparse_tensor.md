description: Converts value to a SparseTensor or Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.convert_to_tensor_or_sparse_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.convert_to_tensor_or_sparse_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/sparse_tensor.py#L439-L465">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts value to a `SparseTensor` or `Tensor`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.convert_to_tensor_or_sparse_tensor(
    value, dtype=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A `SparseTensor`, `SparseTensorValue`, or an object whose type has a
registered `Tensor` conversion function.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Optional element type for the returned tensor. If missing, the type
is inferred from the type of `value`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name to use if a new `Tensor` is created.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `SparseTensor` or `Tensor` based on `value`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If result type is incompatible with `dtype`.
</td>
</tr>
</table>

