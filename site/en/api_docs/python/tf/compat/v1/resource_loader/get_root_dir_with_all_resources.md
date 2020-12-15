description: Get a root directory containing all the data attributes in the build rule.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.resource_loader.get_root_dir_with_all_resources" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.resource_loader.get_root_dir_with_all_resources

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/platform/resource_loader.py#L63-L100">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get a root directory containing all the data attributes in the build rule.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.resource_loader.get_root_dir_with_all_resources()
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The path to the specified file present in the data attribute of py_test
or py_binary. Falls back to returning the same as get_data_files_path if it
fails to detect a bazel runfiles directory.
</td>
</tr>

</table>

