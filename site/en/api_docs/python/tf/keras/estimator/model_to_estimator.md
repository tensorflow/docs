description: Constructs an Estimator instance from given keras model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.estimator.model_to_estimator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.estimator.model_to_estimator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/estimator/__init__.py#L184-L369">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Constructs an `Estimator` instance from given keras model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.estimator.model_to_estimator(
    keras_model=None, keras_model_path=None, custom_objects=None, model_dir=None,
    config=None, checkpoint_format='checkpoint', metric_names_map=None,
    export_outputs=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

If you use infrastructure or other tooling that relies on Estimators, you can
still build a Keras model and use model_to_estimator to convert the Keras
model to an Estimator for use with downstream systems.

For usage example, please see:
[Creating estimators from Keras Models](
  https://www.tensorflow.org/guide/estimators#creating_estimators_from_keras_models).

#### Sample Weights:


Estimators returned by `model_to_estimator` are configured so that they can
handle sample weights (similar to `keras_model.fit(x, y, sample_weights)`).

To pass sample weights when training or evaluating the Estimator, the first
item returned by the input function should be a dictionary with keys
`features` and `sample_weights`. Example below:

```python
keras_model = tf.keras.Model(...)
keras_model.compile(...)

estimator = tf.keras.estimator.model_to_estimator(keras_model)

def input_fn():
  return dataset_ops.Dataset.from_tensors(
      ({'features': features, 'sample_weights': sample_weights},
       targets))

estimator.train(input_fn, steps=1)
```

Example with customized export signature:
```python
inputs = {'a': tf.keras.Input(..., name='a'),
          'b': tf.keras.Input(..., name='b')}
outputs = {'c': tf.keras.layers.Dense(..., name='c')(inputs['a']),
           'd': tf.keras.layers.Dense(..., name='d')(inputs['b'])}
keras_model = tf.keras.Model(inputs, outputs)
keras_model.compile(...)
export_outputs = {'c': tf.estimator.export.RegressionOutput,
                  'd': tf.estimator.export.ClassificationOutput}

estimator = tf.keras.estimator.model_to_estimator(
    keras_model, export_outputs=export_outputs)

def input_fn():
  return dataset_ops.Dataset.from_tensors(
      ({'features': features, 'sample_weights': sample_weights},
       targets))

estimator.train(input_fn, steps=1)
```

Note: We do not support creating weighted metrics in Keras and converting them
to weighted metrics in the Estimator API using `model_to_estimator`.
You will have to create these metrics directly on the estimator spec using the
`add_metrics` function.

To customize the estimator `eval_metric_ops` names, you can pass in the
`metric_names_map` dictionary mapping the keras model output metric names
to the custom names as follows:

```python
  input_a = tf.keras.layers.Input(shape=(16,), name='input_a')
  input_b = tf.keras.layers.Input(shape=(16,), name='input_b')
  dense = tf.keras.layers.Dense(8, name='dense_1')
  interm_a = dense(input_a)
  interm_b = dense(input_b)
  merged = tf.keras.layers.concatenate([interm_a, interm_b], name='merge')
  output_a = tf.keras.layers.Dense(3, activation='softmax', name='dense_2')(
          merged)
  output_b = tf.keras.layers.Dense(2, activation='softmax', name='dense_3')(
          merged)
  keras_model = tf.keras.models.Model(
      inputs=[input_a, input_b], outputs=[output_a, output_b])
  keras_model.compile(
      loss='categorical_crossentropy',
      optimizer='rmsprop',
      metrics={
          'dense_2': 'categorical_accuracy',
          'dense_3': 'categorical_accuracy'
      })

  metric_names_map = {
      'dense_2_categorical_accuracy': 'acc_1',
      'dense_3_categorical_accuracy': 'acc_2',
  }
  keras_est = tf.keras.estimator.model_to_estimator(
      keras_model=keras_model,
      config=config,
      metric_names_map=metric_names_map)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`keras_model`
</td>
<td>
A compiled Keras model object. This argument is mutually
exclusive with `keras_model_path`. Estimator's `model_fn` uses the
structure of the model to clone the model. Defaults to `None`.
</td>
</tr><tr>
<td>
`keras_model_path`
</td>
<td>
Path to a compiled Keras model saved on disk, in HDF5
format, which can be generated with the `save()` method of a Keras model.
This argument is mutually exclusive with `keras_model`.
Defaults to `None`.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
Dictionary for cloning customized objects. This is
used with classes that is not part of this pip package. For example, if
user maintains a `relu6` class that inherits from <a href="../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a>,
then pass `custom_objects={'relu6': relu6}`. Defaults to `None`.
</td>
</tr><tr>
<td>
`model_dir`
</td>
<td>
Directory to save `Estimator` model parameters, graph, summary
files for TensorBoard, etc. If unset a directory will be created with
`tempfile.mkdtemp`
</td>
</tr><tr>
<td>
`config`
</td>
<td>
`RunConfig` to config `Estimator`. Allows setting up things in
`model_fn` based on configuration such as `num_ps_replicas`, or
`model_dir`. Defaults to `None`. If both `config.model_dir` and the
`model_dir` argument (above) are specified the `model_dir` **argument**
takes precedence.
</td>
</tr><tr>
<td>
`checkpoint_format`
</td>
<td>
Sets the format of the checkpoint saved by the estimator
when training. May be `saver` or `checkpoint`, depending on whether to
save checkpoints from <a href="../../../tf/compat/v1/train/Saver.md"><code>tf.compat.v1.train.Saver</code></a> or <a href="../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>.
The default is `checkpoint`. Estimators use name-based `tf.train.Saver`
checkpoints, while Keras models use object-based checkpoints from
<a href="../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>. Currently, saving object-based checkpoints from
`model_to_estimator` is only supported by Functional and Sequential
models. Defaults to 'checkpoint'.
</td>
</tr><tr>
<td>
`metric_names_map`
</td>
<td>
Optional dictionary mapping Keras model output metric
names to custom names. This can be used to override the default Keras
model output metrics names in a multi IO model use case and provide custom
names for the `eval_metric_ops` in Estimator.
The Keras model metric names can be obtained using `model.metrics_names`
excluding any loss metrics such as total loss and output losses.
For example, if your Keras model has two outputs `out_1` and `out_2`,
with `mse` loss and `acc` metric, then `model.metrics_names` will be
`['loss', 'out_1_loss', 'out_2_loss', 'out_1_acc', 'out_2_acc']`.
The model metric names excluding the loss metrics will be
`['out_1_acc', 'out_2_acc']`.
</td>
</tr><tr>
<td>
`export_outputs`
</td>
<td>
Optional dictionary. This can be used to override the
default Keras model output exports in a multi IO model use case and
provide custom names for the `export_outputs` in
<a href="../../../tf/estimator/EstimatorSpec.md"><code>tf.estimator.EstimatorSpec</code></a>. Default is None, which is equivalent to
{'serving_default': <a href="../../../tf/estimator/export/PredictOutput.md"><code>tf.estimator.export.PredictOutput</code></a>}. If not None,
the keys must match the keys of `model.output_names`.
A dict `{name: output}` where:
* name: An arbitrary name for this output.
* output: an `ExportOutput` class such as `ClassificationOutput`,
`RegressionOutput`, or `PredictOutput`. Single-headed models only need
to specify one entry in this dictionary. Multi-headed models should
specify one entry for each head, one of which must be named using
`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`
If no entry is provided, a default `PredictOutput` mapping to
`predictions` will be created.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An Estimator from given keras model.
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
If neither keras_model nor keras_model_path was given.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If both keras_model and keras_model_path was given.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the keras_model_path is a GCS URI.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If keras_model has not been compiled.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If an invalid checkpoint_format was given.
</td>
</tr>
</table>

