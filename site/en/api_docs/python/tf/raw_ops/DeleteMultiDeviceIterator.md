description: A container for an iterator resource.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.DeleteMultiDeviceIterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.DeleteMultiDeviceIterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A container for an iterator resource.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DeleteMultiDeviceIterator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DeleteMultiDeviceIterator(
    multi_device_iterator, iterators, deleter, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`multi_device_iterator`
</td>
<td>
A `Tensor` of type `resource`.
A handle to the multi device iterator to delete.
</td>
</tr><tr>
<td>
`iterators`
</td>
<td>
A list of `Tensor` objects with type `resource`.
A list of iterator handles (unused). This is added so that automatic control dependencies get added during function tracing that ensure this op runs after all the dependent iterators are deleted.
</td>
</tr><tr>
<td>
`deleter`
</td>
<td>
A `Tensor` of type `variant`. A variant deleter.
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

