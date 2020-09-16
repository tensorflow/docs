description: Creates a dataset that emits the key-value pairs in one or more LMDB files.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.LMDBDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.LMDBDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that emits the key-value pairs in one or more LMDB files.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LMDBDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LMDBDataset(
    filenames, output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The Lightning Memory-Mapped Database Manager, or LMDB, is an embedded binary
key-value database. This dataset can read the contents of LMDB database files,
the names of which generally have the `.mdb` suffix.

Each output element consists of a key-value pair represented as a pair of
scalar string `Tensor`s, where the first `Tensor` contains the key and the
second `Tensor` contains the value.

LMDB uses different file formats on big- and little-endian machines.
`LMDBDataset` can only read files in the format of the host machine.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`filenames`
</td>
<td>
A `Tensor` of type `string`.
A scalar or a vector containing the name(s) of the binary file(s) to be
read.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

