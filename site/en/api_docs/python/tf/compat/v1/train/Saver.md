description: Saves and restores variables.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.Saver" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_saver_def"/>
<meta itemprop="property" content="build"/>
<meta itemprop="property" content="export_meta_graph"/>
<meta itemprop="property" content="from_proto"/>
<meta itemprop="property" content="recover_last_checkpoints"/>
<meta itemprop="property" content="restore"/>
<meta itemprop="property" content="save"/>
<meta itemprop="property" content="set_last_checkpoints"/>
<meta itemprop="property" content="set_last_checkpoints_with_time"/>
<meta itemprop="property" content="to_proto"/>
</div>

# tf.compat.v1.train.Saver

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L614-L1347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Saves and restores variables.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.Saver(
    var_list=None, reshape=(False), sharded=(False), max_to_keep=5,
    keep_checkpoint_every_n_hours=10000.0, name=None, restore_sequentially=(False),
    saver_def=None, builder=None, defer_build=(False), allow_empty=(False),
    write_version=tf.train.SaverDef.V2, pad_step_number=(False),
    save_relative_paths=(False), filename=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See [Variables](https://tensorflow.org/guide/variables)
for an overview of variables, saving and restoring.

The `Saver` class adds ops to save and restore variables to and from
*checkpoints*.  It also provides convenience methods to run these ops.

Checkpoints are binary files in a proprietary format which map variable names
to tensor values.  The best way to examine the contents of a checkpoint is to
load it using a `Saver`.

Savers can automatically number checkpoint filenames with a provided counter.
This lets you keep multiple checkpoints at different steps while training a
model.  For example you can number the checkpoint filenames with the training
step number.  To avoid filling up disks, savers manage checkpoint files
automatically. For example, they can keep only the N most recent files, or
one checkpoint for every N hours of training.

You number checkpoint filenames by passing a value to the optional
`global_step` argument to `save()`:

```python
saver.save(sess, 'my-model', global_step=0) ==> filename: 'my-model-0'
...
saver.save(sess, 'my-model', global_step=1000) ==> filename: 'my-model-1000'
```

Additionally, optional arguments to the `Saver()` constructor let you control
the proliferation of checkpoint files on disk:

* `max_to_keep` indicates the maximum number of recent checkpoint files to
  keep.  As new files are created, older files are deleted.   If None or 0,
  no checkpoints are deleted from the filesystem but only the last one is
  kept in the `checkpoint` file.  Defaults to 5 (that is, the 5 most recent
  checkpoint files are kept.)

* `keep_checkpoint_every_n_hours`: In addition to keeping the most recent
  `max_to_keep` checkpoint files, you might want to keep one checkpoint file
  for every N hours of training.  This can be useful if you want to later
  analyze how a model progressed during a long training session.  For
  example, passing `keep_checkpoint_every_n_hours=2` ensures that you keep
  one checkpoint file for every 2 hours of training.  The default value of
  10,000 hours effectively disables the feature.

Note that you still have to call the `save()` method to save the model.
Passing these arguments to the constructor will not save variables
automatically for you.

A training program that saves regularly looks like:

```python
...
# Create a saver.
saver = tf.compat.v1.train.Saver(...variables...)
# Launch the graph and train, saving the model every 1,000 steps.
sess = tf.compat.v1.Session()
for step in xrange(1000000):
    sess.run(..training_op..)
    if step % 1000 == 0:
        # Append the step number to the checkpoint name:
        saver.save(sess, 'my-model', global_step=step)
```

In addition to checkpoint files, savers keep a protocol buffer on disk with
the list of recent checkpoints. This is used to manage numbered checkpoint
files and by `latest_checkpoint()`, which makes it easy to discover the path
to the most recent checkpoint. That protocol buffer is stored in a file named
'checkpoint' next to the checkpoint files.

If you create several savers, you can specify a different filename for the
protocol buffer file in the call to `save()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`var_list`
</td>
<td>
A list of `Variable`/`SaveableObject`, or a dictionary mapping
names to `SaveableObject`s. If `None`, defaults to the list of all
saveable objects.
</td>
</tr><tr>
<td>
`reshape`
</td>
<td>
If `True`, allows restoring parameters from a checkpoint where
the variables have a different shape.
</td>
</tr><tr>
<td>
`sharded`
</td>
<td>
If `True`, shard the checkpoints, one per device.
</td>
</tr><tr>
<td>
`max_to_keep`
</td>
<td>
Maximum number of recent checkpoints to keep. Defaults to 5.
</td>
</tr><tr>
<td>
`keep_checkpoint_every_n_hours`
</td>
<td>
How often to keep checkpoints. Defaults to
10,000 hours.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
String.  Optional name to use as a prefix when adding operations.
</td>
</tr><tr>
<td>
`restore_sequentially`
</td>
<td>
A `Bool`, which if true, causes restore of different
variables to happen sequentially within each device.  This can lower
memory usage when restoring very large models.
</td>
</tr><tr>
<td>
`saver_def`
</td>
<td>
Optional `SaverDef` proto to use instead of running the
builder. This is only useful for specialty code that wants to recreate a
`Saver` object for a previously built `Graph` that had a `Saver`. The
`saver_def` proto should be the one returned by the `as_saver_def()`
call of the `Saver` that was created for that `Graph`.
</td>
</tr><tr>
<td>
`builder`
</td>
<td>
Optional `SaverBuilder` to use if a `saver_def` was not provided.
Defaults to `BulkSaverBuilder()`.
</td>
</tr><tr>
<td>
`defer_build`
</td>
<td>
If `True`, defer adding the save and restore ops to the
`build()` call. In that case `build()` should be called before
finalizing the graph or using the saver.
</td>
</tr><tr>
<td>
`allow_empty`
</td>
<td>
If `False` (default) raise an error if there are no variables
in the graph. Otherwise, construct the saver anyway and make it a no-op.
</td>
</tr><tr>
<td>
`write_version`
</td>
<td>
controls what format to use when saving checkpoints.  It
also affects certain filepath matching logic.  The V2 format is the
recommended choice: it is much more optimized than V1 in terms of memory
required and latency incurred during restore.  Regardless of this
flag, the Saver is able to restore from both V2 and V1 checkpoints.
</td>
</tr><tr>
<td>
`pad_step_number`
</td>
<td>
if True, pads the global step number in the checkpoint
filepaths to some fixed width (8 by default).  This is turned off by
default.
</td>
</tr><tr>
<td>
`save_relative_paths`
</td>
<td>
If `True`, will write relative paths to the
checkpoint state file. This is needed if the user wants to copy the
checkpoint directory and reload from the copied directory.
</td>
</tr><tr>
<td>
`filename`
</td>
<td>
If known at graph construction time, filename used for variable
loading/saving.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `var_list` is invalid.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If any of the keys or values in `var_list` are not unique.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If eager execution is enabled and`var_list` does not specify
a list of variables to save.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`last_checkpoints`
</td>
<td>
List of not-yet-deleted checkpoint filenames.

You can pass any of the returned values to `restore()`.
</td>
</tr>
</table>



## Methods

<h3 id="as_saver_def"><code>as_saver_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L975-L981">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_saver_def()
</code></pre>

Generates a `SaverDef` representation of this saver.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `SaverDef` proto.
</td>
</tr>

</table>



<h3 id="build"><code>build</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L845-L848">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>build()
</code></pre>




<h3 id="export_meta_graph"><code>export_meta_graph</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1219-L1263">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>export_meta_graph(
    filename=None, collection_list=None, as_text=(False), export_scope=None,
    clear_devices=(False), clear_extraneous_savers=(False),
    strip_default_attrs=(False), save_debug_info=(False)
)
</code></pre>

Writes `MetaGraphDef` to save_path/filename.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`filename`
</td>
<td>
Optional meta_graph filename including the path.
</td>
</tr><tr>
<td>
`collection_list`
</td>
<td>
List of string keys to collect.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
If `True`, writes the meta_graph as an ASCII proto.
</td>
</tr><tr>
<td>
`export_scope`
</td>
<td>
Optional `string`. Name scope to remove.
</td>
</tr><tr>
<td>
`clear_devices`
</td>
<td>
Whether or not to clear the device field for an `Operation`
or `Tensor` during export.
</td>
</tr><tr>
<td>
`clear_extraneous_savers`
</td>
<td>
Remove any Saver-related information from the
graph (both Save/Restore ops and SaverDefs) that are not associated with
this Saver.
</td>
</tr><tr>
<td>
`strip_default_attrs`
</td>
<td>
Boolean. If `True`, default-valued attributes will be
removed from the NodeDefs. For a detailed guide, see
[Stripping Default-Valued
Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
</td>
</tr><tr>
<td>
`save_debug_info`
</td>
<td>
If `True`, save the GraphDebugInfo to a separate file,
which in the same directory of filename and with `_debug` added before
the file extension.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `MetaGraphDef` proto.
</td>
</tr>

</table>



<h3 id="from_proto"><code>from_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1010-L1021">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_proto(
    saver_def, import_scope=None
)
</code></pre>

Returns a `Saver` object created from `saver_def`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`saver_def`
</td>
<td>
a `SaverDef` protocol buffer.
</td>
</tr><tr>
<td>
`import_scope`
</td>
<td>
Optional `string`. Name scope to use.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Saver` built from saver_def.
</td>
</tr>

</table>



<h3 id="recover_last_checkpoints"><code>recover_last_checkpoints</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1064-L1080">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>recover_last_checkpoints(
    checkpoint_paths
)
</code></pre>

Recovers the internal saver state after a crash.

This method is useful for recovering the "self._last_checkpoints" state.

Globs for the checkpoints pointed to by `checkpoint_paths`.  If the files
exist, use their mtime as the checkpoint timestamp.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`checkpoint_paths`
</td>
<td>
a list of checkpoint paths.
</td>
</tr>
</table>



<h3 id="restore"><code>restore</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1265-L1335">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>restore(
    sess, save_path
)
</code></pre>

Restores previously saved variables.

This method runs the ops added by the constructor for restoring variables.
It requires a session in which the graph was launched.  The variables to
restore do not have to have been initialized, as restoring is itself a way
to initialize variables.

The `save_path` argument is typically a value previously returned from a
`save()` call, or a call to `latest_checkpoint()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A `Session` to use to restore the parameters. None in eager mode.
</td>
</tr><tr>
<td>
`save_path`
</td>
<td>
Path where parameters were previously saved.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If save_path is None or not a valid checkpoint.
</td>
</tr>
</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1082-L1217">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    sess, save_path, global_step=None, latest_filename=None,
    meta_graph_suffix='meta', write_meta_graph=(True), write_state=(True),
    strip_default_attrs=(False), save_debug_info=(False)
)
</code></pre>

Saves variables.

This method runs the ops added by the constructor for saving variables.
It requires a session in which the graph was launched.  The variables to
save must also have been initialized.

The method returns the path prefix of the newly created checkpoint files.
This string can be passed directly to a call to `restore()`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
A Session to use to save the variables.
</td>
</tr><tr>
<td>
`save_path`
</td>
<td>
String.  Prefix of filenames created for the checkpoint.
</td>
</tr><tr>
<td>
`global_step`
</td>
<td>
If provided the global step number is appended to `save_path`
to create the checkpoint filenames. The optional argument can be a
`Tensor`, a `Tensor` name or an integer.
</td>
</tr><tr>
<td>
`latest_filename`
</td>
<td>
Optional name for the protocol buffer file that will
contains the list of most recent checkpoints.  That file, kept in the
same directory as the checkpoint files, is automatically managed by the
saver to keep track of recent checkpoints.  Defaults to 'checkpoint'.
</td>
</tr><tr>
<td>
`meta_graph_suffix`
</td>
<td>
Suffix for `MetaGraphDef` file. Defaults to 'meta'.
</td>
</tr><tr>
<td>
`write_meta_graph`
</td>
<td>
`Boolean` indicating whether or not to write the meta
graph file.
</td>
</tr><tr>
<td>
`write_state`
</td>
<td>
`Boolean` indicating whether or not to write the
`CheckpointStateProto`.
</td>
</tr><tr>
<td>
`strip_default_attrs`
</td>
<td>
Boolean. If `True`, default-valued attributes will be
removed from the NodeDefs. For a detailed guide, see
[Stripping Default-Valued
Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
</td>
</tr><tr>
<td>
`save_debug_info`
</td>
<td>
If `True`, save the GraphDebugInfo to a separate file,
which in the same directory of save_path and with `_debug` added before
the file extension. This is only enabled when `write_meta_graph` is
`True`
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A string: path prefix used for the checkpoint files.  If the saver is
sharded, this string ends with: '-?????-of-nnnnn' where 'nnnnn'
is the number of shards created.
If the saver is empty, returns None.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `sess` is not a `Session`.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `latest_filename` contains path components, or if it
collides with `save_path`.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If save and restore ops weren't built.
</td>
</tr>
</table>



<h3 id="set_last_checkpoints"><code>set_last_checkpoints</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1034-L1049">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_last_checkpoints(
    last_checkpoints
)
</code></pre>

DEPRECATED: Use set_last_checkpoints_with_time.

Sets the list of old checkpoint filenames.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`last_checkpoints`
</td>
<td>
A list of checkpoint filenames.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
If last_checkpoints is not a list.
</td>
</tr>
</table>



<h3 id="set_last_checkpoints_with_time"><code>set_last_checkpoints_with_time</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L1051-L1062">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_last_checkpoints_with_time(
    last_checkpoints_with_time
)
</code></pre>

Sets the list of old checkpoint filenames and timestamps.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`last_checkpoints_with_time`
</td>
<td>
A list of tuples of checkpoint filenames and
timestamps.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
If last_checkpoints_with_time is not a list.
</td>
</tr>
</table>



<h3 id="to_proto"><code>to_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/saver.py#L983-L1008">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_proto(
    export_scope=None
)
</code></pre>

Converts this `Saver` to a `SaverDef` protocol buffer.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`export_scope`
</td>
<td>
Optional `string`. Name scope to remove.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `SaverDef` protocol buffer.
</td>
</tr>

</table>





