description: Creates a directory and all parent/intermediate directories.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.gfile.MakeDirs" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.gfile.MakeDirs

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/file_io.py#L456-L468">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a directory and all parent/intermediate directories.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.gfile.MakeDirs(
    dirname
)
</code></pre>



<!-- Placeholder for "Used in" -->

It succeeds if dirname already exists and is writable.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`dirname`
</td>
<td>
string, name of the directory to be created
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`errors.OpError`
</td>
<td>
If the operation fails.
</td>
</tr>
</table>

