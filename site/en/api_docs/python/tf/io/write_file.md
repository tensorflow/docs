description: Writes contents to the file at input filename. Creates file and recursively

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.write_file" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.write_file

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Writes contents to the file at input filename. Creates file and recursively

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.io.write_file`, `tf.compat.v1.write_file`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.write_file(
    filename, contents, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

creates directory if not existing.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`filename`
</td>
<td>
A `Tensor` of type `string`.
scalar. The name of the file to which we write the contents.
</td>
</tr><tr>
<td>
`contents`
</td>
<td>
A `Tensor` of type `string`.
scalar. The content to be written to the output file.
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

