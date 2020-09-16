description: Push an element onto the tensor_array.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TensorArrayWriteV3" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TensorArrayWriteV3

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Push an element onto the tensor_array.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorArrayWriteV3`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorArrayWriteV3(
    handle, index, value, flow_in, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type `resource`. The handle to a TensorArray.
</td>
</tr><tr>
<td>
`index`
</td>
<td>
A `Tensor` of type `int32`.
The position to write to inside the TensorArray.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A `Tensor`. The tensor to write to the TensorArray.
</td>
</tr><tr>
<td>
`flow_in`
</td>
<td>
A `Tensor` of type `float32`.
A float scalar that enforces proper chaining of operations.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

