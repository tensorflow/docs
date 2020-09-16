description: Checks whether a quantile stream has been initialized.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Checks whether a quantile stream has been initialized.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.IsBoostedTreesQuantileStreamResourceInitialized(
    quantile_stream_resource_handle, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An Op that checks if quantile stream resource is initialized.

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
resource; The reference to quantile stream resource handle.
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

