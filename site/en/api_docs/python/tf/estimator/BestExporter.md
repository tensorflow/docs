description: This class exports the serving graph and checkpoints of the best models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.BestExporter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="export"/>
</div>

# tf.estimator.BestExporter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



This class exports the serving graph and checkpoints of the best models.

Inherits From: [`Exporter`](../../tf/estimator/Exporter.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.BestExporter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.BestExporter(
    name='best_exporter', serving_input_receiver_fn=None,
    event_file_pattern='eval/*.tfevents.*', compare_fn=_loss_smaller,
    assets_extra=None, as_text=(False), exports_to_keep=5
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class performs a model export everytime the new model is better than any
existing model.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
unique name of this `Exporter` that is going to be used in the
export path.
</td>
</tr><tr>
<td>
`serving_input_receiver_fn`
</td>
<td>
a function that takes no arguments and returns
a `ServingInputReceiver`.
</td>
</tr><tr>
<td>
`event_file_pattern`
</td>
<td>
event file name pattern relative to model_dir. If
None, however, the exporter would not be preemption-safe. To be
preemption-safe, event_file_pattern must be specified.
</td>
</tr><tr>
<td>
`compare_fn`
</td>
<td>
a function that compares two evaluation results and returns
true if current evaluation result is better. Follows the signature:
* Args:
* `best_eval_result`: This is the evaluation result of the best model.
* `current_eval_result`: This is the evaluation result of current
candidate model.
* Returns: True if current evaluation result is better; otherwise,
False.
</td>
</tr><tr>
<td>
`assets_extra`
</td>
<td>
An optional dict specifying how to populate the assets.extra
directory within the exported SavedModel.  Each key should give the
destination path (including the filename) relative to the assets.extra
directory.  The corresponding value gives the full path of the source
file to be copied.  For example, the simple case of copying a single
file without renaming it is specified as `{'my_asset_file.txt':
'/path/to/my_asset_file.txt'}`.
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
whether to write the SavedModel proto in text format. Defaults to
`False`.
</td>
</tr><tr>
<td>
`exports_to_keep`
</td>
<td>
Number of exports to keep.  Older exports will be
garbage-collected.  Defaults to 5.  Set to `None` to disable garbage
collection.
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
if any argument is invalid.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
Directory name.

A directory name under the export base directory where exports of
this type are written.  Should not be `None` nor empty.
</td>
</tr>
</table>



## Methods

<h3 id="export"><code>export</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/exporter.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>export(
    estimator, export_path, checkpoint_path, eval_result, is_the_final_export
)
</code></pre>

Exports the given `Estimator` to a specific format.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`estimator`
</td>
<td>
the `Estimator` to export.
</td>
</tr><tr>
<td>
`export_path`
</td>
<td>
A string containing a directory where to write the export.
</td>
</tr><tr>
<td>
`checkpoint_path`
</td>
<td>
The checkpoint path to export.
</td>
</tr><tr>
<td>
`eval_result`
</td>
<td>
The output of <a href="../../tf/compat/v1/estimator/Estimator.md#evaluate"><code>Estimator.evaluate</code></a> on this checkpoint.
</td>
</tr><tr>
<td>
`is_the_final_export`
</td>
<td>
This boolean is True when this is an export in the
end of training.  It is False for the intermediate exports during the
training. When passing `Exporter` to <a href="../../tf/estimator/train_and_evaluate.md"><code>tf.estimator.train_and_evaluate</code></a>
`is_the_final_export` is always False if <a href="../../tf/estimator/TrainSpec.md#max_steps"><code>TrainSpec.max_steps</code></a> is
`None`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The string path to the exported directory or `None` if export is skipped.
</td>
</tr>

</table>





