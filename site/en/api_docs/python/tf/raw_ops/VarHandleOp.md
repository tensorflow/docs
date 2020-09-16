description: Creates a handle to a Variable resource.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.VarHandleOp" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.VarHandleOp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a handle to a Variable resource.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.VarHandleOp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.VarHandleOp(
    dtype, shape, container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. the type of this variable. Must agree with the dtypes
of all ops using this variable.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`.
The (possibly partially specified) shape of this variable.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
the container this variable is placed in.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
the name by which this variable is referred to.
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

