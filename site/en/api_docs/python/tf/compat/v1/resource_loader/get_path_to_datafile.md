description: Get the path to the specified file in the data dependencies.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.resource_loader.get_path_to_datafile" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.resource_loader.get_path_to_datafile

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/resource_loader.py#L103-L130">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get the path to the specified file in the data dependencies.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.resource_loader.get_path_to_datafile(
    path
)
</code></pre>



<!-- Placeholder for "Used in" -->

The path is relative to tensorflow/

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`path`
</td>
<td>
a string resource path relative to tensorflow/
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The path to the specified file present in the data attribute of py_test
or py_binary.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`IOError`
</td>
<td>
If the path is not found, or the resource can't be opened.
</td>
</tr>
</table>

