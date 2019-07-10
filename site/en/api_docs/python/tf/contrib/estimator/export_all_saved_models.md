page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.export_all_saved_models

``` python
tf.contrib.estimator.export_all_saved_models(
    estimator,
    export_dir_base,
    input_receiver_fn_map,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    strip_default_attrs=False
)
```

Exports requested train/eval/predict graphs as separate SavedModels.

See tf.contrib.estimator.export_all_saved_models for the currently
exposed version of this function.

For each mode passed in via the input_receiver_fn_map,
this method builds a new graph by calling the input_receiver_fn to obtain
feature and label `Tensor`s. Next, this method calls the `Estimator`'s
model_fn in the passed mode to generate the model graph based on
those features and labels, and restores the given checkpoint
(or, lacking that, the most recent checkpoint) into the graph.
Only one of the modes is used for saving variables to the SavedModel
(order of preference: TRAIN, EVAL, then PREDICT), such that up to three
MetaGraphDefs are saved with a single set of variables in a single
SavedModel directory.

For prediction, the exported `MetaGraphDef` will provide one `SignatureDef`
for each element of the export_outputs dict returned from the model_fn,
named using the same keys.  One of these keys is always
signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY, indicating which
signature will be served when a serving request does not specify one.
For each signature, the outputs are provided by the corresponding
`ExportOutput`s, and the inputs are always the input receivers provided by
the serving_input_receiver_fn.

For training and evaluation, the train_op is stored in an extra collection,
and loss, metrics, and predictions are included in a SignatureDef for the
mode in question.

Extra assets may be written into the SavedModel via the assets_extra
argument.  This should be a dict, where each key gives a destination path
(including the filename) relative to the assets.extra directory.  The
corresponding value gives the full path of the source file to be copied.
For example, the simple case of copying a single file without renaming it
is specified as `{'my_asset_file.txt': '/path/to/my_asset_file.txt'}`.

Sample usage:

```python
classifier = tf.estimator.LinearClassifier(
    feature_columns=[age, language])
classifier.train(input_fn=input_fn)

feature_spec = {
    'age': tf.placeholder(dtype=tf.int64),
    'language': array_ops.placeholder(dtype=tf.string)
}
label_spec = tf.placeholder(dtype=dtypes.int64)

train_rcvr_fn = tf.contrib.estimator.build_raw_supervised_input_receiver_fn(
    feature_spec, label_spec)

serve_rcvr_fn = tf.estimator.export.build_parsing_serving_input_receiver_fn(
    feature_spec)

rcvr_fn_map = {
    model_fn_lib.ModeKeys.TRAIN: train_rcvr_fn,
    model_fn_lib.ModeKeys.PREDICT: serve_rcvr_fn,
}

export_dir = tf.contrib.estimator.export_all_saved_models(
    classifier,
    export_dir_base='my_model/',
    input_receiver_fn_map=rcvr_fn_map)

# export_dirs is a dict of directories with SavedModels, which
# can be used for serving, analysis with TFMA, or directly loaded in.
with ops.Graph().as_default() as graph:
  with session.Session(graph=graph) as sess:
    loader.load(sess, [tag_constants.TRAINING], export_dir)
    weights = graph.get_tensor_by_name('linear/linear_model/age/weights')
    ...
```

#### Args:

* <b>`estimator`</b>: an instance of tf.estimator.Estimator
* <b>`export_dir_base`</b>: A string containing a directory in which to create
    timestamped subdirectories containing exported SavedModels.
* <b>`input_receiver_fn_map`</b>: dict of tf.estimator.ModeKeys to input_receiver_fn
    mappings, where the input_receiver_fn is a function that takes no
    argument and returns the appropriate subclass of `InputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported SavedModel, or `None` if no extra assets are needed.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
    the most recent checkpoint found within the model directory is chosen.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
    removed from the NodeDefs. For a detailed guide, see
    [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).


#### Returns:

A dict of tf.estimator.ModeKeys value to string path for each exported
directory.


#### Raises:

* <b>`ValueError`</b>: if any input_receiver_fn is None, no export_outputs
    are provided, or no checkpoint can be found.