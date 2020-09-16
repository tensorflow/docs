description: A placeholder op for a value that will be fed into the computation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Placeholder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Placeholder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A placeholder op for a value that will be fed into the computation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Placeholder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Placeholder(
    dtype, shape=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

N.B. This operation will fail with an error if it is executed. It is
intended as a way to represent a value that will always be fed, and to
provide attrs that enable the fed value to be checked at runtime.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. The type of elements in the tensor.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
An optional <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `None`.
(Optional) The shape of the tensor. If the shape has 0 dimensions, the
shape is unconstrained.
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
A `Tensor` of type `dtype`.
</td>
</tr>

</table>

