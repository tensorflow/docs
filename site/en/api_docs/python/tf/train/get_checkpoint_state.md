description: Returns CheckpointState proto from the "checkpoint" file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.get_checkpoint_state" />
<meta itemprop="path" content="Stable" />
</div>

# tf.train.get_checkpoint_state

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/checkpoint_management.py#L251-L305">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns CheckpointState proto from the "checkpoint" file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.get_checkpoint_state`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.get_checkpoint_state(
    checkpoint_dir, latest_filename=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If the "checkpoint" file contains a valid CheckpointState
proto, returns it.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`checkpoint_dir`
</td>
<td>
The directory of checkpoints.
</td>
</tr><tr>
<td>
`latest_filename`
</td>
<td>
Optional name of the checkpoint file.  Default to
'checkpoint'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A CheckpointState if the state was available, None
otherwise.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the checkpoint read doesn't have model_checkpoint_path set.
</td>
</tr>
</table>

