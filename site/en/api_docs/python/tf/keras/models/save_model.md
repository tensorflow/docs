description: Saves a model as a TensorFlow SavedModel or HDF5 file.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.models.save_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.models.save_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/saving/save.py#L50-L138">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Saves a model as a TensorFlow SavedModel or HDF5 file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.models.save_model`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.models.save_model(
    model, filepath, overwrite=(True), include_optimizer=(True), save_format=None,
    signatures=None, options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Usage:



```
>>> model = tf.keras.Sequential([
...     tf.keras.layers.Dense(5, input_shape=(3,)),
...     tf.keras.layers.Softmax()])
>>> model.save('/tmp/model')
>>> loaded_model = tf.keras.models.load_model('/tmp/model')
>>> x = tf.random.uniform((10, 3))
>>> assert np.allclose(model.predict(x), loaded_model.predict(x))
```

The saved model contains:

    - the model's configuration (topology)
    - the model's weights
    - the model's optimizer's state (if any)

Thus the saved model can be reinstantiated in
the exact same state, without any of the code
used for model definition or training.

Note that the model weights may have different scoped names after being
loaded. Scoped names include the model/layer names, such as
"dense_1/kernel:0"`. It is recommended that you use the layer properties to
access specific variables, e.g. `model.get_layer("dense_1").kernel`.

_SavedModel serialization_

The SavedModel serialization path uses <a href="../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> to save the model
and all trackable objects attached to the model (e.g. layers and variables).
`@tf.function`-decorated methods are also saved. Additional trackable objects
and functions are added to the SavedModel to allow the model to be
loaded back as a Keras Model object.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`model`
</td>
<td>
Keras model instance to be saved.
</td>
</tr><tr>
<td>
`filepath`
</td>
<td>
One of the following:
- String or `pathlib.Path` object, path where to save the model
- `h5py.File` object where to save the model
</td>
</tr><tr>
<td>
`overwrite`
</td>
<td>
Whether we should overwrite any existing model at the target
location, or instead ask the user with a manual prompt.
</td>
</tr><tr>
<td>
`include_optimizer`
</td>
<td>
If True, save optimizer's state together.
</td>
</tr><tr>
<td>
`save_format`
</td>
<td>
Either 'tf' or 'h5', indicating whether to save the model
to Tensorflow SavedModel or HDF5. Defaults to 'tf' in TF 2.X, and 'h5'
in TF 1.X.
</td>
</tr><tr>
<td>
`signatures`
</td>
<td>
Signatures to save with the SavedModel. Applicable to the 'tf'
format only. Please see the `signatures` argument in
<a href="../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> for details.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional <a href="../../../tf/saved_model/SaveOptions.md"><code>tf.saved_model.SaveOptions</code></a> object that specifies
options for saving to SavedModel.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
If save format is hdf5, and h5py is not available.
</td>
</tr>
</table>

