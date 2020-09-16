description: Applies L1 regularization shrink step on the parameters.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SdcaShrinkL1" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SdcaShrinkL1

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies L1 regularization shrink step on the parameters.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SdcaShrinkL1`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SdcaShrinkL1(
    weights, l1, l2, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`weights`
</td>
<td>
A list of `Tensor` objects with type mutable `float32`.
a list of vectors where each value is the weight associated with a
feature group.
</td>
</tr><tr>
<td>
`l1`
</td>
<td>
A `float`. Symmetric l1 regularization strength.
</td>
</tr><tr>
<td>
`l2`
</td>
<td>
A `float`.
Symmetric l2 regularization strength. Should be a positive float.
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

