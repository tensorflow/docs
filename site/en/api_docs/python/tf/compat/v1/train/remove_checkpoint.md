description: Removes a checkpoint given by checkpoint_prefix. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.remove_checkpoint" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.remove_checkpoint

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/checkpoint_management.py#L459-L484">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Removes a checkpoint given by `checkpoint_prefix`. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.remove_checkpoint(
    checkpoint_prefix, checkpoint_format_version=tf.train.SaverDef.V2,
    meta_graph_suffix='meta'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use standard file APIs to delete files with this prefix.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`checkpoint_prefix`
</td>
<td>
The prefix of a V1 or V2 checkpoint. Typically the result
of `Saver.save()` or that of <a href="../../../../tf/train/latest_checkpoint.md"><code>tf.train.latest_checkpoint()</code></a>, regardless of
sharded/non-sharded or V1/V2.
</td>
</tr><tr>
<td>
`checkpoint_format_version`
</td>
<td>
`SaverDef.CheckpointFormatVersion`, defaults to
`SaverDef.V2`.
</td>
</tr><tr>
<td>
`meta_graph_suffix`
</td>
<td>
Suffix for `MetaGraphDef` file. Defaults to 'meta'.
</td>
</tr>
</table>

