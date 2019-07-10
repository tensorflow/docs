page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.export_saved_model_for_mode

``` python
tf.contrib.estimator.export_saved_model_for_mode(
    estimator,
    export_dir_base,
    input_receiver_fn,
    assets_extra=None,
    as_text=False,
    checkpoint_path=None,
    strip_default_attrs=False,
    mode=model_fn_lib.ModeKeys.PREDICT
)
```

Exports a single train/eval/predict graph as a SavedModel.

For a detailed guide, see [Using SavedModel with Estimators](
https://tensorflow.org/guide/saved_model#using_savedmodel_with_estimators).

Sample usage:

```python
classifier = tf.estimator.LinearClassifier(
    feature_columns=[age, language])
classifier.train(input_fn=input_fn, steps=1000)

feature_spec = {
    'age': tf.placeholder(dtype=tf.int64),
    'language': array_ops.placeholder(dtype=tf.string)
}
label_spec = tf.placeholder(dtype=dtypes.int64)

train_rcvr_fn = tf.contrib.estimator.build_raw_supervised_input_receiver_fn(
    feature_spec, label_spec)

export_dir = tf.contrib.estimator.export_saved_model_for_mode(
    classifier,
    export_dir_base='my_model/',
    input_receiver_fn=train_rcvr_fn,
    mode=model_fn_lib.ModeKeys.TRAIN)

# export_dir is a timestamped directory with the SavedModel, which
# can be used for serving, analysis with TFMA, or directly loaded in.
with ops.Graph().as_default() as graph:
  with session.Session(graph=graph) as sess:
    loader.load(sess, [tag_constants.TRAINING], export_dir)
    weights = graph.get_tensor_by_name(''linear/linear_model/age/weights')
    ...
```

This method is a wrapper for _export_all_saved_models, and wraps a raw
input_receiver_fn in a dictionary to pass in to that function.
See _export_all_saved_models for full docs.

See tf.contrib.estimator.export_saved_model_for_mode for the currently
exposed version of this function.

#### Args:

* <b>`estimator`</b>: an instance of tf.estimator.Estimator
* <b>`export_dir_base`</b>: A string containing a directory in which to create
    timestamped subdirectories containing exported SavedModels.
* <b>`input_receiver_fn`</b>: a function that takes no argument and
    returns the appropriate subclass of `InputReceiver`.
* <b>`assets_extra`</b>: A dict specifying how to populate the assets.extra directory
    within the exported SavedModel, or `None` if no extra assets are needed.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format.
* <b>`checkpoint_path`</b>: The checkpoint path to export.  If `None` (the default),
    the most recent checkpoint found within the model directory is chosen.
* <b>`strip_default_attrs`</b>: Boolean. If `True`, default-valued attributes will be
    removed from the NodeDefs. For a detailed guide, see
    [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
* <b>`mode`</b>: tf.estimator.ModeKeys value indicating with mode will be exported.


#### Returns:

The string path to the exported directory.


#### Raises:

* <b>`ValueError`</b>: if input_receiver_fn is None, no export_outputs
    are provided, or no checkpoint can be found.