description: This op is used as a placeholder in If branch functions. It doesn't provide a

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.FakeParam" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.FakeParam

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



This op is used as a placeholder in If branch functions. It doesn't provide a

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FakeParam`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FakeParam(
    dtype, shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
valid output when run, so must either be removed (e.g. replaced with a
function input) or guaranteed not to be used (e.g. if mirroring an
intermediate output needed for the gradient computation of the other branch).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>. The type of the output.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
A <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`.
The purported shape of the output. This is only used for shape inference;
the output will not necessarily have this shape. Can be a partial shape.
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

