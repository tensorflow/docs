robots: noindex

# tf.raw_ops.WriteImageSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>





<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.WriteImageSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.WriteImageSummary(
    writer, step, tag, tensor, bad_color, max_images=3, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`writer`
</td>
<td>
A `Tensor` of type `resource`.
</td>
</tr><tr>
<td>
`step`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`tag`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`tensor`
</td>
<td>
A `Tensor`. Must be one of the following types: `uint8`, `float32`, `half`.
</td>
</tr><tr>
<td>
`bad_color`
</td>
<td>
A `Tensor` of type `uint8`.
</td>
</tr><tr>
<td>
`max_images`
</td>
<td>
An optional `int` that is `>= 1`. Defaults to `3`.
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

