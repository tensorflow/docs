description: Creates a directory with the name dirname.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.gfile.MkDir" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.gfile.MkDir

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/lib/io/file_io.py#L424-L437">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a directory with the name `dirname`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.gfile.MkDir(
    dirname
)
</code></pre>



<!-- Placeholder for "Used in" -->


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


Notes: The parent directories need to exist. Use <a href="../../../../tf/io/gfile/makedirs.md"><code>tf.io.gfile.makedirs</code></a>
  instead if there is the possibility that the parent dirs don't exist.

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

