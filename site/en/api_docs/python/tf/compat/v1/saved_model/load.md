description: Loads the model from a SavedModel as specified by tags. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model.load" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.saved_model.load

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/saved_model/loader_impl.py#L268-L299">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads the model from a SavedModel as specified by tags. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.saved_model.loader.load`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.saved_model.load(
    sess, tags, export_dir, import_scope=None, **saver_kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.loader.load or tf.compat.v1.saved_model.load. There will be a new function for importing SavedModels in Tensorflow 2.0.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sess`
</td>
<td>
The TensorFlow session to restore the variables.
</td>
</tr><tr>
<td>
`tags`
</td>
<td>
Set of string tags to identify the required MetaGraphDef. These should
correspond to the tags used when saving the variables using the
SavedModel `save()` API.
</td>
</tr><tr>
<td>
`export_dir`
</td>
<td>
Directory in which the SavedModel protocol buffer and variables
to be loaded are located.
</td>
</tr><tr>
<td>
`import_scope`
</td>
<td>
Optional `string` -- if specified, prepend this string
followed by '/' to all loaded tensor names. This scope is applied to
tensor instances loaded into the passed session, but it is *not* written
through to the static `MetaGraphDef` protocol buffer that is returned.
</td>
</tr><tr>
<td>
`**saver_kwargs`
</td>
<td>
Optional keyword arguments passed through to Saver.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The `MetaGraphDef` protocol buffer loaded in the provided session. This
can be used to further extract signature-defs, collection-defs, etc.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
MetaGraphDef associated with the tags cannot be found.
</td>
</tr>
</table>

