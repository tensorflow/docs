description: Return the reduction indices for computing gradients of s0 op s1 with broadcast.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BroadcastGradientArgs" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BroadcastGradientArgs

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Return the reduction indices for computing gradients of s0 op s1 with broadcast.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BroadcastGradientArgs`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BroadcastGradientArgs(
    s0, s1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is typically used by gradient computations for a broadcasting operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`s0`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
</td>
</tr><tr>
<td>
`s1`
</td>
<td>
A `Tensor`. Must have the same type as `s0`.
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
A tuple of `Tensor` objects (r0, r1).
</td>
</tr>
<tr>
<td>
`r0`
</td>
<td>
A `Tensor`. Has the same type as `s0`.
</td>
</tr><tr>
<td>
`r1`
</td>
<td>
A `Tensor`. Has the same type as `s0`.
</td>
</tr>
</table>

