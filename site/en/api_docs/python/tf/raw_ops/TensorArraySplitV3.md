description: Split the data from the input value into TensorArray elements.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TensorArraySplitV3" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TensorArraySplitV3

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Split the data from the input value into TensorArray elements.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorArraySplitV3`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorArraySplitV3(
    handle, value, lengths, flow_in, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Assuming that `lengths` takes on values

  ```(n0, n1, ..., n(T-1))```

and that `value` has shape

  ```(n0 + n1 + ... + n(T-1) x d0 x d1 x ...)```,

this splits values into a TensorArray with T tensors.

TensorArray index t will be the subtensor of values with starting position

  ```(n0 + n1 + ... + n(t-1), 0, 0, ...)```

and having size

  ```nt x d0 x d1 x ...```

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
`value`
</td>
<td>
A `Tensor`. The concatenated tensor to write to the TensorArray.
</td>
</tr><tr>
<td>
`lengths`
</td>
<td>
A `Tensor` of type `int64`.
The vector of lengths, how to split the rows of value into the
TensorArray.
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

