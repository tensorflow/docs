description: Generates a checkpoint state proto.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.generate_checkpoint_state_proto" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.generate_checkpoint_state_proto

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/checkpoint_management.py#L66-L128">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Generates a checkpoint state proto.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.generate_checkpoint_state_proto(
    save_dir, model_checkpoint_path, all_model_checkpoint_paths=None,
    all_model_checkpoint_timestamps=None, last_preserved_timestamp=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`save_dir`
</td>
<td>
Directory where the model was saved.
</td>
</tr><tr>
<td>
`model_checkpoint_path`
</td>
<td>
The checkpoint file.
</td>
</tr><tr>
<td>
`all_model_checkpoint_paths`
</td>
<td>
List of strings.  Paths to all not-yet-deleted
checkpoints, sorted from oldest to newest.  If this is a non-empty list,
the last element must be equal to model_checkpoint_path.  These paths
are also saved in the CheckpointState proto.
</td>
</tr><tr>
<td>
`all_model_checkpoint_timestamps`
</td>
<td>
A list of floats, indicating the number of
seconds since the Epoch when each checkpoint was generated.
</td>
</tr><tr>
<td>
`last_preserved_timestamp`
</td>
<td>
A float, indicating the number of seconds since
the Epoch when the last preserved checkpoint was written, e.g. due to a
`keep_checkpoint_every_n_hours` parameter (see
<a href="../../../../tf/train/CheckpointManager.md"><code>tf.train.CheckpointManager</code></a> for an implementation).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
CheckpointState proto with model_checkpoint_path and
all_model_checkpoint_paths updated to either absolute paths or
relative paths to the current save_dir.
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
If `all_model_checkpoint_timestamps` was provided but its length
does not match `all_model_checkpoint_paths`.
</td>
</tr>
</table>

