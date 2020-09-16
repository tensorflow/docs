description: Returns the class associated with name if it is registered with Keras.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.get_registered_object" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.get_registered_object

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/utils/generic_utils.py#L224-L257">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the class associated with `name` if it is registered with Keras.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.get_registered_object`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.get_registered_object(
    name, custom_objects=None, module_objects=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function is part of the Keras serialization and deserialization
framework. It maps strings to the objects associated with them for
serialization/deserialization.

#### Example:


```
def from_config(cls, config, custom_objects=None):
  if 'my_custom_object_name' in config:
    config['hidden_cls'] = tf.keras.utils.get_registered_object(
        config['my_custom_object_name'], custom_objects=custom_objects)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`
</td>
<td>
The name to look up.
</td>
</tr><tr>
<td>
`custom_objects`
</td>
<td>
A dictionary of custom objects to look the name up in.
Generally, custom_objects is provided by the user.
</td>
</tr><tr>
<td>
`module_objects`
</td>
<td>
A dictionary of custom objects to look the name up in.
Generally, module_objects is provided by midlevel library implementers.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
An instantiable class associated with 'name', or None if no such class
exists.
</td>
</tr>

</table>

