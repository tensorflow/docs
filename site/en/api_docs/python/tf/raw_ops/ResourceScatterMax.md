description: Reduces sparse updates into the variable referenced by resource using the max operation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ResourceScatterMax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ResourceScatterMax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reduces sparse updates into the variable referenced by `resource` using the `max` operation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ResourceScatterMax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ResourceScatterMax(
    resource, indices, updates, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation computes

    # Scalar indices
    ref[indices, ...] = max(ref[indices, ...], updates[...])

    # Vector indices (for each i)
    ref[indices[i], ...] = max(ref[indices[i], ...], updates[i, ...])

    # High rank indices (for each i, ..., j)
    ref[indices[i, ..., j], ...] = max(ref[indices[i, ..., j], ...], updates[i, ..., j, ...])

Duplicate entries are handled correctly: if multiple `indices` reference
the same location, their contributions are combined.

Requires `updates.shape = indices.shape + ref.shape[1:]` or `updates.shape = []`.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%" src='https://www.tensorflow.org/images/ScatterAdd.png' alt>
</div>

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`resource`
</td>
<td>
A `Tensor` of type `resource`. Should be from a `Variable` node.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
A tensor of indices into the first dimension of `ref`.
</td>
</tr><tr>
<td>
`updates`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
A tensor of updated values to add to `ref`.
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
The created Operation.
</td>
</tr>

</table>

