description: Converts a tensor to a scalar predicate.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ToBool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ToBool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts a tensor to a scalar predicate.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ToBool`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ToBool(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Converts a tensor to a scalar predicate with the following rules:

- For 0D tensors, truthiness is determined by comparing against a "zero"
  value. For numerical types it is the obvious zero. For strings it is the
  empty string.

- For >0D tensors, truthiness is determined by looking at the number of
  elements. If has zero elements, then the result is false. Otherwise the
  result is true.

This matches the behavior of If and While for determining if a tensor counts
as true/false for a branch condition.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
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
A `Tensor` of type `bool`.
</td>
</tr>

</table>

