description: Asserts that the given Tensor is of the specified type.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_type" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_type

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L1515-L1532">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Asserts that the given `Tensor` is of the specified type.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.debugging.assert_type(
    tensor, tf_type, message=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This can always be checked statically, so this method returns nothing.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor`
</td>
<td>
A `Tensor` or `SparseTensor`.
</td>
</tr><tr>
<td>
`tf_type`
</td>
<td>
A tensorflow type (<a href="../../tf/dtypes.md#float32"><code>dtypes.float32</code></a>, <a href="../../tf.md#int64"><code>tf.int64</code></a>, <a href="../../tf/dtypes.md#bool"><code>dtypes.bool</code></a>,
etc).
</td>
</tr><tr>
<td>
`message`
</td>
<td>
A string to prefix to the default message.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation. Defaults to "assert_type"
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the tensor's data type doesn't match `tf_type`.
</td>
</tr>
</table>

