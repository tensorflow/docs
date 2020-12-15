robots: noindex

# tf.raw_ops.StatelessParameterizedTruncatedNormal

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
<p>`tf.compat.v1.raw_ops.StatelessParameterizedTruncatedNormal`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.StatelessParameterizedTruncatedNormal(
    shape, seed, means, stddevs, minvals, maxvals, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
The shape of the output tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
2 seeds (shape [2]).
</td>
</tr><tr>
<td>
`means`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
The mean parameter of each batch.
</td>
</tr><tr>
<td>
`stddevs`
</td>
<td>
A `Tensor`. Must have the same type as `means`.
The standard deviation parameter of each batch. Must be greater than 0.
</td>
</tr><tr>
<td>
`minvals`
</td>
<td>
A `Tensor`. Must have the same type as `means`.
The minimum cutoff. May be -infinity.
</td>
</tr><tr>
<td>
`maxvals`
</td>
<td>
A `Tensor`. Must have the same type as `means`.
The maximum cutoff. May be +infinity, and must be more than the minval
for each batch.
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
A `Tensor`. Has the same type as `means`.
</td>
</tr>

</table>

