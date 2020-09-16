description: Represents a file asset to hermetically include in a SavedModel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.saved_model.Asset" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.saved_model.Asset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/tracking/tracking.py#L280-L330">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a file asset to hermetically include in a SavedModel.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.saved_model.Asset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.saved_model.Asset(
    path
)
</code></pre>



<!-- Placeholder for "Used in" -->

A SavedModel can include arbitrary files, called assets, that are needed
for its use. For example a vocabulary file used initialize a lookup table.

When a trackable object is exported via <a href="../../tf/saved_model/save.md"><code>tf.saved_model.save()</code></a>, all the
`Asset`s reachable from it are copied into the SavedModel assets directory.
Upon loading, the assets and the serialized functions that depend on them
will refer to the correct filepaths inside the SavedModel directory.

#### Example:



```
filename = tf.saved_model.Asset("file.txt")

@tf.function(input_signature=[])
def func():
  return tf.io.read_file(filename)

trackable_obj = tf.train.Checkpoint()
trackable_obj.func = func
trackable_obj.filename = filename
tf.saved_model.save(trackable_obj, "/tmp/saved_model")

# The created SavedModel is hermetic, it does not depend on
# the original file and can be moved to another path.
tf.io.gfile.remove("file.txt")
tf.io.gfile.rename("/tmp/saved_model", "/tmp/new_location")

reloaded_obj = tf.saved_model.load("/tmp/new_location")
print(reloaded_obj.func())
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`asset_path`
</td>
<td>
A 0-D <a href="../../tf.md#string"><code>tf.string</code></a> tensor with path to the asset.
</td>
</tr>
</table>



