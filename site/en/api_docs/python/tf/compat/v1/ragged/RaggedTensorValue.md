description: Represents the value of a RaggedTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ragged.RaggedTensorValue" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="to_list"/>
</div>

# tf.compat.v1.ragged.RaggedTensorValue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor_value.py#L27-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents the value of a `RaggedTensor`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.ragged.RaggedTensorValue(
    values, row_splits
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: `RaggedTensorValue` should only be used in graph mode; in
eager mode, the <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> class contains its value directly.

See <a href="../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> for a description of ragged tensors.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`values`
</td>
<td>
A numpy array of any type and shape; or a RaggedTensorValue.
</td>
</tr><tr>
<td>
`row_splits`
</td>
<td>
A 1-D int32 or int64 numpy array.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
The numpy dtype of values in this tensor.
</td>
</tr><tr>
<td>
`flat_values`
</td>
<td>
The innermost `values` array for this ragged tensor value.
</td>
</tr><tr>
<td>
`nested_row_splits`
</td>
<td>
The row_splits for all ragged dimensions in this ragged tensor value.
</td>
</tr><tr>
<td>
`ragged_rank`
</td>
<td>
The number of ragged dimensions in this ragged tensor value.
</td>
</tr><tr>
<td>
`row_splits`
</td>
<td>
The split indices for the ragged tensor value.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A tuple indicating the shape of this RaggedTensorValue.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
The concatenated values for all rows in this tensor.
</td>
</tr>
</table>



## Methods

<h3 id="to_list"><code>to_list</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/ragged/ragged_tensor_value.py#L101-L110">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_list()
</code></pre>

Returns this ragged tensor value as a nested Python list.




