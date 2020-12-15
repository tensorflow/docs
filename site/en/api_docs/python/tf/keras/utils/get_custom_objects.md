description: Retrieves a live reference to the global dictionary of custom objects.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.get_custom_objects" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.get_custom_objects

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/utils/generic_utils.py#L92-L110">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Retrieves a live reference to the global dictionary of custom objects.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.get_custom_objects`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.get_custom_objects()
</code></pre>



<!-- Placeholder for "Used in" -->

Updating and clearing custom objects using `custom_object_scope`
is preferred, but `get_custom_objects` can
be used to directly access the current collection of custom objects.

#### Example:



```python
get_custom_objects().clear()
get_custom_objects()['MyObject'] = MyObject
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Global dictionary of names to classes (`_GLOBAL_CUSTOM_OBJECTS`).
</td>
</tr>

</table>

