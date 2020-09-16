description: Constructs an Estimator instance from given keras model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.estimator.model_to_estimator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.keras.estimator.model_to_estimator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/estimator/__init__.py#L34-L129">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Constructs an `Estimator` instance from given keras model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.estimator.model_to_estimator(
    keras_model=None, keras_model_path=None, custom_objects=None, model_dir=None,
    config=None, checkpoint_format='saver'
)
</code></pre>



<!-- Placeholder for "Used in" -->

If you use infrastructure or other tooling that relies on Estimators, you can
still build a Keras model and use model_to_estimator to convert the Keras
model to an Estimator for use with downstream systems.

For usage example, please see:
[Creating estimators from Keras
Models](https://www.tensorflow.org/guide/estimators#creating_estimators_from_keras_models).

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
user maintains a `relu6` class that inherits from <a href="../../../../../tf/keras/layers/Layer.md"><code>tf.keras.layers.Layer</code></a>,
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
save checkpoints from `tf.train.Saver` or <a href="../../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>. This
argument currently defaults to `saver`. When 2.0 is released, the default
will be `checkpoint`. Estimators use name-based `tf.train.Saver`
checkpoints, while Keras models use object-based checkpoints from
<a href="../../../../../tf/train/Checkpoint.md"><code>tf.train.Checkpoint</code></a>. Currently, saving object-based checkpoints from
`model_to_estimator` is only supported by Functional and Sequential
models. Defaults to 'saver'.
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

