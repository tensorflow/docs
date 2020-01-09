page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.custom_object_scope


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/custom_object_scope">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/generic_utils.py#L76-L104">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Provides a scope that changes to `_GLOBAL_CUSTOM_OBJECTS` cannot escape.

### Aliases:

* <a href="/api_docs/python/tf/keras/utils/custom_object_scope"><code>tf.compat.v1.keras.utils.custom_object_scope</code></a>
* <a href="/api_docs/python/tf/keras/utils/custom_object_scope"><code>tf.compat.v2.keras.utils.custom_object_scope</code></a>


``` python
tf.keras.utils.custom_object_scope(*args)
```



<!-- Placeholder for "Used in" -->

Convenience wrapper for `CustomObjectScope`.
Code within a `with` statement will be able to access custom objects
by name. Changes to global custom objects persist
within the enclosing `with` statement. At end of the `with` statement,
global custom objects are reverted to state
at beginning of the `with` statement.

#### Example:



Consider a custom object `MyObject`

```python
    with custom_object_scope({'MyObject':MyObject}):
        layer = Dense(..., kernel_regularizer='MyObject')
        # save, load, etc. will recognize custom object by name
```

#### Arguments:


* <b>`*args`</b>: Variable length list of dictionaries of name,
    class pairs to add to custom objects.


#### Returns:

Object of type `CustomObjectScope`.
