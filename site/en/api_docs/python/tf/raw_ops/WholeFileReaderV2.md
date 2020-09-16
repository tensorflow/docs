description: A Reader that outputs the entire contents of a file as a value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.WholeFileReaderV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.WholeFileReaderV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



A Reader that outputs the entire contents of a file as a value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.WholeFileReaderV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.WholeFileReaderV2(
    container='', shared_name='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

To use, enqueue filenames in a Queue.  The output of ReaderRead will
be a filename (key) and the contents of that file (value).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this reader is placed in the given container.
Otherwise, a default container is used.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
An optional `string`. Defaults to `""`.
If non-empty, this reader is named in the given bucket
with this shared_name. Otherwise, the node name is used instead.
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
A `Tensor` of type `resource`.
</td>
</tr>

</table>

