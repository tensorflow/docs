description: Create the Resource for Quantile Streams.

robots: noindex

# tf.raw_ops.BoostedTreesCreateQuantileStreamResource

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Create the Resource for Quantile Streams.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesCreateQuantileStreamResource`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesCreateQuantileStreamResource(
    quantile_stream_resource_handle, epsilon, num_streams,
    max_elements=1099511627776, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`quantile_stream_resource_handle`
</td>
<td>
A `Tensor` of type `resource`.
resource; Handle to quantile stream resource.
</td>
</tr><tr>
<td>
`epsilon`
</td>
<td>
A `Tensor` of type `float32`.
float; The required approximation error of the stream resource.
</td>
</tr><tr>
<td>
`num_streams`
</td>
<td>
A `Tensor` of type `int64`.
int; The number of streams managed by the resource that shares the same epsilon.
</td>
</tr><tr>
<td>
`max_elements`
</td>
<td>
An optional `int`. Defaults to `1099511627776`.
int; The maximum number of data points that can be fed to the stream.
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

