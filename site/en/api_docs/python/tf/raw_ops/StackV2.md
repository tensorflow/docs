description: A stack that produces elements in first-in last-out order.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.StackV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.StackV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A stack that produces elements in first-in last-out order.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.StackV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StackV2(
    max_size, elem_type, stack_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`max_size`
</td>
<td>
A `Tensor` of type `int32`.
The maximum size of the stack if non-negative. If negative, the stack
size is unlimited.
</td>
</tr><tr>
<td>
`elem_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. The type of the elements on the stack.
</td>
</tr><tr>
<td>
`stack_name`
</td>
<td>
An optional `string`. Defaults to `""`.
Overrides the name used for the temporary stack resource. Default
value is the name of the 'Stack' op (which is guaranteed unique).
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

