

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_custom_objects

``` python
tf.keras.utils.get_custom_objects()
```



Defined in [`tensorflow/python/keras/utils/generic_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/utils/generic_utils.py).

Retrieves a live reference to the global dictionary of custom objects.

Updating and clearing custom objects using `custom_object_scope`
is preferred, but `get_custom_objects` can
be used to directly access `_GLOBAL_CUSTOM_OBJECTS`.

Example:

```python
    get_custom_objects().clear()
    get_custom_objects()['MyObject'] = MyObject
```

#### Returns:

Global dictionary of names to classes (`_GLOBAL_CUSTOM_OBJECTS`).