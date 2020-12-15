description: Load a SavedModel from export_dir.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.saved_model.load" />
<meta itemprop="path" content="Stable" />
</div>

# tf.saved_model.load

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/saved_model/load.py#L512-L603">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Load a SavedModel from `export_dir`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.saved_model.load_v2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.saved_model.load(
    export_dir, tags=None, options=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Signatures associated with the SavedModel are available as functions:

```python
imported = tf.saved_model.load(path)
f = imported.signatures["serving_default"]
print(f(x=tf.constant([[1.]])))
```

Objects exported with <a href="../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> additionally have trackable
objects and functions assigned to attributes:

```python
exported = tf.train.Checkpoint(v=tf.Variable(3.))
exported.f = tf.function(
    lambda x: exported.v * x,
    input_signature=[tf.TensorSpec(shape=None, dtype=tf.float32)])
tf.saved_model.save(exported, path)
imported = tf.saved_model.load(path)
assert 3. == imported.v.numpy()
assert 6. == imported.f(x=tf.constant(2.)).numpy()
```

_Loading Keras models_

Keras models are trackable, so they can be saved to SavedModel. The object
returned by <a href="../../tf/saved_model/load.md"><code>tf.saved_model.load</code></a> is not a Keras object (i.e. doesn't have
`.fit`, `.predict`, etc. methods). A few attributes and functions are still
available: `.variables`, `.trainable_variables` and `.__call__`.

```python
model = tf.keras.Model(...)
tf.saved_model.save(model, path)
imported = tf.saved_model.load(path)
outputs = imported(inputs)
```

Use <a href="../../tf/keras/models/load_model.md"><code>tf.keras.models.load_model</code></a> to restore the Keras model.

_Importing SavedModels from TensorFlow 1.x_

SavedModels from <a href="../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a> or 1.x SavedModel APIs have a flat
graph instead of <a href="../../tf/function.md"><code>tf.function</code></a> objects. These SavedModels will be loaded with
the following attributes:

* `.signatures`: A dictionary mapping signature names to functions.
* `.prune(feeds, fetches) `: A method which allows you to extract
  functions for new subgraphs. This is equivalent to importing the SavedModel
  and naming feeds and fetches in a Session from TensorFlow 1.x.

  ```python
  imported = tf.saved_model.load(path_to_v1_saved_model)
  pruned = imported.prune("x:0", "out:0")
  pruned(tf.ones([]))
  ```

  See <a href="../../tf/compat/v1/wrap_function.md"><code>tf.compat.v1.wrap_function</code></a> for details.
* `.variables`: A list of imported variables.
* `.graph`: The whole imported graph.
* `.restore(save_path)`: A function that restores variables from a checkpoint
  saved from `tf.compat.v1.Saver`.

_Consuming SavedModels asynchronously_

When consuming SavedModels asynchronously (the producer is a separate
process), the SavedModel directory will appear before all files have been
written, and <a href="../../tf/saved_model/load.md"><code>tf.saved_model.load</code></a> will fail if pointed at an incomplete
SavedModel. Rather than checking for the directory, check for
"saved_model_dir/saved_model.pb". This file is written atomically as the last
<a href="../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a> file operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`export_dir`
</td>
<td>
The SavedModel directory to load from.
</td>
</tr><tr>
<td>
`tags`
</td>
<td>
A tag or sequence of tags identifying the MetaGraph to load. Optional
if the SavedModel contains a single MetaGraph, as for those exported from
<a href="../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a>.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
Optional, <a href="../../tf/saved_model/LoadOptions.md"><code>tf.saved_model.LoadOptions</code></a> object that specifies
options for loading.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A trackable object with a `signatures` attribute mapping from signature
keys to functions. If the SavedModel was exported by <a href="../../tf/saved_model/load.md"><code>tf.saved_model.load</code></a>,
it also points to trackable objects, functions, debug info which it has been
saved.
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
If `tags` don't match a MetaGraph in the SavedModel.
</td>
</tr>
</table>

