description: Updates the method name(s) of the SavedModel stored in the given path.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.saved_model.signature_def_utils.MethodNameUpdater" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="replace_method_name"/>
<meta itemprop="property" content="save"/>
</div>

# tf.compat.v1.saved_model.signature_def_utils.MethodNameUpdater

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/method_name_updater.py#L37-L148">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Updates the method name(s) of the SavedModel stored in the given path.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.saved_model.signature_def_utils.MethodNameUpdater(
    export_dir
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `MethodNameUpdater` class provides the functionality to update the method
name field in the signature_defs of the given SavedModel. For example, it
can be used to replace the `predict` `method_name` to `regress`.

Typical usages of the `MethodNameUpdater`
```python
...
updater = tf.compat.v1.saved_model.MethodNameUpdater(export_dir)
# Update all signature_defs with key "foo" in all meta graph defs.
updater.replace_method_name(signature_key="foo", method_name="regress")
# Update a single signature_def with key "bar" in the meta graph def with
# tags ["serve"]
updater.replace_method_name(signature_key="bar", method_name="classify",
                            tags="serve")
updater.save(new_export_dir)
```

Note: This function will only be available through the v1 compatibility
library as tf.compat.v1.saved_model.builder.MethodNameUpdater.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`export_dir`
</td>
<td>
Directory containing the SavedModel files.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`IOError`
</td>
<td>
If the saved model file does not exist, or cannot be successfully
parsed.
</td>
</tr>
</table>



## Methods

<h3 id="replace_method_name"><code>replace_method_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/method_name_updater.py#L74-L117">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>replace_method_name(
    signature_key, method_name, tags=None
)
</code></pre>

Replaces the method_name in the specified signature_def.

This will match and replace multiple sig defs iff tags is None (i.e when
multiple `MetaGraph`s have a signature_def with the same key).
If tags is not None, this will only replace a single signature_def in the
`MetaGraph` with matching tags.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`signature_key`
</td>
<td>
Key of the signature_def to be updated.
</td>
</tr><tr>
<td>
`method_name`
</td>
<td>
new method_name to replace the existing one.
</td>
</tr><tr>
<td>
`tags`
</td>
<td>
A tag or sequence of tags identifying the `MetaGraph` to update. If
None, all meta graphs will be updated.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if signature_key or method_name are not defined or
if no metagraphs were found with the associated tags or
if no meta graph has a signature_def that matches signature_key.
</td>
</tr>
</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/saved_model/method_name_updater.py#L119-L148">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>save(
    new_export_dir=None
)
</code></pre>

Saves the updated `SavedModel`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`new_export_dir`
</td>
<td>
Path where the updated `SavedModel` will be saved. If
None, the input `SavedModel` will be overriden with the updates.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`errors.OpError`
</td>
<td>
If there are errors during the file save operation.
</td>
</tr>
</table>





