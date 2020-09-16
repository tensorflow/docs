description: Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model.get_tensor_from_tensor_info" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.saved_model.get_tensor_from_tensor_info

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/utils_impl.py#L136-L183">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the Tensor or CompositeTensor described by a TensorInfo proto. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.saved_model.get_tensor_from_tensor_info(
    tensor_info, graph=None, import_scope=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.utils.get_tensor_from_tensor_info or tf.compat.v1.saved_model.get_tensor_from_tensor_info.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor_info`
</td>
<td>
A TensorInfo proto describing a Tensor or SparseTensor or
CompositeTensor.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
The tf.Graph in which tensors are looked up. If None, the
current default graph is used.
</td>
</tr><tr>
<td>
`import_scope`
</td>
<td>
If not None, names in `tensor_info` are prefixed with this
string before lookup.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The Tensor or SparseTensor or CompositeTensor in `graph` described by
`tensor_info`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`KeyError`
</td>
<td>
If `tensor_info` does not correspond to a tensor in `graph`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `tensor_info` is malformed.
</td>
</tr>
</table>

