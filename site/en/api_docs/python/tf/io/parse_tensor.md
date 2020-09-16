description: Transforms a serialized tensorflow.TensorProto proto into a Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.parse_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.parse_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Transforms a serialized tensorflow.TensorProto proto into a Tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.parse_tensor`, `tf.compat.v1.parse_tensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.parse_tensor(
    serialized, out_type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`serialized`
</td>
<td>
A `Tensor` of type `string`.
A scalar string containing a serialized TensorProto proto.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
The type of the serialized tensor.  The provided type must match the
type of the serialized tensor and no implicit conversion will take place.
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
A `Tensor` of type `out_type`.
</td>
</tr>

</table>

