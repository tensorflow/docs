description: Builds the SavedModel protocol buffer and saves variables and assets.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model.Builder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="add_meta_graph"/>
<meta itemprop="property" content="add_meta_graph_and_variables"/>
<meta itemprop="property" content="save"/>
</div>

# tf.compat.v1.saved_model.Builder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/saved_model/builder_impl.py#L432-L621">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Builds the `SavedModel` protocol buffer and saves variables and assets.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.saved_model.builder.SavedModelBuilder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.saved_model.Builder(
    export_dir
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `SavedModelBuilder` class provides the functionality to build a 
`SavedModel` protocol buffer. Specifically, this allows multiple meta
graphs to be saved as part of a single language-neutral `SavedModel`,
while sharing variables and assets.

To build a SavedModel, the first meta graph must be saved with variables.
Subsequent meta graphs will simply be saved with their graph definitions. If
assets need to be saved and written or copied to disk, they can be provided
when the meta graph def is added. If multiple meta graph defs are associated
an asset of the same name, only the first version is retained.

Each meta graph added to the SavedModel must be annotated with tags. The tags
provide a means to identify the specific meta graph to load and restore, along
with the shared set of variables and assets.

Typical usage for the `SavedModelBuilder`:

```python
...
builder = tf.compat.v1.saved_model.Builder(export_dir)

with tf.compat.v1.Session(graph=tf.Graph()) as sess:
  ...
  builder.add_meta_graph_and_variables(sess,
                                  ["foo-tag"],
                                  signature_def_map=foo_signatures,
                                  assets_collection=foo_assets)
...

with tf.compat.v1.Session(graph=tf.Graph()) as sess:
  ...
  builder.add_meta_graph(["bar-tag", "baz-tag"])
...

builder.save()
```

Note: This function will only be available through the v1 compatibility
library as tf.compat.v1.saved_model.builder.SavedModelBuilder or
tf.compat.v1.saved_model.Builder. Tensorflow 2.0 will introduce a new
object-based method of creating SavedModels.

## Methods

<h3 id="add_meta_graph"><code>add_meta_graph</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/saved_model/builder_impl.py#L513-L555">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_meta_graph(
    tags, signature_def_map=None, assets_collection=None, legacy_init_op=None,
    clear_devices=(False), main_op=None, strip_default_attrs=(False), saver=None
)
</code></pre>

Adds the current meta graph to the SavedModel.

Creates a Saver in the current scope and uses the Saver to export the meta
graph def. Invoking this API requires the `add_meta_graph_and_variables()`
API to have been invoked before.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tags`
</td>
<td>
The set of tags to annotate the meta graph def with.
</td>
</tr><tr>
<td>
`signature_def_map`
</td>
<td>
The map of signature defs to be added to the meta graph
def.
</td>
</tr><tr>
<td>
`assets_collection`
</td>
<td>
Assets to be saved with SavedModel. Note
that this list should be a subset of the assets saved as part of
the first meta graph in the SavedModel.
</td>
</tr><tr>
<td>
`clear_devices`
</td>
<td>
Set to true if the device info on the default graph should
be cleared.
</td>
</tr><tr>
<td>
`init_op`
</td>
<td>
Op or group of ops to execute when the graph is loaded. Note
that when the init_op is specified it is run after the restore op at
load-time.
</td>
</tr><tr>
<td>
`train_op`
</td>
<td>
Op or group of opts that trains the model when run. This will
not be run automatically when the graph is loaded, instead saved in
a SignatureDef accessible through the exported MetaGraph.
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
An instance of tf.compat.v1.train.Saver that will be used to export
the metagraph. If None, a sharded Saver that restores all variables will
be used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`AssertionError`
</td>
<td>
If the variables for the SavedModel have not been saved
yet, or if the graph already contains one or more legacy init ops.
</td>
</tr>
</table>



<h3 id="add_meta_graph_and_variables"><code>add_meta_graph_and_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/saved_model/builder_impl.py#L557-L615">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_meta_graph_and_variables(
    sess, tags, signature_def_map=None, assets_collection=None, legacy_init_op=None,
    clear_devices=(False), main_op=None, strip_default_attrs=(False), saver=None
)
</code></pre>

Adds the current meta graph to the SavedModel and saves variables.

Creates a Saver to save the variables from the provided session. Exports the
corresponding meta graph def. This function assumes that the variables to be
saved have been initialized. For a given `SavedModelBuilder`, this API must
be called exactly once and for the first meta graph to save. For subsequent
meta graph defs to be added, the `add_meta_graph()` API must be used.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`sess`
</td>
<td>
The TensorFlow session from which to save the meta graph and
variables.
</td>
</tr><tr>
<td>
`tags`
</td>
<td>
The set of tags with which to save the meta graph.
</td>
</tr><tr>
<td>
`signature_def_map`
</td>
<td>
The map of signature def map to add to the meta graph
def.
</td>
</tr><tr>
<td>
`assets_collection`
</td>
<td>
Assets to be saved with SavedModel.
</td>
</tr><tr>
<td>
`clear_devices`
</td>
<td>
Set to true if the device info on the default graph should
be cleared.
</td>
</tr><tr>
<td>
`init_op`
</td>
<td>
Op or group of ops to execute when the graph is loaded. Note
that when the init_op is specified it is run after the restore op at
load-time.
</td>
</tr><tr>
<td>
`train_op`
</td>
<td>
Op or group of ops that trains the model when run. This will
not be run automatically when the graph is loaded, instead saved in
a SignatureDef accessible through the exported MetaGraph.
</td>
</tr><tr>
<td>
`strip_default_attrs`
</td>
<td>
Boolean. If `True`, default-valued attributes will be
removed from the NodeDefs. For a detailed guide, see
[Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
</td>
</tr><tr>
<td>
`saver`
</td>
<td>
An instance of tf.compat.v1.train.Saver that will be used to export the
metagraph and save variables. If None, a sharded Saver that restores
all variables will be used.
</td>
</tr>
</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/saved_model/builder_impl.py#L395-L428">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    as_text=(False)
)
</code></pre>

Writes a `SavedModel` protocol buffer to disk.

The function writes the SavedModel protocol buffer to the export directory
in a serialized format.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`as_text`
</td>
<td>
Writes the SavedModel protocol buffer in text format to
disk. Protocol buffers in text format are useful for debugging, but
parsing fails when it encounters an unknown field and so is not forward
compatible. This means changes to TensorFlow may prevent deployment of
new text format SavedModels to existing serving binaries. Do not deploy
`as_text` SavedModels to production.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The path to which the SavedModel protocol buffer was written.
</td>
</tr>

</table>





