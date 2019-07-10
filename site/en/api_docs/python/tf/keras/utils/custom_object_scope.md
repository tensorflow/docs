page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.custom_object_scope

Provides a scope that changes to `_GLOBAL_CUSTOM_OBJECTS` cannot escape.

### Aliases:

* `tf.compat.v1.keras.utils.custom_object_scope`
* `tf.compat.v2.keras.utils.custom_object_scope`
* `tf.keras.utils.custom_object_scope`

``` python
tf.keras.utils.custom_object_scope(*args)
```



Defined in [`python/keras/utils/generic_utils.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/utils/generic_utils.py).

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
