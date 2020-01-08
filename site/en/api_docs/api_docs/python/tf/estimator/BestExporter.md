

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.BestExporter

## Class `BestExporter`

Inherits From: [`Exporter`](../../tf/estimator/Exporter)



Defined in [`tensorflow/python/estimator/exporter.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/estimator/exporter.py).

This class exports the serving graph and checkpoints of the best models.

This class performs a model export everytime when the new model is better
than any exsiting model.

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    name='best_exporter',
    serving_input_receiver_fn=None,
    event_file_pattern='eval/*.tfevents.*',
    compare_fn=_loss_smaller,
    assets_extra=None,
    as_text=False,
    exports_to_keep=5
)
```

Create an `Exporter` to use with <a href="../../tf/estimator/EvalSpec"><code>tf.estimator.EvalSpec</code></a>.

Example of creating a BestExporter for training and evluation:

```python
def make_train_and_eval_fn():
  # Set up feature columns.
  categorial_feature_a = (
      tf.feature_column.categorical_column_with_hash_bucket(...))
  categorial_feature_a_emb = embedding_column(
      categorical_column=categorial_feature_a, ...)
  ...  # other feature columns

  estimator = tf.estimator.DNNClassifier(
      config=tf.estimator.RunConfig(
          model_dir='/my_model', save_summary_steps=100),
      feature_columns=[categorial_feature_a_emb, ...],
      hidden_units=[1024, 512, 256])

  serving_feature_spec = tf.feature_column.make_parse_example_spec(
      categorial_feature_a_emb)
  serving_input_receiver_fn = (
      tf.estimator.export.build_parsing_serving_input_receiver_fn(
      serving_feature_spec))

  exporter = tf.estimator.BestExporter(
      name="best_exporter",
      serving_input_receiver_fn=serving_input_receiver_fn,
      exports_to_keep=5)

  train_spec = tf.estimator.TrainSpec(...)

  eval_spec = [tf.estimator.EvalSpec(
    input_fn=eval_input_fn,
    steps=100,
    exporters=exporter,
    start_delay_secs=0,
    throttle_secs=5)]

  return tf.estimator.DistributedTrainingSpec(estimator, train_spec,
                                              eval_spec)
```

#### Args:

* <b>`name`</b>: unique name of this `Exporter` that is going to be used in the
    export path.
* <b>`serving_input_receiver_fn`</b>: a function that takes no arguments and returns
    a `ServingInputReceiver`.
* <b>`event_file_pattern`</b>: event file name pattern relative to model_dir. If
    None, however, the exporter would not be preemption-safe. To be
    preemption-safe, event_file_pattern should be specified.
* <b>`compare_fn`</b>: a function that compares two evaluation results and returns
    true if current evaluation result is better. Follows the signature:
    * Args:
      * `best_eval_result`: This is the evaluation result of the best model.
      * `current_eval_result`: This is the evaluation result of current
             candidate model.
    * Returns:
      True if current evaluation result is better; otherwise, False.
* <b>`assets_extra`</b>: An optional dict specifying how to populate the assets.extra
    directory within the exported SavedModel.  Each key should give the
    destination path (including the filename) relative to the assets.extra
    directory.  The corresponding value gives the full path of the source
    file to be copied.  For example, the simple case of copying a single
    file without renaming it is specified as `{'my_asset_file.txt':
    '/path/to/my_asset_file.txt'}`.
* <b>`as_text`</b>: whether to write the SavedModel proto in text format. Defaults to
    `False`.
* <b>`exports_to_keep`</b>: Number of exports to keep.  Older exports will be
    garbage-collected.  Defaults to 5.  Set to `None` to disable garbage
    collection.


#### Raises:

* <b>`ValueError`</b>: if any arguments is invalid.

<h3 id="export"><code>export</code></h3>

``` python
export(
    estimator,
    export_path,
    checkpoint_path,
    eval_result,
    is_the_final_export
)
```





