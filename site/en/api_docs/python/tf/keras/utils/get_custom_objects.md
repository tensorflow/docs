page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_custom_objects

Retrieves a live reference to the global dictionary of custom objects.

### Aliases:

* `tf.compat.v1.keras.utils.get_custom_objects`
* `tf.compat.v2.keras.utils.get_custom_objects`
* `tf.keras.utils.get_custom_objects`

``` python
tf.keras.utils.get_custom_objects()
```



Defined in [`python/keras/utils/generic_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/utils/generic_utils.py).

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
