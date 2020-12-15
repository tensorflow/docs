description: Exports a <a href="../../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> as a Tensorflow SavedModel. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.experimental.export_saved_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.keras.experimental.export_saved_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/saving/saved_model_experimental.py#L64-L146">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Exports a <a href="../../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> as a Tensorflow SavedModel. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.experimental.export_saved_model(
    model, saved_model_path, custom_objects=None, as_text=(False),
    input_signature=None, serving_only=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use `model.save(..., save_format="tf")` or `tf.keras.models.save_model(..., save_format="tf")`.

Note that at this time, subclassed models can only be saved using
`serving_only=True`.

The exported `SavedModel` is a standalone serialization of Tensorflow objects,
and is supported by TF language APIs and the Tensorflow Serving system.
To load the model, use the function
`tf.keras.experimental.load_from_saved_model`.

The `SavedModel` contains:

1. a checkpoint containing the model weights.
2. a `SavedModel` proto containing the Tensorflow backend graph. Separate
   graphs are saved for prediction (serving), train, and evaluation. If
   the model has not been compiled, then only the graph computing predictions
   will be exported.
3. the model's json config. If the model is subclassed, this will only be
   included if the model's `get_config()` method is overwritten.

#### Example:



```python
import tensorflow as tf

# Create a tf.keras model.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=[10]))
model.summary()

# Save the tf.keras model in the SavedModel format.
path = '/tmp/simple_keras_model'
tf.keras.experimental.export_saved_model(model, path)

# Load the saved keras model back.
new_model = tf.keras.experimental.load_from_saved_model(path)
new_model.summary()
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`model`
</td>
<td>
A <a href="../../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> to be saved. If the model is subclassed, the flag
`serving_only` must be set to True.
</td>
</tr><tr>
<td>
`saved_model_path`
</td>
<td>
a string specifying the path to the SavedModel directory.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
Optional dictionary mapping string names to custom classes
or functions (e.g. custom loss functions).
</td>
</tr><tr>
<td>
`as_text`
</td>
<td>
bool, `False` by default. Whether to write the `SavedModel` proto
in text format. Currently unavailable in serving-only mode.
</td>
</tr><tr>
<td>
`input_signature`
</td>
<td>
A possibly nested sequence of <a href="../../../../../tf/TensorSpec.md"><code>tf.TensorSpec</code></a> objects, used
to specify the expected model inputs. See <a href="../../../../../tf/function.md"><code>tf.function</code></a> for more details.
</td>
</tr><tr>
<td>
`serving_only`
</td>
<td>
bool, `False` by default. When this is true, only the
prediction graph is saved.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
If the model is a subclassed model, and serving_only is
False.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the input signature cannot be inferred from the model.
</td>
</tr><tr>
<td>
`AssertionError`
</td>
<td>
If the SavedModel directory already exists and isn't empty.
</td>
</tr>
</table>

