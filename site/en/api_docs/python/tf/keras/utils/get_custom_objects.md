page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_custom_objects


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/get_custom_objects">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/generic_utils.py#L107-L125">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retrieves a live reference to the global dictionary of custom objects.

### Aliases:

* <a href="/api_docs/python/tf/keras/utils/get_custom_objects"><code>tf.compat.v1.keras.utils.get_custom_objects</code></a>
* <a href="/api_docs/python/tf/keras/utils/get_custom_objects"><code>tf.compat.v2.keras.utils.get_custom_objects</code></a>


``` python
tf.keras.utils.get_custom_objects()
```



<!-- Placeholder for "Used in" -->

Updating and clearing custom objects using `custom_object_scope`
is preferred, but `get_custom_objects` can
be used to directly access `_GLOBAL_CUSTOM_OBJECTS`.

#### Example:



```python
    get_custom_objects().clear()
    get_custom_objects()['MyObject'] = MyObject
```

#### Returns:

Global dictionary of names to classes (`_GLOBAL_CUSTOM_OBJECTS`).
