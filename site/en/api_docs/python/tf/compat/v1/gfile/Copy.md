description: Copies data from oldpath to newpath.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.gfile.Copy" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.gfile.Copy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/file_io.py#L486-L499">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Copies data from `oldpath` to `newpath`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.gfile.Copy(
    oldpath, newpath, overwrite=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`oldpath`
</td>
<td>
string, name of the file who's contents need to be copied
</td>
</tr><tr>
<td>
`newpath`
</td>
<td>
string, name of the file to which to copy to
</td>
</tr><tr>
<td>
`overwrite`
</td>
<td>
boolean, if false it's an error for `newpath` to be occupied by
an existing file.
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

