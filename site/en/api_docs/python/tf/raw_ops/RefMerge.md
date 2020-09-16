description: Forwards the value of an available tensor from inputs to output.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RefMerge" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RefMerge

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Forwards the value of an available tensor from `inputs` to `output`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RefMerge`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RefMerge(
    inputs, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`Merge` waits for at least one of the tensors in `inputs` to become available.
It is usually combined with `Switch` to implement branching.

`Merge` forwards the first tensor for become available to `output`, and sets
`value_index` to its index in `inputs`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of at least 1 mutable `Tensor` objects with the same type.
The input tensors, exactly one of which will become available.
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
A tuple of `Tensor` objects (output, value_index).
</td>
</tr>
<tr>
<td>
`output`
</td>
<td>
A mutable `Tensor`. Has the same type as `inputs`.
</td>
</tr><tr>
<td>
`value_index`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

