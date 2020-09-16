description: Loads a model saved via save_model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.models.load_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.models.load_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/saving/save.py#L141-L194">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads a model saved via `save_model`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.models.load_model`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.models.load_model(
    filepath, custom_objects=None, compile=(True)
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

Note that the model weights may have different scoped names after being
loaded. Scoped names include the model/layer names, such as
"dense_1/kernel:0"`. It is recommended that you use the layer properties to
access specific variables, e.g. `model.get_layer("dense_1").kernel`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`filepath`
</td>
<td>
One of the following:
- String or `pathlib.Path` object, path to the saved model
- `h5py.File` object from which to load the model
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
Optional dictionary mapping names
(strings) to custom classes or functions to be
considered during deserialization.
</td>
</tr><tr>
<td>
`compile`
</td>
<td>
Boolean, whether to compile the model
after loading.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras model instance. If the original model was compiled, and saved with
the optimizer, then the returned model will be compiled. Otherwise, the
model will be left uncompiled. In the case that an uncompiled model is
returned, a warning is displayed if the `compile` argument is set to
`True`.
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
if loading from an hdf5 file and h5py is not available.
</td>
</tr><tr>
<td>
`IOError`
</td>
<td>
In case of an invalid savefile.
</td>
</tr>
</table>

